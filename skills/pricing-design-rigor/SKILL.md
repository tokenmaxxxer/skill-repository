---
name: pricing-design-rigor
description: Use when you need guidance on Design-rigor decision rules. Applies to the design-rigor axis.
axis: design-rigor
rule_count_floor: 3
---

# Design-rigor decision rules

Decisions for `pricing-design-rigor` (chain position 3/4): the
design-gate band for CVA-style designs, and the incentive-alignment
decision with its cost.

## Decision rules

1. When fielding CBC, cite the task ratio as a REFERENCE FIGURE only —
   never issue a blocked/warned/clear band verdict on it. Report
   `n·t·a/c` against the ≥500 rule-of-thumb, but do not gate the study
   on it the way CVA's attribute/level/task ratio is gated, because
   CBC's HB estimation tolerates a wider range of designs than CVA's
   full-profile method does.
   source: Sawtooth Software, "Sample Size Rule of Thumb for a
   Choice-Based Conjoint (CBC) Study"
   (https://sawtoothsoftware.com/resources/blog/posts/sample-size-rules-of-thumb) —
   states the n·t·a/c ≥ 500 figure as sample-size guidance, not a
   pass/fail design gate.

2. When fielding CBC, band the TASK COUNT itself: <8 tasks per
   respondent = warned (each attribute level unlikely to reach the ≥6
   appearances HB estimation wants); 8-15 tasks = clear; >15 tasks =
   warned for respondent fatigue. Cite both numbers together — task
   count alone without the per-level-appearance check misses under-
   powered designs that pad task count with too many attribute levels.
   source: Sawtooth Software, "Sample Size Rule of Thumb for a
   Choice-Based Conjoint (CBC) Study" — 8-15 task range and the
   ≥6-appearances-per-level HB heuristic.

3. When the study is NOT incentive-aligned (respondents answer
   hypothetically, no real transaction risk) and a go/no-go price
   decision rides on the output — flag the predictive-validity cost
   explicitly rather than silently accepting the hypothetical number:
   cite the ~12% hit-rate gap AND immediately qualify it with (a) this
   is a raw meta-analytic average, not this study's number, (b) the
   34-article base is subject to publication bias toward positive
   incentive-alignment effects, and (c) hit-rate is a relative-ranking
   metric — it does not certify the absolute WTP level is accurate,
   only that alignment improves which option ranks first. Never state
   the 12% figure as a stand-alone precision claim.
   source: incentive-alignment meta-analysis, 134 effect sizes / 34
   articles, N=12,980
   (https://www.econstor.eu/bitstream/10419/330642/1/11002_2025_Article_9764.pdf) —
   reports the 12% hit-rate increase from incentive alignment.

4. When incentive alignment is under consideration for a conjoint
   study, name its concrete cost before recommending it: incentive-
   aligned designs measurably increase price sensitivity and increase
   none-choice (opt-out) rates relative to hypothetical framing — the
   aligned number is not a strict superset improvement, it shifts the
   distribution. Present both the accuracy gain and this behavioral
   shift together, not the gain alone.
   source: hypothetical-bias meta-analysis, 77 studies / 47 papers /
   115 effect sizes
   (https://link.springer.com/article/10.1007/s11747-019-00666-6) —
   documents the ~21% hypothetical-vs-real WTP gap and higher
   sensitivity to incentive alignment.

5. **[removal]** When the decision is a LOW-STAKES price tweak (within
   an already-validated range, no new tier, no new segment) — drop the
   incentive-alignment requirement entirely rather than defaulting to
   "always incentive-align for rigor." Incentive alignment adds real
   respondent-cost and recruitment friction (higher none-choice,
   smaller usable N); paying that cost for a decision that does not
   need the extra 12% hit-rate accuracy is over-engineering the study,
   not de-risking it.
   source: incentive-alignment meta-analysis
   (https://www.econstor.eu/bitstream/10419/330642/1/11002_2025_Article_9764.pdf) —
   the reported benefit is a predictive-validity gain, which is only
   decision-relevant when the ranking is actually close enough to flip.
