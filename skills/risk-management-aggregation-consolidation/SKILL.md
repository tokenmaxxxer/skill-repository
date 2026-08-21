---
name: risk-management-aggregation-consolidation
description: Use when combining or rolling up scores across related register entries, flagging concentration risk, merging duplicate entries, retiring stale entries, or ordering a consolidated action queue. Applies to the aggregation-consolidation axis.
axis: aggregation-consolidation
rule_count_floor: 10
---

# Risk aggregation / consolidation (removal-heavy axis)

## Trigger

Apply this skill when combining or rolling up scores across related
register entries, when several entries share an underlying counterparty,
vendor, or asset class, when two entries may describe the same
underlying exposure, when a mitigated entry's staleness is in question,
or when ordering a consolidated action queue across entries.

## Procedure

1. When combining scores across positively correlated risks, do not sum
   them linearly (rule 1).
2. When a single counterparty, vendor, or asset class underlies several
   entries, flag the set as a concentration risk and record the
   combined exposure as its own entry (rule 2).
3. When two entries describe the same underlying exposure, merge them
   and delete the duplicate (rule 3).
4. When a mitigated entry's residual score has held at the lowest band
   for multiple cycles with no credible recurrence trigger, retire it
   (rule 4).
5. When ordering a consolidated action queue, sort by severity band
   first and use likelihood/velocity only to break ties within a band
   (rule 5).

## Output shape

A consolidated register view in which correlated/concentrated exposures
are represented as single rolled-up entries (not double-counted or
left implicit), duplicate and stale entries are removed, and the action
queue is ordered by severity band with likelihood/velocity used only as
a tiebreaker.

## Decision rules

1. When combining scores across positively correlated risks (same root
   cause or shared dependency), do not sum their individual scores
   linearly — correlated risks concentrate rather than add
   independently, so a linear sum overstates diversification benefit
   that does not exist between them.
   source: https://www.britannica.com/money/concentration-risk-management
2. When a single counterparty, vendor, or asset class underlies several
   register entries, flag the set as a concentration risk and record
   the combined exposure as its own entry rather than leaving the
   concentration implicit across scattered individual entries — an
   implicit concentration is invisible to a reviewer scanning individual
   scores.
   source: https://www.britannica.com/money/concentration-risk-management
3. Removal: when two register entries describe the same underlying
   exposure from different angles (duplicate root cause, same trigger,
   same mitigation owner), merge them into one entry and delete the
   duplicate rather than tracking both — duplicate entries double-count
   the same exposure in any portfolio-level rollup.
   source: https://fastercapital.com/content/Risk-Aggregation-Data--How-to-Aggregate-and-Consolidate-Your-Risk-Data-across-Different-Sources-and-Dimensions.html
4. Removal: when a register entry's mitigation is complete, its
   residual score has been at the lowest band for multiple consecutive
   review cycles, and no recurrence trigger is credible, retire the
   entry (mark closed, remove from the active register view) instead of
   leaving stale near-zero entries in the active set — stale entries
   dilute a reviewer's attention on the risks that still matter.
   source: https://fastercapital.com/content/Risk-Aggregation-Data--How-to-Aggregate-and-Consolidate-Your-Risk-Data-across-Different-Sources-and-Dimensions.html
5. When ordering a consolidated action queue across register entries,
   sort by severity band first and use likelihood/velocity only to
   break ties within a severity band — never sort by a single score
   that multiplies likelihood and impact together, since a
   high-severity/low-likelihood entry can land below a
   moderate-severity/high-likelihood entry on a multiplied score even
   though the former needs attention regardless of how rare it is.
