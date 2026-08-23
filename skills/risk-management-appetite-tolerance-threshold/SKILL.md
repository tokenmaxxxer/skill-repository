---
name: risk-management-appetite-tolerance-threshold
description: Use when setting or deriving a category- or entity-level risk appetite/tolerance threshold, choosing between appetite and tolerance framing, reconciling thresholds across interacting categories, or tracing a threshold back to its source. Applies to the appetite-tolerance-threshold axis.
metadata:
  axis: appetite-tolerance-threshold
  rule_count_floor: 10
---

# Risk appetite / tolerance threshold setting

## Trigger

Apply this skill when setting `risk-appetite-threshold` for a register
entry, choosing whether to express a threshold in appetite or tolerance
terms, reconciling thresholds across interacting risk categories,
auditing whether a threshold traces back to its entity-level appetite
statement, or a threshold is bound by an external regulatory/contractual
limit.

## Procedure

1. When setting a register entry's threshold, derive it from the
   entity-level appetite statement decomposed for that risk's
   category/objective, never independently (rule 1).
2. When the objective is strategic/business-model-level, express the
   threshold in appetite terms; when operational/day-to-day, express it
   in tolerance terms (rule 2).
3. When multiple risk categories interact, set the combined threshold
   from a portfolio view of how they cascade, not by summing
   independent per-category thresholds (rule 3).
4. When a category-level threshold cannot be traced back to an
   entity-level appetite statement, retire it and re-derive from the
   current statement rather than carrying it forward (rule 4).
5. When a threshold is bound by an external regulatory or contractual
   limit, cite the exact clause/control ID on the entry instead of only
   the generic appetite band (rule 5).

## Output shape

Each register entry's threshold traceable to an entity-level appetite
statement, expressed in appetite or tolerance terms matching its
objective level, reconciled across interacting categories, and citing
any binding external clause/control ID.

## Decision rules

1. When setting `risk-appetite-threshold` for a register entry, derive
   it from the entity-level appetite statement decomposed for that
   risk's category/objective — do not set a category threshold
   independently of the entity-level appetite statement; tolerance is
   appetite broken down per category/objective, not a second, freestanding
   number.
   source: https://www.wolterskluwer.com/en/expert-insights/risk-appetite-and-risk-tolerance-whats-the-difference
2. When a risk's objective is strategic/business-model-level (e.g.
   market entry), express its threshold in appetite terms (broad,
   qualitative risk-acceptance posture); when the objective is
   operational/day-to-day, express its threshold in tolerance terms
   (a measurable variation band in the objective's own units) — using
   an appetite-style qualitative band for an operational threshold makes
   it unmeasurable against the register's numeric residual score.
   source: https://www.fieldguide.io/resource-articles/what-is-risk-tolerance
3. When multiple risk categories interact (e.g. financial + regulatory
   on the same initiative), set the combined threshold from a portfolio
   view of how the categories cascade, not from summing each category's
   independent threshold — independent per-category thresholds miss
   cascade effects between categories.
   source: https://quantivate.com/developing-risk-appetite-and-tolerances/
4. Removal: when a category-level tolerance threshold was set without
   ever tracing back to an entity-level appetite statement, do not
   carry it forward into the next register cycle — retire it and
   re-derive from the current appetite statement, since an
   un-traceable threshold cannot be checked for staleness against
   subsequent appetite changes.
   source: https://www.wolterskluwer.com/en/expert-insights/risk-appetite-and-risk-tolerance-whats-the-difference
5. When a category's threshold is bound by an external regulatory or
   contractual limit (a specific clause, control ID, or numeric cap in
   a named framework), cite that exact clause/control ID on the
   threshold entry instead of stating only the entity-level appetite
   band it was decomposed from — a threshold traceable only to a
   generic appetite band cannot be checked against the specific
   external requirement that actually constrains it when that
   requirement changes.
