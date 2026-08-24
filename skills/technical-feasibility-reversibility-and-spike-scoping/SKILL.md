---
name: technical-feasibility-reversibility-and-spike-scoping
description: >-
  Use when a candidate architectural decision must be sorted into two-way-door
  vs. one-way-door and, for one-way-door candidates, scoped into a timeboxed
  spike with sensitivity/tradeoff points and third-party-checkable acceptance
  criteria. Trigger on requests like "one-way door인지 판단해줘", "is this decision
  reversible", "scope a spike for this unknown", "set the spike timebox and
  acceptance criteria". Do NOT use for stamping the Reversibility field on
  individual probe findings already being written to docs/issue-<n>/reports/technical-feasibility.md (use
  technical-feasibility-reversibility-tag), nor for running the spike itself and
  writing its report (use technical-feasibility-spike-report).
metadata:
  axis: reversibility-and-spike-scoping
  rule_count_floor: 10
  axes:
    - reversibility-and-spike-scoping
    - build-vs-buy-dependency-health
    - license-and-regulatory-risk
    - threat-model-disposition
    - verdict-and-timebox-selection
---

# Decision axis: reversibility classification & spike scoping

## Trigger

Use this axis when the task at hand is sorting a candidate architectural
decision into two-way-door (reversible) vs. one-way-door
(consequential-and-nearly-irreversible), and — for one-way-door
candidates — scoping the spike itself: setting its timebox, naming its
sensitivity and tradeoff points, and writing acceptance criteria before
exploration starts. It is distinct from its sibling axes, which fire
later or on different questions: build-vs-buy-dependency-health judges
whether a specific dependency is healthy enough to adopt,
license-and-regulatory-risk and threat-model-disposition judge legal and
security exposure of a chosen approach, and verdict-and-timebox-selection
assembles the final go/no-go/conditional verdict once all probes
(including this axis's classification) have resolved.

## Procedure

1. Classify the candidate decision as two-way-door (reversible) or
   one-way-door (consequential-and-nearly-irreversible); use this binary,
   not a continuous risk score (rule 1).
2. If two-way-door, let a single engineer or small group decide fast on
   about 70% of the desired data instead of escalating for full
   consensus (rule 2).
3. If one-way-door, route it through the full four-probe evidence bar
   (technical/prior_art/legal_regulatory/threat_model) and escalate to
   `conditional` rather than `go` if any probe cannot resolve to
   pass/fail with cited evidence inside the timebox (rule 3).
4. When scoping what the spike report must contain, name sensitivity
   points and tradeoff points explicitly and classify each as risk or
   non-risk (rule 4).
5. Anchor each candidate quality-attribute scenario to a stakeholder-
   stated business goal, not an engineer's abstract guess (rule 5).
6. Before work starts, agree the spike's timebox (1-3 days) with the
   human; never self-assign it after research has already begun
   (rule 6).
7. If the timebox expires without a conclusive pass/fail, stop and put
   "extend vs. stop" to the human explicitly rather than continuing
   silently (rule 7).
8. When two approaches trade off the same quality attributes at
   different reversibility tiers, prefer the two-way-door option even if
   it scores slightly lower on the sensitivity analysis (rule 8).
9. Draft acceptance criteria before any exploratory work starts, phrased
   so a third party could check pass/fail from the deliverable alone
   (rule 9).
10. Drop any candidate that requires large upfront infrastructure
    investment, specialized hiring, or a fundamental change to how the
    org operates from the two-way-door fast-decide path entirely, even
    if individual line items look reversible in isolation (rule 10).
11. Before accepting a spike candidate that looks workable on first
    pass, hold the verdict and force one more explicit round of
    question-and-answer on what the candidate forecloses (rule 11).

## Output shape

Applying this skill produces a record entry stating the candidate's
reversibility classification (two-way-door or one-way-door), and — when
one-way-door — the spike's agreed timebox, its named sensitivity and
tradeoff points each tagged risk or non-risk, its business-goal-anchored
scenarios, and its pre-written third-party-checkable acceptance
criteria, together with an explicit extend-vs-stop call if the timebox
expired inconclusively.

## Rule index

Full rule text, citations, and counter-examples:
`references/rules.md` in this skill's directory — read it when a
matched rule's detail is needed.

- 1.1 — **when** classifying a candidate architectural decision for the spike report **choose** the two-way-door / one-way-door binary (reversible vs. consequential-and-nearly-i…
- 1.2 — **when** a decision is classified two-way-door **choose** let a single engineer or small group decide fast on ~70% of the desired data rather than escalate for full cons…
- 1.3 — **when** a decision is classified one-way-door **choose** route it through the full four-probe evidence bar (technical/prior_art/ legal_regulatory/threat_model) and esca…
- 1.4 — **when** scoping what the spike report must contain **choose** name the sensitivity points (architectural features that affect a quality-attribute response) and tradeoff…
- 1.5 — **when** writing candidate quality-attribute scenarios for the spike **choose** anchor each scenario to a business goal stated by the stakeholders, not an engineer's gue…
- 1.6 — **when** a spike's timebox is about to be set **choose** 1-3 days agreed with the human BEFORE work starts, never self-assigned after research has already begun — a time…
- 1.7 — **when** a spike's timebox expires with no conclusive pass/fail **choose** stop and put "extend vs. stop" to the human explicitly, never silently continue past the agree…
- 1.8 — **when** two architectural approaches trade off the same quality attributes but at different reversibility tiers **choose** the two-way-door option even if it scores sli…
- 1.9 — **when** a spike's acceptance criteria are being drafted **choose** write them before any exploratory work starts, phrased so a third party (not the spike's author) coul…
- 1.10 — **REMOVAL — when** a candidate architecture requires large upfront infrastructure investment, specialized hiring, or changes how the org fundamentally operates **choose*…
- 1.11 — **when** a spike candidate looks workable on first pass **choose** hold the verdict and force one more round of explicit question-and-answer on what the candidate forecl…
