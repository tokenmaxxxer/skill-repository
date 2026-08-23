---
name: pricing-scope-gate
description: >-
  Use when a pricing-adjacent request first arrives, before any method is
  fielded, to decide whether it names a defined product, whether an existing
  study already covers it within its shelf life, or whether it should be routed
  to market-recon or dropped entirely. Trigger on requests like "이거 가격조사부터 해야
  하나", "do we need new pricing research or is last year's study fine", "how long
  is a WTP study's shelf life", "price something we haven't defined yet". Do NOT
  use once the product and method question are already settled (use
  pricing-method-family).
metadata:
  axis: scope-gate
  rule_count_floor: 2
---

# Scope-gate decision rules

Decisions for `pricing-scope-gate` (chain position 1/4): whether an
existing study already answers the question, or whether to route
elsewhere before any method is fielded.

## Trigger

Use first in the chain (position 1/4), before `pricing-method-family` or
any other pricing skill runs — whenever a pricing-adjacent request
arrives and it is not yet established whether a method should be fielded
at all. Use it to check for an undefined product, an adequate prior
study still within its shelf life, or a request that is not really a
willingness-to-pay question (a rename, a promo discount). Do not use it
once a product and method question are already settled — that is
`pricing-method-family`'s job.

## Procedure

1. Cite decision rule 1 when the request names no defined product, to
   route to `market-recon` and exit without opening a pricing method.
2. Cite decision rule 2 when a prior study already measured the same
   product and segment within its shelf life, to cite that study and
   proceed straight to `pricing-verdict-report` instead of re-fielding.
3. Cite decision rule 3, when judging rule 2's shelf life, to apply the
   concrete 6-12-month-or-material-change cadence rather than an
   open-ended gut call.
4. Cite decision rule 4 when the request is a routine SKU/tier rename or
   a promotional discount with no change to what is delivered, to drop
   the scope-gate study entirely rather than opening a pricing method
   chain.

## Output shape

Applying this skill produces a routing decision made before any method
fields: proceed to `pricing-method-family`, route to `market-recon` and
exit, cite an adequate prior study and skip straight to
`pricing-verdict-report`, or drop the request as not a pricing-method
question at all. It does not itself produce a price number.

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
