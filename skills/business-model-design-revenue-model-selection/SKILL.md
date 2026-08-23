---
name: business-model-design-revenue-model-selection
description: Use when choosing a revenue-model archetype (subscription, usage-based, freemium, marketplace/take-rate, or licensing) for a new or changing business model, based on value-metric alignment, end-user type, consumption pattern, or company stage — upstream of pricing-method-family, which picks a research method within an archetype already chosen here.
metadata:
  axis: revenue-model-selection
  rule_count_floor: 7
---

# Revenue-model archetype selection decision rules

Decision rules for choosing a revenue-model archetype before any
pricing-method research is fielded. Research trail: layer 1
(a16z, OpenView, Bessemer, Strategyzer, David Skok practitioner
sourcing).

## Trigger

Apply this skill when choosing a revenue-model archetype for a new or
changing business model — subscription, usage-based, freemium,
marketplace/take-rate, or licensing — based on value-metric alignment,
end-user type, consumption pattern, or company stage.

## Procedure

1. Choose a pricing metric that scales with customer value received,
   not cost to serve (rule 1).
2. Split on end-user type: usage-based for machine end users,
   subscription for human end users (rule 2).
3. For AI products, shift the metric from seats to output as the task
   becomes automated (rule 3).
4. Default to usage-based when consumption naturally grows with
   customer success, and use the NRR bands to judge model health
   (rule 4).
5. Choose freemium for low-marginal-cost, high-virality products;
   choose marketplace/take-rate when the value-add is matching two
   sides (rule 5).
6. At early stage, optimize for adoption over extraction (rule 6).
7. Use category-wide usage-based adoption as a benchmark signal for
   whether usage-based is a viable default (rule 7).

## Output shape

A named revenue-model archetype (subscription, usage-based, freemium,
marketplace/take-rate, or licensing) with the value-metric,
end-user-type, or stage reasoning behind it, ready to hand off to
`pricing-method-family` for method selection within that archetype.

## Rules

1. Choose a pricing metric that scales with the value the customer
   receives, not the cost to serve them — the metric must correlate
   strongly with value, share in customer success, allow starting
   small and scaling, and grow monotonically for the average customer.
   source: https://openviewpartners.com/usage-based-pricing/

2. When the end user of the product is other software (machine end
   user), usage-based/metered pricing fits because usage tracks
   cleanly to a metric; when the end user is human, subscription fits
   better because humans dislike monitoring their own usage/spend.
   source: https://a16z.com/usage-based-pricing-rule-of-thumb/

3. For AI products, shift the pricing metric from seats/users to
   output (work performed) as the product automates the underlying
   task — a seat-based metric stops tracking value once the human is
   no longer the unit of work.
   source: https://a16z.com/podcast/ai-is-upending-saas-pricing/

4. When consumption naturally grows with customer success, usage-based
   pricing is the standard choice because it expands net dollar
   retention automatically; use Bessemer's benchmark bands to judge
   the resulting model's health: 100% NRR is good, 110% is better,
   120%+ is best.
   source: https://www.bvp.com/atlas/state-of-the-cloud-2023

5. Choose freemium for low-marginal-cost, high-virality products,
   trading revenue predictability for reach (a small paying subset
   plus free-user network value); choose marketplace/take-rate pricing
   (a % of transaction value, not a flat fee) when the business's
   value-add is matching two transacting sides rather than producing
   the good or service itself.
   source: https://www.strategyzer.com/library/business-model-generation-book-summary

6. At early stage, optimize pricing for adoption and customer count
   over per-customer extraction; raise price only once value delivery
   is proven — extracting maximum revenue before value is proven
   trades a larger long-run customer base for near-term revenue the
   business has not yet earned.
   source: https://www.forentrepreneurs.com/saas-metrics-2/

7. **[removal]** When judging whether usage-based pricing is a viable
   default for a category, do not treat it as a niche or unproven
   choice — usage-based pricing is now mainstream (39%+ adoption in
   recent SaaS surveys), displacing pure seat pricing as products
   become infrastructure-like; use that category-wide adoption rate as
   a benchmark signal rather than defaulting to subscription out of
   habit.
   source: https://openviewpartners.com/blog/2023-pricing-data/

## Related skills

- `pricing-method-family` — this skill selects the revenue-model
  archetype; that skill picks the research method to price within it.
- `pricing-tier-structure` — structures tiers within the archetype
  chosen here.
- `finance-unit-economics-ltv-cac-band` — the revenue-model choice made
  here feeds the LTV assumptions that skill bands.
