---
name: conformance-review-finding-record
description: >-
  Use when a requirement has been checked and needs its verdict recorded in
  docs/issue-<n>/reports/conformance-review.md — never to fix or patch what was found. Trigger on requests
  like "record the verdict in docs/issue-<n>/reports/conformance-review.md", "write the finding block with
  evidence and spec_ref", "리뷰 판정 기록해줘". Covers the five-verdict set (Present,
  Surface, Absent, Incorrect, Unverifiable) and the refusal to write a verdict
  with no evidence pointer or spec_ref. Do NOT use for choosing which verdict
  the located evidence supports (use conformance-review-verdict-assignment).

---

# finding-record

Covers both initial recording and dispute resolution (recorded inline,
still against the same finding). Produces the per-requirement finding
record inside `docs/issue-<n>/reports/conformance-review.md`, the skill's record
file, at the requirement blocks below the header block.

This skill never writes to any file other than `docs/issue-<n>/reports/conformance-review.md`. It does
not fix, patch, or suggest a patch for anything it finds — it reports.

## Trigger

Apply this skill once a requirement has been checked and its
verdict needs to be written down in `docs/issue-<n>/reports/conformance-review.md` — never to fix or
patch what was found.

## Procedure

1. Record the verdict solo by default; ask the user only when the
   requirement genuinely cannot be checked from what's available, for
   the missing evidence or access (see "What it asks the user for").
2. Choose exactly one of the five verdicts; never merge them into a bare
   pass/fail (see "The verdict set").
3. Fill in the full field list for the requirement block — requirement,
   spec_ref, verdict, evidence, rationale, and spec_vs_built when the
   verdict is Incorrect (see "The artifact and its field list").
4. Refuse to write Present, Surface, Absent, or Incorrect with no
   evidence pointer or no spec_ref (see "Refusal the skill itself
   enforces").
5. When a finding is disputed, record its re-examination
   inline rather than treating the dispute as a request to fix anything
   (see "What it asks the user for").
6. Before writing, run the per-requirement checklist (see
   "Per-requirement checklist").

## Output shape

One `---`-delimited block per requirement inside `docs/issue-<n>/reports/conformance-review.md`,
carrying the full field list and a verdict from the fixed five-value
set, with a write refused when a required evidence pointer or spec_ref
is missing.

## Rule index

Full rule text, citations, and counter-examples:
`references/rules.md` in this skill's directory — read it when a
matched rule's detail is needed.

- 3.1 — **`requirement`** — a stable identifier for the specific requirement/claim being checked, verbatim from the specification (or a stable id if the spec numbers its own req…
- 3.2 — **`spec_ref`** — the exact clause/section/requirement-id in the spec being checked against, distinct from the free-text `requirement` field above. Where the spec is unnu…
- 3.3 — **`verdict`** — one of the five values above. EARL counterpart: the spec's `result` field — a different 5-value enum (`passed|failed|cantTell|inapplicable|untested`) ove…
- 3.4 — **`evidence`** — a pointer into the actual diff: file path, line number, or hunk. Never a paraphrase of what the diff does — the reproduction path itself, mirroring OWAS…
- 3.5 — **`rationale`** — one line connecting the evidence to the verdict: why this evidence supports this verdict, not a restatement of either
- 3.6 — **`spec_vs_built`** — required only when `verdict: Incorrect`: what the spec required, versus what was actually built. Optional/omitted for every other verdict
- S1 — What it asks the user for → references/rules.md
- S2 — The verdict set → references/rules.md
- S3 — EARL alignment (issue-521 spec) → references/rules.md
- S4 — Refusal the skill itself enforces → references/rules.md
- S5 — What this skill never does → references/rules.md
- S6 — Per-requirement checklist → references/rules.md

## Rationalizations

Documented excuses agents used to skip this gate, each rebutted and tied
back to a rule and its originating incident: see
[references/rationalizations.md](references/rationalizations.md).
