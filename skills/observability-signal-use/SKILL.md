---
name: observability-signal-use
description: Use when placing Utilization, Saturation, or Errors signals on a resource-bound surface. Applies to the signal-use axis.
axis: signal-use
rule_count_floor: 3
---

# USE signal placement (Utilization / Saturation / Errors)

Decision rules for where each of the three USE signals gets a concrete
metric on a resource-bound surface. Research trail: layer 2 (Brendan
Gregg's USE method, Prometheus TSDB resource-cardinality guidance)
plus layer 1 (practitioner saturation-vs-utilization distinctions).

## Trigger

Apply this skill when instrumenting a resource-bound surface and
Utilization, Saturation, or Errors each need a concrete signal
placement.

## Procedure

1. For utilization, measure the resource's busy-time fraction at the
   resource itself, not a derived proxy like request rate (rule 1).
2. For saturation, measure queue/backlog depth or wait-time at the
   resource's admission point in addition to utilization (rule 2).
3. For errors, count resource-level failures distinct from the caller-
   facing errors already tracked by RED on surfaces that use this
   resource (rule 3).
4. When a dashboard already plots utilization and saturation, do not
   add a raw queue-depth gauge as a fourth panel duplicating what
   saturation already shows — fold it into the existing saturation
   panel instead (rule 4).

## Output shape

A busy-time utilization metric, a queue/backlog saturation metric, and
a resource-level error counter per resource-bound surface — with no
duplicate raw queue-depth panel alongside saturation.

## Rules

1. For **utilization**, measure the resource's busy-time fraction over
   the sampling window at the resource itself (CPU busy %, connection-
   pool in-use count / pool size, disk busy %) — not a derived proxy
   like request rate, because utilization is defined as "the average
   time that the resource was busy," a property of the resource, not
   of its callers. source: https://speedscale.com/blog/golden-signals/

2. For **saturation**, measure queue/backlog depth or wait-time at the
   resource's admission point (thread-pool queue length, connection-
   pool wait count, disk I/O queue depth) in addition to utilization —
   a resource can be 100% utilized with zero backlog (steady-state) or
   90% utilized with a growing queue (degrading); utilization alone
   cannot distinguish these, which is exactly why USE keeps saturation
   as a separate signal from utilization. source:
   https://speedscale.com/blog/golden-signals/

3. For **errors**, count resource-level failures distinct from the
   caller-facing errors already tracked by RED on the surfaces that use
   this resource (e.g. connection-pool exhaustion rejections, disk I/O
   errors) — resource errors and request errors are separate axes:
   a resource can throw internal errors (retried transparently) that
   never surface as a caller-visible RED error, and conflating the two
   hides resource degradation until it already causes visible failures.
   source: https://speedscale.com/blog/golden-signals/

4. **REMOVAL**: when a resource-bound surface's dashboard already plots
   utilization and saturation, do not add a raw "queue depth" gauge as
   a fourth panel duplicating what saturation already shows — USE
   defines saturation AS the queue/backlog signal, so a same-window raw
   queue-depth panel is the same data twice under different labels.
   Fold it into the existing saturation panel instead of adding a
   parallel one. source: https://speedscale.com/blog/golden-signals/
