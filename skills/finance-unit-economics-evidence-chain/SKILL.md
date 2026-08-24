---
name: finance-unit-economics-evidence-chain
description: >-
  Use when a unit-economics input, benchmark citation, or headline figure needs
  its sourcing traced, deduplicated, positioned against a peer distribution, or
  checked for a hardcoded value hiding behind a formula-derived one. Trigger on
  requests like "이 벤치마크 출처 확인해줘", "where did this CAC number come from", "audit
  the citations in this financial model", "is this headline figure hardcoded or
  formula-derived". Do NOT use to pick or band the headline metric itself (use
  finance-unit-economics-cac-payback).
metadata:
  axis: evidence-chain
  rule_count_floor: 12
  tier: moderate
---

# Evidence chain — decision rules

## Trigger

Use whenever a unit-economics model, proposal, or benchmark claim needs
its inputs' sourcing checked — an uncited figure, a benchmark pulled
from a secondary source, a stale caveat sitting next to a current
citation, a benchmark cited with no distribution position, or a
headline number whose formula-derived-vs-hardcoded status has not been
verified. This axis underlies every other finance-unit-economics skill
that presents a `source:`-bearing figure; use it to check the citation,
not to produce the metric itself.

## Procedure

1. Cite the 1st ADDITION bullet when a unit-economics input has no
   traceable source, to require a cited report/dataset and date rather
   than a bare number.
2. Cite the 2nd ADDITION bullet when a benchmark is pulled from an
   external report, to prefer the primary/first-party dataset over a
   secondary blog restating it.
3. Cite the REMOVAL bullet when an input already carries a dated source
   citation, to drop a duplicate older "as of" caveat carried over from
   an earlier draft.
4. Cite the 4th ADDITION bullet when citing an external benchmark to
   judge a company's own figure, to state the peer-distribution
   position and measurement period, and to flag any stale prior-period
   input for re-verification.
5. Cite the 5th (final) ADDITION bullet before a model or proposal is
   published, to run an explicit trace pass marking every headline
   figure formula-derived or hardcoded.

## Output shape

A sourcing verdict for each cited input: a dated, traceable citation
(primary preferred over secondary), no duplicate or conflicting
caveats, a stated peer-distribution position and measurement period for
any benchmark comparison, and a formula-derived/hardcoded trace mark
for every headline figure.

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

Every rule in this role spec that carries a `source:` field is itself an
application of this axis — evidence-chain is the role spec's own
practice made explicit as a rule.
