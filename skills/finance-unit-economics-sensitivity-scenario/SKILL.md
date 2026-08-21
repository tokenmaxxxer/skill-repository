---
name: finance-unit-economics-sensitivity-scenario
description: Use when you need guidance on Sensitivity / scenario analysis — decision rules. Applies to the sensitivity-scenario axis.
axis: sensitivity-scenario
rule_count_floor: 12
tier: moderate
---

# Sensitivity / scenario analysis — decision rules

## Decision rules

- **ADDITION**: when the decision is "which assumption matters most,"
  run one-variable sensitivity analysis before scenario analysis rather
  than jumping straight to multi-variable scenarios — sensitivity
  analysis narrows which variables are worth building full scenarios
  around, so scenario work done first wastes effort on combinations
  that don't matter. source:
  https://www.financealliance.io/sensitivity-analysis-vs-scenario-analysis/
  (sensitivity analysis should precede and focus scenario analysis).

- **ADDITION**: when presenting a forward model to a non-finance
  stakeholder, use exactly three named scenarios (base/bull/bear) as
  the default structure rather than an open-ended list of cases — a
  fixed three-case frame is the field's established convention and
  keeps the comparison legible. source:
  https://www.farseer.com/blog/scenario-planning-or-sensitivity-analysis/
  (base case = management's best estimate, bull = optimistic, bear =
  pessimistic).

- **REMOVAL**: when a sensitivity table already varies a driver across
  its full plausible range, cut a duplicate "what-if" appendix slide
  that re-tests the same single variable at only two points — the
  one-line tornado/sensitivity output already contains the two-point
  comparison as a strict subset, so keeping both is unnecessary
  repetition. source:
  https://ibinterviewquestions.com/blog/sensitivity-scenario-analysis-financial-modeling
  (sensitivity tables are built to already sweep a variable's range).

- **ADDITION**: when a variable feeds more than one output (e.g. churn
  feeding both LTV and the payback denominator), define it once, named,
  and reference that single definition everywhere it is used, rather
  than hardcoding the same figure separately in each section — a
  scenario shift to one driver must then visibly propagate to every
  dependent output in the same pass; if two sections' verdicts move by
  different amounts under the same stated shift, that signals they used
  different values for what should be one variable.

## Notes

Sensitivity and scenario analysis are complementary, not
interchangeable — sensitivity narrows the field, scenario tells the
story on the narrowed set. See ltv-churn-assumption.md for the churn
case this axis most often gets applied to.
