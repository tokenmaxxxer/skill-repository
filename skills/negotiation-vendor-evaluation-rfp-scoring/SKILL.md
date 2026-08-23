---
name: negotiation-vendor-evaluation-rfp-scoring
description: Use when designing an RFP's evaluation-criteria section, scoring competing vendor proposals against weighted criteria, or reviewing an existing vendor-scoring matrix for a criterion that can single-handedly decide the award.
metadata:
  axis: weighted-criteria-scoring-integrity
  rule_count_floor: 3
  tier: sparse
---

# Vendor evaluation and RFP scoring

Practitioner rules for weighting evaluation criteria, anchoring numeric
scores, and keeping an RFP's evaluation section auditable and separate
from its requirements section.

## Trigger

Use when designing an RFP's evaluation-criteria section, scoring
competing vendor proposals against weighted criteria, or reviewing an
existing vendor-scoring matrix for a criterion that can single-handedly
decide the award.

## Procedure

1. Assign each evaluation criterion a percentage weight summing to
   100%, and cap any single criterion — commonly 40% — so that no one
   factor, including price, can unilaterally decide the award (rule 1).
2. Write down what each numeric score point means, with a concrete
   example, before scoring any vendor (rule 2).
3. Keep the evaluation-criteria section separate from the RFP's
   technical-requirements section, and document the reasoning behind
   each score (rule 3).

## Output shape

A weighted evaluation-criteria matrix with an explicit per-point
scoring anchor, kept separate from the requirements section, with
documented reasoning behind each vendor's score.

## Decision rules

### 1. Weight every criterion and cap any single criterion from deciding the award alone
- **Condition**: designing an RFP's evaluation-criteria section before proposals are scored
- **Choice**: assign each evaluation criterion a percentage weight, with all weights summing to 100%, and cap any single criterion (commonly 40%) so that no one factor — including price — can unilaterally decide the award
- **Why**: an unweighted or uncapped criteria list lets one factor (most often lowest price) silently dominate the award regardless of the other criteria's stated importance, defeating the purpose of a multi-criteria evaluation
- **Source**: Responsive, "RFP Scoring: How to Evaluate Vendor Proposals", https://www.responsive.io/blog/rfp-scoring ; AutoRFP.ai, "RFP Evaluation Criteria and Scoring Guide", https://www.autorfp.ai/resources/rfp-evaluation-criteria
- **Counter-example test**: an evaluation matrix listing five criteria with no stated weights, where the lowest-price vendor wins regardless of how it scored on the other four, fails this rule.

### 2. Anchor every numeric score point with a concrete example before scoring any vendor
- **Condition**: about to score competing vendor proposals against a numeric scale (e.g. 1-5) on any criterion
- **Choice**: write down what each score point on the scale means, with a concrete example distinguishing it from adjacent points, before scoring any vendor
- **Why**: an unanchored numeric scale — a "3" with no stated meaning — is the named failure mode that lets evaluator bias substitute for the criterion itself, since different evaluators silently apply different standards to the same number
- **Source**: Inventive.ai, "How to Score RFP Responses Objectively", https://www.inventive.ai/blog/rfp-scoring ; Responsive, "RFP Scoring: How to Evaluate Vendor Proposals", https://www.responsive.io/blog/rfp-scoring
- **Counter-example test**: two evaluators independently scoring the same vendor response 2 and 5 on the same criterion, with no written anchor explaining what either number means, fails this rule.

### 3. Keep evaluation criteria separate from requirements and document the reasoning behind each score
- **Condition**: drafting or reviewing an RFP's evaluation-criteria section, or auditing a completed vendor-scoring matrix
- **Choice**: keep the evaluation-criteria section separate from the RFP's technical-requirements section, and document the reasoning behind each score, so the criteria used to judge is never confused with what was merely required, and the award is auditable after the fact
- **Why**: conflating requirements (what a proposal must satisfy to be considered) with evaluation criteria (what differentiates the score between qualifying proposals) makes both sections harder to audit and invites disputes over why one qualifying vendor scored lower than another with no documented reasoning to point to
- **Source**: AutoRFP.ai, "RFP Evaluation Criteria and Scoring Guide", https://www.autorfp.ai/resources/rfp-evaluation-criteria
- **Counter-example test**: an RFP whose "requirements" section also assigns point values, with no separate evaluation-criteria section and no written rationale for any vendor's score, fails this rule.

## Related skills

- `technical-feasibility-build-vs-buy` — once a build-vs-buy analysis
  resolves toward "buy," the vendor short-list routes here for scoring.
- `negotiation-batna-and-zopa-preparation` — once a vendor is selected
  via scoring, price/term negotiation with that vendor chains there.
- `partnerships-bd-deal-structure-selection` — when the "vendor" being
  scored is actually a candidate partner, the deal-vehicle decision
  chains there after scoring narrows the field.
