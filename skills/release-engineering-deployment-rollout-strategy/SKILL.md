---
name: release-engineering-deployment-rollout-strategy
description: Use when choosing between rolling, canary, and blue-green deployment for a service, or setting the rollback threshold and config validation gate for the rollout.
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

## Rules

1. **When** a service is low-risk and changes incrementally on a
   recurring cadence, **choose** rolling deployment as the default —
   update a subset of instances at a time rather than all at once.
   source: getunleash.io, "Canary vs. blue/green vs. rolling
   deployment: How to choose" —
   https://www.getunleash.io/blog/comparing-deployment-strategies-canary-blue-green-and-rolling

2. **When** a service is customer-facing or high-risk and the team has
   monitoring granular enough to detect a problem in a small percentage
   of traffic, **choose** canary deployment — gradual traffic shift
   (e.g. 1%, 5%, 10%) with dedicated canary-instance dashboards at
   lower alert thresholds than the full-traffic dashboards.
   source: TechTarget, "When to use canary vs. blue/green vs. rolling
   deployment" —
   https://www.techtarget.com/searchitoperations/answer/When-to-use-canary-vs-blue-green-vs-rolling-deployment

3. **When** a small number of critical services need instant, simple
   rollback and the team lacks (or doesn't trust) the monitoring
   infrastructure to catch a problem confined to a small canary slice,
   **choose** blue-green deployment — the rollback trigger is a single
   traffic switch, not a metric threshold that must fire correctly.
   source: getunleash.io, "Canary vs. blue/green vs. rolling
   deployment: How to choose" —
   https://www.getunleash.io/blog/comparing-deployment-strategies-canary-blue-green-and-rolling

4. **When** infrastructure cannot support running two full parallel
   environments (blue-green's requirement), **choose** canary or
   rolling instead of forcing blue-green — blue-green's environment-
   doubling cost is a real infrastructure constraint, not just a
   preference.
   source: Educative, "Deployment strategy: blue/green deployment vs.
   canary release" — https://educative.io/blog/blue-green-deployment-vs-canary-release

5. **When** a release carries a major, all-at-once behavioral change
   (not an incremental tweak), **choose** blue-green over rolling — a
   rolling deployment run's instance-by-instance mixed-version window is
   riskier for changes that aren't safe to run in two versions
   simultaneously.
   source: getunleash.io, "Canary vs. blue/green vs. rolling
   deployment: How to choose" —
   https://www.getunleash.io/blog/comparing-deployment-strategies-canary-blue-green-and-rolling

6. **When** running a canary, **choose** to pre-declare the error-rate
   (or latency, saturation) threshold that triggers an automatic
   rollback before the canary starts — never decide the threshold
   ad hoc while watching the rollout, since that invites rationalizing a
   borderline signal as acceptable.
   source: TechTarget, "When to use canary vs. blue/green vs. rolling
   deployment" —
   https://www.techtarget.com/searchitoperations/answer/When-to-use-canary-vs-blue-green-vs-rolling-deployment

7. **When** a rolling deployment needs to be rolled back mid-rollout,
   **choose** to budget for the slowest rollback path of the three
   strategies — a rolling rollback runs the deployment process in
   reverse, instance by instance, so an incident during rolling
   deployment resolves slower than blue-green's instant switch.
   source: caduh, "Blue-Green vs Canary vs Rolling Deployments" —
   https://www.caduh.com/blog/blue-green-vs-canary-vs-rolling-deployments

8. **When** a system is fast-evolving and rolling deployment's
   infrastructure requirements aren't available, **choose** canary as
   the fallback rather than forcing a rolling strategy the
   infrastructure can't actually support.
   source: acquaintsoft, "Blue-Green vs Canary Deployment" —
   https://acquaintsoft.com/blog/blue-green-vs-canary-deployment-strategy-cost

9. **When** scaling a canary from initial exposure to full rollout,
   **choose** to expand exponentially and gate each expansion step on
   the previous step's health signal — never jump straight from a small
   canary percentage to 100%.
   source: sre.google, "Release Engineering" (canary scale-up by
   service criticality) — https://sre.google/sre-book/release-engineering/

10. **REMOVAL** — **when** a service has proven stable enough that its
    canary phase consistently passes with no incidents over many
    releases, **choose** to shorten (not eliminate) the canary soak
    time rather than add extra manual sign-off steps on top of an
    already-reliable automated gate — added ceremony on a proven gate
    is pure toil.
    source: sre.google, "Eliminating Toil" (toil = manual work with no
    enduring value) — https://sre.google/sre-book/eliminating-toil/

11. **REMOVAL** — **when** a team runs both a canary stage and a
    separate blue-green stage for the same release path "just in case,"
    **choose** to pick one rollout strategy per service based on the
    conditions above and remove the redundant second stage — running
    both compounds rollout time without a matching safety gain once the
    conditions above already point to one strategy.
    source: getunleash.io, "Canary vs. blue/green vs. rolling
    deployment: How to choose" —
    https://www.getunleash.io/blog/comparing-deployment-strategies-canary-blue-green-and-rolling

12. **When** monitoring infrastructure cannot yet detect a problem
    confined to a small traffic slice, **choose** blue-green over
    canary until that monitoring gap is closed, rather than run canary
    with thresholds the team can't actually observe.
    source: getunleash.io, "Canary vs. blue/green vs. rolling
    deployment: How to choose" —
    https://www.getunleash.io/blog/comparing-deployment-strategies-canary-blue-green-and-rolling

13. **When** a release carries a config or environment-variable change
    alongside the code change, **choose** to validate that config
    against a schema and a secret-exposure scan before the rollout
    starts, with stricter required fields for production than for
    lower environments (e.g. HTTPS and encryption-at-rest required in
    production, optional in dev) — a config typo or leaked credential
    caught after traffic starts shifting is a second, avoidable
    incident stacked on top of whatever the code change itself risks.
    source: sre.google, "Release Engineering" (hermetic, verified
    inputs as a release precondition) —
    https://sre.google/sre-book/release-engineering/
