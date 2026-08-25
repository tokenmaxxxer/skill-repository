---
issue: 113
role: implementation
loop_state: landed
upstream:
  - path: docs/issue-111/reports/observability.md
    sha: 47faf51e9972676b12085a5e4f6811715f85ad9c
code_under_review:
  - scripts/check_skill_conformance.py
  - skills/accessibility-aria-and-contrast-rules/SKILL.md
  - .githooks/pre-commit
  - install.sh
type: fix
breaking: false
verdict: pass
---

# issue-113 — implementation record

## What was done

Root-cause-first fix for F5+F1 from the issue-111 observability sweep:

1. **F1 (silent opt-in checks)** — `scripts/check_skill_conformance.py`'s
   `--manifest` and `--require-use-when-and-source` arguments used to
   default to `None` (off). They now default to this repo's own checked-in
   manifest files (`scripts/procedure_authored_skills.txt` and
   `scripts/issue_1996_use_when_source_manifest.txt`, resolved relative to
   `repo_root`), so both additive checks always run on a bare invocation.
   The flags remain present and still accept an override path. No
   check-function logic changed.
2. **F1's live violation** — `skills/accessibility-aria-and-contrast-rules/SKILL.md`
   was failing the now-always-on `--require-use-when-and-source` check: its
   citations live only in `references/rules.md` (progressive disclosure),
   so the top-level file had no inline `source: <https?://URL>` line. Added
   one, extending the existing `S1 — Sources` index bullet with inline WCAG
   2.2 / AccName-spec URLs, matching the inline-citation pattern every
   sibling skill in `issue_1996_use_when_source_manifest.txt` already uses.
3. **F5 (no commit-time wiring)** — added a versioned git hook,
   `.githooks/pre-commit`: when any staged path starts with `skills/`, it
   runs `scripts/check_skill_conformance.py` (no flags — relies on the new
   always-on defaults) and refuses the commit on a non-zero exit. Wired via
   `git config core.hooksPath .githooks`, both added to `install.sh` (so
   every future `bash install.sh` run activates it) and run directly in
   this working tree so the acceptance evidence below is live.

## Why

The issue's own resolution path (docs/issue-111/reports/observability.md,
F1/F5 rows) specifies exactly this shape: make the two manifest checks
non-optional in the default invocation, separately fix the live violation,
and wire the unconditional checks into this repo's commit-time enforcement
so the mechanism stops depending on a human remembering two flags. `.githooks/`
+ `core.hooksPath` was chosen over a CI workflow because the repo has no
`.github/` directory, no CI runner, and no Makefile today (confirmed via
`git ls-files`) — a versioned git hook is the smallest change that gives
local, always-on, commit-time enforcement without adding new CI
infrastructure the operator-frozen constraint (2026-08-25, "no added
overhead, no new conflict/stall surfaces") would have to absorb. The
existing PreToolUse `trailer-gate.sh` in this environment's harness plugin
is the same commit-time-enforcement pattern the issue cites as precedent;
it lives outside this repo (shared across every role/rulebook) so it was
not edited — only its pattern (intercept a `git commit`, judge staged
content, refuse on violation) was mirrored inside this repo's own
versioned hook.

## What did not work

None.

## Upstream basis

`docs/issue-111/reports/observability.md` (commit `47faf51`), findings F1
and F5 — the issue text batches these two as "root-cause-first" and its
Acceptance section names `scripts/check_skill_conformance.py` as the gate
and requires executed-live pre-fix/post-fix/refused-commit evidence, all
reproduced below.

## Open findings

None open. F2/F3/F4 from the same sweep are explicitly out of scope for
this issue (batched separately per the sweep's own "batched by mechanism"
framing) and are not touched here.

## Next steps

None — `loop_state` is terminal (`landed`).

## Acceptance evidence

Gate: `scripts/check_skill_conformance.py`. All commands executed live in
this working tree.

**Pre-fix — bare invocation (the pattern every landed session used),
silently passing despite the violation:**

```
$ git stash push -- scripts/check_skill_conformance.py skills/accessibility-aria-and-contrast-rules/SKILL.md
$ python3 scripts/check_skill_conformance.py
273 skills checked
exit=0
```

**Pre-fix — with both flags passed explicitly (never done in this repo's
landed history until now), showing the violation actually existed:**

```
$ python3 scripts/check_skill_conformance.py \
    --manifest scripts/procedure_authored_skills.txt \
    --require-use-when-and-source scripts/issue_1996_use_when_source_manifest.txt
1 violation(s) found in 1 skill(s) (273 skills checked):
  skills/accessibility-aria-and-contrast-rules/SKILL.md:1: missing at least one 'source: <https?:// URL>' citation
exit=1
$ git stash pop
```

**Post-wiring-fix, pre-content-fix — bare invocation now catches the
violation unconditionally, with zero flags passed (proves the wiring, not
just the content fix, is what changed):**

```
$ git stash push -- skills/accessibility-aria-and-contrast-rules/SKILL.md
$ python3 scripts/check_skill_conformance.py
1 violation(s) found in 1 skill(s) (273 skills checked):
  skills/accessibility-aria-and-contrast-rules/SKILL.md:1: missing at least one 'source: <https?:// URL>' citation
exit=1
$ git stash pop
```

**Fully fixed — bare invocation, empty-state acceptance:**

```
$ python3 scripts/check_skill_conformance.py
273 skills checked
exit=0
```

**Commit attempt with a violating SKILL.md, refused by the wiring** (staged
a still-violating edit to `skills/accessibility-aria-and-contrast-rules/SKILL.md`
under `core.hooksPath=.githooks`):

```
$ git add skills/accessibility-aria-and-contrast-rules/SKILL.md
$ git commit -m "test: this should be refused by the pre-commit hook"
1 violation(s) found in 1 skill(s) (273 skills checked):
  skills/accessibility-aria-and-contrast-rules/SKILL.md:1: missing at least one 'source: <https?:// URL>' citation
pre-commit: skill conformance check failed (scripts/check_skill_conformance.py); commit refused.
exit=1
```

The test edit was reset and the real fix restored afterward; it was never
committed.

**Regression checks:**

```
$ python3 scripts/check_progressive_disclosure.py
OK: 273 skills checked, all bodies <= 150 lines; 41 index<->references/rules.md bijections verified.

$ python3 -m pytest test/ -q
58 passed in 0.91s
```

## Skill obligations

- skill-verdict: work-in-english — applied: invoked; all commits, this
  record, code comments, and the new hook script are in English; only this
  final user-facing summary is in Korean.
- skill-verdict: implementation-complexity-coupling-management — applied:
  invoked; rule 9 (order a local pre-merge check pipeline
  cheapest-and-narrowest first, most-expensive-and-broadest last) governed
  the `.githooks/pre-commit` design — it short-circuits on staged-path
  prefix before paying the cost of running the full conformance script.
- skill-verdict: accessibility-aria-and-contrast-rules — applied: invoked;
  rule 5.1's evidence-field framing (an evidence/citation field needs a
  concrete, checkable citation, not a bare pointer) is the same shape as
  this skill's own missing-source defect, and its Sources index
  (`references/rules.md`) supplied the WCAG 2.2 / AccName-spec URLs used
  in the fix.
- other mounted skills: not triggered (implementation-design-pattern-selection,
  implementation-performance-data-structure-choice, implementation-blueprint —
  none of this issue's changes involved a GoF pattern decision, a
  data-structure/algorithm choice, or new multi-module architecture; this
  was a scoped wiring + content fix).
