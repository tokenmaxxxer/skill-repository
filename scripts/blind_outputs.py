#!/usr/bin/env python3
"""Blinding script required by the pre-registration's Field 8.

Protocol source of truth: docs/research/prose-skill-ab-preregistration.md,
Field 8 ("Blinding") — arm labels are stripped before scoring, and the
skill's author (who also runs the mechanical detectors) must not be able to
infer arm from the file being scored.

Reads one or more generate_arm.py output directories (one JSON file per
generation, plus manifest.json in each), strips every tell that could
reveal which arm produced a document, and writes scrambled copies under
opaque ids to a new directory. The id -> arm mapping goes to a SEPARATE
file the scoring step must never read.

Pass every arm's output directory in a SINGLE invocation (--in accepts
multiple paths). Running the script twice into the same --out would reset
the opaque-id numbering and overwrite UNBLINDING_KEY.json, silently losing
the first run's mapping — this is why --in is multi-valued instead of the
script being designed to be run once per arm.

Usage:
    python3 blind_outputs.py \\
        --in generations/off generations/placebo generations/on \\
        --out blinded --seed 7
"""

from __future__ import annotations

import argparse
import json
import random
import sys
from datetime import datetime, timezone
from pathlib import Path

DEFAULT_KEY_FILENAME = "UNBLINDING_KEY.json"

# Fields that would let a scorer infer the arm just by opening the file.
# "arm" is the direct label; the system-prompt fields are the content tell
# (OFF/PLACEBO/ON system prompts differ in wording, so their mere presence
# or text gives the arm away even with the "arm" key removed).
TELL_FIELDS = ("arm", "system_prompt_file", "system_prompt_text")


def _load_generation_records(in_dirs: list[Path]) -> list[tuple[Path, dict]]:
    records = []
    for in_dir in in_dirs:
        if not in_dir.is_dir():
            raise SystemExit(f"Error: --in path is not a directory: {in_dir}")
        for path in sorted(in_dir.glob("*.json")):
            if path.name == "manifest.json":
                continue
            data = json.loads(path.read_text(encoding="utf-8"))
            if "arm" not in data:
                # A file in this directory that isn't a generation record is a
                # sign something is wrong with --in — fail loudly rather than
                # silently skip it, mirroring generate_arm.py's parse self-check.
                raise SystemExit(
                    f"Error: {path} has no 'arm' field — is --in pointing at a "
                    f"generate_arm.py output directory?"
                )
            records.append((path, data))
    if not records:
        raise SystemExit(f"Error: no generation records found under {in_dirs}")
    # Canonical order across all input directories, independent of the order
    # --in paths were given in — full path string is a stable sort key.
    records.sort(key=lambda pr: str(pr[0]))
    return records


def _strip_tells(record: dict) -> dict:
    return {k: v for k, v in record.items() if k not in TELL_FIELDS}


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Strip arm labels and other tells from generate_arm.py output and "
            "write scrambled, opaquely-named copies for blind scoring, per the "
            "pre-registration's Field 8 (docs/research/prose-skill-ab-"
            "preregistration.md). Writes the id->arm mapping to a separate "
            "UNBLINDING_KEY.json that scoring must not read."
        )
    )
    parser.add_argument(
        "--in",
        dest="in_dirs",
        required=True,
        nargs="+",
        help="One or more directories of generate_arm.py output (JSON records + "
        "manifest.json in each). Pass every arm's directory here in one call.",
    )
    parser.add_argument("--out", required=True, help="Directory to write blinded copies to.")
    parser.add_argument(
        "--seed",
        type=int,
        required=True,
        help="Required. Makes the blinding order and opaque-id assignment reproducible.",
    )
    parser.add_argument(
        "--unblinding-key",
        default=None,
        help=(
            "Path for the id->arm mapping. Defaults to UNBLINDING_KEY.json next "
            "to (a sibling of, not inside) --out, so a scoring loop that globs "
            "--out for *.json never picks it up."
        ),
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite an existing --out directory or unblinding-key file. "
        "Without this, a non-empty --out or an existing key file is refused, "
        "since blinding twice into the same place silently loses the "
        "previous run's mapping.",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_arg_parser()
    args = parser.parse_args(argv)

    in_dirs = [Path(p) for p in args.in_dirs]

    out_dir = Path(args.out)
    key_path = (
        Path(args.unblinding_key)
        if args.unblinding_key
        else out_dir.parent / DEFAULT_KEY_FILENAME
    )

    if not args.force:
        if out_dir.exists() and any(out_dir.iterdir()):
            parser.error(
                f"--out {out_dir} already exists and is non-empty. Re-blinding "
                f"into it would overwrite {key_path} and lose the previous "
                f"mapping. Pass --force to overwrite, or choose a fresh --out."
            )
        if key_path.exists():
            parser.error(
                f"{key_path} already exists. Pass --force to overwrite it, or "
                f"choose a different --unblinding-key path."
            )

    out_dir.mkdir(parents=True, exist_ok=True)

    records = _load_generation_records(in_dirs)

    # Deterministic given --seed: sort inputs into a canonical order first
    # (directory listing order is not guaranteed stable across filesystems),
    # then shuffle that canonical order with a seeded RNG.
    order = list(range(len(records)))
    random.Random(args.seed).shuffle(order)

    key_entries: dict[str, dict] = {}
    width = len(str(len(records)))

    for position, idx in enumerate(order, start=1):
        source_path, record = records[idx]
        opaque_id = f"item_{position:0{width}d}"

        blinded = _strip_tells(record)
        blinded["id"] = opaque_id
        (out_dir / f"{opaque_id}.json").write_text(
            json.dumps(blinded, indent=2, ensure_ascii=False), encoding="utf-8"
        )

        key_entries[opaque_id] = {
            "arm": record["arm"],
            "source_file": source_path.name,
            "source_dir": str(source_path.parent),
        }

    key_file = {
        "_warning": (
            "This file maps blinded ids back to arm labels. Do NOT open it "
            "before scoring is complete — doing so defeats the blinding."
        ),
        "seed": args.seed,
        "in_dirs": [str(d) for d in in_dirs],
        "out_dir": str(out_dir),
        "created_at": datetime.now(timezone.utc).isoformat(),
        "mapping": key_entries,
    }
    key_path.write_text(json.dumps(key_file, indent=2, ensure_ascii=False), encoding="utf-8")

    print(f"Blinded {len(records)} record(s) into {out_dir}", file=sys.stderr)
    print(
        f"WARNING: {key_path} contains the id->arm mapping — "
        f"do not open it before scoring is complete.",
        file=sys.stderr,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
