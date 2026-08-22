---
code_under_review:
  - scripts/check_skill_conformance.py
  - test/test_check_skill_conformance.py
loop_state: landed
type: feature
breaking: false
verdict: pass
---

# Implementation report — issue #58

## What was done

Re-implemented (not ported — the deanpeters/Product-Manager-Skills reference
is license-unclear) a skill-schema + citation validator, against this repo's
own frontmatter/rule conventions, and wired it into
`scripts/check_skill_conformance.py` as the single entry point:

- Frontmatter completeness: `name:` matches the skill directory, `description:`
  is non-empty and carries a "Use when ..." trigger sentence (or an
  established synonym marker already used across the tree), and `axis:`/`axes:`
  is present and non-empty whenever the skill declares `rule_count_floor:`
  (i.e. is a numbered-decision-rule skill).
- Per-rule citation check: for any skill with a `## Rules` section of
  `### N. <title>` blocks, every numbered rule block must carry its own
  `source: <https?:// URL>` line.
- Diagnostics now carry `path:line:` per violation (via `line_of()` offset
  math against the raw SKILL.md text), not just the file path.
- All of the above run unconditionally (not behind a manifest opt-in) so a
  clean run of `scripts/check_skill_conformance.py` with no flags covers the
  full tree.

## Why

issue #58 (adoption candidate #1 from the benchmark survey, #56/#57) asks to
mechanically enforce what today is only convention: frontmatter completeness,
a Use-when trigger sentence, and a `source:` line per numbered rule — as a
re-implementation, not a port, following the *pattern* of
`validate-skills.sh`/`check-skill-metadata.py`/`check-skill-triggers.py`
without copying their text.

## Upstream basis

Issue #58; prior art survey in #56/PR #57 (benchmark of skill ecosystems).
Built directly on the existing `scripts/check_skill_conformance.py`
(frontmatter name/description checks, opt-in manifest checks) rather than a
new script, per the issue's "single entry point" requirement.

## Verification

- `python3 -m unittest discover -s test` — 5/5 pass, covering the valid
  fixture and all three violation classes (missing axis, missing Use-when
  sentence, rule with no source: line), each asserting the diagnostic's line
  number.
- `python3 scripts/check_skill_conformance.py` over the live 248-skill tree:
  exits 0, "248 skills checked" — the tree was already conformant under the
  new checks, so no real violations needed fixing.
- Manual fixture run (`/tmp/fixture_repo`) confirmed the CLI's non-zero exit
  and `skills/<name>/SKILL.md:<line>: <reason>` diagnostic format on a
  fixture combining a missing trigger sentence and a sourceless rule.

## What did not work

None.

## Open findings

None.
