---
name: conformance-review-sampling-derivation
description: Use when full enumeration of every requirement/file under review is infeasible and the review needs a defensible sampling scope instead. Applies to the sampling-derivation axis.
metadata:
  axis: sampling-derivation
  rule_count_floor: 3
---

# Sampling derivation

When full enumeration of every requirement/file is infeasible and a review
must state a defensible sampling scope instead.

## Trigger

Apply this skill when full enumeration of every requirement/file under
review is infeasible and the review must state a defensible sampling
scope instead of a complete enumeration.

## Procedure

1. Stratify by risk/change-recency before sampling, drawing a sample
   from each stratum rather than one flat random draw across the whole
   population (rule 1).
2. When items combine along more than one independent dimension, use
   pairwise/t-wise coverage instead of full cross-product enumeration
   (rule 2).
3. State the sampling derivation explicitly in the record — population
   size, stratum definitions, sample size per stratum, and selection
   method — not only the resulting count (rule 3).
4. When a sampled subset returns zero findings, report the zero-finding
   result as-is with the stated sample scope; do not silently extend the
   sample to search for a finding (rule 4).
5. Assign each stratum an impact tier from the requirement's own stated
   consequence of failure, and exempt the highest tier from sampling
   entirely — inspect every item in it (rule 5).

## Output shape

A stated sampling derivation — population size, strata, sample size per
stratum, and selection method — with the highest-impact stratum fully
inspected rather than sampled, and a zero-finding result reported without
post-hoc sample expansion.

## Rules

1. **When** the number of comparable items (files, endpoints, config entries)
   under review exceeds what can be inspected individually within the
   review's scope, **stratify by risk/change-recency before sampling** — pull
   a random sample from each stratum (e.g. changed-this-PR vs. unchanged,
   security-sensitive vs. not) rather than one flat random draw across the
   whole population, so a small but critical stratum isn't diluted away by a
   large low-risk one. source: stratified sampling for conformance review,
   used to ensure unusual/outlier executions are represented even under a
   fixed sample size. ([ResearchGate: Estimation of Software Reliability by
   Stratified Sampling](https://www.researchgate.net/publication/220403866_Estimation_of_Software_Reliability_by_Stratified_Sampling))

2. **When** items combine along more than one independent dimension (e.g. a
   requirement checked across several environments x several input types),
   **use pairwise/t-wise coverage instead of full cross-product enumeration**
   — cover every pairwise interaction at least once rather than testing the
   full combinatorial space, which is the standard trade-off between
   sampling cost and defect-detection effectiveness. source: t-wise
   interaction sampling literature for combinatorial test spaces. ([arXiv:
   T-Wise Presence Condition Coverage and Sampling for Configurable
   Systems](https://arxiv.org/pdf/2205.15180))

3. **When** a sampling derivation is used instead of full enumeration, **state
   the derivation explicitly in the record** (population size, stratum
   definitions, sample size per stratum, and the selection method) rather
   than reporting only the resulting count — an unstated derivation cannot be
   distinguished from an arbitrary spot-check by a later reader. source: this
   repo's own record-claim-citation convention (a bare count claim needs a
   `derived:` line naming how it was produced).

4. **When** a sampled subset turns out to contain zero findings across an
   entire review pass, **do not silently extend the sample to search for a
   finding** — report the zero-finding result as-is with the stated sample
   scope; enlarging the sample only when the first draw came up empty biases
   the review toward finding problems that aren't representative of the whole
   population. (removal) source: stratified-sampling discipline requires the
   sample plan to be fixed before the draw, not adjusted post-hoc based on the
   outcome. ([ResearchGate: Estimation of Software Reliability by Stratified
   Sampling](https://www.researchgate.net/publication/220403866_Estimation_of_Software_Reliability_by_Stratified_Sampling))

5. **When** deriving strata under rule 1, **assign each stratum an impact
   tier from the requirement's own stated consequence of failure (security,
   data-loss, or user-facing-correctness impact vs. cosmetic/internal), and
   exempt the highest tier from sampling entirely** — inspect every item in
   a high-impact stratum rather than drawing a sample from it, reserving
   sampling for the lower-impact strata where a missed item costs little.
   A fixed sample fraction applied uniformly across tiers treats a
   security-critical item and a cosmetic one as equally safe to skip, which
   they are not.
