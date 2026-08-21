---
axis: scope-gate
rule_count_floor: 2
---

# Scope-gate decision rules

Decisions for `pricing-scope-gate` (chain position 1/4): whether an
existing study already answers the question, or whether to route
elsewhere before any method is fielded.

## Decision rules

1. When the request names no defined product (no feature set, no
   variant boundary, no unit-of-sale) yet — do not open a pricing
   method; route to `market-recon` and exit. A pricing method needs a
   fixed object to price; fielding one against an undefined product
   produces numbers that cannot be attributed to anything.
   source: this repo's own chain contract (`README.md`
   "HAND-OFF: if the question is not yet pricing-shaped ... route to
   market-recon and exit").

2. When a prior study already measured the same product+segment within
   the decision's shelf life (no material attribute/segment change
   since), do not re-field a new study — cite the adequate prior study
   by name and proceed straight to `pricing-verdict-report` with that
   study's numbers. Re-running an unchanged study wastes respondent
   budget and produces two conflicting price points for the same
   product, forcing an arbitrary tie-break later.
   source: Sawtooth Software, "Van Westendorp Pricing Model Explained"
   (https://sawtoothsoftware.com/resources/blog/posts/van-westendorp-pricing-sensitivity-meter)
   — treats PSM output as a standing price map to be reused, not
   re-derived per decision.

3. When judging whether rule 2's "shelf life" still holds, use a
   concrete cadence rather than an open-ended gut call: treat a prior
   study as stale (re-field instead of reusing) once either (a) 6-12
   months have passed since it ran, or (b) the priced product's
   delivered value has materially changed since — new tier, added
   capability the segment weights heavily, or a cost-structure shift —
   whichever trigger fires first. An undefined "still valid" judgment
   quietly drifts toward always reusing the old number, which is the
   same respondent-budget-saving bias rule 2 exists to avoid abusing.
   source: general SaaS pricing-review practice of treating pricing as
   a decision revisited on a fixed cadence rather than set at launch
   and left unexamined — corroborated independently by OpenView
   Partners' framing of value-metric fit as something that must keep
   tracking delivered value as a product evolves
   (https://openviewpartners.com/blog/how-to-price-your-product/).

4. **[removal]** When the request is a routine SKU/tier RENAME or a
   promotional discount with no change to what is delivered, drop the
   scope-gate study entirely — do not open a pricing method chain at
   all. A relabeling or time-boxed discount is not a willingness-to-pay
   question; treating it as one manufactures a study for a decision
   that needs none.
   source: this repo's own `USE_WHEN` line ("신규 가격 정책이 걸릴 때") —
   the trigger is a NEW pricing policy, not every price-adjacent text
   change.
