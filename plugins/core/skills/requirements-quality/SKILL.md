---
name: requirements-quality
description: >-
  A procedure for auditing and rewriting natural-language requirements and user stories against
  objective, checkable criteria: EARS pattern conformance for system/functional requirements, and
  the Connextra template plus the QUS 13-criteria checklist for agile user stories. Use it when
  someone wants requirements or user stories reviewed, tightened, or written to a standard — e.g.
  "이 요구사항 문서 검토해줘", "유저스토리 좀 다듬어줘", "이 스펙에 요구사항 품질 체크 해줘", "review these
  requirements", "check this story against INVEST/QUS", "우리 요구사항이 모호한지 감사해줘", "write this as
  an EARS requirement". Every step here produces a binary pass/fail against a named pattern or
  checklist item — never a subjective "does this feel clear" call. Do NOT use it to figure out
  what the requirements *should be* (that's discovery, not audit — see user-discovery), to decide
  whether a feature is worth building at all (diagnose-first / market-recon), or for a single
  already-conformant item that just needs one obvious edit — for that, just make the edit.
---

# Requirements Quality

## First: does this even need the procedure?

- **Is the fix already known and small?** "Change 'user' to 'authenticated user' in story 3," "this one sentence is missing 'shall'" — that's an edit, not an audit. Just make it. Don't run the inventory, don't build a violations table for one line.
- **Is this actually a discovery problem?** If nobody yet knows what the system is supposed to do, no amount of EARS/QUS checking will produce that — this skill audits *stated* requirements, it doesn't invent them. Route to user-discovery instead.
- **Is the input not requirement/story statements at all?** A full PRD needing product judgment, an architecture doc, a roadmap — not this skill's job. This skill's job starts once there are candidate requirement or story *sentences* to check.
- **Is the set tiny (1-2 items) with no shared-template question at stake?** A quick manual pattern check may be enough; you don't need the full six-step machinery. Still keep whatever check you do binary — see the design rule below, it isn't optional just because the procedure is skipped.

Everything below applies once there's an actual set of requirements or stories to audit or rewrite systematically.

## The design rule (non-negotiable)

Every step in this procedure carries an explicit, objective pass/fail test: a syntactic pattern match, an enumerable checklist item present or absent, or a binary yes/no. If a check can't be reduced to one of those three, it does not belong in this procedure — write it into the residual list at Step 6 instead of pretending to audit it. "Check if it's clear" is not a step. "Check whether the sentence contains a word from this ambiguous-term list" is.

## The procedure

### Step 1 — Inventory

Collect every requirement or user story in scope into one numbered list.

**Gate:** a numbered list exists and its count is stated out loud (e.g., "14 requirements, 9 stories"). If you can't produce a count, the inventory isn't done — go find the rest before auditing anything.

### Step 2 — Route by artifact type

Classify each inventoried item into exactly one route:

- **System/functional requirement** ("the system shall…", an API or behavior spec) → Step 3 (EARS conformance).
- **Agile user story** (role/goal/benefit shaped) → Steps 4 and 5 (template check, then QUS).
- **Non-functional requirement** (performance budget, security property, availability target) → do **not** force it through EARS; note it as out of scope for pattern-matching and flag it for whatever NFR format the team already uses. Forcing an NFR into a trigger-response sentence produces a syntactically valid but semantically empty requirement, which is worse than an honest "doesn't fit."

**Gate:** every item in the inventory has exactly one route assigned; nothing is left unclassified.

### Step 3 — EARS conformance check (for requirements)

Test each requirement against the six EARS patterns (Mavin et al., IEEE RE'09):

| Pattern | Form |
|---|---|
| Ubiquitous | "The `<system>` shall `<response>`" |
| Event-driven | "When `<trigger>`, the `<system>` shall `<response>`" |
| State-driven | "While `<state>`, the `<system>` shall `<response>`" |
| Optional feature | "Where `<feature>`, the `<system>` shall `<response>`" |
| Unwanted behavior | "If `<trigger>`, then the `<system>` shall `<response>`" |
| Complex | an explicit, well-formed combination of the above (e.g., "While `<state>`, when `<trigger>`, the `<system>` shall `<response>`") |

**Pass/fail:** the requirement matches exactly one pattern's structure, including keyword order (When/While/Where/If…then, shall). No match = fail. On fail, rewrite into the closest pattern and re-test until it passes, or route it out per the limits below.

**Known limits — state these, don't paper over them:**
- Requirements with several simultaneous preconditions get awkward under EARS. If a faithful rewrite needs three nested When/While clauses, that's a signal to split the requirement into two, not to force a single contorted sentence through the template.
- Non-functional requirements fit the six patterns poorly — a latency budget or a security property isn't naturally a trigger-response sentence. These should already have been routed out at Step 2; if one slipped through, route it out now rather than manufacture a fake pass.

**Gate:** every requirement routed here has a recorded pass/fail verdict, and every fail has either a rewritten passing version or an explicit "routed out, doesn't fit EARS" note with a reason.

### Step 4 — User story template check

For each story, record two yes/no answers:

1. Does a shared team template exist and is it being used — Connextra ("As a `<role>`, I want `<goal>`, so that `<benefit>`") or the team's own documented template? Yes/no.
2. Is the why/so-that (benefit) clause actually present in the story text? Yes/no — clause present or absent, not a judgment about whether the stated reason is *good*.

**Pass = both yes.**

**Evidence note (state this precisely, don't overclaim):** the benefit tracked by this check comes from a team sharing *some* template at all — not from Connextra being superior to any other template. The source is Lucassen et al. 2016, a practitioner-perception survey (N=182, 2015 sample skewed toward Dutch respondents), not a study that measured actual development outcomes. Report it at that grade — "teams that share a template report this benefit," not "using this template causes this benefit."

**Gate:** every story has both yes/no values recorded.

### Step 5 — QUS 13-criteria check (per story)

Run each story against all 13 criteria from the QUS framework (Lucassen et al. 2016, *Requirements Engineering* journal). Each criterion gets an operational, binary test — not a vibe check:

**Syntactic**
1. *Well-formed* — role and goal (means) are both present in their expected slots. Pass = both present.
2. *Atomic* — describes exactly one requirement. Pass = no "and"-joined goal that is independently implementable/testable as a separate story; if splittable, fail.
3. *Minimal* — no implementation/UI/design detail beyond role, goal, benefit. Pass = no solution-level detail found; if present, fail.

**Semantic**
4. *Conceptually sound* — each slot's content matches its label (a goal isn't sitting in the role slot, etc.). Pass = type-match confirmed for every slot.
5. *Problem-oriented* — states the need, not the implementation. Pass = the goal names a "what/why," not a specific "how" (a UI widget, an algorithm); a named "how" fails.
6. *Unambiguous* — contains no term from a known ambiguous/subjective-term list without a defined threshold ("fast," "easy," "user-friendly," "some," "appropriate," etc.). Pass = no flagged term found.
7. *Conflict-free* — checked pairwise against the rest of the inventory for the same role/goal area. Pass = no contradiction detected against another story in the set.

**Pragmatic**
8. *Full sentence* — grammatically complete: role clause + verb + goal clause. Pass = complete sentence structure.
9. *Estimatable* — names a scope a team could in principle size (not open-ended). Pass = goal is bounded, not phrasing like "the app should be good."
10. *Unique* — no duplicate or near-duplicate exists elsewhere in the inventory. Pass = no duplicate found on inventory scan.
11. *Uniform* — follows the same template structure as the rest of the set (the template identified in Step 4). Pass = structural match; mismatch fails.
12. *Independent* — no hard sequential dependency stated or implied on another specific story. Pass = no such dependency found; if one is stated, fail and note the dependency.
13. *Complete* — role and goal are both present without requiring unwritten external context to parse. Pass = self-contained as written.

**Output:** a violations table, story × criterion, one row per story and one column per criterion, each cell marked pass/fail (with a one-line reason for every fail).

**Gate:** the table has a cell for every story × criterion pair — no blanks.

### Step 6 — Report

Deliver three things, in this order:

1. **Violations found** — pulled directly from the Step 3/4/5 tables.
2. **Rewrites proposed** — one rewritten version per failing item, re-checked against the same gate it failed.
3. **Residual list** — what this audit does *not* establish (see the evidence-grade section below; always carry the document-quality-vs-development-outcome distinction into this list by name).

**Gate:** the report contains all three sections, and the residual list explicitly states the outcome-vs-document-quality distinction rather than implying the audit proves development got better.

## Evidence grade — what this actually buys you

Keep these two claims separate in every report; do not let the first quietly stand in for the second.

**Supported: this reduces defects in the requirements document itself.**
- EARS traces to a single-industry case-study lineage (Rolls-Royce aero-engine airworthiness analysis, published IEEE RE'09, Mavin et al.). Broad adoption is reported (Airbus, Intel, NASA), but independent confirmation beyond author self-report exists only for Intel — grade this as single-industry case-study evidence, not a general causal claim.
- QUS's partial-automation tool, AQUSA, measured 93.8% recall over 1,023 user stories across 18 companies — a real, measured detection result. Cite it as a tool-measurement number, not as proof that using QUS improves anything downstream.

**Largely NOT empirically established: this improves development outcomes** (fewer downstream bugs, faster delivery, better product-market fit). Frattini et al. 2023 (*Requirements Engineering* journal), a meta-diagnosis of the field, found that roughly 30% of the 57 primary studies surveyed don't even report downstream effects, and none economically substantiates a defect-cost figure. State this plainly in every residual list: passing EARS/QUS makes the requirement or story better-formed as a document; it is not established that this alone improves what gets built.

## Forbidden citations

Never cite these in an audit's output, even in passing:

- CHAOS report requirements-factor percentages (e.g., claims that requirements/user issues are the top cause of project failure) — refuted under adversarial review; the underlying sample is undocumented.
- The 10-200x defect-cost multiplier presented as settled fact — the Boehm cost-curve's reproducibility is contested and unresolved. If a cost-of-defect argument comes up at all, flag it as contested, never cite the multiplier as established.
