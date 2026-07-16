#!/usr/bin/env python3
"""Generation harness for one arm of the prose-skill A/B experiment.

Protocol source of truth: docs/research/prose-skill-ab-preregistration.md
(Fields 3, 4, 5, 5b, 8, 10 bind this script). Prompts are parsed from the
frozen docs/research/prose-skill-elicitation-set.md (Field 1).

This script calls the Anthropic Messages API directly over
urllib.request/json — Python standard library only, no `anthropic` SDK
dependency (the SDK is intentionally not installed for this experiment).

Usage:
    python3 generate_arm.py --arm off --strata A --n 3 --seed 42 --dry-run
    python3 generate_arm.py --arm on --system-prompt-file skill.txt \\
        --strata A,B,C --n 3 --seed 42 --out generations/on
"""

from __future__ import annotations

import argparse
import json
import os
import random
import re
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

# Pre-registration Field 4 pins the model to claude-sonnet-5 for this run.
# Changing this constant voids comparability with any prior-round generations
# already collected under this pre-registration — do not "upgrade" it later
# without a new pre-registration.
MODEL = "claude-sonnet-5"

ANTHROPIC_API_URL = "https://api.anthropic.com/v1/messages"
ANTHROPIC_VERSION = "2023-06-01"

# Field 4: max_tokens is a hard ceiling on TOTAL output — thinking tokens and
# response text share it. 16000 leaves headroom for adaptive thinking (always
# pinned on below) plus a full technical document without truncating
# mid-sentence; claude-sonnet-5 supports up to 128K. Truncated generations
# are still recorded (see `truncated` on each record) and excluded from
# pattern counts downstream, per Field 4's registered exclusion rule.
MAX_TOKENS = 16000

# Field 4: "thinking is pinned explicitly to {"type": "adaptive"}, not
# omitted." On claude-sonnet-5 an omitted `thinking` field runs adaptive
# anyway (a silent change from Sonnet 4.6, which ran thinking-off when
# omitted) — so omitting it would leave the experiment's largest output-side
# variable undeclared. Pinning it identically across all three arms makes
# that a recorded decision rather than an accident, and per-arm thinking
# spend (usage.output_tokens, which includes thinking tokens) is itself a
# registered manipulation check, not noise to smooth over.
THINKING_CONFIG = {"type": "adaptive"}

# Field 4: "Sampling parameters are not free variables on this model."
# claude-sonnet-5 rejects non-default temperature/top_p/top_k with a 400, so
# they are never sent and are not exposed as CLI flags — exposing them would
# be a footgun that turns an entire batch into null results the moment
# someone sets one. Recorded verbatim in every record so the record stays
# self-describing about what was (not) a free variable.
SAMPLING_NOT_SETTABLE = "api_default_not_settable"

# Field 4: batch-void threshold. Not enforced by this script (truncation can
# only be known after generation), but recorded in the manifest so a human
# or a downstream check can act on it without a separate analysis pass.
TRUNCATION_VOID_THRESHOLD = 0.05

# Retry policy for the API call itself (429 / 5xx). Not part of the
# pre-registration; chosen to bound worst-case wall-clock time for a full run.
MAX_RETRIES = 6
BACKOFF_BASE_SECONDS = 1.0
BACKOFF_CAP_SECONDS = 60.0

REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_ELICITATION_FILE = (
    REPO_ROOT / "docs" / "research" / "prose-skill-elicitation-set.md"
)

EXPECTED_COUNTS = {"A": 20, "B": 42, "C": 10}


# ---------------------------------------------------------------------------
# Elicitation-set parsing
# ---------------------------------------------------------------------------


def _extract_section(text: str, start_heading: str, end_heading: str | None) -> str:
    start = text.index(start_heading)
    end = text.index(end_heading, start) if end_heading else len(text)
    return text[start:end]


def _parse_stratum_a(section_text: str) -> list[dict]:
    """Stratum A is a markdown table: | ID | Lang | Document type | Reader background | Prompt |."""
    entries = []
    for raw_line in section_text.splitlines():
        line = raw_line.strip()
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) != 5:
            continue
        if not re.match(r"^A\d{2}$", cells[0]):
            continue  # header row, separator row ("---"), or malformed
        entries.append(
            {
                "id": cells[0],
                "language": cells[1],
                "document_type": cells[2],
                "reader_background": cells[3],
                "prompt": cells[4],
            }
        )
    return entries


