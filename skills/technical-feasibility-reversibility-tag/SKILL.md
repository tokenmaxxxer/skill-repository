---
name: technical-feasibility-reversibility-tag
description: >-
  Use when a finding is about to be written to a probe-resolution field in
  docs/issue-<n>/reports/technical-feasibility.md by spike-report, stride-table, build-vs-buy, or
  license-scan, and it has not yet been classified as a one-way or two-way door.
  Adds a Reversibility field — `one-way` or `two-way` plus a one-line
  cost-to-undo reason — to every finding, scaling the evidence bar before a
  probe may resolve `pass`. Trigger on requests like "reversibility tag 붙여줘",
  "tag this finding one-way or two-way", "cost to undo this decision", "can this
  probe resolve pass yet". Do NOT use for classifying a whole architectural
  decision and scoping its spike/timebox up front (use
  technical-feasibility-reversibility-and-spike-scoping).

---

# Reversibility tag

**Stage:** `probing` — cross-cutting across all four probes
(technical, prior-art, legal-regulatory, threat-model), not a probe of its
own.

This is a standing directive to the agent, not a question put to the user.
Bezos's one-way-door / two-way-door framing: some decisions are
consequential and hard to reverse (a one-way door) and must be made
methodically and carefully; others are cheap to reverse (a two-way door)
and can be made quickly. Reversibility is not a fifth probe — it is a field
on every finding the other four probes produce, and it scales how much
evidence a probe needs before it can resolve `pass`.

## Trigger

This applies whenever any of the four feasibility probes — `spike-report`,
`stride-table`, `build-vs-buy`, or `license-scan` — has produced a finding
that is about to be written into a probe-resolution field
(`technical`, `prior_art`, `legal_regulatory`, `threat_model`) in
`docs/issue-<n>/reports/technical-feasibility.md`. It applies to the agent itself, not as a question
to surface to the user.

## Procedure

1. Before writing any probe-resolution field, take each finding produced by
   the four probes and classify it as a one-way or two-way door (see ## What
   it does, before any probe-resolution field is written).
2. Record the classification and a one-line reason for it inline as a field
   on the finding within the probe artifact that produced it, not as a
   standalone file (see ## Artifact).
3. Add the **Reversibility** field itself — `one-way` or `two-way` plus the
   one-line reason of what it would cost to undo — to every finding (see
   ## Field added to every finding).
4. Before resolving a probe as `pass`, check whether any one-way-door
   findings still lack the heavier evidence this tag requires, and if so
   say so to the user instead of resolving optimistically (see ## Rule).

## Output shape

Applying this skill does not produce a new file; it adds a Reversibility
field — `one-way` or `two-way` plus a one-line cost-to-undo reason — inline
to each finding already being written into the relevant probe artifact
(the spike report, STRIDE table row, build-vs-buy comparison row, or
license-scan entry), which in turn feeds the probe-resolution fields in
`docs/issue-<n>/reports/technical-feasibility.md`.

## What it does, before any probe-resolution field is written

For every finding produced by `spike-report`, `stride-table`,
`build-vs-buy`, or `license-scan`, classify it:

- **One-way door** — hard or costly to reverse (e.g. a core architectural
  dependency, a data-model choice migrating data later would be expensive
  to undo). Require more rigorous, more corroborated evidence before that
  finding is allowed to support a probe resolving `pass`.
- **Two-way door** — cheap and quick to reverse (e.g. a config flag, a
  vendor contract that can be cancelled). A lighter evidence bar is
  acceptable.

## Artifact

Not a separate file. This tag is written inline as a field on each finding
within the probe artifact that produced it (the spike report, the STRIDE
table row, the build-vs-buy comparison row, the license-scan entry) —
never a standalone `feasibility/reversibility.md`. Like those artifacts,
this write is not the skill record and is not gated.

## Field added to every finding

- **Reversibility** — `one-way` or `two-way`, plus a one-line reason (what
  would it cost, in time or money, to undo this if it turns out wrong).

## Rule

A probe's resolution field in `docs/issue-<n>/reports/technical-feasibility.md` (`technical`,
`prior_art`, `legal_regulatory`, `threat_model`) should not be written as
`pass` if any of its one-way-door findings lack the heavier evidence this
tag calls for — say so to the user rather than resolving optimistically.
