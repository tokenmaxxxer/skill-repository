---
name: ml-engineering-rollout-promotion-rollback
description: >-
  Use when staging a new model version's rollout through shadow, canary, and
  full traffic, or defining its automated rollback trigger. Applies to the
  rollout-promotion-rollback axis — offline-eval -> shadow -> canary -> full
  ordering, SLO-gated 5-10% canary slices, pre-declared rollback thresholds,
  documented stage-skips at low traffic. Trigger on requests like "카나리 배포 계획
  세워줘", "shadow deployment", "automated rollback trigger", "canary ramp plan".
  Do NOT use for judging whether the underlying launch metric itself is
  trustworthy (use ml-engineering-evaluation-discipline).
metadata:
  axis: rollout-promotion-rollback
  rule_count_floor: 5
---

# Rollout staging, promotion, and rollback

Research trail: Google Cloud Architecture Center's ML production-readiness guidelines (canary/shadow rollout guidance) as the practitioner layer; Qwak's shadow-vs-canary comparison as a cross-check. Fetched this session.

## Trigger

Apply this skill when staging a new model version's path from
offline-ready to full production traffic, or defining what triggers an
automated rollback — distinguishing it from serving-pattern-selection
(which serving architecture the model runs under, a separate choice)
and evaluation-discipline (whether the underlying launch decision's
metric is trustworthy in the first place).

## Procedure

1. Order the rollout offline-eval -> shadow -> canary -> full, never
   skipping straight to full traffic (rule 1).
2. Use shadow deployment — duplicate live traffic, log outputs, never
   serve them — to validate against the live serving pipeline with zero
   user-facing risk (rule 2).
3. After shadow validation passes, use canary with an initial 5-10%
   traffic slice gated by automated SLO threshold checks to decide
   ramp-or-halt, not manual dashboard eyeballing (rule 3).
4. Roll back automatically when canary or full-rollout metrics breach a
   pre-declared rollback threshold, with the trigger defined before the
   rollout starts (rule 4).
5. When traffic volume is too low for shadow or canary to reach a
   meaningful sample within an acceptable window, drop that stage and go
   directly to a conservative, longer-ramp canary instead of running it
   as theater (rule 5).

## Output shape

A staged rollout plan (offline-eval -> shadow -> canary -> full, or a
documented stage-skip when traffic is too low) with a pre-declared,
automated rollback trigger.

## Rules

1. When a new model version is ready to enter production, order the rollout offline-eval -> shadow -> canary -> full rather than skipping straight to full traffic, so each stage substantiates confidence before the next stage increases user exposure. source: https://docs.cloud.google.com/architecture/guidelines-for-developing-high-quality-ml-solutions

2. When validating a new model against the live serving pipeline before exposing it to any real user, use shadow deployment (duplicate live traffic to the new model, log its outputs, never serve them) rather than canary — shadow carries zero user-facing risk while still validating the pipeline under real production data. source: https://www.qwak.com/post/shadow-deployment-vs-canary-release-of-machine-learning-models

3. When a model has passed shadow validation and needs controlled live exposure, use canary with an initial small traffic slice (5-10%) gated by automated threshold checks against the service's SLOs to decide whether to ramp or halt, rather than manual eyeballing of dashboards. source: https://docs.cloud.google.com/architecture/guidelines-for-developing-high-quality-ml-solutions

4. When canary or full-rollout metrics breach a pre-declared rollback threshold (SLO breach or model-quality regression), roll back automatically rather than waiting on a human decision cycle — the rollback trigger must be defined before the rollout starts, not improvised after a breach is observed. source: https://docs.cloud.google.com/architecture/guidelines-for-developing-high-quality-ml-solutions

5. **REMOVAL**: When traffic volume is too low for a shadow or canary stage to reach a statistically meaningful comparison sample within an acceptable rollout window, drop that stage from the pipeline for this model rather than running it as theater — go directly from offline evaluation to a conservative canary with a longer ramp instead. source: https://www.qwak.com/post/shadow-deployment-vs-canary-release-of-machine-learning-models
