---
name: growth-analytics-metric-selection
description: >-
  Use when choosing a team's North Star / one metric that matters for its current business
  stage, or when a record proposes more than one metric as the live North Star. Applies to
  the metric-selection axis. Trigger on requests like "노스스타 지표 뭐로 할까", "pick our one metric
  that matters", "we have three North Stars — fix it", "should the OMTM change now that the
  stage changed". Ties the pick to the stage's current bottleneck and enforces exactly one
  live North Star. Do NOT use for slicing an already-chosen metric by channel/cohort/device
  (use growth-analytics-segmentation).
metadata:
  axis: metric-selection
  rule_count_floor: 2
---

# One-metric-that-matters selection rules

## Trigger

Apply this skill when a team is choosing what to call its North Star /
one metric that matters for its current business stage, or when a
record proposes more than one metric flagged as the live North Star for
the same review window.

## Procedure

1. When choosing the North Star / one metric that matters, pick the
   single metric tied to the stage's current bottleneck, not the metric
   that is easiest to move, and revisit the choice as the stage changes
   (rule 1).
2. When more than one metric is proposed as `is_north_star=true` for the
   same review window, cut all but one (rule 2).

## Output shape

Exactly one live North Star metric, tied to the current stage's
bottleneck, with any competing candidates removed.

1. **When** a team is choosing what to call the North Star / one metric
   that matters for a given business stage, **pick the single metric
   tied to the stage's current bottleneck, not the metric that is
   easiest to move** — OMTM selection is stage-dependent (the right
   metric for an empathy-stage product differs from a growth-stage
   product) and must be revisited as the stage changes, not fixed once.
   Source: Croll & Yoskovitz, *Lean Analytics* (O'Reilly, 2013), ch. 3,
   "The One Metric That Matters" — cited via
   https://www.oreilly.com/library/view/lean-analytics/9781449335670/
   (fetched 2026-08-13; publisher landing page confirming chapter/thesis).

2. **REMOVAL** — when a record proposes more than one metric as
   `is_north_star=true` for the same review window, **cut all but one**;
   the recomputation rule forces exactly one live North Star because a
   set of "several KPIs" prevents anyone from knowing which number the
   org will actually act on.
   Source: Croll & Yoskovitz, *Lean Analytics* (2013), ch. 3 (OMTM
   uniqueness argument), same citation as above.

## Related skills

- [growth-analytics-segmentation](../growth-analytics-segmentation/SKILL.md) — once a metric is selected, segmentation decides how to slice it for analysis.
