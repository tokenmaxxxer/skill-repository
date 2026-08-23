#!/usr/bin/env python3
"""Lint for issue #99: description enrichment conformance.

Checks every skills/*/SKILL.md description: field for the five
acceptance criteria of issue #99:

  1. Opens with the Use-when condition sentence (a trigger-marker
     phrase must start the description, so the condition stays first).
  2. Carries >= 3 quoted user phrasings ("..."), at least one of which
     contains Korean (Hangul) text — these are the retrieval vocabulary
     the spawn pipeline's BM25 index matches task text against.
  3. Carries a "Do NOT use" clause naming a concrete alternative skill
     (checked only for skills that have >= 1 sibling in the same family
     prefix, where confusion risk exists; the clause must contain the
     directory name of at least one other existing skill).
  4. Stays under 1024 characters.
  5. Never describes the procedure/output — the SDO trap: the verbs
     returns/produces/outputs/generates/emits are banned from
     descriptions (a summarizing description lets the agent skip the
     body).

Exits 0 printing "<n> skills checked" when clean; exits 1 printing one
`path: reason` diagnostic per violation otherwise.
"""
import re
import sys
from pathlib import Path

# Family prefixes (issue #99: siblings = same family prefix). A skill
# belongs to a family iff its directory name equals the prefix or starts
# with "<prefix>-". Families with >= 2 members require a Do-NOT clause.
FAMILY_PREFIXES = (
    "api-design",
    "architecture",
    "brand-design",
    "business-model-design",
    "capacity-planning",
    "conformance-review",
    "content-strategy",
    "customer-support",
    "data-engineering",
    "data-modeling",
    "decision",
    "defect-verification",
    "design-artifact",
    "devrel",
    "finance-unit-economics",
    "game",
    "growth-analytics",
    "implementation",
    "incident-response",
    "knowledge-management",
    "knowledge-work",
    "kubernetes-workload",
    "legal-compliance",
    "localization",
    "market-analysis",
    "marketing",
    "ml-engineering",
    "negotiation",
    "observability",
    "org-design",
    "partnerships-bd",
    "pricing",
    "product-discovery",
    "refactoring-legacy",
    "release-engineering",
    "risk-management",
    "sales",
    "secure-coding",
    "technical-feasibility",
    "technical-writing",
    "test",
    "upstream-defect-report",
    "user-discovery",
    "ux-engineering",
    "verify",
)

TRIGGER_OPENERS = (
    "use when",
    "use this",
    "use whenever",
    "use while",
    "use to",
    "use as",
    "use it",
    "invoke when",
    "invoke this",
    "invoke whenever",
)

SDO_VERB_RE = re.compile(r"\b(returns?|produces?|outputs?|generates?|emits?)\b", re.IGNORECASE)
QUOTED_RE = re.compile(r'"([^"]+)"')
HANGUL_RE = re.compile(r"[가-힣]")
MAX_DESCRIPTION_CHARS = 1024
MIN_PHRASINGS = 3


def family_of(name):
    for prefix in FAMILY_PREFIXES:
        if name == prefix or name.startswith(prefix + "-"):
            return prefix
    return None


def extract_frontmatter(text):
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---", 4)
    if end == -1:
        return None
    return text[4:end]


def parse_description(frontmatter):
    m = re.search(r"^description:[ \t]*(.*)$", frontmatter, re.MULTILINE)
    if m is None:
        return None
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
        return " ".join(lines).strip()
    return value.strip('"').strip("'")


def check_description(name, description, sibling_names, all_names):
    """Return a list of reason strings for one skill's description.

    sibling_names: other skills in the same family (may be empty).
    all_names: every skill directory name in the corpus.
    """
    reasons = []
    if not description:
        return ["missing or empty description:"]

    lowered = description.lower()
    if not any(lowered.startswith(opener) for opener in TRIGGER_OPENERS):
        reasons.append(
            'description must OPEN with the Use-when condition sentence '
            '(e.g. "Use when ...") — the condition stays first'
        )

    phrasings = QUOTED_RE.findall(description)
    if len(phrasings) < MIN_PHRASINGS:
        reasons.append(
            f"description has {len(phrasings)} quoted user phrasing(s); "
            f"needs >= {MIN_PHRASINGS} (in double quotes)"
        )
    if not any(HANGUL_RE.search(p) for p in phrasings):
        reasons.append(
            "description has no Korean (Hangul) quoted user phrasing; needs >= 1"
        )

    if sibling_names:
        m = re.search(r"\bDo NOT\b", description)
        if m is None:
            reasons.append(
                f"description has no \"Do NOT use\" clause (family "
                f"'{family_of(name)}' has {len(sibling_names)} sibling(s); "
                f"confusion risk exists)"
            )
        else:
            tail = description[m.start():]
            named = [n for n in all_names if n != name and n in tail]
            if not named:
                reasons.append(
                    'the "Do NOT" clause names no concrete alternative skill '
                    "(must contain another skill's directory name)"
                )

    if len(description) >= MAX_DESCRIPTION_CHARS:
        reasons.append(
            f"description is {len(description)} chars; must stay under "
            f"{MAX_DESCRIPTION_CHARS}"
        )

    sdo = SDO_VERB_RE.search(description)
    if sdo:
        reasons.append(
            f"description contains banned procedure/output verb "
            f"'{sdo.group(0)}' (SDO trap: never describe the procedure/output)"
        )

    return reasons


def main():
    repo_root = Path(__file__).resolve().parent.parent
    skills_dir = repo_root / "skills"
    skill_dirs = sorted(p for p in skills_dir.iterdir() if p.is_dir()) if skills_dir.is_dir() else []
    all_names = [p.name for p in skill_dirs]

    families = {}
    for name in all_names:
        fam = family_of(name)
        if fam:
            families.setdefault(fam, []).append(name)

    violations = []
    checked = 0
    for skill_dir in skill_dirs:
        skill_md = skill_dir / "SKILL.md"
        if not skill_md.is_file():
            continue
        checked += 1
        frontmatter = extract_frontmatter(skill_md.read_text(encoding="utf-8"))
        description = parse_description(frontmatter) if frontmatter else None
        fam = family_of(skill_dir.name)
        siblings = [n for n in families.get(fam, []) if n != skill_dir.name] if fam else []
        for reason in check_description(skill_dir.name, description, siblings, all_names):
            violations.append((skill_dir.name, reason))

    if violations:
        print(f"{len(violations)} violation(s) found ({checked} skills checked):")
        for name, reason in violations:
            print(f"  skills/{name}/SKILL.md: {reason}")
        return 1
    print(f"{checked} skills checked")
    return 0


if __name__ == "__main__":
    sys.exit(main())
