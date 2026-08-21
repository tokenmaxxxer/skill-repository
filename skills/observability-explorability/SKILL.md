---
name: observability-explorability
description: Use when you need guidance on Explorability (unplanned production questions). Applies to the explorability axis.
axis: explorability
rule_count_floor: 3
---

# Explorability (unplanned production questions)

Decision rules for keeping a design open to ad-hoc, not-pre-defined
questions rather than only pre-built dashboards. Research trail: layer
2 (Charity Majors' observability definition — high cardinality, high
dimensionality, explorability) plus layer 1 (practitioner ad-hoc-query
patterns from the Honeycomb/observability-2.0 lineage).

## Rules

1. When designing a new dashboard for a surface, always retain the raw
   high-dimensionality event/span data behind it (not only the
   pre-aggregated panel series) — Majors' settled definition of
   observability requires "high cardinality, high dimensionality, and
   explorability" together; a dashboard backed only by pre-aggregated
   series can answer the questions it was built for and nothing else,
   which is the exact gap explorability exists to close. source:
   https://8thlight.com/insights/podcast-into-the-unknown-unknowns-observability-with-charity-majors

2. When an incident investigation needs a breakdown the existing
   dashboards don't have (e.g. "which customer tier's requests are
   slow, filtered by region and by this one new deploy"), the design
   must support answering it by querying the raw dimensional data
   directly, not by shipping new code to add a new pre-aggregated
   panel — the practitioner value claim for explorability is
   "enabling users to ask new questions without re-instrumenting code,"
   so a design that requires a code change to answer a new question has
   not met this axis. source:
   https://8thlight.com/insights/podcast-into-the-unknown-unknowns-observability-with-charity-majors

3. **REMOVAL**: when a proposal lists many candidate pre-built
   dashboard panels but none of them are backed by queryable raw
   dimensional data (only pre-aggregated counters/histograms with fixed
   label sets), do not add yet another fixed panel to cover the next
   anticipated question — cut the panel-proliferation approach and
   route the underlying raw events/spans to a system that supports
   ad-hoc query instead; more fixed panels do not substitute for
   explorability, they are the failure mode explorability is defined
   against. source:
   https://8thlight.com/insights/podcast-into-the-unknown-unknowns-observability-with-charity-majors
