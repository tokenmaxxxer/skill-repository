---
name: growth-analytics-segmentation
description: Use when stage-to-stage drop-off is being reported, or when a funnel-diagnosis report states a bottleneck hypothesis with no named segment behind it. Applies to the segmentation axis.
axis: segmentation
rule_count_floor: 2
---

# Segmentation / drop-off localization rules

## Trigger

Apply this skill when stage-to-stage drop-off is being reported, or when
a funnel-diagnosis report states a bottleneck hypothesis as "probably X"
with no segment evidence named.

## Procedure

1. When reporting stage-to-stage drop-off, break it down by at least one
   segment axis (channel, cohort, or device) and name the specific cell
   where the drop concentrates, instead of stating a single funnel-wide
   number (rule 1).
2. When a bottleneck hypothesis is stated with no reference to which
   segment motivated it, cut the unsupported hypothesis (rule 2).

## Output shape

Drop-off reported per named segment cell, with every bottleneck
hypothesis traceable to the segment evidence that produced it.

1. **When** stage-to-stage drop-off is reported, **break it down by at
   least one segment axis (channel, cohort, or device) and name the
   specific cell where the drop concentrates**, instead of stating a
   single funnel-wide drop-off number — an aggregate rate can average
   away a bottleneck that is severe in one segment and absent in others,
   which is exactly the vanity-metric failure the AARRR framework warns
   against applying at the whole-funnel level.
   Source: Amplitude, "The Pirate Metrics Framework (AARRR)" —
   https://amplitude.com/blog/pirate-metrics-framework (actionable vs.
   vanity metric guidance, fetched 2026-08-13).

2. **REMOVAL** — when a funnel-diagnosis report states a bottleneck
   hypothesis as "probably X" with no reference to which segment
   motivated it, **cut the unsupported hypothesis** rather than publish
   it; a causal claim that does not trace to the segment evidence that
   produced it is not distinguishable from a guess.
   Source: Croll & Yoskovitz, *Lean Analytics* (2013), ch. 3 (metric
   must be actionable, comparable, and tied to a specific segment to
   support a decision) — same citation as metric-selection.md.
