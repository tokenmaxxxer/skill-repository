---
name: observability-cardinality-budget
description: Use when a candidate metric label/tag/attribute needs to be classified by cardinality risk before it ships, or when an existing metric already carries a high-cardinality label. Applies to the cardinality-budget axis.
metadata:
  axis: cardinality-budget
  rule_count_floor: 3
---

# Cardinality budgeting for instrumentation dimensions

Decision rules for classifying candidate labels/tags/attributes by
cardinality risk and choosing a handling policy before they ship.
Research trail: layer 2 (Prometheus TSDB cardinality-explosion
mechanics, OpenTelemetry semconv cardinality guidance) plus layer 1
(practitioner drop/hash/bucket remediation patterns).

## Trigger

Apply this skill when a candidate metric label/tag/attribute needs to
be classified by cardinality risk before it ships, or when an existing
metric already carries a high-cardinality label.

## Procedure

1. Classify the candidate dimension's value space: unbounded and
   growing with user/request volume routes to trace/log attributes, not
   a metric label (rule 1).
2. A continuous numeric value needed for grouping gets bucketed into a
   small fixed set of ranges before it becomes a label (rule 2).
3. A stable low-cardinality dimension used across many metrics for
   correlation stays a shared label (rule 3).
4. For an existing metric already carrying a high-cardinality label,
   drop it via relabeling at the collection layer and replace dependent
   dashboard queries with the bucketed/aggregated replacement, rather
   than grandfathering it forward (rule 4).

## Output shape

A cardinality classification (unbounded/continuous/stable) per
candidate dimension with its resulting handling policy — route to
traces/logs, bucket, keep as shared label, or relabel-and-replace for
legacy labels.

## Rules

1. When a candidate dimension's value space is unbounded and grows with
   user/request volume (user_id, request_id, session_id, trace_id,
   span_id, raw URL path with path params), classify it as
   high-cardinality and never attach it as a metric label/tag — "adding
   a single label such as user_id or request_id to a widely used metric
   can multiply active series counts by millions overnight," and
   Prometheus's TSDB index lives in memory, so this converts directly
   into OOM/ingestion failure. Route these to trace/log attributes
   instead of metric labels — those systems, unlike metrics TSDBs, are
   built for high-cardinality dimensions. source:
   https://last9.io/blog/how-to-manage-high-cardinality-metrics-in-prometheus/

2. When a candidate dimension is a continuous numeric value needed for
   grouping (e.g. payload size, latency bucket) rather than raw
   identity, bucket it into a small fixed set of ranges before it
   becomes a label — bucketing is the named remediation for continuous-
   numeric dimensions specifically because raw numeric values behave
   like unbounded-cardinality identifiers otherwise. source:
   https://last9.io/blog/how-to-manage-high-cardinality-metrics-in-prometheus/

3. When a candidate dimension is a stable low-cardinality dimension used
   across many metrics for correlation (region, environment, service
   name, http.method), keep it as a shared label and use it to partition
   dashboards/alerts — OpenTelemetry semconv guidance recommends
   sticking to shared, standardized attribute names precisely so
   dashboards and queries "work across different services... without
   translation," which only holds when the label set stays small and
   stable. source: https://last9.io/blog/otel-naming-best-practices/

4. **REMOVAL**: when an existing metric already carries a high-
   cardinality label that was added before this budget existed (e.g. a
   legacy `user_id` label on a request counter), do not "grandfather"
   it forward into new dashboards that reference it — drop the label
   via relabeling (`metric_relabel_configs` / `labeldrop`) at the
   collection layer and replace any dashboard query built on it with
   one built on the bucketed/aggregated replacement, rather than
   propagating the unbounded label into new panels because it's
   already there. source:
   https://last9.io/blog/how-to-manage-high-cardinality-metrics-in-prometheus/
