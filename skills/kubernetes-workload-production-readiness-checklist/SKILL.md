---
name: kubernetes-workload-production-readiness-checklist
description: Use when reviewing a Kubernetes workload manifest before it goes to production, or auditing an existing workload for missing production-readiness basics (resources, probes, PDB, HPA, non-root, graceful shutdown).
axis: production-readiness-checklist
rule_count_floor: 6
---

# Kubernetes production-readiness checklist

## Trigger

Apply this skill when a Kubernetes Deployment/StatefulSet manifest is
being reviewed before its first production deploy, or when auditing an
existing workload that has had an availability or resource incident and
needs a systematic readiness pass rather than a one-off fix.

## Procedure

1. Check resource requests/limits are present and sane — cross-check
   against `kubernetes-workload-requests-limits-decision` (rule 1).
2. Check liveness/readiness (and startup, if slow-booting) probes exist
   and are correctly scoped — cross-check against
   `kubernetes-workload-probe-selection` (rule 2).
3. Check a PodDisruptionBudget exists and is sized correctly —
   cross-check against `kubernetes-workload-pdb-sizing` (rule 3).
4. Check autoscaling behavior is deliberate, not default — cross-check
   against `kubernetes-workload-hpa-behavior` (rule 4).
5. Check the container runs as non-root and handles SIGTERM for
   graceful shutdown (rule 5, rule 6).
6. Do not treat "it deployed successfully" as evidence of readiness —
   readiness is these specific properties, checked explicitly (rule 6).

## Output shape

A checklist verdict per property (resources, probes, PDB, HPA,
non-root, graceful shutdown) stating pass/fail/not-applicable with the
specific gap named, not a general "looks fine" assessment.

## Rules

1. Verify every container declares CPU/memory `requests` and a memory
   `limit` sized from observed usage, not left at cluster defaults or
   omitted — an unrequested or unlimited container is a readiness gap
   even if the workload has run without incident so far, since the
   failure mode (bad scheduling, OOM-killing a neighbor) only surfaces
   under load or contention. source: https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/

2. Verify liveness and readiness probes are both present, target
   distinct concerns (liveness never checks an external dependency),
   and a startup probe exists for any slow-booting container — a
   workload missing readiness probes gets traffic before it can
   actually serve it; a workload missing liveness probes never
   self-heals from a hang. source: https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/

3. Verify a `PodDisruptionBudget` exists for any workload that must
   stay available during a node drain or cluster upgrade, and that its
   threshold does not accidentally block all voluntary eviction (e.g.
   `minAvailable` equal to replica count) — an absent or misconfigured
   PDB is invisible until the next cluster upgrade, at which point it
   either provides zero protection or blocks the upgrade outright.
   source: https://kubernetes.io/docs/tasks/run-application/configure-pdb/

4. If the workload uses a `HorizontalPodAutoscaler`, verify it is not
   also pinned to a static replica count elsewhere, and that its
   stabilization windows and chosen metric are deliberate rather than
   left at Kubernetes defaults unexamined. source: https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/

5. Verify the container runs as a non-root user (`securityContext.
   runAsNonRoot: true` or equivalent) rather than relying on the image's
   default user — running as root inside the container expands the
   blast radius of a container-escape vulnerability. source: https://learnkube.com/production-best-practices

6. Verify the application handles SIGTERM to drain in-flight requests
   and exit cleanly within `terminationGracePeriodSeconds`, rather than
   relying on Kubernetes' SIGKILL fallback — a workload that ignores
   SIGTERM drops in-flight requests on every rollout and every node
   drain, not just during incidents. source: https://learnkube.com/production-best-practices

## Sources

- https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/
- https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/
- https://kubernetes.io/docs/tasks/run-application/configure-pdb/
- https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/
- https://learnkube.com/production-best-practices
