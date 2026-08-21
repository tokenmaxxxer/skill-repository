---
name: refactoring-legacy-strangler-fig-migration
description: Use when choosing between Strangler Fig and Branch by Abstraction for a legacy migration, scoping a migration slice, verifying a new implementation's correctness before cutover, or deciding when to decommission the legacy path.
axis: strangler-fig-migration
rule_count_floor: 5
---

# Strangler fig migration

Research trail: Martin Fowler's original Strangler Fig naming, Azure Architecture Center's Strangler Fig pattern page, AWS Prescriptive Guidance's Branch-by-Abstraction page, and practitioner comparisons (Simran Chawla; techdebt.best; ishir.com/Security Boulevard modernization write-ups) covering when each pattern applies and how decommissioning is actually executed.

## Trigger

Apply this skill when choosing between the Strangler Fig pattern and
Branch by Abstraction for a legacy migration, scoping which slice of
functionality to migrate together, verifying a new implementation's
correctness before routing production traffic to it, or deciding when
a fully-migrated legacy path is safe to decommission.

## Procedure

1. Use the Strangler Fig pattern when the functionality has an
   externally interceptable request boundary (rule 1).
2. Use Branch by Abstraction when the functionality is embedded
   in-process with no interceptable boundary (rule 2).
3. Re-scope a migration slice when business, code, deployment, and team
   boundaries do not agree along the code boundary alone (rule 3).
4. Run a parallel run/shadow-traffic comparison before routing real
   traffic when output correctness can't be verified by review alone
   (rule 4).
5. Wait for a monitoring-confirmed zero-traffic signal on the legacy
   path before touching legacy code for a fully-migrated slice (rule 5).
6. After confirming zero legacy traffic, actually delete the old code
   path, its unused data, and the routing rule (rule 6).
7. Define an explicit adapter/translation layer at the facade boundary
   and forbid either side's internals from crossing it directly
   (rule 7).

## Output shape

A migration executed as reversible, boundary-scoped slices — Strangler
Fig or Branch by Abstraction as the boundary dictates — each verified
by parallel-run comparison and monitoring-confirmed zero traffic before
its legacy path is actually deleted through an explicit translation
layer.

## Rules

1. When a migration can intercept legacy functionality at a request boundary (an HTTP endpoint, a message queue, a CLI entry point) that is easily identifiable and independently routable, use the Strangler Fig pattern (a facade/proxy that routes requests between legacy and new implementations) rather than a big-bang rewrite — this distributes migration risk across many small, reversible routing changes instead of one irreversible cutover event. source: https://learn.microsoft.com/en-us/azure/architecture/patterns/strangler-fig

2. When the functionality to modernize is embedded deep inside a single codebase with upstream in-process callers (not reachable at a request boundary), use Branch by Abstraction (introduce an interface in front of the old implementation, build the new implementation behind the same interface, switch callers over) rather than Strangler Fig — Strangler Fig requires a boundary you can intercept externally, which deeply embedded logic does not have. source: https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-decomposing-monoliths/branch-by-abstraction.html

3. When business boundaries, code boundaries, deployment boundaries, and team boundaries do not agree for the functionality being migrated, do not force a Strangler Fig slice along the code boundary alone — re-scope the slice to match where those boundaries actually agree, since a mismatch turns the migration into ongoing cross-team coordination rather than an architecture change the routing layer can execute alone. source: https://simranchawla.com/unlocking-legacy-systems-strangler-fig-branch-by-abstraction-and-parallel-run-explained/

4. When a capability's output correctness cannot be verified by code review alone (financial calculations, complex business rules), run the new implementation in parallel with the old one (parallel run / shadow traffic) and compare outputs before routing real traffic to the new path — this proves correctness under production-like conditions before the routing layer is allowed to switch the capability over, which review of the new code cannot substitute for. source: https://simranchawla.com/unlocking-legacy-systems-strangler-fig-branch-by-abstraction-and-parallel-run-explained/

5. When a slice of functionality has been fully migrated and its new implementation is receiving all production traffic, wait for monitoring to confirm zero live traffic is reaching the legacy path for that slice before touching the legacy code — treating "the new path looks stable" as sufficient without a monitoring-confirmed zero-traffic signal risks decommissioning a path still in use by a caller the migration didn't account for. source: https://www.ishir.com/blog/332928/the-strangler-fig-pattern-how-to-modernize-legacy-systems-without-a-big-bang-rewrite.htm

6. **REMOVAL**: When a slice has been confirmed at zero legacy traffic, actually delete the old code path, its now-unused data (after any required grace period), and the routing rule that once split traffic to it — leaving the dead legacy path in place ("zombie code") is itself still debt and the step teams most often skip; decommissioning is not complete until the deletion actually lands, not just the traffic cutover. source: https://securityboulevard.com/2026/07/the-strangler-fig-pattern-how-to-modernize-legacy-systems-without-a-big-bang-rewrite/

7. When the facade routes a slice between legacy and modern implementations, define an explicit adapter/translation layer at that boundary and forbid either side's internal concepts, types, or field names from crossing it directly — without a named translation point, legacy assumptions leak forward into the new implementation and new-side assumptions leak backward into the legacy path, defeating the isolation the facade was introduced to provide.
