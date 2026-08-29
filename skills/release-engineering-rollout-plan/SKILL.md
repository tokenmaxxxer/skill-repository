---
name: release-engineering-rollout-plan
description: >-
  Use when working the release-engineering skill's rollout phase
  — asking the user for, or deriving from the readiness record, the traffic
  curve and per-step metric thresholds that gate progressive delivery, written
  to ops/rollout-plan.md before the rollout to rollout and rollout to incident
  agent rows can read them. Trigger on requests like "write the rollout plan",
  "canary step thresholds and bake time", "traffic curve for progressive
  delivery", "카나리 롤아웃 계획 세워줘". Do NOT use for the readiness checklist upstream
  of rollout (use release-engineering-readiness-checklist) or the
  post-incident writeup (release-engineering-postmortem).

---

# rollout-plan — the canary/progressive-delivery plan

Covers the `rollout` phase. Entered once `readiness to rollout` fires
(checklist complete, every yes item has a pointable artifact).

## Trigger

Apply this skill while working the `rollout` phase: declaring or deriving
the traffic curve and per-step metric thresholds before the agent-owned
`rollout to rollout`/`rollout to incident` rows can read them —
distinguishing it from the readiness checklist (`readiness-checklist`)
and the post-incident postmortem (`postmortem`).

## Procedure

1. Ask the user for (or derive from the readiness record) the traffic
   curve, bake time, metric queries, and per-step thresholds (see "What
   it asks the user for").
2. Write one step entry per traffic increment to `ops/rollout-plan.md`,
   each with a `result: pending` field (see "What it writes, and
   where").
3. Let the agent promote itself `rollout to rollout` when a step's
   result comes back clean against its declared threshold, with no
   human turn required (see "How the agent-owned rows read it").
4. Let the agent declare `rollout to incident` immediately on a breach
   past a step's hard threshold, without waiting to be asked (see "How
   the agent-owned rows read it").
5. For `rollout to steady`, do not self-promote even after the last
   canary step passes — ask the user for an explicit promotion approval
   in their own turn first (see "How the agent-owned rows read it").

## Output shape

`ops/rollout-plan.md`, one step entry per traffic increment (bake time,
metric queries, pass/fail/inconclusive thresholds, `result:` field), read
mechanically by the `rollout to rollout` and `rollout to incident`
agent-owned transitions; `rollout to steady` instead waits on the user's
own explicit approval turn.

## What it asks the user for

Either directly, or derived from the readiness record if already implied
there:

- The traffic curve: per-step traffic percentage (e.g. 5% -> 25% -> 50% ->
  100%).
- Wait/bake time per step.
- The metric queries evaluated at each step (request error rate, p99
  latency, and at least one business metric — the commonly tracked triad).
- The pass/fail/inconclusive threshold for each metric at each step —
  either Kayenta-style score bands (`pass >= 90`, `marginal >= 75`) or
  Flagger-style fields (`interval`, `stepWeight`, `maxWeight`, `threshold`:
  the number of failed checks tolerated before automatic abort).

(`docs/reports/research/2026-07-27-role-practice/ops.md`, "Progressive
rollout (canary / staged deploy)".)

## What it writes, and where

`ops/rollout-plan.md`, one entry per step:

```markdown
## Step 1 — 5% traffic
- bake_time: 10m
- metrics:
  - name: error_rate
    query: <metric query>
    threshold: pass >= 90 / marginal >= 75   # or Flagger-style threshold count
  - name: p99_latency
    query: <metric query>
    threshold: <value>
- result: pending   # pending | pass | marginal | fail
```

This file is not `docs/issue-<n>/reports/release-engineering.md` — writing it is never gated. Only the
resulting write to `docs/issue-<n>/reports/release-engineering.md` (the step promotion or the incident
declaration) is gated, and only on table membership.

## How the agent-owned rows read it

- `rollout to rollout`: when a step's `result` comes back clean against its
  declared threshold, the agent promotes to the next step itself — no
  human turn required. This mirrors Argo Rollouts/Flagger/Kayenta's
  auto-promote loops, which are real, mature production practice for
  exactly this decision.
- `rollout to incident`: when a step's `result` is a breach past its hard
  pre-set threshold, the agent declares the incident itself, immediately,
  without waiting to be asked. Raising costs nothing; understating costs
  more (PostHog's "when in doubt, raise it anyway," carried into the
  companion interaction research for `ops`).
- `rollout to steady`: NOT agent-owned. Even once the last canary step
  passes, cutover to full/production traffic is a human call in every
  source that names this moment — ask the user for an explicit promotion
  approval in their own turn before writing `phase: steady` (see
  `readiness-checklist`'s "Working `rollout to steady`" section for the
  exact wording expected).
