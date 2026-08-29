---
name: requirements-engineering-rules
description: >-
  Use when selecting an EARS sentence template while drafting a requirement, assigning a
  requirement's verification method, spotting a weak/ambiguous word or double reading, spotting a
  conjunction or mixed-verification-method requirement, deciding traceability-link granularity,
  breaking a MoSCoW-tier tie, or reviewing a spec for gold-plating/redundancy/staleness.
  Condition-matched drafting rules for the requirements-engineering skill. Trigger on requests like
  "이 요구사항 EARS 템플릿으로 써줘", "검증 방법 뭐로 지정하지", "write this as an event-driven EARS requirement",
  "assign a verification method for this requirement", "break this MoSCoW tie". Do NOT use for
  auditing a finished requirements document or user story against QUS/INVEST checklists (use
  requirements-quality) or for pulling test cases out of acceptance criteria (test-derivation).
metadata:
  subject: issue-1174
  rule_count_floor: 23
  axes: 7
  tier: rich
---

# Requirements-engineering operational playbook

Condition -> choice -> source decision rules for drafting requirements
(contract v3 skill: requirements-engineering). Distilled per-skill
research per issue #1174 amendment 1; evidence trail in
docs/issue-1174/reports/scout-brief.md. Rules are decisions, not
definitions: each names the triggering condition and the choice it
forces.

## Trigger

Use this skill when: selecting an EARS sentence template while drafting a
requirement (rules 1-6); assigning a requirement's verification method
(rules 7-11b); spotting a weak/ambiguous word or a statement admitting two
or more readings (rules 12-15); spotting a conjunction joining two
capabilities or a requirement needing two verification methods (rules
16-17); deciding traceability-link granularity or updating a stale link
(rules 18-20); breaking a MoSCoW-tier tie or classifying an unstated-
necessity requirement (rules 21-22); or reviewing a spec for gold-plating,
redundant coverage, supersession, missing subtraction pass, or an
unresolvable requirement (rules 23-27).

## Procedure

1. EARS-pattern selection (rules 1-6): classify the requirement's
   condition — always-true, event-triggered, state-persistent,
   error/fault, optional-feature, or multi-clause — and write it in the
   matching EARS template (ubiquitous, event-driven, state-driven,
   unwanted-behavior, feature, or complex).
2. Verification-method selection (rules 7-11b): assign one of Inspection,
   Demonstration, Test, or Analysis per the requirement's confirmability;
   never leave the method unset; pair a Test/Demonstration requirement
   with a literal runnable check when one exists; run a whole-batch
   consistency/coverage pass before handoff.
3. Ambiguity detection & resolution (rules 12-15): flag listed weak
   words, superlatives, and open-ended terms for a measurable/bounded
   restatement; log any statement admitting two or more readings and
   resolve to one before assigning an ID; rewrite negative statements as
   the positive capability they assert.
4. Singularity/atomicity (rules 16-17): split a requirement joined by a
   conjunction into independently verifiable requirements, and split a
   requirement that would need two different verification methods to
   close.
