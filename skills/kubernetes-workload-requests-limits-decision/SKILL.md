---
name: kubernetes-workload-requests-limits-decision
description: Use when setting a container's CPU/memory requests and limits in a Kubernetes manifest, deciding whether a workload needs a CPU limit at all, or diagnosing an OOMKilled or CPU-throttled pod.
axis: requests-limits-decision
rule_count_floor: 6
---

# Kubernetes resource requests/limits decision rules

## Trigger

Apply this skill when writing or reviewing a container's `resources:`
block in a Pod/Deployment spec, when a pod is being OOMKilled or
CPU-throttled and the request/limit values are suspect, or when
deciding whether a given container should carry a CPU limit at all.

## Procedure

1. Always set a `requests` value for both CPU and memory on every
   container — never leave a production container unrequested (rule 1).
2. Always set a memory `limit`, and set it equal to the memory
   `request` for predictable, Guaranteed-QoS behavior on latency-
   sensitive workloads (rule 2, rule 3).
3. Do not reflexively set a CPU `limit` — decide based on whether
   throttling under burst is acceptable for this workload (rule 4).
4. Size requests from observed usage (e.g. VPA recommendations or
   historical metrics), not from a guessed round number (rule 5).
5. On OOMKilled, raise the memory request/limit pair; on CPU
   throttling with a CPU limit set, raise or remove the CPU limit
   rather than the request (rule 6).

## Output shape

A `resources:` block (or a diagnosis) stating the CPU/memory request
value, the CPU/memory limit value (or the explicit decision to omit a
CPU limit), and the QoS class this produces, each traceable to the
rule below that forced the choice.

## Rules

1. Every container running in production must declare a CPU and memory
   `requests` value — the scheduler uses `requests` to place the pod on
   a node with enough allocatable capacity, and an unrequested
   container can be scheduled onto a node with no real headroom for it,
   then get evicted first under node pressure. source: https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/

2. Set memory `limits` on every container — memory is not compressible,
   so a container that exceeds its memory limit is OOMKilled rather
   than throttled; without a limit at all, one runaway container can
   exhaust node memory and take down co-located pods. source: https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/

3. For latency-sensitive workloads, set memory `limits` equal to memory
   `requests` (and do the same for CPU if a CPU limit is used) to get
   the Guaranteed QoS class — Guaranteed pods are the last to be
   evicted under node memory pressure, unlike Burstable or BestEffort
   pods. source: https://kubernetes.io/docs/concepts/scheduling-eviction/node-pressure-eviction/

4. **REMOVAL**: Do not set a CPU `limit` by default — CPU is
   compressible, so a container exceeding its CPU limit is throttled
   (via CFS quota) rather than killed, and a too-tight CPU limit
   silently degrades latency during legitimate bursts even when the
   node has spare CPU capacity sitting idle; only set a CPU limit when
   you specifically want to cap a workload's spare-capacity usage
   (e.g. for cost/tenancy isolation), not as a default hygiene practice.
   source: https://home.robusta.dev/blog/stop-using-cpu-limits

5. Derive request values from observed usage (e.g. a VPA
   recommendation, or historical CPU/memory metrics under real load),
   not from a guessed round number — over-requesting wastes cluster
   capacity and under-requesting causes scheduling onto nodes that
   cannot actually sustain the workload. source: https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/

6. When diagnosing a pod, treat OOMKilled as a memory request/limit
   problem (raise the pair, or fix a leak) and CPU throttling as a CPU
   limit problem (raise or remove the CPU limit) — do not "fix" CPU
   throttling by raising the memory limit or vice versa; the two
   resources fail through different mechanisms (kill vs. throttle) and
   need independent diagnosis. source: https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/

## Sources

- https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/
- https://kubernetes.io/docs/concepts/scheduling-eviction/node-pressure-eviction/
- https://home.robusta.dev/blog/stop-using-cpu-limits
- https://learnkube.com/production-best-practices
