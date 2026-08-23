---
name: risk-management-likelihood-impact-scale
description: >-
  Use when calibrating a risk's likelihood or impact band, reconciling
  divergent rater scores, or deciding whether a quantitative loss estimate
  belongs alongside the qualitative rating. Trigger on requests like "is this
  Rare or Possible", "raters disagree by two bands", "리스크 영향도 등급 매겨줘",
  "annualized loss expectancy alongside the score". Do NOT use for rolling
  calibrated scores up across entries (use
  risk-management-aggregation-consolidation).
metadata:
  axis: likelihood-impact-scale
  rule_count_floor: 10
---

# Likelihood x impact scale calibration

Operational rules for building/reading the rating bands that feed
`risk-score-inherent`/`risk-score-residual` in the register schema
(register schema itself is owned by `risk-register-methodology`; this
axis is the calibration judgment behind the numbers that go in it).

## Trigger

Apply this skill when calibrating a risk's likelihood or impact band,
when two raters' scores diverge, when a likelihood band was set by
verbal impression rather than the written scale, or when a risk carries
a quantifiable dollar-denominated loss estimate, distinguishing it from
`risk-register-methodology` (which owns the register schema the
resulting scores feed into).

## Procedure

1. When a risk has no in-org history but is known in comparable
   operations, rate likelihood "Possible" (3/5), not "Rare" (1/5)
   (rule 1).
2. When impact would cross $1M or produce fatality/regulatory
   enforcement, rate impact "Severe/Catastrophic" (5/5) regardless of
   likelihood (rule 2).
3. When two raters diverge by more than one band on either axis,
   reconcile against the band's written definition text rather than
   averaging silently (rule 3).
4. When a likelihood band was set by verbal impression with no
   band-definition text cited, delete the score and re-rate against the
   written scale (rule 4).
5. When a risk carries a plausible dollar-denominated loss estimate,
   record the annualized-loss-expectancy figure alongside the
   qualitative band, not in place of it (rule 5).

## Output shape

A likelihood band and an impact band for the risk, each traceable to
the written 5-level scale definition rather than verbal impression or a
silently-averaged split score, with an annualized-loss-expectancy figure
attached when a quantifiable estimate exists.

## Decision rules

1. When a risk has no historical occurrence in this org but is known to
   occur in the same industry/comparable operations, rate likelihood
   "Possible" (3/5), not "Rare" (1/5) — "Rare" is reserved for events
   with no known precedent anywhere in the sector.
   source: https://mindsetcyber.com.au/iso-31000-risk-matrix/
2. When impact would cross $1M or produce fatality/regulatory
   enforcement, rate impact "Severe/Catastrophic" (5/5) regardless of
   how low likelihood is scored — severity bands are anchored to
   absolute consequence thresholds, not adjusted downward to offset a
   low likelihood score.
   source: https://risguard.com/en/create-a-risk-matrix/
3. When two raters score the same risk more than one band apart on
   either axis, do not average the two scores silently — reconcile
   against the band's written definition text before recording a
   single score, so the register never holds an unreconciled average
   that neither rater actually endorsed.
   source: https://mindsetcyber.com.au/iso-31000-risk-matrix/
4. Removal: when a risk's likelihood band was set by verbal impression
   ("seems unlikely") with no band-definition text cited, delete the
   score and re-rate against the written 5-level scale before it enters
   the register — an uncited verbal score does not satisfy ISO 31000's
   evaluation-input requirement.
   source: https://mindsetcyber.com.au/iso-31000-risk-matrix/
5. When a risk carries a plausible dollar-denominated loss estimate
   (frequency of occurrence x expected single-event loss), record that
   annualized-loss-expectancy figure alongside the qualitative
   likelihood/impact band rather than in place of it — a
   qualitative-only score cannot be compared against a budget or an
   insurance limit, and a quantitative-only score loses the band's
   comparability across dissimilar risk types.
