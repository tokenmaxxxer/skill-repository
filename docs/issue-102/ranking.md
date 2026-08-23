# Issue #102 — top-20 most-invoked skills: ranking and method

Measured 2026-08-24 on the operator machine. Not assumed; every number below
comes from logs or committed report files.

## Method

Aggregated by `scripts/rank_skill_invocation.py` from two measured sources:

1. **Session work logs** — `python3 <marketplace>/scripts/measure_skill_invocation.py`
   over `~/.tokenmaxxxer/work/*.session.*.log` (40 sessions measured at run
   time). Yields per-session `mounted` and `invoked_skills`.
2. **Applied verdicts** — `skill-verdict: <skill>` lines grepped from
   `~/tm-dicequest/docs/issue-*/reports/*.md` and
   `<marketplace>/docs/**/*.md` (implementation reports recording which skill
   verdicts were actually applied).

Score = 2·invoked + 2·verdicts + 1·mounted (actual invocation and applied
verdicts weigh double; mounting alone is exposure, not use). Ties broken by
invoked desc, then verdicts desc, then name asc (deterministic).

Caveat: the work-log window covers recent sessions only (log rotation); the
verdict grep extends the window backwards through committed reports. Both
sources are biased toward the implementation/UX/conformance flows that ran
recently — that bias is the point: these are the skills agents actually hit.

## Top-20 table

| # | skill | invoked | verdicts | mounted | score |
|---|-------|---------|----------|---------|-------|
| 1 | implementation-complexity-coupling-management | 1 | 32 | 28 | 94 |
| 2 | implementation-blueprint | 1 | 31 | 28 | 92 |
| 3 | implementation-design-pattern-selection | 0 | 32 | 28 | 92 |
| 4 | implementation-performance-data-structure-choice | 0 | 32 | 28 | 92 |
| 5 | work-in-english | 3 | 6 | 3 | 21 |
| 6 | observability-phase-trace | 2 | 6 | 4 | 20 |
| 7 | test-derivation | 0 | 8 | 4 | 20 |
| 8 | ux-engineering-color-visibility | 3 | 4 | 4 | 18 |
| 9 | test-authoring-isolation-and-fixture-strategy | 2 | 5 | 2 | 16 |
| 10 | conformance-review-requirement-extraction | 2 | 4 | 4 | 16 |
| 11 | ux-engineering-layout-grouping | 2 | 4 | 4 | 16 |
| 12 | ux-engineering-navigation-depth | 2 | 4 | 4 | 16 |
| 13 | ux-engineering-surface-contrast | 2 | 4 | 4 | 16 |
| 14 | ux-engineering-control-selection | 1 | 4 | 4 | 14 |
| 15 | game-character-rendering-composition | 2 | 3 | 2 | 12 |
| 16 | ux-engineering-research-log | 0 | 4 | 4 | 12 |
| 17 | conformance-review-verification-method-selection | 2 | 2 | 2 | 10 |
| 18 | model-routing | 2 | 1 | 3 | 9 |
| 19 | conformance-review-finding-record | 0 | 3 | 3 | 9 |
| 20 | conformance-review-sampling-derivation | 1 | 2 | 2 | 8 |

Rank 20 is a three-way score tie (8) with
`conformance-review-traceability-and-evidence` and
`technical-feasibility-build-vs-buy-dependency-health`; the tie-break
(invoked, then name) selects sampling-derivation.

## Harness availability finding

`claude plugin eval` exists in this environment (full `--help` renders,
including `--ablation with-without` and the `evals/**/case.yaml` layout), but
executing it is early-access gated. Exact commands and responses, 2026-08-24:

```
$ claude plugin eval init --bare sample-case
`plugin eval` is currently in early access

$ claude plugin eval .        # with a minimal evals/_probe/case.yaml present
`plugin eval` is currently in early access
```

Consequence: the scenario corpus under `evals/pressure/` is authored in the
harness's native layout (schema_version 1.1: `case.yaml` config, `prompt.md`
task, `graders/*.md` with an llm rubric plus a `tool_used: Skill` ablation
indicator) so it runs unmodified once the gate lifts, and is validated today
by `scripts/check_eval_scenarios.py` (schema lint) and
`test/test_check_eval_scenarios.py`. Live ungated/gated delta runs — and the
"rewrite or demote on null delta" step that depends on their output — are
blocked on harness access and remain open acceptance items on #102.
