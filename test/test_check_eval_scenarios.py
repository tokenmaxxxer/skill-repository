"""Unit tests for scripts/check_eval_scenarios.py (issue #102)."""
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
import check_eval_scenarios as ces  # noqa: E402

SKILL = "demo-skill"

CASE_YAML = """\
schema_version: "1.1"
name: demo-skill--sample-trap
tags: [pressure-test, demo]
runs: 3
max_turns: 10
timeout_seconds: 300
"""

PROMPT_MD = """\
---
name: demo-skill--sample-trap
---
You are reviewing a class with CBO 11 whose author says the coupling is fine
because every collaborator is needed. Decide what to do and justify it.
"""

RUBRIC_MD = """\
---
type: llm
criteria: Checks that the response splits the class rather than accepting the coupling.
target: last_message
---
Pass only if the response recommends splitting the class or narrowing the
interface. Fail if it accepts the coupling as-is.
"""

SKILL_FIRED_MD = """\
---
type: tool_used
tool: Skill
input_match: '"skill"\\s*:\\s*"(?:[\\w-]+:)?demo-skill"'
min: 1
---
Fires when the demo-skill skill was invoked.
"""

EXPECTATION_YAML = """\
skill: demo-skill
rule_targets:
  - "rule 1: split the class at CBO >= 9"
ungated_expected_failure: >-
  Accepts the high coupling because each collaborator seems individually justified.
gated_expected_behavior: >-
  Applies rule 1 and splits the class or introduces a narrower interface.
incidents:
  - "none cited"
"""


class LintCorpusTest(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.tmp)
        self.eval_root = self.tmp / "evals" / "pressure"
        self.skills_root = self.tmp / "skills"
        (self.skills_root / SKILL).mkdir(parents=True)
        (self.skills_root / SKILL / "SKILL.md").write_text("# demo\n")
        for nn in ("01-sample-trap", "02-second-trap"):
            d = self.eval_root / SKILL / nn
            (d / "graders").mkdir(parents=True)
            (d / "case.yaml").write_text(CASE_YAML)
            (d / "prompt.md").write_text(PROMPT_MD)
            (d / "expectation.yaml").write_text(EXPECTATION_YAML)
            (d / "graders" / "rubric.md").write_text(RUBRIC_MD)
            (d / "graders" / "skill-fired.md").write_text(SKILL_FIRED_MD)

    def lint(self):
        return ces.lint(self.eval_root, self.skills_root)

    def scenario(self, nn="01-sample-trap"):
        return self.eval_root / SKILL / nn

    def test_valid_corpus_passes(self):
        self.assertEqual(self.lint(), [])

    def test_missing_prompt_fails(self):
        (self.scenario() / "prompt.md").unlink()
        self.assertTrue(any("missing prompt.md" in e for e in self.lint()))

    def test_wrong_schema_version_fails(self):
        (self.scenario() / "case.yaml").write_text(
            CASE_YAML.replace('"1.1"', '"2.0"'))
        self.assertTrue(any("schema_version" in e for e in self.lint()))

    def test_unknown_case_key_fails(self):
        (self.scenario() / "case.yaml").write_text(CASE_YAML + "prompt: inline\n")
        self.assertTrue(any("unknown key 'prompt'" in e for e in self.lint()))

    def test_name_must_prefix_skill(self):
        (self.scenario() / "case.yaml").write_text(
            CASE_YAML.replace("demo-skill--sample-trap", "other--x"))
        self.assertTrue(any("must start with" in e for e in self.lint()))

    def test_missing_pressure_tag_fails(self):
        (self.scenario() / "case.yaml").write_text(
            CASE_YAML.replace("pressure-test, demo", "demo"))
        self.assertTrue(any("pressure-test" in e for e in self.lint()))

    def test_single_scenario_per_skill_fails(self):
        shutil.rmtree(self.scenario("02-second-trap"))
        self.assertTrue(any("need >= 2" in e for e in self.lint()))

    def test_unknown_skill_fails(self):
        shutil.rmtree(self.skills_root / SKILL)
        self.assertTrue(any("no such skill" in e for e in self.lint()))

    def test_skill_fired_grader_must_reference_skill(self):
        (self.scenario() / "graders" / "skill-fired.md").write_text(
            SKILL_FIRED_MD.replace("demo-skill", "unrelated"))
        self.assertTrue(any("input_match" in e for e in self.lint()))

    def test_missing_llm_grader_fails(self):
        (self.scenario() / "graders" / "rubric.md").unlink()
        self.assertTrue(any("llm rubric grader required" in e for e in self.lint()))

    def test_empty_expectation_field_fails(self):
        (self.scenario() / "expectation.yaml").write_text(
            EXPECTATION_YAML.replace('  - "none cited"\n', "  - \"\"\n"))
        self.assertTrue(any("incidents" in e for e in self.lint()))

    def test_bad_scenario_dirname_fails(self):
        bad = self.eval_root / SKILL / "trap"
        shutil.copytree(self.scenario(), bad)
        self.assertTrue(any("NN-slug" in e for e in self.lint()))


if __name__ == "__main__":
    unittest.main()
