---
name: observability-signal-golden
description: Use when you need guidance on Golden Signals placement (Latency / Traffic / Errors / Saturation). Applies to the signal-golden axis.
axis: signal-golden
rule_count_floor: 3
---

# Golden Signals placement (Latency / Traffic / Errors / Saturation)

Decision rules for where the four Golden Signals get instrumented on a
service-rollup surface (a service-level view aggregating multiple
request-driven and resource-bound children). Research trail: layer 2
(Google SRE book's Four Golden Signals) plus layer 1 (practitioner
guidance on combining RED+USE into a rollup rather than re-instrumenting).

## Rules

1. For **latency** and **traffic**, roll up from the service's own RED
   instrumentation (duration histogram, request counter) rather than
   re-instrumenting at the service-rollup layer — Golden Signals'
   latency/traffic/errors are the same three signals RED already
   covers at finer grain, so the rollup should aggregate the existing
   histograms/counters, not add parallel collection points. source:
   https://speedscale.com/blog/golden-signals/

2. For **saturation**, roll up from the service's constituent
   resources' USE saturation signals (pool queues, CPU/memory
   pressure across the service's instances) — saturation is the one
   Golden Signal RED does not carry, and it is defined identically to
   USE's saturation, so the rollup's saturation panel should be a
   max/percentile-across-instances of the already-collected USE
   saturation series. source: https://speedscale.com/blog/golden-signals/

3. For **errors**, aggregate the same classified error counters RED
   already emits per request (caller-fault vs service-fault) rather
   than introduce a single service-level error boolean — collapsing
   classification away at rollup time loses exactly the actionability
   distinction signal-red rule 2 established, and it cannot be
   recovered later from an already-collapsed rollup metric. source:
   https://www.groundcover.com/blog/4-golden-signals

4. **REMOVAL**: when a service-rollup dashboard is being built for a
   service whose children already publish RED+USE dashboards, do not
   instrument fresh latency/traffic/error/saturation collection points
   at the rollup layer "to be self-contained" — this doubles the
   telemetry surface and creates two sources of truth that drift
   whenever a child surface changes; the rollup should ONLY aggregate
   the children's existing series, never emit its own competing raw
   ones. source: https://speedscale.com/blog/golden-signals/
