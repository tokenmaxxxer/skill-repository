---
name: business-model-design-platform-design
description: Use when deciding which side of a two-sided platform to subsidize, setting a marketplace take-rate, assessing multi-homing risk to platform defensibility, or sequencing a platform launch to solve the chicken-and-egg cold-start problem.
metadata:
  axis: platform-design
  rule_count_floor: 5
---

# Two-sided/multi-sided platform design decision rules

Decision rules for two-sided and multi-sided platform pricing
structure, governance, and launch sequencing. Research trail: layer 2
(Rochet & Tirole, "Platform Competition in Two-Sided Markets";
Hagiu, HBS/MIT Sloan) plus layer 1 (NfX network-effects practitioner
content).

## Trigger

Apply this skill when deciding which side of a two-sided platform to
subsidize, setting a marketplace take-rate, assessing multi-homing
risk to platform defensibility, or sequencing a platform launch to
solve the chicken-and-egg cold-start problem.

## Procedure

1. Subsidize the side with the greater cross-side network externality;
   recover margin on the less elastic side (rule 1).
2. Treat below-cost pricing on the subsidized side as a deliberate
   structural choice, not predation (rule 2).
3. Decide pricing, governance, and design jointly across sides, not
   pricing in isolation (rule 3).
4. When one side's multi-homing rises, expect pricing/steering power
   to shift toward the other side (rule 4).
5. Sequence launch from a viable single-player mode before assuming
   network effects will carry cold-start (rule 5).

## Output shape

A named subsidized side with the cross-side-externality reasoning, a
take-rate or price-allocation decision consistent with that reasoning,
a stated launch sequence addressing cold-start, and a multi-homing
risk read on platform defensibility.

## Rules

1. Subsidize the side generating the greater cross-side network
   externality; recover margin on the side with lower price
   elasticity — total price level and price allocation between sides
   are independent levers, so a platform can hold total price fixed
   and still change volume/profit by shifting the split between sides.
   source: https://www.tse-fr.eu/sites/default/files/medias/doc/wp/2002/platform.pdf

2. Treat below-cost or zero pricing on one side as often optimal, not
   predatory, when that side's participation is what attracts the
   profitable side — e.g. cardholders subsidized while merchants pay —
   because the subsidized side's low price is what generates the
   cross-side value the paying side buys.
   source: https://www.tse-fr.eu/sites/default/files/medias/doc/wp/2002/platform.pdf

3. Decide pricing, governance, and design jointly across sides rather
   than treating "which side to subsidize" as an isolated pricing
   question — a pricing decision made without also deciding governance
   (who can access which side, under what rules) and design (how sides
   interact) misses the bundle those three decisions actually form.
   source: https://sloanreview.mit.edu/article/strategic-decisions-for-multisided-platforms/

4. When multi-homing rises on one side (e.g. sellers dual-listing
   across marketplaces), expect pricing and steering power to shift
   toward the other side and platform defensibility to erode — a side
   that can costlessly participate on competing platforms has less to
   lose from the platform's pricing power than a single-homing side
   does.
   source: https://www.nfx.com/post/network-effects-manual

5. **[removal]** When sequencing a platform launch, do not assume
   network effects alone will solve chicken-and-egg — start from
   whether the product has a viable "single-player mode" delivering
   standalone value before the network exists, and launch that mode
   first; a platform with no standalone value for an early single
   participant has nothing to offer the first side while it waits for
   the second side to arrive.
   source: https://www.nfx.com/post/network-effects-manual

## Related skills

- `business-model-design-revenue-model-selection` — marketplace/
  take-rate archetype selection happens there; this skill governs the
  two-sided pricing structure once that archetype is chosen.
- `pricing-tier-structure` — structures tiers within a chosen side's
  pricing once the subsidize/recover split is set.
