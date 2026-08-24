---
name: release-engineering-readiness-checklist
description: >-
  Use when working the release-engineering role's readiness phase,
  preparing to move from readiness to rollout, or checking what the
  record gate requires before the readiness record will pass. Trigger on requests like "walk the PRR readiness checklist", "is the
  service ready for rollout", "every checklist yes needs a pointable
  artifact", "출시 준비 체크리스트 점검해줘". Covers the seven Production Readiness Review
  dimensions, each resolving to yes/no backed by a dashboard URL, config key,
  or runbook path. Do NOT use for declaring the traffic curve and per-step
  thresholds after readiness passes (use release-engineering-rollout-plan).

---

# readiness-checklist — the release-engineering role's gate, worked from the inside

Covers the `readiness` phase. Asks the user, dimension by dimension,
whether each of the seven Production Readiness Review (PRR) items is
satisfied and — for every "yes" — what the pointable artifact is (a
dashboard URL, a config key, a runbook path). Writes the checklist into
`docs/issue-<n>/reports/release-engineering.md`'s `## Checklist` section, the file this plugin's `readiness
to rollout` transition is gated on.

The seven dimensions (converged open-source PRR shape, `docs/reports/
research/2026-07-27-role-practice/ops.md`):

1. Service Levels — is the SLO/SLI defined?
2. Architecture Design Review — has the design been reviewed?
3. Performance — has it been load-tested?
4. Documentation — does a runbook exist?
5. Observability — do dashboards/alerts exist?
6. Testing — has failure-injection been done?
7. Deployment Strategy — is a rollback path defined?

The record shape is enforced mechanically by the plugin's record gate, not
by judgment calls. This skill is the operator's-eye view of what that gate
actually checks, so the record gets written in a shape that passes it
instead of bouncing off it.

## Trigger

Apply this skill while working the `readiness` phase, preparing to move
`readiness to rollout`, or checking what the record gate requires before a
write to `docs/issue-<n>/reports/release-engineering.md` will pass — distinguishing it from the
specification/feasibility work upstream of ops, which this skill does not
cover.

## Procedure

1. Write `docs/issue-<n>/reports/release-engineering.md` with `phase: readiness` at role start
   (see "Working role start").
2. Walk the seven PRR dimensions with the user, recording each as
   yes/no plus a pointable artifact for every yes, in the `##
   Checklist` section's exact gate-required shape (see "The state
   file" and the seven dimensions list).
3. Before flipping `phase: rollout`, re-read every `yes` item and
   confirm its `artifact:` field points at something a stranger could
   actually open — if not, mark it `no` instead (see "Working
   `readiness to rollout`").
4. Once every item resolves and every yes has a real artifact, move to
   `rollout` (agent-owned, no human gate) and hand off to `rollout-plan`
   for the agent-owned canary/incident rows (see "Working `readiness to
   rollout`, and `rollout`'s own agent-owned steps").
5. For `rollout to steady`, read the user's own turn for an unambiguous
   approval statement before writing the transition — never accept a
   bare "ok" (see "Working `rollout to steady`").
6. While `phase: steady`, read `error_budget:` before any transition
   back toward a release and refuse if exhausted, routing a true P0
   through the user (see "Steady state and the error budget").
7. For `steady to incident` and back, require the filed, human-reviewed
   postmortem before writing `incident to steady` or `incident to
   readiness` (see "Closing an incident").

## Output shape

`docs/issue-<n>/reports/release-engineering.md`'s `## Checklist` section, one line per PRR dimension in
the gate's exact `- item: ... | status: yes|no | artifact: ...` shape,
plus the resulting phase moves (readiness to rollout to steady, and
incident handling) each gated per the sections above.

## Rule index

Full rule text, citations, and counter-examples:
`references/rules.md` in this skill's directory — read it when a
matched rule's detail is needed.

- S1 — The state file → references/rules.md
- S2 — Working role start → references/rules.md
- S3 — Working `readiness to rollout` → references/rules.md
- S4 — Working `readiness to rollout`, and `rollout`'s own agent-owned steps → references/rules.md
- S5 — Working `rollout to steady` → references/rules.md
- S6 — Steady state and the error budget → references/rules.md
- S7 — Closing an incident → references/rules.md
