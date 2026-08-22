---
code_under_review:
  - scripts/check_skill_conformance.py
  - test/test_check_skill_conformance.py
  - skills/secure-coding-dependency-supply-chain-security/SKILL.md
  - skills/kubernetes-workload-requests-limits-decision/SKILL.md
  - skills/brand-design-icon-system-svg/SKILL.md
  - README.md
loop_state: landed
type: feature
breaking: false
verdict: pass
---

# Issue #62 — opt-in `globs:` trigger field

## What was done

- `scripts/check_skill_conformance.py`: added `check_globs_field()`,
  wired into `check_skill()`. `globs:` is optional; when present it must
  be a YAML list of one or more non-empty patterns, each containing a
  glob wildcard (`*` or `?`). Inline scalars and empty/malformed lists
  are rejected with a line-numbered diagnostic.
- `test/test_check_skill_conformance.py`: added four fixture tests —
  valid `globs:` list, malformed inline scalar, pattern with no
  wildcard, empty list — plus the existing full-repo-tree test now also
  covers the three skills below.
- Added `globs:` to three existing SKILL.md files whose trigger is
  genuinely file-pattern-shaped:
  - `skills/secure-coding-dependency-supply-chain-security/SKILL.md`
    (`**/requirements*.txt`, `**/package.json`, `**/package-lock.json`,
    `**/go.mod`, `**/Cargo.toml`, `**/Gemfile`)
  - `skills/kubernetes-workload-requests-limits-decision/SKILL.md`
    (`**/*.yaml`, `**/*.yml`)
  - `skills/brand-design-icon-system-svg/SKILL.md` (`**/*.svg`)
- `README.md`: added a "`globs:` (opt-in, 파일 패턴 트리거)" section
  under "스킬 추가하기" documenting the field's semantics — opt-in, list
  shape, wildcard requirement, and that it supplements rather than
  replaces the `description:` trigger sentence.

## Why

Issue #62 (benchmark adoption #4, Cursor `.mdc` globs) asks for an
opt-in machine-scoped trigger signal for skills whose actual trigger
condition is "this file changed," not prose intent. Schema-addition
only, per the issue's own scope note — no rewrite of unrelated skills.

## Upstream basis

Issue #62 acceptance criteria; existing `scripts/check_skill_conformance.py`
and `test/test_check_skill_conformance.py` from issue #58 (commit 663be63)
as the extension point.

## Doc-placement ladder

- [x] `scripts/check_skill_conformance.py` — validation logic
- [x] `test/test_check_skill_conformance.py` — fixture tests (malformed +
  valid)
- [x] 3x `skills/*/SKILL.md` — opt-in field adopted on genuinely
  file-pattern-shaped skills
- [x] `README.md` — semantics doc section for consumers (README.md is
  excepted from the docs/ bucket rule)

## Build-now bypass

CORE_BUILD_NOW=1 was set in this session's environment by the spawner;
delivered directly per contract v3 s19a — no separate phase-1
proposal/survey round.

## Verification

- `python3 -m pytest test/test_check_skill_conformance.py -v` — 9 passed,
  0 failed, 0 skipped (5 pre-existing + 4 new `globs:` fixture tests).
- `python3 scripts/check_skill_conformance.py` — `248 skills checked`,
  exit 0 (full-repo conformance green, including the 3 edited skills).

## What did not work

None.

## Open findings

None.
