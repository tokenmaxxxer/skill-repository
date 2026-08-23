#!/usr/bin/env python3
"""Fixture-based tests for scripts/check_progressive_disclosure.py (issue #100).

Covers: body over 150 lines, index<->references bijection break (missing
and extra ids), missing/empty references/rules.md, and a passing corpus run
against the real skills/ tree.
"""
import importlib.util
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))
import pd_lib  # noqa: E402

SPEC = importlib.util.spec_from_file_location(
    "check_progressive_disclosure",
    REPO_ROOT / "scripts" / "check_progressive_disclosure.py",
)
pdcheck = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(pdcheck)

FM = "---\nname: s\ndescription: Use when testing.\n---\n"

BODY_OK = """# s

## Trigger
x

## Rule index

- 1.1 — when a, do b
- 1.2 — when c, do d
"""

REFS_OK = """# s — full rules

## Rules

1. when a, do b.
   source: https://example.com

2. when c, do d.
   source: https://example.com
"""


class Fixture:
    def __init__(self, body, refs):
        self.tmp = tempfile.TemporaryDirectory()
        root = Path(self.tmp.name) / "skills" / "s"
        root.mkdir(parents=True)
        (root / "SKILL.md").write_text(FM + body)
        if refs is not None:
            (root / "references").mkdir()
            (root / "references" / "rules.md").write_text(refs)
        self.skills_root = str(Path(self.tmp.name) / "skills")


def run_check(body, refs):
    fx = Fixture(body, refs)
    old = pdcheck.ROOT
    pdcheck.ROOT = fx.skills_root
    try:
        return pdcheck.check()[2]
    finally:
        pdcheck.ROOT = old


class TestProgressiveDisclosure(unittest.TestCase):
    def test_passing_fixture(self):
        self.assertEqual(run_check(BODY_OK, REFS_OK), [])

    def test_body_over_150(self):
        body = BODY_OK + "\n" * 160
        errs = run_check(body, REFS_OK)
        self.assertTrue(any("> 150" in e for e in errs))

    def test_bijection_break_extra_index_id(self):
        body = BODY_OK.replace("- 1.2 — when c, do d", "- 1.2 — when c, do d\n- 9.9 — ghost rule")
        errs = run_check(body, REFS_OK)
        self.assertTrue(any("bijection" in e and "9.9" in e for e in errs))

    def test_bijection_break_missing_index_id(self):
        body = BODY_OK.replace("- 1.2 — when c, do d\n", "")
        errs = run_check(body, REFS_OK)
        self.assertTrue(any("bijection" in e and "1.2" in e for e in errs))

    def test_missing_references_file(self):
        errs = run_check(BODY_OK, None)
        self.assertTrue(any("missing" in e for e in errs))

    def test_empty_references_file(self):
        errs = run_check(BODY_OK, "")
        self.assertTrue(any("empty" in e for e in errs))

    def test_token_counter(self):
        self.assertFalse(pd_lib.tokens("a b c") - (pd_lib.tokens("c b") + pd_lib.tokens("a x")))
        self.assertTrue(pd_lib.tokens("a b c") - pd_lib.tokens("a b"))

    def test_real_corpus_passes(self):
        r = subprocess.run(
            [sys.executable, str(REPO_ROOT / "scripts" / "check_progressive_disclosure.py")],
            capture_output=True, text=True)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)


if __name__ == "__main__":
    unittest.main()
