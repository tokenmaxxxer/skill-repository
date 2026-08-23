---
name: pricing-verdict-report
description: >-
  Use when a pricing method has already yielded raw numbers (PSM crossings,
  conjoint utilities or preference share) and they need to be assembled into a
  labeled six-element verdict — naming what the figures actually mean, stating
  the residual list, and handing off revenue/volume questions rather than
  answering them from the same data. Trigger on requests like "PSM 결과 정리해줘", "is
  the PSM intersection the optimal price", "report the conjoint preference
  share", "write up the pricing verdict". Do NOT use to check a design's rigor
  before it fields (use pricing-design-rigor).
metadata:
  axis: verdict-assembly
  rule_count_floor: 3
---

# Verdict-assembly decision rules

Decisions for `pricing-verdict-report` (chain position 4/4): the
assembled six-element verdict and correct labeling of the numbers it
carries.

## Trigger

Use at the end of the chain (position 4/4), once a research method has
already produced raw numbers (PSM crossings or conjoint utilities/share)
and those numbers need to be assembled into a final, correctly-labeled
verdict. Use it to catch mislabeling (PSM as "optimal price", conjoint as
a volume forecast) and to route revenue/profit/volume residuals to
`finance-unit-economics` rather than answering them from the same
dataset. Do not use it to choose or design the method itself — that is
upstream.

## Procedure

1. Cite decision rule 1 when reporting a Van Westendorp output, to label
   the intersection points by their actual statistical meaning, never as
   "optimal price."
2. Cite decision rule 2 when reporting a conjoint output, to label it
   "preference share," never a unit-volume or revenue forecast.
3. Cite decision rule 3 when the residual list includes revenue, profit,
   or unit-volume questions, to name them as residuals and hand off to
   `finance-unit-economics` rather than answering them from the study's
   own data.
4. Cite decision rule 4 every time a verdict is recorded, to assemble all
   six elements including the "what it cannot answer" line, even when the
   numeric result looks unambiguous.
5. Cite decision rule 5 when the residual list is empty, to state that
   explicitly and skip the `finance-unit-economics` hand-off rather than
   issuing it out of habit.

## Output shape

Applying this skill produces a six-element verdict record: method,
family, what it collects, what it therefore cannot answer, the numbers
with correctly scoped labels, and the residual list — with a conditional
hand-off to `finance-unit-economics` only when that residual list
actually contains revenue/profit/volume questions.

## Decision rules

1. When reporting a Van Westendorp output, label the intersection
   points by their actual statistical meaning — "point of marginal
   cheapness" / "point of marginal expensiveness" / "indifference
   price point" — never as "optimal price" or "the price to charge."
   PSM measures perceived acceptability thresholds from stated intent,
   not a revenue- or profit-maximizing point; presenting it as an
   optimum implies an optimization the method never ran.
   source: SurveyMonkey, "How To Use The Van Westendorp Price
   Sensitivity Meter"
   (https://www.surveymonkey.com/market-research/resources/van-westendorp-price-sensitivity-meter/) —
   defines the acceptable-range and point outputs from the four raw
   questions, with no revenue-optimization step in the method.

2. When reporting a conjoint output, label it "preference share" (or
   "relative WTP among the tested bundles"), never "unit-volume
   forecast" or "revenue projection." Conjoint measures stated
   preference among a fixed choice set; it does not model market size,
   awareness, distribution, or purchase-frequency — the inputs a volume
   number needs. State this omission in the verdict's residual list
   rather than silently extrapolating a volume figure from share data.
   source: this repo's `README.md` HAND-OFF line ("if the residual list
   includes revenue/profit/volume ... fire the hand-off to
   finance-unit-economics instead of extrapolating from data that
   doesn't contain them").

3. When the residual list includes revenue, profit, or unit-volume
   questions, do not answer them from the pricing study's own data —
   name them explicitly as residuals and hand off to
   `finance-unit-economics` in the same verdict record. A pricing
   method's evidence base (stated price thresholds or attribute
   utilities) structurally cannot certify unit economics; closing that
   gap from the same dataset manufactures a false confirmation.
   source: this repo's own chain HAND-OFF line, `pricing-verdict-report`
   plugin.

4. Assemble all six elements every time a verdict is recorded — method,
   family, what it collects, what it therefore cannot answer, the
   numbers with correctly scoped labels, and the residual list — never
   drop the "what it cannot answer" element even when the numeric
   result looks unambiguous. A clean-looking PSM curve or conjoint
   share output still cannot answer volume/margin/competitive-response
   questions, and omitting that line is how a threshold number gets
   read downstream as a revenue commitment.
   source: this repo's `README.md` PRODUCES line ("method, family, what
   it collects, what it therefore cannot answer, the numbers ..., the
   residual list").

5. **[removal]** When the verdict's residual list is empty (the fielded
   method's own data already answers every question the decision asked)
   — do not add a boilerplate hand-off line to `finance-unit-economics`
   out of habit. State the residual list as empty explicitly and skip
   the hand-off; forcing a hand-off with nothing to hand off manufactures
   downstream work for a role that has nothing to check.
   source: this repo's `README.md` HAND-OFF line, read literally — the
   hand-off is conditioned on the residual actually containing
   revenue/profit/volume, not issued unconditionally.
