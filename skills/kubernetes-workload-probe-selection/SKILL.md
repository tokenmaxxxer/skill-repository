---
name: kubernetes-workload-probe-selection
description: Use when configuring a container's liveness, readiness, or startup probe in a Kubernetes manifest, or diagnosing a pod stuck in a restart loop or never receiving traffic.
metadata:
  axis: probe-selection
  rule_count_floor: 6
---

# Kubernetes probe selection rules

## Trigger

Apply this skill when adding or reviewing `livenessProbe`,
`readinessProbe`, or `startupProbe` on a container spec, or when a pod
is crash-looping on startup, is restarted needlessly under load, or is
Ready but not actually able to serve traffic.

## Procedure

1. Distinguish the two purposes first: liveness restarts a deadlocked
   container, readiness gates traffic to a not-yet-ready container
   (rule 1).
2. Never point a liveness probe at an external dependency (database,
   downstream API) — only check the process's own health (rule 2).
3. For a slow-starting container, add a `startupProbe` rather than
   loosening the liveness probe's timing (rule 3).
4. Give readiness and liveness probes distinct endpoints/logic when the
   container has any external dependency to check (rule 4).
5. Set failure thresholds and periods wide enough to tolerate transient
   slowness, not tuned to the fastest observed response (rule 5, rule 6).

## Output shape

A probe configuration (or diagnosis) stating which probe type(s) are
used, what each checks, and the timing/threshold values, each
traceable to the rule below that forced the choice.

## Rules

1. Use `livenessProbe` only to detect "the process is alive but stuck
   in a state it cannot recover from" and restart the container in
   that case; use `readinessProbe` to detect "the process is not yet
   ready to accept traffic" and remove the pod from Service endpoints
   without restarting it — conflating the two (e.g. using one probe
   for both) either restarts a pod that just needs more warm-up time or
   keeps sending traffic to a genuinely deadlocked process. source: https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/

2. **REMOVAL**: Never make a liveness probe depend on an external
   service (database connection, downstream API reachability) — if the
   liveness check fails because a database is briefly unreachable,
   Kubernetes restarts the application container even though the
   container process itself is healthy, which does nothing to fix the
   database and can cascade into a restart storm across every replica
   at once. source: https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/

3. For a container with a slow or variable startup time (JVM warm-up,
   large cache preload), add a `startupProbe` that disables liveness
   and readiness checks until it succeeds, rather than setting a long
   `initialDelaySeconds` or a lenient `failureThreshold` on the
   liveness probe — a startup probe gives slow-boot protection without
   permanently weakening the liveness probe's ability to catch a real
   post-startup hang. source: https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/

4. When a container has an external dependency worth checking (e.g. can
   it reach its database), check that dependency in the readiness
   probe only, never in liveness — an unreachable dependency should
   pull the pod out of the Service's endpoint list (readiness) without
   triggering a container restart that cannot fix the dependency
   (liveness). source: https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/

5. Set probe `periodSeconds`/`timeoutSeconds`/`failureThreshold` wide
   enough to absorb normal transient latency spikes under load, not
   tuned to the container's fastest observed response time — a probe
   tuned too tight flaps a healthy pod's readiness (or restarts it)
   under ordinary load variance. source: https://learnkube.com/production-best-practices

6. Combine a non-trivial `failureThreshold` with a `periodSeconds` that
   together tolerate at least one full garbage-collection pause or
   request-queue backlog for the workload's language/runtime, rather
   than the Kubernetes defaults unexamined — the defaults are a
   starting point, not a production-sized value for every workload.
   source: https://learnkube.com/production-best-practices

## Sources

- https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/
- https://learnkube.com/production-best-practices
