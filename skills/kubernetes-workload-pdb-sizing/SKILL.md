---
name: kubernetes-workload-pdb-sizing
description: >-
  Use when creating or sizing a PodDisruptionBudget for a Kubernetes workload,
  or deciding whether minAvailable or maxUnavailable is the right field for a
  given replica count. Trigger on requests like "node drain blocked by PDB",
  "minAvailable vs maxUnavailable", "PDB 값 어떻게 잡아", "cluster upgrade dropped
  availability". Do NOT use for a full pre-production manifest audit across
  all readiness properties (use
  kubernetes-workload-production-readiness-checklist).
metadata:
  axis: pdb-sizing
  rule_count_floor: 5
---

# Kubernetes PodDisruptionBudget sizing rules

## Trigger

Apply this skill when writing a `PodDisruptionBudget` for a Deployment/
StatefulSet, choosing between `minAvailable` and `maxUnavailable`, or
reviewing why a node drain/cluster upgrade is blocked or is dropping
availability below expectations.

## Procedure

1. Add a PDB to every workload that must stay available during
   voluntary disruptions (node drains, cluster upgrades) — an absent
   PDB means no protection at all (rule 1).
2. Never set a PDB that allows zero pods to be evicted when replicas
   equal the PDB threshold — this can block draining a node
   indefinitely (rule 2).
3. Use `maxUnavailable` for workloads where a fixed headroom in
   absolute pods matters regardless of replica count; use
   `minAvailable` when a floor on serving capacity matters regardless
   of how many replicas exist (rule 3).
4. Never set `minAvailable` equal to the replica count — this
   guarantees zero eviction tolerance (rule 4).
5. For single-replica workloads, understand that any non-zero PDB
   value still blocks voluntary eviction of the only pod — decide
   deliberately whether that is intended (rule 5).

## Output shape

A `PodDisruptionBudget` spec stating `minAvailable` or `maxUnavailable`
and its value, sized against the workload's actual replica count, each
traceable to the rule below that forced the choice.

## Rules

1. Any workload that must keep serving during a voluntary disruption
   (node drain, cluster autoscaler scale-down, cluster upgrade) needs
   an explicit `PodDisruptionBudget` — without one, the eviction API
   has no constraint stopping it from draining every replica of that
   workload off a node being drained at once. source: https://kubernetes.io/docs/tasks/run-application/configure-pdb/

2. **REMOVAL**: Never configure a PDB whose threshold allows zero
   voluntary evictions when the workload is at its normal replica
   count (e.g. `minAvailable` equal to current replica count, or
   `maxUnavailable: 0` on a workload that cannot scale up first) — a
   zero-eviction-tolerance PDB can permanently block a node drain or
   cluster upgrade from completing, since the eviction API refuses any
   eviction that would violate the budget. source: https://kubernetes.io/docs/tasks/run-application/configure-pdb/

3. Choose `maxUnavailable` when the workload needs a fixed absolute (or
   percentage) cap on how many pods may be down at once regardless of
   total replica count (e.g. "never more than 1 pod down"); choose
   `minAvailable` when the workload needs a floor on how many pods must
   stay serving regardless of replica count (e.g. "always at least 3
   serving") — the two fields express complementary but not
   interchangeable constraints, and picking the wrong one for the
   workload's actual concern produces a PDB that is technically valid
   but does not protect the property that matters. source: https://kubernetes.io/docs/tasks/run-application/configure-pdb/

4. **REMOVAL**: Never set `minAvailable` numerically equal to the
   workload's replica count — this is mathematically identical to
   `maxUnavailable: 0` and produces the same drain-blocking failure
   mode as rule 2; if zero-disruption tolerance is genuinely intended,
   that decision needs to be made explicitly (and paired with a scaling
   plan) rather than arrived at accidentally via this off-by-one
   sizing mistake. source: https://kubernetes.io/docs/tasks/run-application/configure-pdb/

5. For a single-replica workload, recognize that setting
   `minAvailable: 1` (or `maxUnavailable: 0`) blocks voluntary eviction
   of that one pod entirely, since there is no other replica to absorb
   the disruption — decide deliberately whether the workload should
   have a PDB at all in this case, rather than adding one reflexively
   from a multi-replica template. source: https://learnkube.com/production-best-practices

## Sources

- https://kubernetes.io/docs/tasks/run-application/configure-pdb/
- https://learnkube.com/production-best-practices
