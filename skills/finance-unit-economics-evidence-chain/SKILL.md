---
name: finance-unit-economics-evidence-chain
description: Use when you need guidance on Evidence chain — decision rules. Applies to the evidence-chain axis.
axis: evidence-chain
rule_count_floor: 12
tier: moderate
---

# Evidence chain — decision rules

## Decision rules

- **ADDITION**: when a unit-economics input (CAC, churn, gross margin)
  has no traceable source, cite the specific report/dataset and date it
  came from rather than presenting it as a bare number — an uncited
  number in a finance model is unfalsifiable and cannot be re-checked
  when benchmarks move, as they visibly did between 2023 and 2026 (CAC
  payback moved from 14 to 18 months in that window). source:
  https://foundrycro.com/blog/cac-payback-benchmarks-2026/ (benchmark
  drift documented year over year).

- **ADDITION**: for a benchmark pulled from an external report, prefer a
  primary or first-party dataset (e.g. an aggregator's own survey data)
  over a secondary blog restating another site's numbers — chained
  citations degrade the number's traceability with every hop. source:
  https://www.nature.com/articles/s41586-021-03380-y (methodological
  standard: claims traced to the study that generated the data, not a
  restatement).

- **REMOVAL**: when a model's input already has a dated source citation
  attached, drop a duplicate "as of [older date]" caveat carried over
  from an earlier draft — an outdated caveat next to a current citation
  creates two conflicting dates for the same number instead of one
  authoritative one. source:
  https://gc-bs.org/articles/the-impact-of-cognitive-load-on-decision-making-efficiency/
  (conflicting or redundant information increases cognitive load and
  degrades decision quality — extraneous load from stale content is a
  design defect, not neutral filler).

- **ADDITION**: when citing an external benchmark to judge a company's
  own figure, state where in the peer distribution the company sits
  (e.g. median, top-quartile) and the period the benchmark was measured
  over — a single-cutoff citation with no distribution position is not
  enough, since the same cutoff can mean "median" in one dataset and
  "top-quartile" in another, and benchmarks shift year to year; also
  flag any input carried forward from a prior period's plan as stale,
  and re-verify it, once actuals have moved materially away from that
  plan.

- **ADDITION**: before a unit-economics model or proposal is published,
  run an explicit trace pass over every headline figure and mark each
  one as formula-derived (linked to a live input) or hardcoded — a
  hardcoded number sitting where a live-linked one is expected passes
  every other evidence-chain check while silently going stale the
  moment its upstream input changes, and this failure mode is
  invisible unless it is checked for directly rather than assumed away
  by the sourcing rules above.

## Notes

Every rule in this rulebook that carries a `source:` field is itself an
application of this axis — evidence-chain is the rulebook's own
practice made explicit as a rule.
