---
name: finance-unit-economics-sensitivity-scenario
description: Use when a forward unit-economics model needs sensitivity analysis sequenced before scenario work, a fixed three-scenario frame, a deduplicated what-if appendix, or a single named definition for a variable feeding more than one output.
axis: sensitivity-scenario
rule_count_floor: 12
tier: moderate
---

# Sensitivity / scenario analysis — decision rules

## Trigger

Use when a forward unit-economics model is being stress-tested —
deciding which assumption matters most, presenting a model to a
non-finance stakeholder, reviewing a sensitivity table alongside a
what-if appendix, or defining a variable (e.g. churn) that feeds more
than one downstream output. Use it before
`finance-unit-economics-ltv-churn-assumption`'s scenario framing when
the question is general sequencing of sensitivity vs. scenario work,
not the churn-specific case.

## Procedure

1. Cite the 1st ADDITION bullet when the decision is which assumption
   matters most, to run one-variable sensitivity analysis before
   scenario analysis.
2. Cite the 2nd ADDITION bullet when presenting a forward model to a
   non-finance stakeholder, to use exactly three named scenarios
   (base/bull/bear).
3. Cite the REMOVAL bullet when a sensitivity table already varies a
   driver across its full plausible range, to cut a duplicate two-point
   what-if appendix.
4. Cite the 4th (final) ADDITION bullet when a variable feeds more than
   one output, to define it once, named, and reference that single
   definition everywhere, checking that dependent outputs move
   consistently under the same stated shift.

## Output shape

A sensitivity/scenario package: a sensitivity pass run before scenario
work, a fixed three-named-scenario (base/bull/bear) presentation for
non-finance stakeholders, no duplicate what-if appendix alongside a
full-range sensitivity table, and single, named, consistently-referenced
definitions for any variable feeding multiple outputs.

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

## Related skills

- [finance-unit-economics-proposal-shape](../finance-unit-economics-proposal-shape/SKILL.md) — a sensitivity scenario needs a shaped proposal from this skill as its baseline case.
