#!/usr/bin/env python3
"""Check every skills/*/SKILL.md for conformant frontmatter, trigger
sentence, and per-rule citations. Single entry point for skill conformance
(issue #58): re-implemented against this repo's own schema, not ported from
any external tool.

A skill is conformant iff its SKILL.md starts with a YAML frontmatter
block (delimited by `---` lines) that contains:
  - a non-empty `name:` equal to the skill's directory name
  - a non-empty `description:` that contains a usage/trigger clause
    (a "Use when ..." sentence, or an established synonym marker — see
    TRIGGER_MARKERS)
  - a non-empty `axis:` or `axes:` field, when the skill declares
    `rule_count_floor:` (i.e. is a numbered-decision-rule skill)

and, when its body has a `## Rules` section of `### N. <title>` blocks,
every such numbered rule block contains at least one `source: <https?://
URL>` citation line.

Exits 0 (printing "<n> skills checked") when every skill is conformant,
including the vacuous "0 skills checked" case for an empty skills/ dir.
Exits 1, printing one `path:line: reason` diagnostic per violation,
otherwise.

Optional --manifest <path> adds an additive, opt-in check: every skill
directory name listed in the manifest file (one per line, blank lines
and lines starting with `#` ignored) must have a SKILL.md body
containing `## Trigger`, `## Procedure`, and `## Output shape` headings
(any order). Skills not listed in the manifest are unaffected by this
check.

Optional --require-use-when-and-source <path> adds an additive, opt-in
check: every skill directory name listed in that file (same one-per-
line format as --manifest) must have a `description:` containing the
literal substring "use when" (case-insensitive) and a SKILL.md body
citing at least one `source:`/`Source:` URL anywhere (a strictly
narrower re-check than the always-on per-rule citation check above).
"""
import argparse
import re
import sys
from pathlib import Path

PROCEDURE_HEADINGS = ("## Trigger", "## Procedure", "## Output shape")

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

SOURCE_LINE_RE = re.compile(r"(?im)^.*source:.*https?://\S+")
RULE_HEADING_RE = re.compile(r"^### *(\d+)\.", re.MULTILINE)
NEXT_TOP_HEADING_RE = re.compile(r"\n## [^#]")
RULE_SOURCE_RE = re.compile(r"(?im)^\s*-?\s*source:\s*https?://\S+")


def load_manifest(manifest_path):
    names = set()
    for line in manifest_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        names.add(line)
    return names


def check_procedure_sections(skill_md):
    text = skill_md.read_text(encoding="utf-8")
    missing = [h for h in PROCEDURE_HEADINGS if h not in text]
    if missing:
        return [(1, f"missing procedure section(s): {', '.join(missing)}")]
    return []


def line_of(text, index):
    return text.count("\n", 0, index) + 1


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


def has_axis_field(frontmatter):
    """True iff `axis:` has a non-empty scalar, or `axes:` has a non-empty
    scalar/count or at least one `- item` list entry beneath it."""
    axis = parse_field(frontmatter, "axis")
    if axis:
        return True
    m = re.search(r"^axes:[ \t]*(.*)$", frontmatter, re.MULTILINE)
    if m is None:
        return False
    value = m.group(1).strip()
    if value:
        return True
    for line in frontmatter[m.end():].splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith("-"):
            return True
        break
    return False


def check_use_when_and_source(skill_md, description):
    reasons = []
    if description is None or "use when" not in description.lower():
        reasons.append((1, 'description: missing a literal "Use when" clause'))
    text = skill_md.read_text(encoding="utf-8")
    if not SOURCE_LINE_RE.search(text):
        reasons.append((1, "missing at least one 'source: <https?:// URL>' citation"))
    return reasons


