---
axis: ltv-churn-assumption
rule_count_floor: 12
tier: moderate
---

# LTV churn-assumption — decision rules

## Decision rules

- **ADDITION**: when a model's churn rate is derived from a single
  cohort younger than 12 months, apply a wider confidence band on the
  resulting LTV rather than treat it as a point estimate — sensitivity
  analysis exists precisely to expose which input (churn is typically
  the highest-leverage one in an LTV formula) most changes the outcome,
  so an unstable churn input demands a range, not a point. source:
  https://www.synario.com/resources/blog/how-to-perform-a-financial-sensitivity-analysis/
  (sensitivity analysis identifies which input variables matter most to
  an outcome).

- **ADDITION**: for a subscription business with usage-based expansion,
  model gross-margin-adjusted LTV rather than revenue-only LTV — an
  unadjusted revenue figure overstates the metric investors actually
  compare against CAC. source:
  https://www.fiscallion.io/blog/saas-unit-economics (SaaS unit
  economics guide framing LTV alongside gross margin and the Rule of
  40).

- **REMOVAL**: when a churn assumption is already stress-tested via
  scenario analysis (bull/base/bear), drop a separately maintained
  "optimistic case" LTV line from the same table — a redundant ad hoc
  case duplicates what the bull-case scenario already covers and adds a
  second, uncoordinated set of assumptions to keep in sync. source:
  https://www.farseer.com/blog/scenario-planning-or-sensitivity-analysis/
  (the base/bull/bear three-scenario framework is the standard
  structure; ad hoc cases outside it fragment the model).

- **ADDITION**: when defining the churn/acquisition events that feed
  the retention figure, define them by economic substance (the date the
  last paid period ends; a "reactivation" for a returning customer
  rather than a fresh acquisition) — not by a user-initiated action (a
  cancel click, a support ticket) or a loose "new signup" count — since
  a definition tied to user action is gameable (moving the cancel
  button, treating win-backs as new logos) in a way a paid-period-end
  definition is not.

## Notes

Churn is the LTV input most sensitive to model error; treat any churn
number without a stated cohort age and sample size as unverified per
finance-evidence-chain.md.
