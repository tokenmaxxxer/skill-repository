#!/usr/bin/env python3
"""Corpus lint for issue-100 progressive disclosure.

Asserts, for every skill in skills/:
  1. SKILL.md body (below the frontmatter) is at most 150 lines;
  2. if the skill has references/rules.md, the body carries a
     '## Rule index' whose ids map 1:1 (bijection) onto the ids
     extractable from references/rules.md — same multiset, no duplicates;
  3. every references/rules.md a body index points at exists and is
     non-empty.

Exit 0 with a summary on success; exit 1 listing every violation.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from pd_lib import split_frontmatter, parse_index, reference_ids  # noqa: E402

ROOT = os.path.join(os.path.dirname(__file__), "..", "skills")
THRESHOLD = 150


def check():
    errors = []
    checked = with_refs = 0
    for d in sorted(os.listdir(ROOT)):
        sd = os.path.join(ROOT, d)
        if not os.path.isdir(sd):
            continue
        path = os.path.join(sd, "SKILL.md")
        try:
            _, body = split_frontmatter(open(path, encoding="utf-8").read())
        except Exception as e:
            errors.append(f"{d}: unreadable/no frontmatter ({e})")
            continue
        checked += 1
        if len(body) > THRESHOLD:
            errors.append(f"{d}: body is {len(body)} lines (> {THRESHOLD})")
        ref_path = os.path.join(sd, "references", "rules.md")
        idx = parse_index(body)
        if idx is None and not os.path.exists(ref_path):
            continue
        with_refs += 1
        if not os.path.exists(ref_path):
            errors.append(f"{d}: has a rule index but references/rules.md is missing")
            continue
        if os.path.getsize(ref_path) == 0:
            errors.append(f"{d}: references/rules.md is empty")
            continue
        if idx is None:
            errors.append(f"{d}: references/rules.md exists but body has no '## Rule index'")
            continue
        if len(idx) != len(set(idx)):
            dupes = sorted({i for i in idx if idx.count(i) > 1})
            errors.append(f"{d}: duplicate index ids {dupes}")
        ref = reference_ids(open(ref_path, encoding="utf-8").read().split("\n"))
        if sorted(idx) != sorted(ref):
            missing = sorted(set(ref) - set(idx))
            extra = sorted(set(idx) - set(ref))
            errors.append(
                f"{d}: index<->references not a bijection "
                f"(index-only={extra}, references-only={missing})")
    return checked, with_refs, errors


def main():
    checked, with_refs, errors = check()
    if errors:
        print(f"FAIL: {len(errors)} violation(s)")
        for e in errors:
            print("  -", e)
        sys.exit(1)
    print(f"OK: {checked} skills checked, all bodies <= {THRESHOLD} lines; "
          f"{with_refs} index<->references/rules.md bijections verified.")


if __name__ == "__main__":
    main()
