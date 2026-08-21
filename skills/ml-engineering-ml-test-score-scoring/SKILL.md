---
name: ml-engineering-ml-test-score-scoring
description: Use when you need guidance on ML Test Score scoring discipline (Breck et al. 2017). Applies to the ml-test-score-scoring axis.
axis: ml-test-score-scoring
rule_count_floor: 5
---

# ML Test Score scoring discipline (Breck et al. 2017)

Research trail: Breck, Cai, Nielsen, Salib & Sculley, "The ML Test Score: A Rubric for ML Production Readiness and Technical Debt Reduction" (IEEE Big Data 2017), the named primary source for this role's Data/Model/Infrastructure/Monitoring Tests sections; TensorFlow Data Validation (TFX) docs for the training-serving skew mechanics one of the rubric's items requires. Fetched this session.

## Rules

1. When scoring the Data Tests section, check feature expectations/distribution/schema against a codified schema (not eyeballed) and record a numeric score per item per the rubric, rather than a pass/fail narrative paragraph — Breck et al.'s rubric is built around per-item scoring, not prose summary. source: https://research.google/pubs/the-ml-test-score-a-rubric-for-ml-production-readiness-and-technical-debt-reduction/

2. When scoring Model Tests, include both an explicit offline-metric-vs-baseline comparison AND a separate staleness-tolerance check, not a single combined "accuracy is fine" note — the rubric names these as distinct scored items because a model can pass one and fail the other. source: https://research.google/pubs/the-ml-test-score-a-rubric-for-ml-production-readiness-and-technical-debt-reduction/

3. When checking for training-serving skew as part of ML Infrastructure/Model Tests, compare training and serving feature statistics using a skew comparator (L-infinity norm for simple numeric cases, Jensen-Shannon divergence when features mix categorical and numeric) rather than a manual spot-check of a handful of examples. source: https://www.tensorflow.org/tfx/guide/tfdv

4. When scoring Monitoring Tests, wire an active drift/skew alert to a threshold that pages someone, not just a dashboard someone might glance at — the rubric's monitoring section exists specifically because launch-time correctness erodes silently over time without an active trigger. source: https://research.google/pubs/the-ml-test-score-a-rubric-for-ml-production-readiness-and-technical-debt-reduction/

5. **REMOVAL**: When a Data/Model/Infrastructure/Monitoring test item cannot be automated and only exists as a documented manual checklist step, drop it from the counted-test score entirely (score it as not passing, don't grant partial credit for "documented but manual") — the rubric's intent is to distinguish automated verification from unverified process description. source: https://research.google/pubs/the-ml-test-score-a-rubric-for-ml-production-readiness-and-technical-debt-reduction/
