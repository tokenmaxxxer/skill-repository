#!/usr/bin/env python3
"""BM25-style token-overlap sanity check for issue #99.

Reproduces the live retrieval failure: a game-balance task text scored
ZERO game skills in top-8 (top hits were legal-compliance and finance
via the spurious token "band"). After enrichment, the game skill
descriptions must carry the concrete domain nouns the task text carries.

Asserts, over skills/*/SKILL.md descriptions:
  - game-growth-system-design and game-design-core-loop-and-progression
    each share >= 3 content tokens with the task text, and
  - both rank above finance-unit-economics-ltv-cac-band by naive
    tf overlap (sum over shared tokens of description term frequency).

Exits 0 with a ranking printout on success, 1 on failure.
"""
import re
import sys
from collections import Counter
from pathlib import Path

TASK_TEXT = (
    "per-stage monster damage/HP scaling for the growth system: "
    "balance derivation so each stage's monsters land in the 8-12 band "
    "of hits-to-kill, damage and HP scaling per stage"
)

STOPWORDS = {
    "a", "an", "and", "are", "as", "at", "be", "by", "each", "for", "from",
    "in", "is", "it", "its", "no", "not", "of", "on", "or", "per", "so",
    "that", "the", "this", "to", "with", "when", "use", "s",
}

MUST_RANK = ("game-growth-system-design", "game-design-core-loop-and-progression")
MUST_BEAT = "finance-unit-economics-ltv-cac-band"
MIN_SHARED = 3


def tokenize(text):
    return [t for t in re.findall(r"[a-z0-9]+", text.lower()) if t not in STOPWORDS and not t.isdigit()]


def parse_description(text):
    if not text.startswith("---\n"):
        return ""
    end = text.find("\n---", 4)
    frontmatter = text[4:end]
    m = re.search(r"^description:[ \t]*(.*)$", frontmatter, re.MULTILINE)
    if m is None:
        return ""
    value = m.group(1).strip()
    if value in ("", ">-", "|", ">", "|-"):
        lines = []
        for line in frontmatter[m.end():].splitlines():
            if line.startswith(("  ", "\t")):
                lines.append(line.strip())
            elif line.strip() == "":
                continue
            else:
                break
        return " ".join(lines)
    return value


def main():
    repo_root = Path(__file__).resolve().parent.parent
    task_tokens = set(tokenize(TASK_TEXT))
    scores = {}
    shared = {}
    for skill_dir in sorted((repo_root / "skills").iterdir()):
        skill_md = skill_dir / "SKILL.md"
        if not skill_md.is_file():
            continue
        tf = Counter(tokenize(parse_description(skill_md.read_text(encoding="utf-8"))))
        common = task_tokens & set(tf)
        shared[skill_dir.name] = common
        scores[skill_dir.name] = sum(tf[t] for t in common)

    ranking = sorted(scores, key=scores.get, reverse=True)
    print("Task:", TASK_TEXT)
    print("\nTop 8 by naive tf overlap:")
    for name in ranking[:8]:
        print(f"  {scores[name]:3d}  {name}  shared={sorted(shared[name])}")
    print(f"\n{MUST_BEAT}: score={scores[MUST_BEAT]}, shared={sorted(shared[MUST_BEAT])}")

    ok = True
    for name in MUST_RANK:
        n = len(shared[name])
        print(f"{name}: score={scores[name]}, shared({n})={sorted(shared[name])}")
        if n < MIN_SHARED:
            print(f"FAIL: {name} shares {n} < {MIN_SHARED} content tokens with the task text")
            ok = False
        if scores[name] <= scores[MUST_BEAT]:
            print(f"FAIL: {name} ({scores[name]}) does not rank above {MUST_BEAT} ({scores[MUST_BEAT]})")
            ok = False
    if ok:
        print("\nRetrieval sanity: PASS")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
