---
name: risk-management-monitoring-review-cadence
description: Use when setting or adjusting a register entry's review cadence, an event or mitigation-completion changes an entry's status, or a legacy cadence may no longer be justified. Applies to the monitoring-review-cadence axis.
axis: monitoring-review-cadence
rule_count_floor: 10
---

# Monitoring / review cadence selection

## Trigger

Apply this skill when setting a register entry's `review-date` cadence,
when a risk's velocity affects how that cadence should be adjusted, when
a material risk event fires outside the scheduled cadence, when a
Low-score entry's legacy cadence has gone unchanged for multiple cycles,
or when a mitigation control is marked complete.

## Procedure

1. Set the baseline cadence from residual score: High/Critical monthly,
   Medium quarterly, Low annual (rule 1).
2. When velocity is high, shorten the baseline cadence by at least one
   tier even if score alone would not require it (rule 2).
3. When a material risk event occurs, review the entry immediately
   regardless of its scheduled `review-date` (rule 3).
4. When a Low-score, low-velocity entry's cadence has held unchanged
   for multiple cycles with no movement, drop its frequency to the
   longest tier (rule 4).
5. When a mitigation control is marked complete, trigger an immediate
   residual re-score and re-derive the cadence from the fresh score
   (rule 5).

## Output shape

A `review-date` cadence per register entry derived from its current
residual score and velocity (not a stale pre-mitigation or legacy
setting), with immediate out-of-cycle reviews triggered by qualifying
events.

## Decision rules

1. When a register entry's residual score is High or Critical, set
   `review-date` to a monthly cadence; Medium to quarterly; Low to
   annual — as the default baseline before velocity adjustment (rule 2).
   source: https://sbnsoftware.com/blog/how-often-should-risk-assessments-be-reviewed-and-updated/
2. When a risk's velocity is high (it can materialize and start
   affecting objectives within days/weeks of a trigger event) shorten
   the baseline cadence from rule 1 by at least one tier (e.g. quarterly
   -> monthly) even if its score alone would not require it — cadence
   must track velocity in addition to score, not score alone.
   source: https://www.wolterskluwer.com/en/expert-insights/what-is-risk-velocity-and-should-you-track-it
3. When a material risk event occurs (a trigger condition fires, a
   control fails, a related risk's score changes), review that entry
   immediately regardless of its scheduled `review-date` — cadence is a
   ceiling on review interval, not a floor that defers an event-driven
   review.
   source: https://sbnsoftware.com/blog/how-often-should-risk-assessments-be-reviewed-and-updated/
4. Removal: when a Low-score, low-velocity entry has been reviewed on
   an unchanged cadence for multiple cycles with no score movement and
   no active mitigation-plan progress expected, drop its review
   frequency to the longest tier (annual/biennial) rather than
   continuing a shorter legacy cadence set when its score was higher —
   do not carry forward a review frequency the entry's current risk
   profile no longer justifies.
   source: https://sbnsoftware.com/blog/how-often-should-risk-assessments-be-reviewed-and-updated/
5. When a mitigation control is marked complete, trigger an immediate
   residual-risk re-score and re-derive the review cadence from that
   fresh residual score — do not let the entry keep the cadence set
   from its pre-mitigation (inherent) score, since the whole point of
   the completed control was to change the risk the entry represents.
