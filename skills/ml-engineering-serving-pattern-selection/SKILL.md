---
name: ml-engineering-serving-pattern-selection
description: Use when choosing between batch, online-synchronous, and online-asynchronous/streaming serving for a model workload, or deciding whether to micro-batch requests. Applies to the serving-pattern-selection axis.
axis: serving-pattern-selection
rule_count_floor: 5
---

# Serving pattern selection (batch / online-sync / online-async-streaming)

Research trail: practitioner layer from Xebia's ML serving architecture taxonomy and the Clipper low-latency prediction-serving system (academic/systems paper); throughput-latency tradeoff literature on request batching. All fetched this session.

## Trigger

Apply this skill when choosing how a model workload should be served —
batch, online-synchronous, or online-asynchronous/streaming — or
deciding whether to micro-batch concurrent requests, distinguishing it
from rollout-promotion-rollback (how a chosen serving pattern's model
version gets staged into production, a separate concern) and
slo-definition-tradeoffs (what latency/availability target the chosen
pattern must then hit).

## Procedure

1. When output tolerates minutes-to-hours latency and inputs arrive as
   bounded batches, use batch serving over online serving (rule 1).
2. When a user-facing request needs a prediction synchronously within
   the request/response cycle, use online-synchronous serving over
   batch (rule 2).
3. When input arrives as a continuous, unbounded stream with
   non-blocking downstream consumers, use online-asynchronous/streaming
   serving rather than forcing a synchronous path onto it (rule 3).
4. When accelerator cost dominates the budget and the latency budget
   allows a short queuing delay, micro-batch concurrent requests rather
   than serving one at a time (rule 4).
5. When a workload's traffic shape has shifted from the pattern it was
   originally chosen for, drop the mismatched pattern and re-choose
   rather than layering compensating infrastructure on top of it
   (rule 5).

## Output shape

One serving-pattern choice (batch, online-synchronous, or
online-asynchronous/streaming) per workload, plus an explicit
micro-batching decision when accelerator cost dominates, re-evaluated
when the workload's traffic shape changes.

## Rules

1. When output can tolerate minutes-to-hours latency and inputs arrive as bounded batches (e.g. a nightly scoring job), use batch serving rather than online serving — batch processing operates on complete, bounded datasets and trades latency for throughput/cost efficiency. source: https://xebia.com/blog/ml-serving-architectures/

2. When a user-facing request needs a prediction synchronously within the request/response cycle, use online-synchronous serving rather than batch, so the caller gets a fresh result on every call instead of a stale precomputed one. source: https://arxiv.org/pdf/1612.03079

3. When input arrives as a continuous, unbounded stream and downstream consumers don't block waiting on a synchronous response, use online-asynchronous/streaming serving rather than forcing a synchronous request path onto an inherently async workload. source: https://xebia.com/blog/ml-serving-architectures/

4. When GPU/accelerator cost dominates the serving budget and the per-request latency budget allows a short queuing delay, batch multiple concurrent requests together (micro-batching) rather than serving one request at a time — this improves throughput/utilization at the cost of added per-request latency, so it only applies when that tradeoff is acceptable. source: https://medium.com/better-ml/throughput-latency-tradeoff-in-llm-inference-5a9e0d1d2c14

5. **REMOVAL**: When a serving pattern was chosen for a workload whose traffic shape has since shifted (bursty-interactive to steady bulk, or vice versa), drop the now-mismatched pattern rather than layering compensating infrastructure (extra caching, request coalescing) on top of the wrong base pattern — treat pattern mismatch as a design smell to fix at the source, not paper over. source: https://xebia.com/blog/ml-serving-architectures/
