---
name: ml-engineering-rollout-promotion-rollback
description: Use when you need guidance on Rollout staging, promotion, and rollback. Applies to the rollout-promotion-rollback axis.
axis: rollout-promotion-rollback
rule_count_floor: 5
---

# Rollout staging, promotion, and rollback

Research trail: Google Cloud Architecture Center's ML production-readiness guidelines (canary/shadow rollout guidance) as the practitioner layer; Qwak's shadow-vs-canary comparison as a cross-check. Fetched this session.

## Rules

1. When a new model version is ready to enter production, order the rollout offline-eval -> shadow -> canary -> full rather than skipping straight to full traffic, so each stage substantiates confidence before the next stage increases user exposure. source: https://docs.cloud.google.com/architecture/guidelines-for-developing-high-quality-ml-solutions

2. When validating a new model against the live serving pipeline before exposing it to any real user, use shadow deployment (duplicate live traffic to the new model, log its outputs, never serve them) rather than canary — shadow carries zero user-facing risk while still validating the pipeline under real production data. source: https://www.qwak.com/post/shadow-deployment-vs-canary-release-of-machine-learning-models

3. When a model has passed shadow validation and needs controlled live exposure, use canary with an initial small traffic slice (5-10%) gated by automated threshold checks against the service's SLOs to decide whether to ramp or halt, rather than manual eyeballing of dashboards. source: https://docs.cloud.google.com/architecture/guidelines-for-developing-high-quality-ml-solutions

4. When canary or full-rollout metrics breach a pre-declared rollback threshold (SLO breach or model-quality regression), roll back automatically rather than waiting on a human decision cycle — the rollback trigger must be defined before the rollout starts, not improvised after a breach is observed. source: https://docs.cloud.google.com/architecture/guidelines-for-developing-high-quality-ml-solutions

5. **REMOVAL**: When traffic volume is too low for a shadow or canary stage to reach a statistically meaningful comparison sample within an acceptable rollout window, drop that stage from the pipeline for this model rather than running it as theater — go directly from offline evaluation to a conservative canary with a longer ramp instead. source: https://www.qwak.com/post/shadow-deployment-vs-canary-release-of-machine-learning-models
