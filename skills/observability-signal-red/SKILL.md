---
name: observability-signal-red
description: Use when placing Rate, Errors, or Duration signals on a request-driven surface. Applies to the signal-red axis.
metadata:
  axis: signal-red
  rule_count_floor: 3
---

# RED signal placement (Rate / Errors / Duration)

Decision rules for where each of the three RED signals gets a concrete
counter/classifier/histogram on a request-driven surface. Research
trail: layer 2 (RED method per Tom Wilkie, Google SRE latency-SLI
guidance) plus layer 1 (percentile-vs-average practitioner pitfalls).

## Trigger

Apply this skill when instrumenting a request-driven surface and Rate,
Errors, or Duration each need a concrete signal placement.

## Procedure

1. For rate, place a monotonic request counter at the single choke
   point every request passes through, not scattered per-handler
   counters (rule 1).
2. For errors, classify by response/outcome category rather than a
   single boolean success/fail counter (rule 2).
3. For duration, use a histogram and read back percentiles, never an
   arithmetic mean and never an average of per-instance percentiles
   (rule 3).
4. When a surface already emits a duration histogram, do not
   additionally instrument a separate average-latency gauge — read the
   percentile off the existing histogram instead (rule 4).

## Output shape

A choke-point rate counter, an outcome-classified error counter, and a
duration histogram read back as percentiles per request-driven surface
— with no separate average-latency gauge duplicating the histogram.

## Rules

1. For **rate**, place a monotonic request counter at the single choke
   point every request for that surface passes through (the router/
   middleware entry, not scattered per-handler counters) — a rate
   metric derived from N separate per-handler counters double-counts or
   under-counts whenever a handler is refactored, while a single
   choke-point counter stays correct across refactors. source:
   https://speedscale.com/blog/golden-signals/

2. For **errors**, classify by response/outcome category (e.g.
   4xx-caller-fault vs 5xx-service-fault vs timeout) rather than a
   single boolean success/fail counter — Golden-Signals/RED guidance
   treats "error rate" as a rate that must be actionable, and a single
   boolean collapses caller-side mistakes (which need no on-call
   action) into the same signal as service-side faults (which do),
   defeating the alert's purpose. source:
   https://www.groundcover.com/blog/4-golden-signals

3. For **duration**, use a histogram and read back p50/p95/p99, never
   an arithmetic mean and never an average of per-instance percentiles
   — the mean can sit under an alert threshold while p99 is 30x higher,
   and averaging percentiles across hosts/windows is mathematically
   invalid (a documented example: per-host p99s averaging to 550ms
   while the true fleet p99 is 1000ms). source:
   https://one2n.io/blog/sre-math-percentiles-in-sre-why-averages-lie-about-latency

4. **REMOVAL**: when a surface already emits a duration histogram, do
   not additionally instrument a separate "average latency" gauge
   alongside it "for a quick summary" — the average is the specific
   number the percentile literature shows misleads on tail behavior,
   and a dashboard carrying both trains viewers to trust whichever one
   looks better that day. Drop the average gauge; read p50 off the
   existing histogram for the "typical" number instead. source:
   https://clickhouse.com/resources/engineering/percentiles-vs-averages