def _parse_bc_section(
    section_text: str, prefix: str, extra_fields: list[tuple[str, str]]
) -> list[dict]:
    """Strata B/C are bold-id entries: **B01** (KO) — topic / Prompt: ... / <extra fields>."""
    id_re = re.compile(rf"^\*\*({prefix}\d{{2}})\*\*\s*\((KO|EN)\)\s*—\s*(.*)$")
    prompt_re = re.compile(r"^Prompt:\s*(.*)$")
    field_res = [(name, re.compile(rf"^{re.escape(label)}:\s*(.*)$")) for name, label in extra_fields]

    entries: list[dict] = []
    current: dict | None = None

    for raw_line in section_text.splitlines():
        line = raw_line.strip()

        m = id_re.match(line)
        if m:
            if current is not None:
                entries.append(current)
            current = {
                "id": m.group(1),
                "language": m.group(2),
                "topic": m.group(3),
                "prompt": None,
            }
            for name, _ in extra_fields:
                current[name] = None
            continue

        if current is None:
            continue

        m = prompt_re.match(line)
        if m:
            current["prompt"] = m.group(1)
            continue

        for name, regex in field_res:
            m = regex.match(line)
            if m:
                current[name] = m.group(1)
                break

    if current is not None:
        entries.append(current)
    return entries


def parse_elicitation_set(path: Path) -> dict[str, list[dict]]:
    """Parse the frozen elicitation set and verify exactly 20/42/10 prompts.

    A silent parse miss here would corrupt the sample without anyone
    noticing until scoring — so every count and every required field is
    checked and any mismatch is a hard failure, not a warning.
    """
    if not path.exists():
        raise SystemExit(f"Error: elicitation set not found at {path}")

    text = path.read_text(encoding="utf-8")

    a_section = _extract_section(text, "## Stratum A", "## Stratum B")
    b_section = _extract_section(text, "## Stratum B", "## Stratum C")
    c_section = _extract_section(text, "## Stratum C", "## Counts")

    stratum_a = _parse_stratum_a(a_section)
    stratum_b = _parse_bc_section(
        b_section, "B", [("required_proposition", "Required proposition")]
    )
    stratum_c = _parse_bc_section(
        c_section,
        "C",
        [("mechanism", "Mechanism"), ("failure_condition", "Failure condition")],
    )

    errors = []
    counts = {"A": len(stratum_a), "B": len(stratum_b), "C": len(stratum_c)}
    for stratum, expected in EXPECTED_COUNTS.items():
        if counts[stratum] != expected:
            errors.append(
                f"Stratum {stratum}: parsed {counts[stratum]} prompts, expected {expected}"
            )

    for stratum_name, entries in (("A", stratum_a), ("B", stratum_b), ("C", stratum_c)):
        for entry in entries:
            missing = [k for k, v in entry.items() if v is None]
            if missing:
                errors.append(
                    f"Stratum {stratum_name} entry {entry.get('id')}: missing field(s) {missing}"
                )

    if errors:
        raise SystemExit(
            "Elicitation set parse self-check FAILED (this is not recoverable — "
            "fix the parser or the source file, never proceed with a partial sample):\n  "
            + "\n  ".join(errors)
        )

    return {"A": stratum_a, "B": stratum_b, "C": stratum_c}


# ---------------------------------------------------------------------------
# API call
# ---------------------------------------------------------------------------


def _compute_backoff(attempt: int) -> float:
    """AWS-style full-jitter exponential backoff. Not seeded by --seed —
    retry timing depends on live network conditions, so making it
    reproducible would be a lie; only generation ORDER is seeded."""
    ceiling = min(BACKOFF_CAP_SECONDS, BACKOFF_BASE_SECONDS * (2 ** (attempt - 1)))
    return random.uniform(0, ceiling)


