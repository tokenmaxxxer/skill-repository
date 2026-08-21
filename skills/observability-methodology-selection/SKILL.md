---
name: observability-methodology-selection
description: Use when a touched surface needs exactly one signal methodology (RED, USE, or Golden Signals) chosen, or when a redundant methodology dashboard is proposed on top of an existing one. Applies to the methodology-selection axis.
axis: methodology-selection
rule_count_floor: 3
---

# Signal-methodology selection (RED / USE / Golden Signals)

Decision rules for picking exactly one signal methodology per touched
surface (this rulebook's own `observability-methodology-selector`
phase-1 duty). Research trail: layer 2 (named methodologies — Tom
Wilkie's RED method, Brendan Gregg's USE method, Google's Four Golden
Signals — verified at source) plus layer 1 (practitioner framing of
when each applies, as documented by SRE-adjacent writeups that trace
back to the originating talks/books).

## Trigger

Apply this skill when a touched surface needs exactly one signal
methodology chosen, or when a new methodology dashboard is proposed
for a surface that already has one.

## Procedure

1. If the surface is a request-driven service boundary, choose RED
   (rule 1).
2. If the surface is a finite resource a service consumes rather than
   a request path, choose USE (rule 2).
3. When a surface already has a named RED or USE dashboard and a new
   Golden Signals overview panel is proposed that just restates the
   same numbers at coarser granularity, drop the redundant overview
   rather than add it (rule 3).

## Output shape

Exactly one named methodology (RED or USE) assigned per touched
surface, with no redundant duplicate-methodology overview panel added
where one already exists.

## Rules

1. When the surface is a request-driven service boundary (an HTTP/RPC
   endpoint, a queue consumer handling discrete messages), choose
   **RED** (Rate, Errors, Duration) — the RED method was built by Tom
   Wilkie specifically as "a focused model for microservice
   observability" around per-request throughput, error volume, and
   duration, not resource state. source:
   https://speedscale.com/blog/golden-signals/

2. When the surface is a finite resource a service consumes rather than
   a request path (CPU, disk, memory, connection pool, thread pool,
   queue depth), choose **USE** (Utilization, Saturation, Errors) —
   USE is "resource-centric and designed for system-level monitoring
   (e.g., hosts, containers, load balancers)," and applying RED's
   rate/duration framing to a resource that has no discrete "request"
   produces meaningless rate/duration series. source:
   https://speedscale.com/blog/golden-signals/

3. **REMOVAL**: when a single surface already has a named RED or USE
   dashboard in place and a new "Golden Signals overview" panel is
   proposed on top of it that just restates the same latency/error
   numbers at coarser granularity, do not add the third dashboard —
   Golden Signals is not a superset requiring separate instrumentation;
   for comprehensive coverage the practitioner guidance is to combine
   latency/traffic/errors from RED with saturation from USE onto the
   SAME surface's existing panels, not maintain a parallel Golden
   Signals view. Drop the redundant overview rather than instrument it.
   source: https://speedscale.com/blog/golden-signals/
