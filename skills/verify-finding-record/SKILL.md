---
name: verify-finding-record
description: >-
  Use when a reproduction attempt has been made and needs its outcome written down in
  docs/issue-<n>/reports/defect-verification.md — never to fix or patch what was found. Trigger on requests
  like "record the attempt in docs/issue-<n>/reports/defect-verification.md", "reproduced vs not-reproduced
  outcome block", "blocked needs-repro-access entry", "재현 시도 결과 기록해줘". Covers
  the three-value outcome set and the escalating finding block addressed to
  coding. Do NOT use for attaching the severity band to an already-recorded
  finding (use verify-severity-classification); the review-side analog is
  conformance-review-finding-record.

---

# finding-record

Covers both initial recording and dispute resolution or re-examination
(recorded inline, still against the same attempt). Produces the per-attempt outcome record, and any escalating
`finding` block, inside `docs/issue-<n>/reports/defect-verification.md`, the role's record file, at the
attempt blocks below the header block.

This skill never writes to any file other than `docs/issue-<n>/reports/defect-verification.md`. It does
not fix, patch, or suggest a patch for anything it finds — it reports.

## Trigger

Apply this skill once a reproduction attempt has been made and its outcome needs
to be written down in `docs/issue-<n>/reports/defect-verification.md` — never to fix or patch what
was found.

## Procedure

1. Record the outcome solo by default; ask the user only when a
   reproduction genuinely cannot be attempted from what's available, for
   the missing access or input (see "What it asks the user for").
2. Choose exactly one of the three outcomes; never merge them into a
   bare pass/fail (see "The outcome set").
3. Fill in the full field list for the attempt block — attempt, outcome,
   evidence, steps, expected/actual when applicable, evidence_kind, and
   environment (see "The artifact and its field list").
4. When the attempt reproduces, additionally write the inline `finding`
   block per the role-handoff contract's `finding` row, addressed to
   coding, carrying its severity (see "The artifact and its field
   list").
5. Refuse to write `reproduced` with no `evidence` pointer, and require
   an `evidence` field for `not-reproduced` and
   `blocked: needs-repro-access` alike (see "Refusal the skill itself
   enforces").
6. In `reproduced`, record a disputed finding's re-examination inline
   rather than treating the dispute as a request to fix anything (see
   "What it asks the user for").

## Output shape

One `---`-delimited block per attempt inside `docs/issue-<n>/reports/defect-verification.md`,
carrying the full field list and exactly one of the three outcome
values, with an escalating `finding` block attached when the attempt
reproduces, and a write refused when a required evidence pointer is
missing.

## Rule index

Full rule text, citations, and counter-examples:
`references/rules.md` in this skill's directory — read it when a
matched rule's detail is needed.

- 3.1 — **`attempt`** — a stable identifier for what was being tested, verbatim reference to the claim under test (a qa defect report, a review requirement marked `Present`, or…
- 3.2 — **`outcome`** — `reproduced`, `not-reproduced`, or `blocked: needs-repro-access`
- 3.3 — **`evidence`** — a pointer into the actual reproduction: repro steps, commit sha, run output, or a log excerpt. Never a paraphrase of what was attempted — the reproducti…
- 3.4 — **`steps`** — what was actually run or checked to attempt the reproduction (the marketplace `roles/specs/defect-verification.spec.json` names this same content `repro_st…
- 3.5 — **`expected`** / **`actual`** — required only when the claim under test states an expectation (mirrors the IEEE 829 Test Incident Report shape); omit when not applicable
- 3.6 — **`evidence_kind`** — what the `evidence` pointer actually is (recording, transcript, log excerpt, diff, command output), stated rather than left implicit, so a reader i…
- 3.7 — **`environment`** — the commit sha and run/build context, captured at the moment the attempt is made rather than reconstructed afterward; a reconstructed environment not…
- S1 — What it asks the user for → references/rules.md
- S2 — The outcome set → references/rules.md
- S3 — Refusal the skill itself enforces → references/rules.md
- S4 — What this skill never does → references/rules.md
