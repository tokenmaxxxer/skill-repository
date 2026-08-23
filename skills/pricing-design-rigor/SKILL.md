---
name: pricing-design-rigor
description: >-
  Use when a conjoint study design or fielding plan is already chosen and needs
  a rigor check — banding a CBC/CVA design's task ratio and task count, or
  deciding whether and how to incentive-align the study before it fields.
  Trigger on requests like "컨조인트 설계 검토해줘", "is 12 choice tasks too many for this
  CBC", "check the task ratio of our conjoint design", "should we
  incentive-align the WTP study". Do NOT use to pick between PSM and conjoint in
  the first place (use pricing-method-family).
metadata:
  axis: design-rigor
  rule_count_floor: 3
---

# Design-rigor decision rules

Decisions for `pricing-design-rigor` (chain position 3/4): the
design-gate band for CVA-style designs, and the incentive-alignment
decision with its cost.

## Trigger

Use once `pricing-method-family` has already routed the decision to a
conjoint method (CBC or CVA) and a concrete design — attributes, levels,
task count, sample size — is on the table to be fielded or reviewed.
This is chain position 3/4: it does not choose the method family (that
is `pricing-method-family`'s job upstream), it grades the rigor of a
design already chosen, specifically the CBC/CVA task-ratio and task-count
bands and the incentive-alignment cost/benefit call. Do not use it to
pick between PSM and conjoint in the first place, and do not use it once
a verdict is already being assembled (that is `pricing-verdict-report`
downstream).

## Procedure

1. Cite decision rule 1 when the study is CBC-based, to report the
   task ratio (n·t·a/c) as a reference figure only, never a banded
   verdict.
2. Cite decision rule 2 when the study is CBC-based, to band the task
   count itself (warned/clear/warned) alongside the per-level-appearance
   check.
3. Cite decision rule 3 when the study is not incentive-aligned and a
   go/no-go price decision rides on the output, to flag the predictive-
   validity cost with its three required qualifications.
4. Cite decision rule 4 when incentive alignment is under consideration,
   to name its concrete behavioral cost (price sensitivity, none-choice
   rate) alongside the accuracy gain.
5. Cite decision rule 5 when the decision is a low-stakes price tweak
   within an already-validated range, to drop the incentive-alignment
   requirement rather than defaulting to always incentive-aligning.

## Output shape

Applying this skill produces a design-rigor verdict for the fielded or
proposed conjoint study: a banded task-ratio/task-count assessment
(reference-figure-only for CBC, blocked/warned/clear for CVA), plus an
explicit incentive-alignment decision that states its cost alongside any
accuracy benefit claimed. It does not itself produce a price number or a
method choice — only a rigor judgment on the design already chosen.

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

## Related skills

- [pricing-tier-structure](../pricing-tier-structure/SKILL.md) — rigor checks apply to a tier structure once pricing-tier-structure has laid one out.
