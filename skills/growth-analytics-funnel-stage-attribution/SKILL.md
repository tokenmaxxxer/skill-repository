---
name: growth-analytics-funnel-stage-attribution
description: Use when a proposed metric counts raw registrations, installs, or signups, or when a dashboard reports one blended conversion rate spanning multiple funnel stages. Applies to the funnel-stage-attribution axis.
axis: funnel-stage-attribution
rule_count_floor: 2
---

# Funnel-stage attribution rules

## Trigger

Apply this skill when a metric is proposed as a `funnel_stage` record
counting raw registrations, installs, or signups, or when a dashboard
reports a single blended "conversion rate" spanning acquisition through
revenue.

## Procedure

1. When a metric counts raw registrations, installs, or signups with no
   downstream usage check, classify it as acquisition, not activation,
   and require a separate activation metric before treating the signup
   number as progress (rule 1).
2. When a dashboard reports one blended conversion rate spanning
   acquisition through revenue, drop the blended figure and report only
   per-stage-pair rates (rule 2).

## Output shape

Each metric correctly attributed to its AARRR stage (acquisition vs.
activation kept separate), with any multi-stage conversion figure
replaced by per-stage-pair rates.

1. **When** a metric is proposed as a `funnel_stage` record and it counts
   raw registrations, installs, or signups with no downstream usage
   check, **treat it as acquisition, not activation**, and require a
   separate activation metric before treating the signup number as
   progress — a registration spike with no "aha moment" measured
   afterward is fool's-gold acquisition volume, not evidence of value
   delivered.
   Source: Amplitude, "The Pirate Metrics Framework (AARRR)" —
   https://amplitude.com/blog/pirate-metrics-framework (stage
   definitions + vanity-metric warning, fetched 2026-08-13).

2. **REMOVAL** — when a dashboard reports one blended "conversion rate"
   spanning acquisition through revenue, **drop the blended figure** and
   report only per-stage-pair rates; a single aggregate number cannot be
   attributed to any one AARRR stage and hides which stage actually
   moved.
   Source: Amplitude, "The Pirate Metrics Framework (AARRR)" —
   https://amplitude.com/blog/pirate-metrics-framework (stage-specific
   metrics section, fetched 2026-08-13).
