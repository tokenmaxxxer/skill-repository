#!/usr/bin/env python3
"""Tests for scripts/check_description_enrichment.py (issue #99).

Covers the five acceptance criteria on fixture descriptions, plus a
corpus-wide test asserting the whole skills/ tree is enriched.
"""
import importlib.util
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SPEC = importlib.util.spec_from_file_location(
    "check_description_enrichment",
    REPO_ROOT / "scripts" / "check_description_enrichment.py",
)
lint = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(lint)

GOOD = (
    'Use when tuning a stage scaling curve or monster balance. '
    'Trigger on "stage scaling", "balance curve", "몬스터 밸런스 잡아줘". '
    'Do NOT use for core-loop design (use game-design-core-loop-and-progression).'
)
ALL_NAMES = ["game-growth-system-design", "game-design-core-loop-and-progression"]
SIBLINGS = ["game-design-core-loop-and-progression"]


def check(description, siblings=SIBLINGS, name="game-growth-system-design"):
    return lint.check_description(name, description, siblings, ALL_NAMES)


class CheckDescriptionEnrichmentTest(unittest.TestCase):
    def test_good_description_passes(self):
        self.assertEqual(check(GOOD), [])

    def test_must_open_with_use_when(self):
        bad = "A skill for balance. " + GOOD
        self.assertTrue(any("OPEN" in r for r in check(bad)), check(bad))

    def test_needs_three_quoted_phrasings(self):
        bad = GOOD.replace('"stage scaling", ', "")
        self.assertTrue(any("phrasing" in r for r in check(bad)), check(bad))

    def test_needs_korean_phrasing(self):
        bad = GOOD.replace('"몬스터 밸런스 잡아줘"', '"monster balance"')
        self.assertTrue(any("Korean" in r for r in check(bad)), check(bad))

    def test_do_not_clause_required_with_siblings(self):
        bad = GOOD.split("Do NOT")[0]
        self.assertTrue(any("Do NOT" in r for r in check(bad)), check(bad))

    def test_do_not_clause_not_required_without_siblings(self):
        no_do_not = GOOD.split("Do NOT")[0]
        self.assertEqual(check(no_do_not, siblings=[]), [])

    def test_do_not_clause_must_name_concrete_skill(self):
        bad = GOOD.replace(
            "(use game-design-core-loop-and-progression)", "(use something else)"
        )
        self.assertTrue(any("concrete alternative" in r for r in check(bad)), check(bad))

    def test_length_cap(self):
        bad = GOOD + " x" * 600
        self.assertTrue(any("chars" in r for r in check(bad)), check(bad))

    def test_sdo_verbs_banned(self):
        bad = GOOD + " Produces a balance spec."
        self.assertTrue(any("SDO" in r for r in check(bad)), check(bad))

    def test_family_of(self):
        self.assertEqual(lint.family_of("game-growth-system-design"), "game")
        self.assertEqual(lint.family_of("api-design-error-design"), "api-design")
        self.assertIsNone(lint.family_of("diagnose-first"))
        # market-recon must not match the "marketing" family
        self.assertIsNone(lint.family_of("market-recon"))

    def test_full_repo_tree_is_enriched(self):
        skills_dir = REPO_ROOT / "skills"
        skill_dirs = sorted(p for p in skills_dir.iterdir() if p.is_dir())
        all_names = [p.name for p in skill_dirs]
        families = {}
        for name in all_names:
            fam = lint.family_of(name)
            if fam:
                families.setdefault(fam, []).append(name)
        violations = []
        checked = 0
        for skill_dir in skill_dirs:
            skill_md = skill_dir / "SKILL.md"
            if not skill_md.is_file():
                continue
            checked += 1
            frontmatter = lint.extract_frontmatter(skill_md.read_text(encoding="utf-8"))
            description = lint.parse_description(frontmatter) if frontmatter else None
            fam = lint.family_of(skill_dir.name)
            siblings = [n for n in families.get(fam, []) if n != skill_dir.name] if fam else []
            for reason in lint.check_description(skill_dir.name, description, siblings, all_names):
                violations.append((skill_dir.name, reason))
        self.assertGreater(checked, 0)
        self.assertEqual(violations, [], f"violations found: {violations}")


if __name__ == "__main__":
    unittest.main()
