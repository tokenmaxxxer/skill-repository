---
name: release-engineering-deployment-rollout-strategy
description: >-
  Use when choosing between rolling, canary, and blue-green deployment for a
  service, or setting the rollback threshold and config validation gate for
  the rollout. Trigger on requests like "canary or blue-green here",
  "pre-declare the rollback threshold", "exponential canary traffic steps",
  "배포 전략 뭘로 할까". Do NOT use for the ops-role rollout state's per-step plan
  file in ops/rollout-plan.md (use release-engineering-rollout-plan).
metadata:
  axis: deployment-rollout-strategy
  rule_count_floor: 13

---

# Deployment rollout strategy

## Trigger

Apply this skill when choosing a deployment mechanism (rolling, canary,
blue-green) for a release, pre-declaring the metric threshold that
triggers rollback, or deciding whether infrastructure/monitoring
constraints rule a strategy in or out.

## Procedure

1. Default to rolling deployment for a low-risk service on a recurring
   cadence (rule 1); choose canary for a customer-facing or high-risk
   service with monitoring granular enough to detect a problem in a
   small traffic slice (rule 2); choose blue-green for critical services
   needing instant rollback where that granular monitoring isn't
   trusted (rule 3).
2. Rule out blue-green when infrastructure can't run two full parallel
   environments (rule 4), and prefer blue-green over rolling for a
   major all-at-once behavioral change unsafe to run in two versions at
   once (rule 5); rule out canary when monitoring can't yet detect a
   small-slice problem (rule 12), falling back to canary when rolling's
   infrastructure requirements aren't met (rule 8).
3. Pre-declare the canary's rollback threshold before the rollout
   starts, never ad hoc mid-rollout (rule 6), and budget for rolling
   deployment's slower, instance-by-instance rollback path (rule 7).
4. Scale a canary's traffic exponentially, gating each expansion step on
   the previous step's health signal (rule 9).
5. Shorten (not eliminate) a proven service's canary soak time rather
   than add manual sign-off on top of an already-reliable gate (rule
   10), and collapse a redundant "canary plus blue-green for the same
   path" setup to one strategy chosen by the conditions above (rule 11).
6. Validate any accompanying config/env-var change against a schema and
   secret-exposure scan before the rollout starts, with stricter
   required fields in production than lower environments (rule 13).

## Output shape

A chosen deployment strategy (rolling/canary/blue-green) for the
release, its pre-declared rollback threshold, and, where a config change
accompanies it, confirmation the config passed schema/secret-exposure
validation — each traceable to the rule above that forced it.

## Rule index

Full rule text, citations, and counter-examples:
`references/rules.md` in this skill's directory — read it when a
matched rule's detail is needed.

- 1.1 — **When** a service is low-risk and changes incrementally on a recurring cadence, **choose** rolling deployment as the default — update a subset of instances at a time ra…
- 1.2 — **When** a service is customer-facing or high-risk and the team has monitoring granular enough to detect a problem in a small percentage of traffic, **choose** canary de…
- 1.3 — **When** a small number of critical services need instant, simple rollback and the team lacks (or doesn't trust) the monitoring infrastructure to catch a problem confine…
- 1.4 — **When** infrastructure cannot support running two full parallel environments (blue-green's requirement), **choose** canary or rolling instead of forcing blue-green — bl…
- 1.5 — **When** a release carries a major, all-at-once behavioral change (not an incremental tweak), **choose** blue-green over rolling — a rolling deployment run's instance-by…
- 1.6 — **When** running a canary, **choose** to pre-declare the error-rate (or latency, saturation) threshold that triggers an automatic rollback before the canary starts — nev…
- 1.7 — **When** a rolling deployment needs to be rolled back mid-rollout, **choose** to budget for the slowest rollback path of the three strategies — a rolling rollback runs t…
- 1.8 — **When** a system is fast-evolving and rolling deployment's infrastructure requirements aren't available, **choose** canary as the fallback rather than forcing a rolling…
- 1.9 — **When** scaling a canary from initial exposure to full rollout, **choose** to expand exponentially and gate each expansion step on the previous step's health signal — n…
- 1.10 — **REMOVAL** — **when** a service has proven stable enough that its canary phase consistently passes with no incidents over many releases, **choose** to shorten (not elim…
- 1.11 — **REMOVAL** — **when** a team runs both a canary stage and a separate blue-green stage for the same release path "just in case," **choose** to pick one rollout strategy…
- 1.12 — **When** monitoring infrastructure cannot yet detect a problem confined to a small traffic slice, **choose** blue-green over canary until that monitoring gap is closed,…
- 1.13 — **When** a release carries a config or environment-variable change alongside the code change, **choose** to validate that config against a schema and a secret-exposure s…
