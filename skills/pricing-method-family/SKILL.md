---
axis: method-family-selection
rule_count_floor: 3
---

# Method-family selection decision rules

Decisions for `pricing-method-family` (chain position 2/4): which
input the decision needs, which method family collects that input,
and — if conjoint-family — CBC vs rating-based (CVA).

## Decision rules

1. When the decision needs a price-perception THRESHOLD (is this price
   psychologically "too cheap"/"too expensive" for a single, largely
   unbundled product) and no tradeoff between features/attributes is
   in question — choose the Van Westendorp PSM family, which collects
   exactly that: four self-reported price thresholds (too cheap, bargain,
   expensive, too expensive) plotted as cumulative curves.
   source: Wikipedia, "Van Westendorp's Price Sensitivity Meter"
   (https://en.wikipedia.org/wiki/Van_Westendorp's_Price_Sensitivity_Meter) —
   PSM's four questions and the marginal-cheapness/expensiveness
   intersection points.

2. When the decision needs PREFERENCE SHARE across competing bundles
   with multiple attributes (features x price x tier) trading off
   against each other — choose the conjoint family (CBC or rating-based),
   which collects relative attribute-level utilities, not a single
   threshold. A tiering/bundling question is conjoint-shaped; a single
   price-level question is not.
   source: Sawtooth Software, "What is Choice-Based Conjoint?"
   (https://sawtoothsoftware.com/help/lighthouse-studio/manual/what-is-choice-based-conjoint.html).

3. Within conjoint family: when the product has >6 attributes or the
   study needs market-simulator "what if we drop this tier" outputs —
   choose CBC (discrete-choice tasks), not rating-based CVA. CBC scales
   to more attributes and produces share-of-preference simulations
   directly; CVA (full-profile ranking/rating) degrades past roughly
   6 attributes because ranking effort per profile grows combinatorially.
   source: Sawtooth Software, "Sample Size Rule of Thumb for a CBC Study"
   (https://sawtoothsoftware.com/resources/blog/posts/sample-size-rules-of-thumb) —
   CBC task design guidance (8-15 tasks, each attribute level appearing
   ≥6 times per respondent) assumes the discrete-choice format this
   scale requires.

4. Within conjoint family: when the study is small-N (pilot, <100
   respondents) and the decision only needs part-worth utilities for a
   handful (≤6) of attributes with no simulator need — choose
   rating-based CVA over CBC. CBC's task-efficiency requirements
   (Johnson & Orme's n·t·a/c ≥ 500 rule) are hard to satisfy at low N;
   CVA extracts more information per respondent at small samples
   because every profile rated contributes a data point, not just a
   binary/discrete pick.
   source: Sawtooth Software, "Sample Size Rule of Thumb for a
   Choice-Based Conjoint (CBC) Study"
   (https://sawtoothsoftware.com/resources/blog/posts/sample-size-rules-of-thumb).

5. **[removal]** When neither PSM's threshold framing nor conjoint's
   attribute-tradeoff framing fits — the question is price STRUCTURE
   (how many tiers, what gates what) rather than price LEVEL — do not
   force-fit a method family. State "none of these" explicitly and
   hand off straight to `pricing-design-rigor` with no method fielded,
   per this repo's own HAND-OFF line. Forcing a WTP method onto a
   pure-structure question produces a price number for a question that
   was never about a number.
   source: this repo's `README.md` HAND-OFF line for
   `pricing-method-family` ("if 'none of these' methods fit ... state
   that explicitly and continue to pricing-design-rigor with no method
   fielded").
