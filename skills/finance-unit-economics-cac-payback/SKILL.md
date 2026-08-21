---
name: finance-unit-economics-cac-payback
description: Use when a proposal or model needs a CAC payback headline metric picked, banded by motion, kept isolated from overhead, or jointly checked against gross margin and burn multiple before it is called healthy.
axis: cac-payback
rule_count_floor: 12
tier: moderate
---

# CAC payback — decision rules

## Trigger

Use when a unit-economics proposal or model is choosing or presenting
its headline efficiency metric — deciding between CAC payback and
LTV:CAC, banding a payback figure against a benchmark, isolating the
payback calculation from overhead, or declaring a business "healthy" on
the strength of a payback number. Do not use it to compute LTV:CAC
magnitude itself (that is `finance-unit-economics-ltv-cac-band`) or to
source/cite the inputs feeding the payback figure (that is
`finance-unit-economics-evidence-chain`).

## Procedure

1. Cite the 1st ADDITION bullet when blended CAC payback is under 12
   months, to prefer payback over LTV:CAC as the headline board-facing
   efficiency metric.
2. Cite the 2nd ADDITION bullet when the motion is SMB self-serve
   (sub-$15K ACV), to apply the segment-specific 8-12 month band rather
   than a flat threshold.
3. Cite the REMOVAL bullet when the payback calculation already
   isolates variable acquisition cost, to drop fully-loaded overhead
   allocation from the same headline number.
4. Cite the 4th (final ADDITION) bullet before calling the unit
   economics "healthy" on a cleared payback figure alone, to check it
   jointly against gross margin and burn multiple and state explicitly
   which of the three did not clear when only some do.

## Output shape

A CAC payback verdict: the chosen headline metric (payback vs.
LTV:CAC) with its rationale, a segment-appropriate band applied to the
payback figure, a payback number isolated to variable acquisition cost,
and — when "healthy" is claimed — an explicit joint check against gross
margin and burn multiple naming which of the three metrics did and did
not clear.

## Decision rules

- **ADDITION**: when a proposal's blended CAC payback period is under 12
  months, prefer payback period over LTV:CAC as the headline efficiency
  metric — payback is grounded in realized cash recovery rather than
  projected lifetime value, so use it for near-term board-facing
  decisions. source: Bessemer 2026 efficiency bar summarized in
  https://foundrycro.com/blog/cac-payback-benchmarks-2026/ (median
  payback rose to 18 months in 2026, healthy bar remains <=12 months).

- **ADDITION**: for an SMB self-serve motion (sub-$15K ACV), apply the
  8-12 month payback band as the pass/fail threshold rather than a
  single flat number — segment-specific bands avoid penalizing
  self-serve deals for structurally faster payback than enterprise.
  source: https://foundrycro.com/blog/cac-payback-benchmarks-2026/
  (SMB 8-12mo, mid-market 14-18mo, enterprise 18-24mo+ bands).

- **REMOVAL**: when a payback calculation already isolates variable
  acquisition cost, drop fully-loaded overhead allocation from the same
  headline number — mixing the two collapses a decision-grade cash
  metric back into an accounting metric and defeats the reason payback
  was chosen over LTV:CAC in the first place. source:
  https://foundrycro.com/blog/cac-payback-benchmarks-2026/ (payback is
  framed against real cash, not projections, precisely because it
  excludes projection-only inputs).

- **ADDITION**: when a payback figure clears its band, do not call the
  unit economics healthy on that basis alone — check it jointly against
  gross margin and burn multiple (net new spend / net new ARR) in the
  same verdict, since a payback figure can clear its band while the
  business is bleeding cash on gross margin or overall burn efficiency;
  require all three to clear together before using the word "healthy,"
  and state explicitly which of the three did not clear when only some
  do.

## Notes

Payback and LTV:CAC measure different things — speed vs. magnitude —
and neither substitutes for the other; see ltv-cac-band.md for the
magnitude-side rules.