def call_messages_api(
    api_key: str,
    system_prompt_text: str | None,
    user_prompt: str,
) -> tuple[dict | None, str | None, int]:
    """Returns (response_json, error_message, retry_count).

    Exactly one of (response_json, error_message) is non-None. A failed
    call after exhausting retries, or a non-retryable error, returns
    (None, "<message>", retry_count) — the caller records this as an
    explicit null result. It is never retried against a different arm's
    system prompt, and never silently dropped.
    """
    payload: dict = {
        "model": MODEL,
        "max_tokens": MAX_TOKENS,
        "thinking": THINKING_CONFIG,
        "messages": [{"role": "user", "content": user_prompt}],
    }
    # No temperature / top_p / top_k key: Field 4 — claude-sonnet-5 rejects
    # non-default values with a 400, so these are never free variables here.
    #
    # The OFF arm must send NO system field at all — not "system": "" —
    # because the whole experiment turns on the OFF arm being genuinely
    # uninstructed. An empty string is still a present field and some
    # backends may treat that differently from true omission, so we omit
    # the key entirely rather than risk it.
    if system_prompt_text is not None:
        payload["system"] = system_prompt_text

    body = json.dumps(payload).encode("utf-8")
    headers = {
        "x-api-key": api_key,
        "anthropic-version": ANTHROPIC_VERSION,
        "content-type": "application/json",
    }

    attempt = 0
    while True:
        req = urllib.request.Request(
            ANTHROPIC_API_URL, data=body, headers=headers, method="POST"
        )
        try:
            with urllib.request.urlopen(req, timeout=300) as resp:
                return json.loads(resp.read().decode("utf-8")), None, attempt
        except urllib.error.HTTPError as e:
            error_body = e.read().decode("utf-8", errors="replace")
            code = e.code
            retryable = code == 429 or 500 <= code < 600
            if retryable and attempt < MAX_RETRIES:
                attempt += 1
                delay = _compute_backoff(attempt)
                print(
                    f"[retry] HTTP {code} (attempt {attempt}/{MAX_RETRIES}), "
                    f"waiting {delay:.1f}s: {error_body[:300]}",
                    file=sys.stderr,
                )
                time.sleep(delay)
                continue
            return None, f"HTTP {code}: {error_body}", attempt
        except urllib.error.URLError as e:
            # Connection-level failure (DNS, refused, timeout) — no HTTP
            # status to inspect. Treated as retryable like a 5xx since it is
            # almost always transient, capped the same way.
            if attempt < MAX_RETRIES:
                attempt += 1
                delay = _compute_backoff(attempt)
                print(
                    f"[retry] network error (attempt {attempt}/{MAX_RETRIES}), "
                    f"waiting {delay:.1f}s: {e}",
                    file=sys.stderr,
                )
                time.sleep(delay)
                continue
            return None, f"URLError after {MAX_RETRIES} retries: {e}", attempt


def _extract_response_text(response_json: dict) -> str:
    parts = []
    for block in response_json.get("content", []):
        if block.get("type") == "text":
            parts.append(block.get("text", ""))
    return "".join(parts)


# ---------------------------------------------------------------------------
# Task planning
# ---------------------------------------------------------------------------


def build_tasks(elicitation: dict[str, list[dict]], strata: list[str], n: int) -> list[dict]:
    """Canonical (unshuffled) task list, in stratum-then-ID-then-index order."""
    tasks = []
    for stratum in ("A", "B", "C"):
        if stratum not in strata:
            continue
        for entry in elicitation[stratum]:
            for gen_index in range(n):
                tasks.append({"stratum": stratum, "entry": entry, "generation_index": gen_index})
    return tasks


