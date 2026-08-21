#!/usr/bin/env python3
"""Check every skills/*/SKILL.md for conformant frontmatter.

A skill is conformant iff its SKILL.md starts with a YAML frontmatter
block (delimited by `---` lines) that contains:
  - a non-empty `name:` equal to the skill's directory name
  - a non-empty `description:` that contains a usage/trigger clause
    (not just a bare restatement of the title)

Exits 0 (printing "<n> skills checked") when every skill is conformant,
including the vacuous "0 skills checked" case for an empty skills/ dir.
Exits 1, listing every violator (path + reason), otherwise.
"""
import re
import sys
from pathlib import Path

TRIGGER_MARKERS = (
    "use when",
    "use this",
    "use whenever",
    "use while",
    "use to",
    "use as",
    "use it",
    "trigger",
    "invoke when",
    "invoke this",
    "invoke whenever",
)


def extract_frontmatter(text):
    if not text.startswith("---\n") and text != "---":
        return None
    end = text.find("\n---", 4)
    if end == -1:
        return None
    return text[4:end]


def parse_field(frontmatter, field):
    # Matches "field: value" or "field: >-" / "field: |" block scalars.
    m = re.search(rf"^{field}:[ \t]*(.*)$", frontmatter, re.MULTILINE)
    if m is None:
        return None
    value = m.group(1).strip()
    if value in ("", ">-", "|", ">", "|-"):
        # Block scalar: collect indented continuation lines.
        lines = frontmatter[m.end():].splitlines()
        block_lines = []
        for line in lines:
            if line.startswith(("  ", "\t")):
                block_lines.append(line.strip())
            elif line.strip() == "":
                continue
            else:
                break
        return " ".join(block_lines).strip()
    return value.strip('"').strip("'")


def check_skill(skill_md, dirname):
    text = skill_md.read_text(encoding="utf-8")
    frontmatter = extract_frontmatter(text)
    if frontmatter is None:
        return ["missing frontmatter"]

    reasons = []

    name = parse_field(frontmatter, "name")
    if not name:
        reasons.append("missing or empty name:")
    elif name != dirname:
        reasons.append(f"name: '{name}' does not match directory '{dirname}'")

    description = parse_field(frontmatter, "description")
    if not description:
        reasons.append("missing or empty description:")
    else:
        lowered = description.lower()
        if not any(marker in lowered for marker in TRIGGER_MARKERS):
            reasons.append("description: has no usage/trigger clause")

    return reasons


def main():
    repo_root = Path(__file__).resolve().parent.parent
    skills_dir = repo_root / "skills"

    skill_dirs = sorted(p for p in skills_dir.iterdir() if p.is_dir()) if skills_dir.is_dir() else []

    violations = []
    checked = 0
    for skill_dir in skill_dirs:
        skill_md = skill_dir / "SKILL.md"
        if not skill_md.is_file():
            violations.append((skill_dir.name, ["missing SKILL.md"]))
            continue
        checked += 1
        reasons = check_skill(skill_md, skill_dir.name)
        if reasons:
            violations.append((skill_dir.name, reasons))

    if violations:
        print(f"{len(violations)} violation(s) found ({checked} skills checked):")
        for name, reasons in violations:
            for reason in reasons:
                print(f"  skills/{name}/SKILL.md: {reason}")
        return 1

    print(f"{checked} skills checked")
    return 0


if __name__ == "__main__":
    sys.exit(main())
