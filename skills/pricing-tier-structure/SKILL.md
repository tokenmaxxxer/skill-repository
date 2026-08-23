---
name: pricing-tier-structure
description: >-
  Use when a verdict has already settled a correctly-labeled price point or
  preference share and the question turns to packaging it — choosing a
  value-metric billing unit and assembling a Good/Better/Best tier structure
  with a deliberate anchor tier. Trigger on requests like "요금제 티어 짜줘", "good
  better best packaging", "what unit should we bill on", "which tier should be
  the anchor". Do NOT use to choose or grade the research method behind the
  numbers (use pricing-method-family).
metadata:
  axis: tier-structure
  rule_count_floor: 2
---

# Tier-structure decision rules

Decisions for `pricing-verdict-report` (chain position 4/4), the
tier-structure element of this role's PRODUCES line: how a fielded
verdict's numbers assemble into packaging, once the research-method
rules elsewhere in this chain have produced a correctly-labeled price
point or preference share.

## Trigger

Use once a research method elsewhere in the chain has already produced a
correctly-labeled price point or preference share and the remaining
question is packaging: what unit to bill on, and how to assemble a
Good/Better/Best structure around the fielded numbers. Do not use it to
choose or grade the underlying research method (that is
`pricing-method-family` / `pricing-design-rigor` upstream), and do not
use it when the decision never asked a tiering/packaging question in the
first place.

## Procedure

1. Cite decision rule 1 before assigning any unit as the pricing metric,
   to run the value-metric test explicitly and record whether delivered
   value grows with that unit.
2. Cite decision rule 2 when assembling a Good/Better/Best tier
   structure from a fielded verdict, to assign the anchor role to the
   middle tier deliberately rather than wherever the numbers happen to
   land.
3. Cite decision rule 3 when the fielded verdict covers a single-product,
   single-price decision with no tiering question in scope, to skip the
   Good/Better/Best assembly entirely.

## Output shape

Applying this skill produces a packaging decision: either a named,
value-metric-tested billing unit plus a Good/Better/Best structure with
an explicit anchor tier, or an explicit statement that no tier structure
applies because the decision was never a packaging question.

## Decision rules

1. Before assigning ANY unit (seats, usage, records, API calls, a flat
   fee) as the pricing metric for a tier structure, run the value-metric
   test explicitly and record the answer: "as a customer's use of this
   unit grows, does their delivered value grow with it?" A metric that
   fails this test (e.g. billing per login when logins don't track
   value) produces a bill customers experience as arbitrary rather than
   fair, and it decouples revenue growth from the value the product
   actually delivers — the tier structure will look internally
   consistent while silently mispricing every account that grows
   differently from the metric.
   source: OpenView Partners, "How to Capture the Right Value Metrics to
   Accurately Price Your Product"
   (https://openviewpartners.com/blog/how-to-price-your-product/) —
   states the value-metric test as legible-without-a-spreadsheet,
   aligned with how the customer receives value, and scaling with usage/
   success so accounts expand without renegotiation.

2. When assembling a Good/Better/Best tier structure from a fielded
   verdict, assign the recommended-purchase anchor role to the MIDDLE
   tier deliberately, not to whichever tier the numbers happen to land
   on: price Good as the credible entry point, Better as the tier most
   customers should land on (the one the verdict's numbers should be
   optimized to make attractive), and Best at roughly 2-3x Better so its
   presence makes Better look reasonable by contrast rather than
   expensive in isolation. A tier structure with no explicit anchor
   tier lets whichever price a study output lands on become the de
   facto anchor by accident, which may not be the tier the business
   actually wants most customers choosing.
   source: general SaaS Good-Better-Best packaging convention (three
   tiers differentiated by feature gating, usage limits, and support
   level, with the middle tier structured as the default recommendation)
   — this convention's decoy/anchor logic is standard multi-tier
   pricing-page practice, distinct from and complementary to this
   rulebook's own conjoint/PSM design-rigor rules, which govern how the
   underlying price points are measured, not how they are packaged into
   tiers.

3. **[removal]** When the fielded verdict covers a single-product,
   single-price decision (no tiering question was ever in scope — e.g.
   the request is scope-gate rule 1's "not yet pricing-shaped" exit, or
   a flat-fee product with no packaging variants under consideration) —
   do not force a Good/Better/Best assembly onto the verdict. Inventing
   tiers for a decision that only asked "what single price" manufactures
   a packaging structure nobody requested and adds a decoy/anchor
   judgment call the verdict has no data to inform.
   source: this repo's own chain scope (`README.md` PRODUCES line names
   "tier structure" as one of three outputs, not a mandatory element of
   every verdict) — tiering is conditional on the decision actually
   being a packaging question.

## Related skills

- [pricing-design-rigor](../pricing-design-rigor/SKILL.md) — after structuring tiers, run pricing-design-rigor to check the result for honesty gaps.