def check_rule_sources(text):
    """Every numbered `### N. ...` block under a `## Rules` section must
    carry its own `source: <https?:// URL>` citation line."""
    marker = "\n## Rules"
    start = text.find(marker)
    if start == -1 and text.startswith("## Rules"):
        start = 0
    else:
        start += 1  # skip the leading \n, point at "## Rules"
    if start < 0:
        return []
    section_start = start + len("## Rules")
    tail = text[section_start:]
    end_match = NEXT_TOP_HEADING_RE.search(tail)
    section = tail[: end_match.start()] if end_match else tail
    section_offset = section_start

    heads = list(RULE_HEADING_RE.finditer(section))
    reasons = []
    for i, head in enumerate(heads):
        block_start = head.end()
        block_end = heads[i + 1].start() if i + 1 < len(heads) else len(section)
        block = section[block_start:block_end]
        if not RULE_SOURCE_RE.search(block):
            abs_index = section_offset + head.start()
            reasons.append(
                (line_of(text, abs_index), f"rule {head.group(1)}: missing 'source: <https?:// URL>' line")
            )
    return reasons


def check_skill(skill_md, dirname):
    text = skill_md.read_text(encoding="utf-8")
    frontmatter = extract_frontmatter(text)
    if frontmatter is None:
        return [(1, "missing frontmatter")]

    reasons = []

    name_match = re.search(r"^name:[ \t]*(.*)$", frontmatter, re.MULTILINE)
    name = parse_field(frontmatter, "name")
    name_line = line_of(text, 4 + name_match.start()) if name_match else 1
    if not name:
        reasons.append((name_line, "missing or empty name:"))
    elif name != dirname:
        reasons.append((name_line, f"name: '{name}' does not match directory '{dirname}'"))

    desc_match = re.search(r"^description:[ \t]*(.*)$", frontmatter, re.MULTILINE)
    description = parse_field(frontmatter, "description")
    desc_line = line_of(text, 4 + desc_match.start()) if desc_match else 1
    if not description:
        reasons.append((desc_line, "missing or empty description:"))
    else:
        lowered = description.lower()
        if not any(marker in lowered for marker in TRIGGER_MARKERS):
            reasons.append((desc_line, 'description: has no "Use when ..." trigger sentence'))

    rule_count_floor = parse_field(frontmatter, "rule_count_floor")
    if rule_count_floor and not has_axis_field(frontmatter):
        reasons.append((1, "missing or empty axis:/axes: (required alongside rule_count_floor:)"))

    reasons += check_rule_sources(text)

    return reasons


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", type=Path, default=None)
    parser.add_argument("--require-use-when-and-source", type=Path, default=None)
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parent.parent
    skills_dir = repo_root / "skills"

    manifest_names = load_manifest(args.manifest) if args.manifest else set()
    use_when_source_names = (
        load_manifest(args.require_use_when_and_source)
        if args.require_use_when_and_source
        else set()
    )

    skill_dirs = sorted(p for p in skills_dir.iterdir() if p.is_dir()) if skills_dir.is_dir() else []

    violations = []
    checked = 0
    for skill_dir in skill_dirs:
        skill_md = skill_dir / "SKILL.md"
        if not skill_md.is_file():
            violations.append((skill_dir.name, [(1, "missing SKILL.md")]))
            continue
        checked += 1
        reasons = check_skill(skill_md, skill_dir.name)
        if skill_dir.name in manifest_names:
            reasons += check_procedure_sections(skill_md)
        if skill_dir.name in use_when_source_names:
            text = skill_md.read_text(encoding="utf-8")
            frontmatter = extract_frontmatter(text)
            description = parse_field(frontmatter, "description") if frontmatter else None
            reasons += check_use_when_and_source(skill_md, description)
        if reasons:
            violations.append((skill_dir.name, reasons))

    if violations:
        total = sum(len(reasons) for _, reasons in violations)
        print(f"{total} violation(s) found in {len(violations)} skill(s) ({checked} skills checked):")
        for name, reasons in sorted(violations):
            for line, reason in sorted(reasons):
                print(f"  skills/{name}/SKILL.md:{line}: {reason}")
        return 1

    print(f"{checked} skills checked")
    return 0


if __name__ == "__main__":
    sys.exit(main())
