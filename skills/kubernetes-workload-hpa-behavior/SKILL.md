---
name: kubernetes-workload-hpa-behavior
description: >-
  Use when configuring a HorizontalPodAutoscaler's scaling behavior
  (stabilization windows, scale-up/down policies), choosing HPA metrics, or
  diagnosing flapping/thrashing replica counts. Trigger on requests like "HPA
  keeps flapping", "stabilizationWindowSeconds tuning", "HPA 메트릭 뭐로 잡을까",
  "replicas oscillating under load". Do NOT use for sizing a container's
  CPU/memory requests and limits (use
  kubernetes-workload-requests-limits-decision).
metadata:
  axis: hpa-behavior
  rule_count_floor: 5
---

# Kubernetes HPA behavior rules

## Trigger

Apply this skill when writing or reviewing a `HorizontalPodAutoscaler`,
choosing which metric(s) drive scaling, tuning `behavior.scaleUp`/
`behavior.scaleDown` stabilization windows, or diagnosing a workload
whose replica count oscillates rapidly under normal load.

## Procedure

1. Never combine HPA with a fixed/pinned replica count set elsewhere
   (e.g. a GitOps-managed static `replicas:`) — the two fight each
   other (rule 1).
2. Set an asymmetric stabilization window: short for scale-up, longer
   for scale-down, to avoid premature capacity removal (rule 2).
3. Choose metrics that actually reflect load-bearing capacity for the
   workload, not just CPU by default (rule 3).
4. Set `minReplicas` high enough to absorb a single-pod loss without a
   capacity gap, and `maxReplicas` bounded by real downstream/cluster
   capacity (rule 4).
5. Diagnose replica flapping as a stabilization-window or metric-noise
   problem, not a min/max-replica problem (rule 5).

## Output shape

An HPA spec (or diagnosis) stating the chosen metric(s), the
`minReplicas`/`maxReplicas` bounds, and the scale-up/scale-down
stabilization windows, each traceable to the rule below that forced
the choice.

## Rules

1. **REMOVAL**: Never manage a workload with both an HPA and a fixed,
   externally-pinned `replicas:` value (e.g. a GitOps tool that
   reconciles `replicas:` back to a static number) — the two control
   loops overwrite each other's decisions, producing a workload that
   either never scales or gets reset to the static count immediately
   after the HPA scales it. source: https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/

2. Configure `behavior.scaleUp.stabilizationWindowSeconds` short (or 0)
   and `behavior.scaleDown.stabilizationWindowSeconds` meaningfully
   longer (e.g. several minutes) — scaling up quickly protects against
   under-capacity during a real load spike, while a longer scale-down
   window prevents the HPA from removing capacity the moment a
   transient spike subsides, only to need it again minutes later.
   source: https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/

3. Choose the HPA's driving metric(s) to reflect what actually
   constrains this workload's serving capacity (request concurrency,
   queue depth, a custom application metric) rather than defaulting to
   CPU utilization for every workload — CPU is a poor proxy for
   capacity on I/O-bound or memory-bound services, and an HPA scaling
   on the wrong metric under- or over-provisions relative to real
   demand. source: https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/

4. Set `minReplicas` to at least 2 (or higher) for any workload that
   cannot tolerate a capacity gap while a single pod is unavailable
   (rollout, node failure), and set `maxReplicas` bounded by actual
   downstream capacity (database connection limits, cluster node
   capacity) rather than an arbitrarily large ceiling — an unbounded
   `maxReplicas` can let a runaway scale-up event exhaust a shared
   downstream dependency. source: https://learnkube.com/production-best-practices

5. When replica count flaps rapidly under roughly steady load, treat it
   as a stabilization-window-too-short or metric-too-noisy problem —
   widen the relevant stabilization window or switch to a
   smoother/aggregated metric source — rather than compensating by
   narrowing `minReplicas`/`maxReplicas`, which does not address the
   oscillation's cause. source: https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/

## Sources

- https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/
- https://learnkube.com/production-best-practices
