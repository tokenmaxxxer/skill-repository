---
name: product-discovery-guardrail-metrics
description: >-
  Use this skill while the product skill is in `hypothesis-registered`, before the transition
  to `measuring`, to name guardrail metrics that must not move adversarially, and read it
  again once `measuring` starts so breaches are checked against what was named. Trigger
  alongside metric/threshold/decision-rule registration, on requests like "측정 들어가기 전에 가드레일
  등록해줘", "which metrics must not degrade", "add guardrails to the hypothesis record", "check
  this result against the registered guardrails". Do NOT use to register the primary metric,
  threshold, or decision rule themselves (use product-discovery-hypothesis-testing).
---

# Guardrail metrics for `hypothesis-registered` / `measuring`

**Stage:** `hypothesis-registered` (written); read again at
`measuring` (not written there).

**What it asks the user for:** which metrics must NOT move adversarially
while the experiment runs — distinct from the primary metric (the one the
experiment is trying to move) and from secondary metrics (which explain
why the primary moved). Per
`docs/reports/research/2026-07-27-role-practice/product.md`: practitioners
separate three metric tiers, and an experiment that wins on the primary
metric but breaches a guardrail is treated as reduced-trust or stopped
outright, regardless of the primary-metric result.

**What it produces:** a non-empty guardrail-metrics list, each entry
naming the metric and the direction/threshold that counts as a breach.
This list *is* this skill spec's `critical_success_factors`
(`product-discovery.spec.json`'s field for "what must hold, or the result
doesn't count"): a guardrail named non-empty at hypothesis-registration
time and checked at measurement time is exactly a critical success
factor stated in the vocabulary this plugin already uses — no separate
field or artifact is needed to satisfy `critical_success_factors`.

**Where it is written:** the same spec/state artifact's guardrail-metrics
field — write it alongside `metric`, `threshold`, and `decision_rule` in
`docs/issue-<n>/reports/product-discovery.md`'s companion hypothesis fields (wherever this repo's
`hypothesis-testing` skill already writes those three; guardrail metrics
join them as a fourth required field on the same artifact). This does not
change which file is the gated state file — `docs/issue-<n>/reports/product-discovery.md` remains
the only gated write; the guardrail field lives in the hypothesis record
alongside metric/threshold/decision_rule.

**Field list:**

- Guardrail metric name (one row per guardrail metric; at least one row
  required)
- Adversarial-direction / threshold (what counts as a breach)
- Action on breach (e.g. "stop outright" or "reduced trust, re-examine")

## Trigger

Apply this skill while the product skill is in `hypothesis-registered`,
before the transition to `measuring`, to name guardrail metrics that
must not move adversarially — distinct from the primary metric or
threshold, which belong to `hypothesis-testing` — and again at
`measuring` to check incoming data against the list named here.

## Procedure

1. After the metric/threshold/decision rule are drafted, ask the user
   what must not get worse while the experiment runs (see `## How to run
   the conversation`).
2. For each guardrail named, ask what counts as a breach (direction and
   threshold) and the action on breach, and write it into the hypothesis
   record before reporting `hypothesis-registered` complete (see `## How
   to run the conversation`).
3. Enforce the field non-empty before `researching to hypothesis-registered`
   (and by extension `hypothesis-registered to measuring`) (see
   `## Precondition this skill enforces`).
4. At `measuring`, read the list back when checking incoming data — never
   let a guardrail move silently because the primary metric is winning
   (see `## How to run the conversation`).

## Output shape

A non-empty guardrail-metrics list on the same hypothesis record as
metric/threshold/decision_rule, each entry naming the metric, its
breach direction/threshold, and the action to take on breach.

## Precondition this skill enforces

`researching to hypothesis-registered` (and by extension,
`hypothesis-registered to measuring`) requires this field non-empty, the
same discipline already applied to `metric`, `threshold`, and
`decision_rule`. Do not let the package move to `hypothesis-registered`
with an empty guardrail list.

## How to run the conversation

1. After the metric/threshold/decision rule are drafted, ask the user:
   "what must not get worse while we run this — what are the guardrail
   metrics?"
2. For each one named, ask what counts as a breach (direction and
   threshold) and what should happen if it breaches (stop outright vs.
   reduced trust).
3. Write all of it into the hypothesis record before reporting
   `hypothesis-registered` complete.
4. At `measuring`, read this list back when checking incoming data — do
   not silently let a guardrail move because the primary metric is
   winning.

## Common mistakes this skill exists to prevent

- Moving to `hypothesis-registered` with metric/threshold/decision_rule
  filled in but no guardrail metrics named.
- Treating a guardrail breach as something to explain away once the
  primary metric shows a win — the whole point of naming it up front is
  that a breach is not a fresh judgment call at read-out time.
