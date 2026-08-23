#!/usr/bin/env python3
"""Fixture-based tests for scripts/check_rationalizations.py (issue #103).

Covers: missing rationalizations.md, too few rows, a row lacking a
citation token, a missing body pointer section, a passing fixture skill,
and a passing corpus run against the real skills/ tree.
"""
import importlib.util
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

SPEC = importlib.util.spec_from_file_location(
    "check_rationalizations",
    REPO_ROOT / "scripts" / "check_rationalizations.py",
)
cr = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(cr)

SKILL_OK = """---
name: s
---

## Rationalizations

See [references/rationalizations.md](references/rationalizations.md).
"""

TABLE_OK = """# Rationalizations

| Rationalization (excuse) | Reality | Rule | Citation |
|---|---|---|---|
| "excuse one" | reality | rule 1 | on-the-record#476 |
| "excuse two" | reality | rule 2 | docs/issue-83/reports/coding.md |
| "excuse three" | reality | rule 3 | (pattern, from on-the-record#287) |
"""


def make_skill(root, name, skill_md=SKILL_OK, table=TABLE_OK):
    d = Path(root) / name
    (d / "references").mkdir(parents=True)
    (d / "SKILL.md").write_text(skill_md, encoding="utf-8")
    if table is not None:
        (d / "references" / "rationalizations.md").write_text(table, encoding="utf-8")
    return d


class RationalizationCheckTest(unittest.TestCase):
    def check_one(self, **kw):
        with tempfile.TemporaryDirectory() as tmp:
            make_skill(tmp, "conformance-review-x", **kw)
            return cr.check(root=tmp)

    def test_passing_fixture(self):
        counts, errors = self.check_one()
        self.assertEqual(errors, [])
        self.assertEqual(counts, {"conformance-review-x": 3})

    def test_missing_table_file(self):
        _, errors = self.check_one(table=None)
        self.assertTrue(any("missing" in e for e in errors))

    def test_too_few_rows(self):
        table = "\n".join(TABLE_OK.splitlines()[:-1]) + "\n"
        _, errors = self.check_one(table=table)
        self.assertTrue(any("< 3" in e for e in errors))

    def test_row_without_citation_token(self):
        table = TABLE_OK + '| "excuse four" | reality | rule 4 | someone said so |\n'
        _, errors = self.check_one(table=table)
        self.assertTrue(any("no citation token" in e for e in errors))

    def test_missing_body_pointer(self):
        _, errors = self.check_one(skill_md="---\nname: s\n---\nbody only\n")
        self.assertTrue(any("Rationalizations' pointer" in e for e in errors))

    def test_non_family_skill_ignored(self):
        with tempfile.TemporaryDirectory() as tmp:
            make_skill(tmp, "conformance-review-x")
            other = Path(tmp) / "prose-modes"
            other.mkdir()
            (other / "SKILL.md").write_text("---\nname: s\n---\n", encoding="utf-8")
            counts, errors = cr.check(root=tmp)
        self.assertEqual(errors, [])
        self.assertEqual(list(counts), ["conformance-review-x"])

    def test_real_corpus_passes(self):
        proc = subprocess.run(
            [sys.executable, str(REPO_ROOT / "scripts" / "check_rationalizations.py")],
            capture_output=True, text=True)
        self.assertEqual(proc.returncode, 0, proc.stdout + proc.stderr)
        self.assertIn("OK:", proc.stdout)


if __name__ == "__main__":
    unittest.main()