5. Traceability-link granularity (rules 18-20): link at requirement-to-
   test granularity for regulated/high-blast-radius work, coarser
   feature-to-group granularity for low-risk/exploratory work (stated in
   the matrix's status field), and always update a row's link/status in
   the same change a requirement changes in.
6. Prioritization tie-break (rules 21-22): break same-tier MoSCoW ties by
   Kano category (Must-Be > Performance > Delighter); return an
   unclassifiable requirement to elicitation rather than defaulting it to
   Could-Have.
7. REMOVAL (rules 23-27): delete gold-plated requirements outright, merge
   redundant requirements to one surviving ID, archive superseded
   requirements, run a dedicated subtraction-only review pass, and
   recommend removal (logged `unverifiable`/`source-unresolvable`) for a
   requirement that repeatedly fails ambiguity resolution.

## Output shape

A cited condition -> choice -> source decision per requirement-engineering
judgment point: the EARS template chosen, the verification method
assigned, the ambiguity flagged and its resolution, the singularity split
performed, the traceability granularity chosen, the MoSCoW+Kano tie-break
result, or the removal/merge/archive action taken — each traceable to the
rule number(s) it was derived from.

## Rule index

Full rule text, citations, and counter-examples:
`references/rules.md` in this skill's directory — read it when a
matched rule's detail is needed.

- 1.1 — Condition: the requirement holds under all system states with no trigger ("the system shall always X"). Choice: write it as a **ubiquitous** requirement — no When/While/…
- 1.2 — Condition: the requirement's behavior is triggered by a discrete event that can be detected at a point in time. Choice: use the **event-driven** template, "When <trigger…
- 1.3 — Condition: the requirement's behavior is active only while a condition/state persists (not a point event). Choice: use the **state-driven** template, "While <state>, the…
- 1.4 — Condition: the requirement describes handling of an error, fault, or undesired condition. Choice: use the **unwanted-behavior** template, "If <trigger>, then the <system…
- 1.5 — Condition: the requirement applies only when an optional feature/configuration is present. Choice: use the **feature** (Where) template, "Where <feature is included>, th…
- 1.6 — Condition: a drafted sentence needs two or more of When/While/Where clauses to be true. Choice: this is a **complex** EARS requirement — keep the clause order fixed (Whi…
- 2.7 — Condition: correctness can be confirmed by visual/documentary examination (e.g. a UI label matches spec text, a config value is present). Choice: verification method = *…
- 2.8 — Condition: correctness requires exercising the system and observing behavior end-to-end, without instrumented measurement (e.g. "the wizard completes in 3 clicks"). Choi…
- 2.9 — Condition: correctness requires a measured, repeatable execution against expected output (e.g. a numeric threshold, an API contract). Choice: verification method = **Tes…
- 2.10 — Condition: correctness cannot be directly observed or executed (e.g. a capacity/scalability projection, a security property provable only by modeling). Choice: verificat…
- 2.11 — Condition: a requirement's verification method cannot be assigned to any of the four. Choice: treat this as a drafting defect, not an escape hatch — rewrite the requirem…
- 3.12 — Condition: a requirement uses a listed weak word/phrase (adequate, as appropriate, as a minimum, effective, as required, normal, provide for, timely, easy to, user-frien…
- 3.13 — Condition: a requirement uses a superlative, comparative phrase, or open-ended term ("best", "faster", "as needed", "etc."). Choice: flag as an ambiguity-smell and requi…
- 3.14 — Condition: a requirement statement admits two or more distinct readings under a plain reading by a domain-competent reader. Choice: log it in the ambiguity list (stateme…
- 3.15 — Condition: a requirement is phrased as a negative statement ("the system shall not fail to..."). Choice: rewrite as the positive capability it actually asserts; a negati…
- 4.16 — Condition: a requirement sentence contains a conjunction ("and", "or") joining two independently verifiable capabilities. Choice: split into two requirements, each with…
- 4.17 — Condition: a requirement's downstream verification would need two different verification methods (e.g. part Inspection, part Test) to close. Choice: this is a signal the…
- 5.18 — Condition: the project is regulated/audit-bound or a requirement's failure has high blast radius (safety, compliance, payment). Choice: link at requirement-to-single-tes…
- 5.19 — Condition: the project is low-risk/exploratory and a fine-grained matrix would cost more reviewer time than it returns. Choice: link at feature-to-requirement-group gran…
- 5.20 — Condition: a requirement changes after its matrix row already exists. Choice: update the row's downstream_link and status in the same change, never leave a stale link —…
- 6.21 — Condition: two requirements compete for a fixed delivery slot and both pass the Must/Should/Could MoSCoW screen at the same tier. Choice: break the tie by Kano category…
- 6.22 — Condition: a requirement cannot be classified into any MoSCoW tier because no stakeholder has stated its necessity. Choice: this is not a Could-Have by default — return…
- 7.23 — Condition: a requirement's capability is not traceable to any stated stakeholder need (Axis 6's "Necessary" characteristic fails) — this is **gold-plating**. Choice: del…
- 7.24 — Condition: two or more requirements in the spec assert the same verifiable behavior under different IDs (redundant coverage). Choice: merge into one requirement and reta…
- 7.25 — Condition: a requirement is superseded by a later, more specific requirement covering the same behavior. Choice: remove the superseded requirement from the active spec (…
- 7.26 — Condition: reviewing a draft spec, the reviewer's default search for changes is additive ("what's missing") and no explicit subtraction pass has been run. Choice: run a…
- 7.27 — Condition: a requirement has failed the ambiguity-resolution gate (Axis 3, rule 14) more than once across review cycles with no stakeholder able to resolve the reading.…
- S1 — Removal-category self-check → references/rules.md
