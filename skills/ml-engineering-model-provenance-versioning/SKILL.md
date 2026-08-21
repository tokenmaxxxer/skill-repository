---
name: ml-engineering-model-provenance-versioning
description: Use when you need guidance on Model provenance (model card) and data/model versioning. Applies to the model-provenance-versioning axis.
axis: model-provenance-versioning
rule_count_floor: 5
---

# Model provenance (model card) and data/model versioning

Research trail: Mitchell, Wu, Zaldivar, Barnes, Vasserman, Hutchinson, Spitzer, Raji & Gebru, "Model Cards for Model Reporting" (FAT* 2019), the named source for the model-card field set (via a 2024 secondary discussion of its categories); MLflow/DVC practitioner docs for data/model versioning and lineage. Fetched this session.

## Rules

1. When authoring a model card, include all of the source framework's named sections (model details, intended use, factors, metrics, evaluation data, training data, ethical considerations, caveats and recommendations) rather than a convenient subset — omitting training data or limitations makes the card non-conforming to the framework it claims to follow. source: https://arxiv.org/pdf/2403.15394

2. When writing the Intended Use section of a model card, state both the primary intended uses/users AND explicit out-of-scope use cases, not just the positive case — the framework requires both so a downstream user can tell misuse from intended use. source: https://arxiv.org/pdf/2403.15394

3. When registering a trained model artifact, assign it a version identifier traceable to the run/experiment that produced it (e.g. a model-registry version tied to its originating training run), rather than an ad hoc filename or date string, so any deployed model can be traced back to its lineage. source: https://lakefs.io/blog/mlflow-data-versioning/

4. When the training dataset for a model changes, version the dataset itself (e.g. a data-version-control commit tied to a specific Git commit) and record that version identifier alongside the model version, rather than versioning the model artifact alone — an unversioned dataset breaks reproducibility even when the model artifact is versioned. source: https://lakefs.io/blog/mlflow-data-versioning/

5. **REMOVAL**: When a model card's Ethical Considerations section only restates generic boilerplate (e.g. "may reflect biases present in training data") with no model-specific risk finding, drop the boilerplate and require it be rewritten from actual evaluation findings on this model — the framework treats this section as the one most in need of model-specific rather than generic content. source: https://arxiv.org/pdf/2403.15394
