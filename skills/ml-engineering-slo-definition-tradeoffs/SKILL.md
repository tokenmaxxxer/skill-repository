---
name: ml-engineering-slo-definition-tradeoffs
description: Use when setting or auditing a model-serving SLO and its error-budget policy, including deploy-velocity tradeoffs as the budget depletes. Applies to the slo-definition-tradeoffs axis.
metadata:
  axis: slo-definition-tradeoffs
  rule_count_floor: 5
---

# SLO definition and error-budget tradeoffs

Research trail: Google SRE book (service level objectives) and SRE workbook (error budget policy, implementing SLOs) as the named-methodology primary source; Nobl9's error-budget guide as a practitioner cross-check. Fetched this session.

## Trigger

Apply this skill when defining or auditing a latency/availability/
throughput/cost SLO for a serving model, or deciding how deploy velocity
should respond as an error budget depletes — distinguishing it from
serving-pattern-selection (which architecture is chosen before an SLO is
set) and rollout-promotion-rollback (the rollback mechanics once an SLO
breach is detected, a separate concern from defining the SLO itself).

## Procedure

1. Derive an SLO target from actual user tolerance for degraded
   service, not a round default picked without justification (rule 1).
2. Use a ~99% availability tier for internal/tooling-facing services;
   move to 99.9%+ for payment or other critical user-facing paths, never
   reuse the lower figure there (rule 2).
3. When the error budget has less than 25% remaining for its
   measurement window, slow deploys and prioritize reliability work over
   shipping new changes (rule 3).
4. When the error budget reaches 0% for its window, freeze
   non-reliability deploys until the budget recovers (rule 4).
5. When an SLI duplicates an already-tracked latency/availability/
   throughput signal without adding new user-facing information, drop it
   rather than letting the dashboard grow unboundedly (rule 5).

## Output shape

An SLO table (latency/availability/throughput/cost) with each target
justified by user tolerance, plus a stated deploy-velocity policy keyed
to remaining error budget.

## Rules

1. When defining a latency/availability/throughput/cost SLO for a serving model, derive the target from actual user tolerance for degraded service, not a round default like "99.9%" picked without justification — an SLO exists to state what makes users unhappy, not to hit an arbitrary number. source: https://sre.google/sre-book/service-level-objectives/

2. When the service is internal/tooling-facing, an availability SLO around 99% (~7.2h/month downtime budget) is an acceptable choice; when the service sits on a payment or other critical user-facing path, do not reuse that figure — move to a 99.9%+ tier instead, since the user-impact cost of downtime differs by orders of magnitude between the two cases. source: https://sre.google/sre-book/service-level-objectives/

3. When a serving SLO's error budget for its measurement window has less than 25% remaining, slow down model/service deploys and prioritize reliability work over shipping new changes, rather than continuing default release velocity. source: https://sre.google/workbook/error-budget-policy/

4. When a serving SLO's error budget reaches 0% for its window, freeze non-reliability model/service deploys until the budget recovers, rather than continuing to ship model updates against an already-exhausted budget. source: https://sre.google/workbook/error-budget-policy/

5. **REMOVAL**: When a service SLO table already tracks latency, availability, and throughput, drop any additional SLI that duplicates one of these without adding a new user-facing signal (e.g. a redundant p50 latency metric sitting next to p99 that no alert or decision actually consumes) rather than letting the dashboard grow unboundedly. source: https://sre.google/workbook/implementing-slos/
