#!/usr/bin/env python3
"""Schema lint for the pressure-test eval scenario corpus (issue #102).

Validates evals/pressure/<skill>/<NN>-<slug>/ scenario dirs against the
`claude plugin eval` case layout (schema_version 1.1: case.yaml config,
prompt.md task, graders/*.md) plus the repo-local expectation.yaml
documentation contract. Exits non-zero with per-file findings on any
violation. Pure stdlib + PyYAML; runnable without the eval harness.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
EVAL_ROOT = REPO_ROOT / "evals" / "pressure"
SKILLS_ROOT = REPO_ROOT / "skills"

CASE_ALLOWED_KEYS = {
    "schema_version", "name", "tags", "runs", "max_turns",
    "timeout_seconds", "allowed_tools",
}
CASE_REQUIRED_KEYS = {
    "schema_version", "name", "tags", "runs", "max_turns", "timeout_seconds",
}
EXPECTATION_REQUIRED_KEYS = {
    "skill", "rule_targets", "ungated_expected_failure",
    "gated_expected_behavior", "incidents",
}
MIN_SCENARIOS_PER_SKILL = 2

FRONTMATTER_RE = re.compile(r"\A---\n(.*?)\n---\n(.*)\Z", re.DOTALL)


def split_frontmatter(text):
    """Return (frontmatter_dict_or_None, body)."""
    m = FRONTMATTER_RE.match(text)
    if not m:
        return None, text
    try:
        fm = yaml.safe_load(m.group(1))
    except yaml.YAMLError:
        return None, m.group(2)
    return (fm if isinstance(fm, dict) else None), m.group(2)


def check_case_yaml(path, skill, errors):
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError) as e:
        errors.append(f"{path}: unreadable or invalid YAML ({e})")
        return
    if not isinstance(data, dict):
        errors.append(f"{path}: top level must be a mapping")
        return
    keys = set(data)
    for k in sorted(CASE_REQUIRED_KEYS - keys):
        errors.append(f"{path}: missing required key '{k}'")
    for k in sorted(keys - CASE_ALLOWED_KEYS):
        errors.append(f"{path}: unknown key '{k}'")
    if data.get("schema_version") != "1.1":
        errors.append(f"{path}: schema_version must be the string \"1.1\"")
    name = data.get("name")
    if not (isinstance(name, str) and name.startswith(skill + "--")):
        errors.append(f"{path}: name must start with '{skill}--'")
    tags = data.get("tags")
    if not (isinstance(tags, list) and "pressure-test" in tags):
        errors.append(f"{path}: tags must be a list containing 'pressure-test'")
    for field in ("runs", "max_turns", "timeout_seconds"):
        v = data.get(field)
        if not (isinstance(v, int) and v >= 1):
            errors.append(f"{path}: {field} must be an integer >= 1")


def check_prompt_md(path, errors):
    fm, body = split_frontmatter(path.read_text(encoding="utf-8"))
    if fm is None or not isinstance(fm.get("name"), str) or not fm["name"]:
        errors.append(f"{path}: needs YAML frontmatter with a non-empty 'name'")
    if len(body.strip()) < 40:
        errors.append(f"{path}: prompt body missing or too short to be a real task")


def check_graders(gdir, skill, errors):
    if not gdir.is_dir():
        errors.append(f"{gdir}: missing graders/ directory")
        return
    graders = sorted(gdir.glob("*.md"))
    if not graders:
        errors.append(f"{gdir}: no grader files")
        return
    types = []
    for g in graders:
        fm, body = split_frontmatter(g.read_text(encoding="utf-8"))
        if fm is None or "type" not in fm:
            errors.append(f"{g}: needs frontmatter with a 'type'")
            continue
        gtype = fm["type"]
        types.append(gtype)
        if gtype == "llm":
            if not (isinstance(fm.get("criteria"), str) and fm["criteria"].strip()):
                errors.append(f"{g}: llm grader needs non-empty 'criteria'")
            if len(body.strip()) < 20:
                errors.append(f"{g}: llm grader rubric body missing")
        elif gtype == "tool_used":
            if fm.get("tool") != "Skill":
                errors.append(f"{g}: tool_used grader must target tool: Skill")
            im = fm.get("input_match", "")
            if not (isinstance(im, str) and skill in im):
                errors.append(f"{g}: input_match must reference '{skill}'")
            if fm.get("min", 1) < 1:
                errors.append(f"{g}: skill-fired grader needs min >= 1")
        else:
            allowed = {"regex", "tool_order", "file_exists", "baseline"}
            if gtype not in allowed:
                errors.append(f"{g}: unknown grader type '{gtype}'")
    if "llm" not in types:
        errors.append(f"{gdir}: at least one llm rubric grader required")
    if "tool_used" not in types:
        errors.append(f"{gdir}: skill-fired tool_used grader required (ablation indicator)")


def check_expectation(path, skill, errors):
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError) as e:
        errors.append(f"{path}: unreadable or invalid YAML ({e})")
        return
    if not isinstance(data, dict):
        errors.append(f"{path}: top level must be a mapping")
        return
    for k in sorted(EXPECTATION_REQUIRED_KEYS - set(data)):
        errors.append(f"{path}: missing required key '{k}'")
    if data.get("skill") != skill:
        errors.append(f"{path}: skill must be '{skill}'")
    for field in ("rule_targets", "incidents"):
        v = data.get(field)
        if not (isinstance(v, list) and v and all(isinstance(x, str) and x.strip() for x in v)):
            errors.append(f"{path}: {field} must be a non-empty list of non-empty strings")
    for field in ("ungated_expected_failure", "gated_expected_behavior"):
        v = data.get(field)
        if not (isinstance(v, str) and len(v.strip()) >= 20):
            errors.append(f"{path}: {field} must be a substantive string")


def lint(eval_root=EVAL_ROOT, skills_root=SKILLS_ROOT):
    errors = []
    if not eval_root.is_dir():
        return [f"{eval_root}: eval corpus directory missing"]
    skill_dirs = sorted(p for p in eval_root.iterdir() if p.is_dir())
    if not skill_dirs:
        return [f"{eval_root}: no skill scenario directories"]
    for sdir in skill_dirs:
        skill = sdir.name
        if not (skills_root / skill / "SKILL.md").is_file():
            errors.append(f"{sdir}: no such skill '{skill}' in skills/")
        scenarios = sorted(p for p in sdir.iterdir() if p.is_dir())
        if len(scenarios) < MIN_SCENARIOS_PER_SKILL:
            errors.append(
                f"{sdir}: {len(scenarios)} scenario(s); need >= {MIN_SCENARIOS_PER_SKILL}")
        for sc in scenarios:
            if not re.match(r"^\d{2}-[a-z0-9-]+$", sc.name):
                errors.append(f"{sc}: dir name must be NN-slug")
            for fname, checker in (
                ("case.yaml", lambda p: check_case_yaml(p, skill, errors)),
                ("prompt.md", lambda p: check_prompt_md(p, errors)),
                ("expectation.yaml", lambda p: check_expectation(p, skill, errors)),
            ):
                f = sc / fname
                if f.is_file():
                    checker(f)
                else:
                    errors.append(f"{sc}: missing {fname}")
            check_graders(sc / "graders", skill, errors)
    return errors


def main():
    errors = lint()
    if errors:
        for e in errors:
            print(f"FAIL {e}")
        print(f"\n{len(errors)} violation(s)")
        return 1
    skills = sorted(p.name for p in EVAL_ROOT.iterdir() if p.is_dir())
    total = sum(1 for p in EVAL_ROOT.glob("*/*") if p.is_dir())
    print(f"OK {len(skills)} skills, {total} scenarios, 0 violations")
    return 0


if __name__ == "__main__":
    sys.exit(main())
