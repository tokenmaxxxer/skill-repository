#!/usr/bin/env python3
"""Corpus lint for issue-103 rationalization tables.

For every skill in the judgment-gate families (conformance-review-*,
defect-verification-*, implementation-*), asserts:

  1. references/rationalizations.md exists and carries a markdown table
     with at least MIN_ROWS data rows (4 columns: excuse, reality, rule,
     citation);
  2. every row's citation cell carries a citation token — an issue/PR
     reference (``#<digits>``) or a record path (a token containing
     ``/`` or ending in ``.md``); "(pattern, from <source>)" rows must
     still name such a token inside the parenthetical;
  3. the SKILL.md body contains a ``## Rationalizations`` section
     pointing at references/rationalizations.md (placement policy:
     full table in references/, short pointer in the body, keeping
     bodies under the progressive-disclosure 150-line cap).

Exit 0 with a per-skill row-count summary on success; exit 1 listing
every violation.
"""
import os
import re
import sys

ROOT = os.path.join(os.path.dirname(__file__), "..", "skills")
FAMILY_PREFIXES = ("conformance-review-", "defect-verification-", "implementation-")
MIN_ROWS = 3
CITATION_RE = re.compile(r"#\d+|[\w.\-]+/[\w.\-/]+|\S+\.md\b")


def table_rows(text):
    """Return the data rows (list of cell-lists) of the first 4-column table."""
    rows = []
    for line in text.splitlines():
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 4:
            continue
        if set(cells[0]) <= {"-", " ", ":"}:  # separator row
            continue
        if cells[0].lower().startswith("rationalization"):  # header row
            continue
        rows.append(cells)
    return rows


def check(root=ROOT):
    errors = []
    counts = {}
    for d in sorted(os.listdir(root)):
        if not d.startswith(FAMILY_PREFIXES):
            continue
        sd = os.path.join(root, d)
        if not os.path.isdir(sd):
            continue
        ref = os.path.join(sd, "references", "rationalizations.md")
        if not os.path.exists(ref):
            errors.append(f"{d}: references/rationalizations.md is missing")
            continue
        rows = table_rows(open(ref, encoding="utf-8").read())
        counts[d] = len(rows)
        if len(rows) < MIN_ROWS:
            errors.append(f"{d}: only {len(rows)} table row(s) (< {MIN_ROWS})")
        for i, cells in enumerate(rows, 1):
            if not CITATION_RE.search(cells[3]):
                errors.append(
                    f"{d}: row {i} citation cell has no citation token "
                    f"(#issue or path): {cells[3]!r}")
        skill_md = open(os.path.join(sd, "SKILL.md"), encoding="utf-8").read()
        if "## Rationalizations" not in skill_md:
            errors.append(f"{d}: SKILL.md body lacks a '## Rationalizations' pointer section")
        elif "references/rationalizations.md" not in skill_md:
            errors.append(f"{d}: '## Rationalizations' section does not point at references/rationalizations.md")
    if not counts:
        errors.append("no judgment-gate family skills found under skills/")
    return counts, errors


def main():
    counts, errors = check()
    if errors:
        print(f"FAIL: {len(errors)} violation(s)")
        for e in errors:
            print("  -", e)
        sys.exit(1)
    total = sum(counts.values())
    print(f"OK: {len(counts)} judgment-gate skills carry a Rationalizations "
          f"table ({total} cited rows, min {min(counts.values())}/skill).")
    for d, n in sorted(counts.items()):
        print(f"  {d}: {n} rows")


if __name__ == "__main__":
    main()
