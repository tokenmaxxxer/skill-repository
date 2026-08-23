#!/usr/bin/env python3
"""One-shot frontmatter normalization for skills/*/SKILL.md.

Text-level surgery only: never re-serializes an entire frontmatter
block through a YAML dumper. For each non-conformant skill (per
check_skill_conformance.py), it either:
  - prepends a new frontmatter block (no-frontmatter case), or
  - inserts `name:`/`description:` lines into an existing frontmatter
    block, preserving any `axis:`/`rule_count_floor:` fields verbatim
    and the delimiter/body bytes untouched, or
  - rewrites only a wrong `name:` value's line in place.

Already-conformant skills (name == dirname, description has a
usage/trigger clause) are left byte-for-byte untouched.
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from check_skill_conformance import (  # noqa: E402
    extract_frontmatter,
    parse_field,
    parse_custom_field,
    check_skill,
    TRIGGER_MARKERS,
)


def has_trigger_clause(description):
    lowered = description.lower()
    return any(marker in lowered for marker in TRIGGER_MARKERS)


def derive_title(text):
    m = re.search(r"^#\s+(.+)$", text, re.MULTILINE)
    if m:
        return m.group(1).strip()
    return None


def derive_description(title, axis, dirname):
    subject = title if title else dirname.replace("-", " ")
    desc = f"Use when you need guidance on {subject}."
    if axis:
        desc += f" Applies to the {axis} axis."
    return desc


def normalize_file(skill_md, dirname):
    text = skill_md.read_text(encoding="utf-8")
    frontmatter = extract_frontmatter(text)

    if frontmatter is None:
        # No-frontmatter case: prepend a new block, body untouched.
        title = derive_title(text)
        description = derive_description(title, None, dirname)
        new_block = f"---\nname: {dirname}\ndescription: {description}\n---\n\n"
        return new_block + text, True

    changed = False
    name = parse_field(frontmatter, "name")
    description = parse_field(frontmatter, "description")

    fm_end = text.find("\n---", 4)  # index of the '\n' preceding the closing '---'
    body_from_close = text[fm_end:]  # '\n---' onward, untouched

    if name is None:
        # axis-only case: insert name + description right after opening '---'.
        title = derive_title(text)
        axis = parse_custom_field(frontmatter, "axis")
        new_description = derive_description(title, axis, dirname)
        insertion = f"name: {dirname}\ndescription: {new_description}\n"
        # Rebuild explicitly: opening delimiter, inserted fields, then the
        # original frontmatter body (axis/rule_count_floor etc.) unchanged.
        original_fm_body = frontmatter[1:] if frontmatter.startswith("\n") else frontmatter
        new_text = "---\n" + insertion + original_fm_body + body_from_close
        return new_text, True
    elif name != dirname:
        # name mismatch: rewrite only that line's value in place.
        new_frontmatter, n = re.subn(
            r"^(name:)[ \t]*.*$",
            rf"\1 {dirname}",
            frontmatter,
            count=1,
            flags=re.MULTILINE,
        )
        assert n == 1
        changed = True
        frontmatter = new_frontmatter

    if description is None or not description.strip():
        title = derive_title(text)
        axis = parse_custom_field(frontmatter, "axis")
        new_description = derive_description(title, axis, dirname)
        if re.search(r"^description:", frontmatter, re.MULTILINE):
            frontmatter = re.sub(
                r"^(description:)[ \t]*.*$",
                rf"\1 {new_description}",
                frontmatter,
                count=1,
                flags=re.MULTILINE,
            )
        else:
            frontmatter = frontmatter.rstrip("\n") + f"\ndescription: {new_description}\n"
        changed = True
    elif not has_trigger_clause(description):
        # Description exists but has no usage/trigger clause: prepend one,
        # replacing the whole field (block scalar or inline) in place so no
        # stale continuation lines are left behind.
        title = derive_title(text)
        prefix = f"Use when applying {title or dirname.replace('-', ' ')}. "
        new_description = prefix + description
        field_pattern = re.compile(
            r"^description:[ \t]*(?:>-|>|\|-|\|)?[ \t]*\n(?:[ \t]+.*\n?)*"
            r"|^description:[ \t]*.*\n?",
            re.MULTILINE,
        )
        frontmatter, n = field_pattern.subn(
            f"description: {new_description}\n", frontmatter, count=1
        )
        assert n == 1
        changed = True

    if not changed:
        return text, False

    new_text = "---\n" + frontmatter + body_from_close
    return new_text, True


def main():
    repo_root = Path(__file__).resolve().parent.parent
    skills_dir = repo_root / "skills"

    normalized = []
    skipped = []
    for skill_dir in sorted(p for p in skills_dir.iterdir() if p.is_dir()):
        skill_md = skill_dir / "SKILL.md"
        if not skill_md.is_file():
            continue
        reasons = check_skill(skill_md, skill_dir.name)
        if not reasons:
            skipped.append(skill_dir.name)
            continue
        new_text, changed = normalize_file(skill_md, skill_dir.name)
        if changed:
            skill_md.write_text(new_text, encoding="utf-8")
            normalized.append(skill_dir.name)

    print(f"{len(normalized)} skill(s) normalized, {len(skipped)} already conformant")
    return 0


if __name__ == "__main__":
    sys.exit(main())
