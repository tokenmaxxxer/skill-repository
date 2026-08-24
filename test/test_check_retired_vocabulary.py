#!/usr/bin/env python3
"""Fixture-based tests for scripts/check_retired_vocabulary.py (issue #109).

Covers: a retired term matching (case-insensitive and case-sensitive),
an allowlisted line passing, a clean fixture corpus, and a zero-match
run against the real skills/ tree with the committed vocabulary file.
"""
import importlib.util
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

SPEC = importlib.util.spec_from_file_location(
    "check_retired_vocabulary",
    REPO_ROOT / "scripts" / "check_retired_vocabulary.py",
)
crv = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(crv)

VOCAB_FIXTURE = """\
# fixture vocabulary
i|\\bdraft-reported\\b
c|\\bPRODUCES\\b
i|\\broles/[\\w-]+\\b
ALLOW|roles/specs/|LIVE: fixture pointer
"""


def write_fixture(root, name, text):
    d = root / "skills" / name
    d.mkdir(parents=True)
    (d / "SKILL.md").write_text(text, encoding="utf-8")


class RetiredVocabularyTest(unittest.TestCase):
    def run_check(self, skills):
        tmp = Path(tempfile.mkdtemp())
        vocab = tmp / "vocab.txt"
        vocab.write_text(VOCAB_FIXTURE, encoding="utf-8")
        for name, text in skills.items():
            write_fixture(tmp, name, text)
        errors, files, n_pat, n_allow = crv.check(
            root=str(tmp / "skills"), vocab=str(vocab))
        return errors

    def test_retired_term_flagged_case_insensitive(self):
        errors = self.run_check({"a": "in the Draft-Reported state\n"})
        self.assertEqual(len(errors), 1)
        self.assertIn("draft-reported", errors[0])

    def test_case_sensitive_term(self):
        self.assertEqual(
            self.run_check({"a": "the PRODUCES field\n"}) and 1, 1)
        self.assertEqual(self.run_check({"a": "the produces field\n"}), [])

    def test_allowlist_exempts_verified_live_term(self):
        self.assertEqual(
            self.run_check({"a": "see roles/specs/x.spec.json\n"}), [])
        self.assertEqual(
            len(self.run_check({"a": "see roles/product.json\n"})), 1)

    def test_clean_corpus_passes(self):
        self.assertEqual(self.run_check({"a": "nothing retired here\n"}), [])

    def test_real_corpus_zero_matches(self):
        errors, files, n_pat, n_allow = crv.check()
        self.assertEqual(errors, [])
        self.assertGreaterEqual(files, 273)
        self.assertGreater(n_pat, 0)
        self.assertGreater(n_allow, 0)


if __name__ == "__main__":
    unittest.main()
