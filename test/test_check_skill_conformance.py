#!/usr/bin/env python3
"""Fixture-based tests for scripts/check_skill_conformance.py (issue #58).

Builds a throwaway skills/ tree per test and runs check_skill() directly
against fixture SKILL.md files, covering the three violation classes named
in issue #58's acceptance: a missing axis, a missing Use-when trigger
sentence, and a numbered rule with no source: line.
"""
import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SPEC = importlib.util.spec_from_file_location(
    "check_skill_conformance", REPO_ROOT / "scripts" / "check_skill_conformance.py"
)
conformance = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(conformance)

VALID_SKILL = """\
---
name: sample-skill
description: Use when deciding something and you need a decision rule.
axis: sample-axis
rule_count_floor: 1
---

# Sample Skill

## Rules

### 1. Sample rule title
- condition: something is true.
- choice: do the thing.
- why: because.
- source: https://example.com/sample-source
"""


def write_skill(tmp_path, dirname, content):
    skill_dir = tmp_path / dirname
    skill_dir.mkdir(parents=True, exist_ok=True)
    (skill_dir / "SKILL.md").write_text(content, encoding="utf-8")
    return skill_dir / "SKILL.md"


class CheckSkillConformanceTest(unittest.TestCase):
    def setUp(self):
        self._tmpdir = tempfile.TemporaryDirectory()
        self.tmp_path = Path(self._tmpdir.name)
        self.addCleanup(self._tmpdir.cleanup)

    def test_valid_fixture_has_no_violations(self):
        skill_md = write_skill(self.tmp_path, "sample-skill", VALID_SKILL)
        self.assertEqual(conformance.check_skill(skill_md, "sample-skill"), [])

    def test_missing_axis_is_flagged_with_line(self):
        content = VALID_SKILL.replace("axis: sample-axis\n", "")
        skill_md = write_skill(self.tmp_path, "sample-skill", content)
        reasons = conformance.check_skill(skill_md, "sample-skill")
        messages = [r for _, r in reasons]
        self.assertTrue(
            any("axis" in m for m in messages),
            f"expected an axis violation, got: {messages}",
        )

    def test_missing_use_when_sentence_is_flagged_with_line(self):
        content = VALID_SKILL.replace(
            "description: Use when deciding something and you need a decision rule.",
            "description: Handles decisions about something.",
        )
        skill_md = write_skill(self.tmp_path, "sample-skill", content)
        reasons = conformance.check_skill(skill_md, "sample-skill")
        matches = [(line, m) for line, m in reasons if "trigger sentence" in m]
        self.assertEqual(len(matches), 1)
        line, _ = matches[0]
        self.assertEqual(line, 3)  # the description: line in the fixture

    def test_rule_with_no_source_is_flagged_with_line(self):
        content = VALID_SKILL.replace(
            "- source: https://example.com/sample-source\n", ""
        )
        skill_md = write_skill(self.tmp_path, "sample-skill", content)
        reasons = conformance.check_skill(skill_md, "sample-skill")
        matches = [(line, m) for line, m in reasons if "rule 1" in m and "source" in m]
        self.assertEqual(len(matches), 1)
        line, _ = matches[0]
        self.assertEqual(content.splitlines()[line - 1].strip(), "### 1. Sample rule title")

    def test_valid_globs_field_has_no_violations(self):
        content = VALID_SKILL.replace(
            "rule_count_floor: 1\n",
            'rule_count_floor: 1\nglobs:\n  - "**/*.yaml"\n  - "**/requirements*.txt"\n',
        )
        skill_md = write_skill(self.tmp_path, "sample-skill", content)
        self.assertEqual(conformance.check_skill(skill_md, "sample-skill"), [])

    def test_malformed_globs_scalar_is_flagged(self):
        content = VALID_SKILL.replace(
            "rule_count_floor: 1\n",
            "rule_count_floor: 1\nglobs: **/*.yaml\n",
        )
        skill_md = write_skill(self.tmp_path, "sample-skill", content)
        reasons = conformance.check_skill(skill_md, "sample-skill")
        self.assertTrue(any("inline scalar" in m for _, m in reasons), reasons)

    def test_globs_pattern_without_wildcard_is_flagged(self):
        content = VALID_SKILL.replace(
            "rule_count_floor: 1\n",
            'rule_count_floor: 1\nglobs:\n  - "package.json"\n',
        )
        skill_md = write_skill(self.tmp_path, "sample-skill", content)
        reasons = conformance.check_skill(skill_md, "sample-skill")
        self.assertTrue(any("no glob wildcard" in m for _, m in reasons), reasons)

    def test_empty_globs_list_is_flagged(self):
        content = VALID_SKILL.replace(
            "rule_count_floor: 1\n",
            "rule_count_floor: 1\nglobs:\n",
        )
        skill_md = write_skill(self.tmp_path, "sample-skill", content)
        reasons = conformance.check_skill(skill_md, "sample-skill")
        self.assertTrue(any("empty or malformed" in m for _, m in reasons), reasons)

    def test_full_repo_tree_is_conformant(self):
        skills_dir = REPO_ROOT / "skills"
        violations = []
        checked = 0
        for skill_dir in sorted(p for p in skills_dir.iterdir() if p.is_dir()):
            skill_md = skill_dir / "SKILL.md"
            if not skill_md.is_file():
                violations.append((skill_dir.name, [(1, "missing SKILL.md")]))
                continue
            checked += 1
            reasons = conformance.check_skill(skill_md, skill_dir.name)
            if reasons:
                violations.append((skill_dir.name, reasons))
        self.assertGreater(checked, 0)
        self.assertEqual(violations, [], f"violations found: {violations}")


if __name__ == "__main__":
    unittest.main()