def _prompt_metadata(stratum: str, entry: dict) -> dict:
    if stratum == "A":
        return {
            "document_type": entry["document_type"],
            "reader_background": entry["reader_background"],
        }
    if stratum == "B":
        return {"topic": entry["topic"], "required_proposition": entry["required_proposition"]}
    return {
        "topic": entry["topic"],
        "mechanism": entry["mechanism"],
        "failure_condition": entry["failure_condition"],
    }


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Generate documents for one arm of the pre-registered prose-skill A/B "
            "experiment by calling the Anthropic Messages API directly (stdlib "
            "urllib only, no anthropic SDK). Protocol: "
            "docs/research/prose-skill-ab-preregistration.md (Fields 3, 4, 5, 5b, "
            "8, 10). Prompts: docs/research/prose-skill-elicitation-set.md."
        )
    )
    parser.add_argument("--arm", required=True, choices=["off", "placebo", "on"])
    parser.add_argument(
        "--system-prompt-file",
        default=None,
        help="Path to the system prompt text file. Required for --arm placebo/on; "
        "must NOT be passed for --arm off.",
    )
    parser.add_argument(
        "--strata",
        default="A,B,C",
        help="Comma-separated subset of A,B,C to generate for (default: A,B,C).",
    )
    parser.add_argument("--n", type=int, default=3, help="Generations per prompt (default: 3).")
    parser.add_argument(
        "--seed",
        type=int,
        required=True,
        help="Required. Seeds the generation-order shuffle (Field 4: no time-based "
        "or other implicit randomness).",
    )
    parser.add_argument("--out", default="./generations", help="Output directory.")
    parser.add_argument(
        "--elicitation-file",
        default=str(DEFAULT_ELICITATION_FILE),
        help="Path to the frozen elicitation set markdown (default: the repo's copy).",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Parse prompts, print the plan (counts per stratum, total API calls, "
        "arm, seed), and exit WITHOUT calling the API. Works with no API key set.",
    )
    return parser


def _arm_stats(records: list[dict]) -> dict:
    """Truncation and output-token stats for the manifest, so Field 4's 5%
    void threshold and the thinking-spend manipulation check are readable
    without a separate analysis pass."""
    succeeded = [r for r in records if r["error"] is None]
    truncated = [r for r in succeeded if r["truncated"]]
    output_tokens = [
        r["usage"]["output_tokens"]
        for r in succeeded
        if r.get("usage") and "output_tokens" in r["usage"]
    ]
    total_output_tokens = sum(output_tokens)
    n_succeeded = len(succeeded)
    truncation_rate = (len(truncated) / n_succeeded) if n_succeeded else 0.0
    return {
        "total_generations": len(records),
        "succeeded": n_succeeded,
        "failed": len(records) - n_succeeded,
        "truncated_count": len(truncated),
        "truncated_rate": truncation_rate,
        "exceeds_truncation_void_threshold": truncation_rate > TRUNCATION_VOID_THRESHOLD,
        "total_output_tokens": total_output_tokens,
        "mean_output_tokens": (total_output_tokens / n_succeeded) if n_succeeded else 0.0,
    }


def main(argv: list[str] | None = None) -> int:
    parser = build_arg_parser()
    args = parser.parse_args(argv)

    if args.arm == "off" and args.system_prompt_file is not None:
        parser.error("--system-prompt-file must not be passed when --arm off")
    if args.arm != "off" and args.system_prompt_file is None:
        parser.error(f"--system-prompt-file is required when --arm {args.arm}")

    strata = [s.strip().upper() for s in args.strata.split(",") if s.strip()]
    invalid = [s for s in strata if s not in ("A", "B", "C")]
    if invalid:
        parser.error(f"--strata contains invalid value(s): {invalid} (allowed: A, B, C)")
    if not strata:
        parser.error("--strata must name at least one of A, B, C")

    # Parse + self-check the elicitation set BEFORE anything else — this is
    # what satisfies the "fail loudly on a silent parse miss" requirement,
    # and it runs on every invocation, dry-run or not.
    elicitation = parse_elicitation_set(Path(args.elicitation_file))

    tasks = build_tasks(elicitation, strata, args.n)
    counts_per_stratum = {
        s: len(elicitation[s]) * args.n for s in strata
    }
    total_planned = len(tasks)

    if args.dry_run:
        print("=== DRY RUN: generate_arm.py ===")
        print("Pre-registration: docs/research/prose-skill-ab-preregistration.md")
        print(
            f"Elicitation set parse self-check OK: "
            f"A={len(elicitation['A'])} B={len(elicitation['B'])} C={len(elicitation['C'])} "
            f"(expected 20/42/10)"
        )
        print()
        print(f"Arm: {args.arm}")
        print(f"System prompt file: {args.system_prompt_file}")
        print(f"Seed: {args.seed}")
        print(f"Strata selected: {','.join(strata)}")
        print(f"n per prompt: {args.n}")
        print(f"Model: {MODEL}")
        print(f"Thinking: {THINKING_CONFIG} (pinned on all arms, Field 4)")
        print(f"Temperature / top_p / top_k: {SAMPLING_NOT_SETTABLE} (Field 4 — never sent)")
        print(f"Max tokens: {MAX_TOKENS}")
        print()
        print("Counts per stratum (selected only):")
        for s in strata:
            n_prompts = len(elicitation[s])
            print(f"  {s}: {n_prompts} prompts x {args.n} = {counts_per_stratum[s]} calls")
        print()
        print(f"Total planned API calls: {total_planned}")
        print()
        print("No API calls made (dry run).")
        return 0

    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print(
            "Error: ANTHROPIC_API_KEY environment variable is not set. "
            "Never pass the key as a CLI argument (it would land in shell history).",
            file=sys.stderr,
        )
        return 1

    system_prompt_text = None
    if args.system_prompt_file is not None:
        sp_path = Path(args.system_prompt_file)
        if not sp_path.exists():
            print(f"Error: --system-prompt-file not found: {sp_path}", file=sys.stderr)
            return 1
        # Read exactly as-is — no strip/normalize — so the recorded
        # "system_prompt_text" in every record is byte-for-byte what was sent.
        system_prompt_text = sp_path.read_text(encoding="utf-8")

    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)

    # Generation order is randomized via the required --seed — never via
    # time.time() or any other implicit source. Only the CALL ORDER is
    # shuffled; each task keeps its originally-assigned generation_index
    # (0..n-1 per prompt) regardless of when it actually runs.
    order = list(range(len(tasks)))
    random.Random(args.seed).shuffle(order)

    started_at = datetime.now(timezone.utc).isoformat()
    record_filenames: list[str] = []
    records_for_manifest: list[dict] = []

    for position, task_idx in enumerate(order, start=1):
        task = tasks[task_idx]
        stratum = task["stratum"]
        entry = task["entry"]
        gen_index = task["generation_index"]
        prompt_id = entry["id"]

        print(
            f"[{position}/{total_planned}] arm={args.arm} {prompt_id} "
            f"gen={gen_index}",
            file=sys.stderr,
        )

        response_json, error, retries = call_messages_api(
            api_key=api_key,
            system_prompt_text=system_prompt_text,
            user_prompt=entry["prompt"],
        )

        record = {
            "prompt_id": prompt_id,
            "stratum": stratum,
            "language": entry["language"],
            "arm": args.arm,
            "generation_index": gen_index,
            "model": MODEL,
            "thinking": THINKING_CONFIG,
            "temperature": SAMPLING_NOT_SETTABLE,
            "top_p": SAMPLING_NOT_SETTABLE,
            "top_k": SAMPLING_NOT_SETTABLE,
            "max_tokens": MAX_TOKENS,
            "seed": args.seed,
            "system_prompt_file": args.system_prompt_file,
            "system_prompt_text": system_prompt_text,
            "user_prompt": entry["prompt"],
            "prompt_metadata": _prompt_metadata(stratum, entry),
            "content_blocks": None,
            "response_text": None,
            "usage": None,
            "stop_reason": None,
            "truncated": False,
            "response_id": None,
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "retries": retries,
            "error": None,
        }

        if response_json is not None:
            # Full content block list, not just concatenated text — thinking
            # blocks and text blocks must stay distinguishable by "type"
            # (Field 4 manipulation check needs thinking spend per arm).
            record["content_blocks"] = response_json.get("content")
            record["response_text"] = _extract_response_text(response_json)
            # Usage recorded verbatim, not cherry-picked: output_tokens
            # includes thinking tokens, needed whole for the thinking-spend
            # comparison across arms.
            record["usage"] = response_json.get("usage")
            record["stop_reason"] = response_json.get("stop_reason")
            record["truncated"] = record["stop_reason"] == "max_tokens"
            record["response_id"] = response_json.get("id")
        else:
            record["error"] = error

        filename = f"{args.arm}__{prompt_id}__gen{gen_index:02d}.json"
        (out_dir / filename).write_text(
            json.dumps(record, indent=2, ensure_ascii=False), encoding="utf-8"
        )
        record_filenames.append(filename)
        records_for_manifest.append(record)

    finished_at = datetime.now(timezone.utc).isoformat()

    stats = _arm_stats(records_for_manifest)

    manifest = {
        "arm": args.arm,
        "system_prompt_file": args.system_prompt_file,
        "strata": strata,
        "n_per_prompt": args.n,
        "seed": args.seed,
        "model": MODEL,
        "thinking": THINKING_CONFIG,
        "temperature": SAMPLING_NOT_SETTABLE,
        "top_p": SAMPLING_NOT_SETTABLE,
        "top_k": SAMPLING_NOT_SETTABLE,
        "max_tokens": MAX_TOKENS,
        "elicitation_file": str(args.elicitation_file),
        "started_at": started_at,
        "finished_at": finished_at,
        "total_planned": total_planned,
        "total_succeeded": stats["succeeded"],
        "total_failed": stats["failed"],
        "truncation_void_threshold": TRUNCATION_VOID_THRESHOLD,
        # Keyed by arm (this run's arm only — one invocation = one arm) so a
        # later merge across the three arms' manifests can combine these
        # dicts without renaming keys.
        "arm_stats": {args.arm: stats},
        "records": record_filenames,
    }
    (out_dir / "manifest.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8"
    )

    print(
        f"Done: {stats['succeeded']} succeeded, {stats['failed']} failed, "
        f"{total_planned} planned, "
        f"{stats['truncated_count']} truncated ({stats['truncated_rate']:.1%}). "
        f"Output: {out_dir}",
        file=sys.stderr,
    )
    if stats["exceeds_truncation_void_threshold"]:
        print(
            f"WARNING: truncation rate {stats['truncated_rate']:.1%} exceeds the "
            f"Field 4 void threshold ({TRUNCATION_VOID_THRESHOLD:.0%}) — this batch "
            f"is void per the pre-registration and must be re-run at a higher ceiling.",
            file=sys.stderr,
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
