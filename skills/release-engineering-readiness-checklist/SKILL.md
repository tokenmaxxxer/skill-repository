---
name: release-engineering-readiness-checklist
description: >-
  Use when working the ops role's readiness state (ops/state.md status
  readiness), preparing to move readiness -> rollout, or checking what
  state-gate.sh (PreToolUse) requires before a write to ops/state.md will
  pass. Trigger on requests like "walk the PRR readiness checklist", "is the
  service ready for rollout", "every checklist yes needs a pointable
  artifact", "출시 준비 체크리스트 점검해줘". Covers the seven Production Readiness Review
  dimensions, each resolving to yes/no backed by a dashboard URL, config key,
  or runbook path. Do NOT use for declaring the traffic curve and per-step
  thresholds after readiness passes (use release-engineering-rollout-plan).

---

# readiness-checklist — the ops role's gate, worked from the inside

Belongs to the `readiness` state. Asks the user, dimension by dimension,
whether each of the seven Production Readiness Review (PRR) items is
satisfied and — for every "yes" — what the pointable artifact is (a
dashboard URL, a config key, a runbook path). Writes the checklist into
`ops/state.md`'s `## Checklist` section, the file this plugin's `readiness
-> rollout` transition is gated on.

The seven dimensions (converged open-source PRR shape, `docs/reports/
research/2026-07-27-role-practice/ops.md`):

1. Service Levels — is the SLO/SLI defined?
2. Architecture Design Review — has the design been reviewed?
3. Performance — has it been load-tested?
4. Documentation — does a runbook exist?
5. Observability — do dashboards/alerts exist?
6. Testing — has failure-injection been done?
7. Deployment Strategy — is a rollback path defined?

This role's state machine (`docs/specs/state-machine.md`) is enforced
mechanically by two hooks in this plugin, not by judgment calls. This skill
is the operator's-eye view of what those hooks actually check, so the state
file gets written in a shape that passes the gate instead of bouncing off it.

## Trigger

Apply this skill while working the `readiness` state, preparing to move
`readiness -> rollout`, or checking what `state-gate.sh` requires before a
write to `ops/state.md` will pass — distinguishing it from the
specification/feasibility work upstream of ops, which this skill does not
cover.

## Procedure

1. Write `ops/state.md` with `status: readiness` at `idle -> readiness`
   (see "Working `idle -> readiness`").
2. Walk the seven PRR dimensions with the user, recording each as
   yes/no plus a pointable artifact for every yes, in the `##
   Checklist` section's exact gate-required shape (see "The state
   file" and the seven dimensions list).
3. Before flipping `status: rollout`, re-read every `yes` item and
   confirm its `artifact:` field points at something a stranger could
   actually open — if not, mark it `no` instead (see "Working
   `readiness -> rollout`").
4. Once every item resolves and every yes has a real artifact, move to
   `rollout` (agent-owned, no human gate) and hand off to `rollout-plan`
   for the agent-owned canary/incident rows (see "Working `readiness ->
   rollout`, and `rollout`'s own agent-owned steps").
5. For `rollout -> steady`, read the user's own turn for an unambiguous
   approval statement before writing the transition — never accept a
   bare "ok" (see "Working `rollout -> steady`").
6. While `status: steady`, read `error_budget:` before any transition
   back toward a release and refuse if exhausted, routing a true P0
   through the user (see "Steady state and the error budget").
7. For `steady -> incident` and back, require the filed, human-reviewed
   postmortem before writing `incident -> steady` or `incident ->
   readiness` (see "Closing an incident").

## Output shape

`ops/state.md`'s `## Checklist` section, one line per PRR dimension in
the gate's exact `- item: ... | status: yes|no | artifact: ...` shape,
plus the resulting `status:` transitions (`readiness -> rollout ->
steady`, and incident handling) each gated per the sections above.

## Rule index

Full rule text, citations, and counter-examples:
`references/rules.md` in this skill's directory — read it when a
matched rule's detail is needed.

- S1 — The state file → references/rules.md
- S2 — Working `idle -> readiness` → references/rules.md
- S3 — Working `readiness -> rollout` → references/rules.md
- S4 — Working `readiness -> rollout`, and `rollout`'s own agent-owned steps → references/rules.md
- S5 — Working `rollout -> steady` → references/rules.md
- S6 — Steady state and the error budget → references/rules.md
- S7 — Closing an incident → references/rules.md
