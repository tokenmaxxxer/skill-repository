#!/usr/bin/env python3
"""issue-100: split >150-body-line SKILL.md into rule-index body + references/rules.md.

Mechanical, validated per file:
  - frontmatter is byte-identical (never touched);
  - KEEP sections (Trigger / Procedure / Output shape / framing) stay in the body;
  - MOVE sections go verbatim into references/rules.md (extended, never clobbered);
  - the body gains a '## Rule index' whose ids map 1:1 onto ids extractable
    from references/rules.md (asserted here and by check_progressive_disclosure.py);
  - token preservation: every word token of the old file is findable in
    new SKILL.md ∪ references/rules.md (asserted, reported).

Usage: python3 scripts/split_progressive_disclosure.py [--dry-run]
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from pd_lib import (  # noqa: E402
    split_frontmatter, sections, is_keep, extract_rules,
    reference_ids, tokens, _one_line,
)

ROOT = os.path.join(os.path.dirname(__file__), "..", "skills")
THRESHOLD = 150

# Per-file: headings that would normally be KEEP but are forced to move
# (lowercased). pricing-research's report template is reference material.
OVERRIDE_MOVE = {
    "pricing-research": {"report format", "related skills",
                         "first: does this even need the procedure?"},
}

import re  # noqa: E402
from pd_lib import RULE_B, RULE_C  # noqa: E402


def _rule_tail_start(lines):
    """Index where full rule text begins inside a KEEP section, or None.

    A rule tail is a `### <n>.` block, or a top-level numbered item whose
    block carries a source citation (Procedure step lists carry none).
    """
    fence = False
    for i, ln in enumerate(lines):
        if ln.startswith("```"):
            fence = not fence
        if fence:
            continue
        if RULE_B.match(ln):
            return i
        if RULE_C.match(ln) and not ln.startswith(" "):
            j = i + 1
            while j < len(lines) and (lines[j].startswith((" ", "\t")) or lines[j] == ""):
                if re.match(r"^\s*-?\s*source:", lines[j], re.I):
                    return i
                j += 1
    return None


def split_skill(d, dry):
    path = os.path.join(ROOT, d, "SKILL.md")
    text = open(path, encoding="utf-8").read()
    fm, body = split_frontmatter(text)
    if len(body) <= THRESHOLD:
        return None
    secs = sections(body)
    forced = OVERRIDE_MOVE.get(d, set())
    keep, move = [], []
    for head, lines in secs:
        if is_keep(head) and not (head and head[3:].strip().lower() in forced):
            tail = _rule_tail_start(lines)
            if tail is not None:
                keep.append((head, lines[:tail]))
                title = head[3:].strip() if head else "body"
                move.append((f"## Rules (moved from “{title}”)", lines[tail:]))
            else:
                keep.append((head, lines))
        else:
            move.append((head, lines))

    # Build references/rules.md content: moved sections verbatim,
    # unparseable sections get an [S#] anchor for section-level indexing.
    ref_lines = [
        f"# {d} — full rules and citations",
        "",
        "Moved verbatim from SKILL.md by issue-100 progressive disclosure.",
        "The SKILL.md body carries the rule index; read this file when a",
        "matched rule's full text, citation, or counter-example is needed.",
        "",
    ]
    s_count = 0
    s_index = []
    for head, lines in move:
        rules = extract_rules(([head] if head else []) + lines)
        if rules:
            if head:
                ref_lines.append(head)
            ref_lines.extend(lines)
        else:
            s_count += 1
            title = head[3:].strip() if head else "untitled"
            ref_lines.append(f"## [S{s_count}] {title}")
            ref_lines.extend(lines)
            s_index.append(f"- S{s_count} — {_one_line(title)} → references/rules.md")
    # Extract ids from the assembled reference file itself, so index ids are
    # by construction the same ids the corpus lint will re-extract.
    index = []
    for r in extract_rules(ref_lines):
        stmt = r["cond"] + ((" → " + r["verdict"]) if r["verdict"] and r["verdict"] != r["cond"] else "")
        index.append(f"- {r['id']} — {stmt}")
    index += s_index

    if not index:
        return ("skip-no-move", d, len(body), len(body))

    new_body = []
    for head, lines in keep:
        if head:
            new_body.append(head)
        new_body.extend(lines)
    while new_body and new_body[-1] == "":
        new_body.pop()
    new_body += ["", "## Rule index", "",
                 "Full rule text, citations, and counter-examples:",
                 "`references/rules.md` in this skill's directory — read it when a",
                 "matched rule's detail is needed.", ""]
    new_body += index
    new_body.append("")

    ref_dir = os.path.join(ROOT, d, "references")
    ref_path = os.path.join(ref_dir, "rules.md")
    ref_text = "\n".join(ref_lines) + "\n"
    if os.path.exists(ref_path):
        raise SystemExit(f"{d}: references/rules.md already exists — refusing to clobber")

    new_text = "\n".join(fm + new_body)

    # Validation 1: bijection index ↔ references
    idx_ids = [ln.split(" — ")[0][2:] for ln in index]
    ref_ids = reference_ids(ref_text.split("\n"))
    if sorted(idx_ids) != sorted(ref_ids) or len(idx_ids) != len(set(idx_ids)):
        raise SystemExit(f"{d}: index/reference id mismatch\n  idx={idx_ids}\n  ref={ref_ids}")

    # Validation 2: token preservation (old ⊆ new ∪ references)
    lost = tokens(text) - (tokens(new_text) + tokens(ref_text))
    if lost:
        raise SystemExit(f"{d}: token loss: {dict(lost)}")

    if not dry:
        os.makedirs(ref_dir, exist_ok=True)
        open(ref_path, "w", encoding="utf-8").write(ref_text)
        open(path, "w", encoding="utf-8").write(new_text)
    return ("split", d, len(body), len(new_body), len(idx_ids))


def main():
    dry = "--dry-run" in sys.argv
    results = []
    for d in sorted(os.listdir(ROOT)):
        if not os.path.isdir(os.path.join(ROOT, d)):
            continue
        r = split_skill(d, dry)
        if r:
            results.append(r)
    over_after = 0
    for r in results:
        if r[0] == "split":
            _, d, before, after, n = r
            flag = " STILL>150" if after > THRESHOLD else ""
            if after > THRESHOLD:
                over_after += 1
            print(f"{d}: {before} -> {after} body lines, {n} index entries{flag}")
        else:
            print(f"{r[1]}: SKIPPED (nothing movable), body={r[2]}")
    print(f"\n{len([r for r in results if r[0]=='split'])} split, "
          f"{over_after} still over {THRESHOLD}. Token preservation: PASS (asserted per file).")


if __name__ == "__main__":
    main()
