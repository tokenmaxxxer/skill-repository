---
name: release-engineering-error-budget-policy
description: >-
  Use when working the ops role's steady state (ops/state.md status:
  steady) to write, per SLI, the measurement method, SLO target,
  measurement window, and consequence table that gates steady ->
  readiness on error_budget: ok, or when a true P0/security-fix exception
  needs to be routed around an exhausted budget.
  Do NOT use to define what "healthy" means from scratch — this role
  consumes the SLO/measurement design feasibility already produced; it
  does not invent it.
---

# error-budget-policy — the steady-state handoff contract

Belongs to the `steady` state. Ops does not define what "healthy" means —
that is the measurement design `feasibility` already produced and `ops`
was handed at `idle -> readiness`. This skill's job is only to write down
the policy consequence, per SLI, so the `steady` refusal rule has something
mechanical to read.

## Trigger

Apply this skill while working the `steady` state: writing or updating
the per-SLI error-budget policy that `error_budget:` reads before any
`steady -> readiness` transition, or handling a dispute about whether the
budget calculation is right or an exception applies.

## Procedure

1. For each SLI, record the fields per "Fields, per SLI" below into
   `ops/error-budget-policy.md` (see "Where it is written").
2. Leave `ops/state.md`'s `error_budget:` field for the mechanical
   `steady -> readiness` check to read; do not edit it to unblock a
   transition (see "How it is read").
3. If the field reads `exhausted`, refuse the transition outright,
   regardless of readiness, except for true P0/security-fix work — route
   that exception through the user rather than editing the field (see
   "How it is read").
4. If the user disputes the budget reading or an exception's validity,
   escalate to the named human path (the CTO, in the sourced practice)
   rather than resolve it by editing the field (see "How it is read").

## Output shape

`ops/error-budget-policy.md`, one section per SLI (measurement method,
SLO target, measurement window, consequence table), read by
`ops/state.md`'s `error_budget:` field, which the `steady -> readiness`
transition checks mechanically before proceeding.

## Fields, per SLI (Google's error-budget-policy shape)

- **Measurement method** — what raw signal (e.g. proportion of requests
  under a latency threshold).
- **SLO target** — the target percentage (e.g. 99.9%).
- **Measurement window** — the trailing window it is computed over (e.g.
  trailing 28 days).
- **Consequence table** — within budget: releases proceed at normal
  velocity. Budget exhausted: only P0/security-fix releases proceed until
  back within budget.

(`docs/reports/research/2026-07-27-role-practice/ops.md`, "Error budget
accounting" and "Error budget policy doc".)

## Where it is written

`ops/error-budget-policy.md`, one section per SLI:

```markdown
## <SLI name>
- measurement_method:
- slo_target:
- measurement_window:
- consequence:
    within_budget: releases proceed normally
    exhausted: only P0/security-fix releases proceed until back within budget
```

Writing this file is never gated — it is not `ops/state.md`.

## How it is read

`ops/state.md`'s `error_budget:` field (`ok` / `exhausted`) is checked
mechanically before `steady -> readiness`. If `exhausted`, the transition
is refused outright, regardless of how ready the next change looks — this
mirrors the policy's own carve-out that only P0/security-fix work proceeds
while the budget is spent. That carve-out is not automatic: route a true
P0 through the user rather than editing `error_budget:` to `ok` to unblock
it, which would be lying to the gate about a state that isn't true.

Disputes about whether the budget calculation is right, or whether an
exception applies, are the one place this policy names an explicit human
escalation path in the sourced practice (to the CTO, in Google's telling) —
if the user disputes the reading, that is a conversation to have, not a
field to silently overwrite.
