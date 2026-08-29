---
name: verify-severity-classification
description: >-
  Use when a
  reproduced defect's finding is addressed to coding and needs a severity band
  attached — never to decide whether the attempt reproduced at all. Trigger on
  requests like "set severity on the verify finding", "blocking or advisory
  for coding", "map the bug-bar band to finding_type", "재현된 결함 blocking인지
  advisory인지 정해줘". Maps a deterministic band (Chromium five bands or Microsoft
  bug bar) to the blocking/advisory gate value on the docs/issue-<n>/reports/defect-verification.md finding
  block. Do NOT use for writing the attempt and outcome block itself (use
  verify-finding-record); the review-side analog is
  conformance-review-severity-classification.

---

# severity-classification

Runs after `finding-record` has already recorded a
`reproduced` outcome and its accompanying `finding` block — this skill only
sets that finding's `severity` field, per
the spawning contract's §5: "`severity: blocking | advisory`.
`blocking` means loops that DEPEND ON the addressed skill's output pause
until the finding is resolved. `advisory` means downstream loops continue;
the finding is context, not a gate."

## Trigger

Apply this skill once `finding-record` has already recorded a `reproduced` outcome
and its finding needs a severity band attached before it can gate
landing — never to decide whether the attempt reproduced at all.

## Procedure

1. Compute the band solo by default; ask the user only when the band is
   disputed after the fact by coding, in which case retain the finding
   and adjust the recorded band rather than dropping it (see "What it
   asks the user for").
2. Choose one of the two sourced deterministic band shapes for the
   engagement — Chromium's five bands or Microsoft's four-level bug bar
   — never an averaged subjective score (see "The shape of the
   classification").
3. Map the chosen band to the closed `blocking|advisory` gate value the
   contract's gates actually consult, keeping the two spec fields
   distinct (see "Two distinct spec fields, not one").
4. Write the resulting `severity` field onto the finding's existing
   block in `docs/issue-<n>/reports/defect-verification.md`, never as a separate artifact (see "The
   artifact").

## Output shape

A `severity` field written onto the existing finding block in
`docs/issue-<n>/reports/defect-verification.md`, holding one deterministic band value mapped to a
`blocking|advisory` gate value — never a new file, never an averaged
score.

## What it asks the user for

Nothing to compute the band itself — severity is verify's own judgment
call, made solo, from what the reproduction demonstrated. It asks the user
only if a severity band is disputed after the fact by coding, in which case
it may retain the finding but adjust the recorded band — the finding is
never dropped on dispute, only re-rated.

## The shape of the classification

A **deterministic table-lookup**, not an averaged subjective score, mirroring
the practice research review skill already established for this
org's use of severity: Microsoft's SDL bug bar replaced DREAD's averaged
damage/reproducibility/exploitability/affected-users/discoverability score
for being too subjective and inconsistently scored. This skill uses one of
two sourced deterministic band shapes, chosen by the engagement:

- **Chromium's five bands** — Critical (S0) / High (S1) / Medium (S2) /
  Low (S3) / Unknown (S4), each defined by a concrete capability (arbitrary
  code/resource access at full privilege = Critical; cross-origin data read
  or code exec in another origin's context = High; limited info
  read/modify, or harmless-alone-but-combinable = Medium;
  higher-severity-in-theory but with extreme mitigating/limited-scope
  factors = Low). A Chromium-scale severity of Critical or High normally
  maps to `severity: blocking`; Medium, Low, or Unknown normally maps to
  `severity: advisory`, subject to the engagement's own judgment.
- **Microsoft's four-level bug bar** — Critical / Important / Moderate /
  Low, looked up from characteristics of the finding (attacker
  authentication state: anonymous vs. authenticated; scope: default vs.
  special-configuration scenario; persistence: temporary vs. permanent),
  not computed from a weighted average. Critical or Important normally
  maps to `severity: blocking`; Moderate or Low normally maps to
  `severity: advisory`.

Do not use DREAD's averaged-score shape for this skill, per the sourced
disagreement above. `blocking` vs. `advisory` is the field this contract's
gates actually consult (§5); the chosen band scale is a tool for reaching
that call consistently, not a contract-visible field itself.

## Two distinct spec fields, not one

The marketplace `roles/specs/defect-verification.spec.json` names two
separate fields where this skill and `finding-record` together produce
one deterministic band and one closed gate value: its `severity` field is
the free-text deterministic band this skill computes (Chromium's five
bands or Microsoft's four-level bug bar, above); its `finding_type` field
is the closed `blocking|advisory` enum that `finding-record` writes onto
the finding block and that this skill spec's gates (`verify-finding-gate`,
`verify-outcome-gate`) actually consult. The two must not be collapsed:
`severity` informs the `finding_type` call but is not itself the gated
value.

## The artifact

Writes a `severity` field onto the finding's existing block in
`docs/issue-<n>/reports/defect-verification.md` (the same block `finding-record` wrote), not a separate
file — this is an addition to an existing finding, not a new artifact.

## What this skill never does

- Compute severity as an average of subjective factors (the DREAD shape).
- Decide whether a defect reproduced — that is `finding-record`'s job,
  prior to this skill running.
- Fix, patch, or propose remediation for the finding it classifies.
- Let a `review-record` in `loop_state: reported` with a clean verdict
  downgrade or drop a `severity: blocking` finding — per contract §4,
  review's and verify's verdicts are independent.
