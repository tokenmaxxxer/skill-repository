---
name: technical-feasibility-spike-report
description: >-
  Use when a feasibility role's `probing` state needs one uncertain technical
  question answered inside an agreed timebox before a feasibility verdict can be
  drafted. Runs the human-in-the-loop negotiation at both ends
  (question/timebox/acceptance criteria agreed first; report at timebox end) and
  writes the spike report artifact. Trigger on requests like "스파이크 돌려줘", "run a
  timeboxed spike", "spike report for this unknown", "timebox expired, what
  now". Do NOT use for classifying the decision's reversibility or scoping
  sensitivity/tradeoff points before exploration starts (use
  technical-feasibility-reversibility-and-spike-scoping).
---

# Spike report

**Stage:** `probing`, technical probe.

A spike is a timeboxed investigation whose output is knowledge, not
shippable code. This skill runs the human-in-the-loop negotiation the
research found at both ends of a spike (agreeing the question and timebox
before starting; reporting back at the timebox's end) and writes the
resulting spike report as one artifact — never asks for everything in one
turn.

## Trigger

This probe applies once the feasibility role has entered the `probing`
state and there is a single, specific technical unknown blocking the
feasibility verdict — something that must be resolved by a timeboxed
investigation (not a broad exploration) before `docs/issue-<n>/reports/technical-feasibility.md`'s
technical-probe field can be filled in.

## Procedure

1. Ask the user for the question, the proposed timebox, and the acceptance
   criteria, one at a time, and do not start investigating until all three
   are agreed (see "What it asks the user for, one thing at a time").
2. While investigating, record Tasks/Activities as they happen, without
   asking the user to approve the spike's internal method (see "While
   investigating").
3. If the timebox expires without a conclusive answer, stop, report the
   remaining gaps, and let the user decide whether to open a new,
   separately-scoped timebox or record the gap as an open finding (see "If
   the timebox expires with no conclusive answer").
4. On completion, record Tasks/Activities, Outcomes/Learnings, a
   Recommendation, and open questions, and classify every finding as a
   one-way or two-way door via the `reversibility-tag` skill before writing
   the technical-probe resolution (see "On completion").
5. Write the spike report to its project-local artifact file using the
   template's field skeleton, keeping this write ungated while the
   `docs/issue-<n>/reports/technical-feasibility.md` record itself remains gated by
   the record gate (see "Artifact" and "Field list (spike-report-template.md)").
6. Where the marketplace spec expects one record file to carry all four
   required fields, keep the spike report as its own separate project-local
   artifact and only summarize/link it from the main record, per the
   deliberate, unresolved structural difference (see "Spec write_scope gap
   (issue-53)").
7. Refuse to mark Acceptance Criteria complete if its timestamp postdates
   the timebox's recorded start, and say so plainly rather than silently
   backdating the field (see "Timestamp discipline").

## Output shape

Applying this skill produces one project-local spike report file (e.g.
`feasibility/spike-report-<slug>.md`), filled in against the
`spike-report-template.md` field skeleton (Spike Title, Description/Goal,
Type of spike, Estimated Timebox, Acceptance Criteria, Tasks/Activities,
Outcomes/Learnings, Recommendation, Open questions), plus a
technical-probe resolution (`pass`/`fail`/`blocked` plus evidence) written
into `docs/issue-<n>/reports/technical-feasibility.md` that points at or summarizes that report.

## What it asks the user for, one thing at a time

1. **The question** — what specifically do we need to know to resolve the
   technical probe? State it as a single, answerable question, not a broad
   area.
2. **A proposed timebox** — 1 to 3 days is the convergent practitioner
   range; ask the user to confirm or adjust it. Do not start work until the
   user has agreed the timebox, not merely heard it proposed.
3. **Acceptance criteria** — write what "answered" looks like *before* work
   starts, not after. This is the load-bearing discipline: acceptance
   criteria written after the investigation is indistinguishable from
   post-hoc rationalization, and this skill refuses to accept it that way
   (see "Timestamp discipline" below).

Only after all three are agreed does the skill begin the investigation.

## While investigating

Record Tasks/Activities as they happen. The spike's internal method (which
tool, which throwaway script) is not something to ask the user about — no
sourced practice reviews or approves a spike's means, only its question and
timebox.

## If the timebox expires with no conclusive answer

Stop. Do not silently keep going. Report to the user: what gaps remain,
and what more time would likely buy. The user decides: extend with a
**new**, separately-scoped timebox (its own acceptance criteria, not a
silent continuation of the old one), or stop and record the gap as an open
finding. Write the extension (or the
stop-and-record decision) into the spike report; this write is to the
spike report artifact, not the role record, and is not itself gated.

## On completion

Record: Tasks/Activities, Outcomes/Learnings (findings), a Recommendation,
and any open questions for future work. Then classify every finding this
probe produced as a one-way or two-way door (Bezos framing) using the
`reversibility-tag` skill's standing directive before writing the
technical-probe field's resolution (`pass`/`fail`/`blocked` plus evidence)
in `docs/issue-<n>/reports/technical-feasibility.md`.

## Artifact

Writes to `docs/issue-<n>/reports/technical-feasibility.md`'s own project (a project-local spike
report file, one per spike, e.g. `feasibility/spike-report-<slug>.md`),
using the field skeleton at
`feasibility-cycle/skills/spike-report/templates/spike-report-template.md`.
This artifact write is not gated — only the `docs/issue-<n>/reports/technical-feasibility.md`
record itself is gated, by the record gate. The
technical-probe resolution field in `docs/issue-<n>/reports/technical-feasibility.md` should point at
(or summarize) the spike report file, and its evidence should not be
written until the acceptance criteria are actually met or the timebox
stop-and-record decision is made.

## Field list (spike-report-template.md)

- Spike Title
- Description/Goal (the question being investigated) (spec: `spike_goal`)
- Type of spike (technical / functional / architectural)
- Estimated Timebox (spec: `timebox`)
- Acceptance Criteria — written and timestamped before work starts
- Tasks/Activities
- Outcomes/Learnings (spec: `findings`)
- Recommendation
- Open questions for future work

## Spec write_scope gap (issue-53)

The marketplace's realized `technical-feasibility.spec.json` expects one
record file (`write_scope`) to carry all four required fields
(`spike_goal`, `timebox`, `findings`, `decision`). This role spec instead
keeps the spike report as its own project-local artifact, separate from
`docs/issue-<n>/reports/technical-feasibility.md`, and only summarizes/links it from the main
record's technical-probe field. This is a deliberate, unresolved
structural difference — not silently reconciled — see README.md's
"Spec vocabulary mapping" section for the field-by-field mapping and
`decision` correspondence.

## Timestamp discipline

Refuse to mark Acceptance Criteria complete if its recorded timestamp
postdates the timebox's recorded start — that ordering violation is exactly
the "acceptance criteria written after the fact" failure mode the practice
research names. If you notice this has already happened, say so plainly to
the user rather than silently backdating the field.
