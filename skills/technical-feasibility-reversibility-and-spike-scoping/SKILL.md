---
name: technical-feasibility-reversibility-and-spike-scoping
description: Use when a candidate architectural decision must be sorted into two-way-door vs. one-way-door and, for one-way-door candidates, scoped into a timeboxed spike with sensitivity/tradeoff points and third-party-checkable acceptance criteria — not when the task is comparing dependency health, license/regulatory exposure, threat-model disposition, or assembling the final verdict/timebox record.
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

## Rules

1. **when** classifying a candidate architectural decision for the
   spike report **choose** the two-way-door / one-way-door binary
   (reversible vs. consequential-and-nearly-irreversible), not a
   continuous "risk score" — the binary is what determines the
   deliberation mode in the next rule.
   source: "Some decisions are consequential and irreversible or
   nearly irreversible — one-way doors ... other decisions are
   changeable, reversible — they're two-way doors" — Amazon's Day 1
   culture writeup, AWS Executive Insights
   (https://aws.amazon.com/executive-insights/content/how-amazon-defines-and-operationalizes-a-day-1-culture/).

2. **when** a decision is classified two-way-door **choose** let a
   single engineer or small group decide fast on ~70% of the desired
   data rather than escalate for full consensus — the point of two-way
   doors is speed, and waiting for 90%+ certainty is itself the
   failure mode on this class.
   source: "the strategy for two-way doors is simple: since they are
   easily reversible ... make these decisions as fast as possible ...
   act with only about 70% of the data" — Product Talk, "Two-Way Door
   Decision" (https://www.producttalk.org/glossary-discovery-two-way-door-decision/).

3. **when** a decision is classified one-way-door **choose** route it
   through the full four-probe evidence bar (technical/prior_art/
   legal_regulatory/threat_model) and escalate to `conditional` rather
   than `go` if any probe cannot resolve to pass/fail with cited
   evidence within the timebox — one-way doors "must be made
   methodically, carefully, slowly, with great deliberation and
   consultation."
   source: same AWS Day 1 culture writeup as rule 1
   (https://aws.amazon.com/executive-insights/content/how-amazon-defines-and-operationalizes-a-day-1-culture/).

4. **when** scoping what the spike report must contain **choose**
   name the sensitivity points (architectural features that affect a
   quality-attribute response) and tradeoff points (features where two
   quality attributes move in opposite directions under the same
   parameter) explicitly, and end by classifying each as risk or
   non-risk — a spike that lists options without this classification
   has not actually located the risk.
   source: "Sensitivity points are features ... that affect responses
   to quality attribute requirements ... Tradeoff points are
   compromises ... By the end of the ATAM, all sensitivity points and
   tradeoff points should be categorized as either a risk or a
   non-risk" — Wikipedia, "Architecture tradeoff analysis method"
   (https://en.wikipedia.org/wiki/Architecture_tradeoff_analysis_method),
   corroborated by SEI's ATAM technical report
   (https://www.sei.cmu.edu/documents/629/2000_005_001_13706.pdf).

5. **when** writing candidate quality-attribute scenarios for the
   spike **choose** anchor each scenario to a business goal stated by
   the stakeholders, not an engineer's guess at what "performance" or
   "security" means in the abstract — ATAM evaluations exist to expose
   risk against business goals, and an ungrounded scenario cannot be
   scored as risk or non-risk.
   source: "ATAM evaluations expose architectural risks that
   potentially inhibit the achievement of an organization's business
   goals" — Wikipedia, ATAM
   (https://en.wikipedia.org/wiki/Architecture_tradeoff_analysis_method).

6. **when** a spike's timebox is about to be set **choose** 1-3 days
   agreed with the human BEFORE work starts, never self-assigned after
   research has already begun — a timebox set after the fact is not a
   stopping condition, it is a rationalization.
   source: spec `timebox` field, feasibility role directive
   (docs/specs feasibility role contract, this repo's own
   `feasibility/hooks/directive.sh`) — feasibility/hooks/directive.sh.

7. **when** a spike's timebox expires with no conclusive pass/fail
   **choose** stop and put "extend vs. stop" to the human explicitly,
   never silently continue past the agreed box — an expired timebox
   that keeps running unannounced defeats the reason a timebox was set
   (to bound one-way-door deliberation cost, rule 3).
   source: feasibility role directive, this repo —
   feasibility/hooks/directive.sh.

8. **when** two architectural approaches trade off the same quality
   attributes but at different reversibility tiers **choose** the
   two-way-door option even if it scores slightly lower on the
   sensitivity analysis — reopening a two-way door to correct a
   suboptimal pick costs less than living with a wrong one-way-door
   pick, per the framework's own stated tradeoff.
   source: "If you make a suboptimal two-way door decision, you don't
   have to live with the consequences for long — you can reopen the
   door" — Product Talk
   (https://www.producttalk.org/glossary-discovery-two-way-door-decision/).

9. **when** a spike's acceptance criteria are being drafted **choose**
   write them before any exploratory work starts, phrased so a third
   party (not the spike's author) could check pass/fail from the
   deliverable alone — criteria written after exploration invites
   fitting the criteria to whatever was found, which defeats the
   evidence bar this role enforces (no verdict until all probes
   resolve with cited evidence).
   source: feasibility role directive, spike-report/reversibility-tag
   skill contract, this repo — feasibility/hooks/directive.sh.

10. **REMOVAL — when** a candidate architecture requires large upfront
    infrastructure investment, specialized hiring, or changes how the
    org fundamentally operates **choose** drop it from the two-way-door
    fast-decide path entirely and force it through full one-way-door
    deliberation, regardless of how reversible any individual line
    item inside it looks in isolation — AWS's 2006 launch is the
    canonical one-way-door example precisely because the aggregate
    commitment, not any single reversible sub-decision, made it
    irreversible.
    source: "Amazon's launch of Web Services (AWS) in 2006 illustrates
    Bezos' framework as a one-way door decision. Launching AWS required
    massive infrastructure investment, hiring thousands of engineers
    ... and fundamentally changing how Amazon viewed itself" —
    ThynkIQ, "Reversible vs Irreversible Decisions: Bezos' Framework"
    (https://thynkiq.com/blog/reversible-vs-irreversible-decisions).

11. **when** a spike candidate looks workable on first pass **choose**
    hold the verdict and force one more round of explicit
    question-and-answer on what the candidate forecloses (which
    alternatives become harder or impossible once it ships) before
    accepting it — a candidate accepted on first-pass workability
    alone skips exactly the tradeoff-articulation step that separates
    a reasoned spike from a guess, and that gap only surfaces once the
    foreclosed alternative is needed later.
    source: survey of guided architecture-decision tools — the guided
    flow forces a series of forced-choice questions ("which existing
    product is this most like," "what does this version deliberately
    NOT do," conflict-resolution tradeoffs) before any implementation
    detail is allowed, rather than accepting the first workable
    answer.
