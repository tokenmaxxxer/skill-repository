---
name: finance-unit-economics-ltv-cac-band
description: Use when an LTV:CAC ratio needs a motion-specific CAC band, an investor-facing framing that avoids overstating the 3:1 bar, a normalized per-cohort LTV input, or a healthy/watch/critical verdict scoped to the company's segment.
metadata:
  axis: ltv-cac-band
  rule_count_floor: 12
  tier: moderate
---

# LTV:CAC band — decision rules

## Trigger

Use when computing, presenting, or verdicting an LTV:CAC ratio —
choosing the CAC band to compare against, framing the 3:1 ratio for an
investor audience, deciding whether the Magic Number belongs alongside
it, normalizing the LTV input feeding the ratio, or scoring the final
verdict. Do not use it to compute payback speed (that is
`finance-unit-economics-cac-payback`) or the LTV churn assumption
itself (that is `finance-unit-economics-ltv-churn-assumption`).

## Procedure

1. Cite the 1st ADDITION bullet when the company's motion is
   PLG/self-service, to target the motion-specific CAC band instead of
   a blended company-wide average.
2. Cite the 2nd ADDITION bullet when making an investor-facing
   efficiency claim, to cite the 3:1 ratio only alongside the fact that
   just 44% of SaaS companies clear it.
3. Cite the REMOVAL bullet when both LTV:CAC and payback already clear
   their bar, to cut the Magic Number from the same headline table.
4. Cite the 4th ADDITION bullet when the LTV input feeding the ratio is
   computed, to normalize it to a fixed time-window and compute it per
   cohort/channel before blending.
5. Cite the 5th (final) ADDITION bullet before scoring an LTV:CAC
   verdict, to confirm the target segment/stage and report the verdict
   as healthy, watch, or critical rather than binary pass/fail.

## Output shape

An LTV:CAC verdict: a motion-appropriate CAC band, an investor-facing
ratio framed with its peer-clearance rate, a headline table without a
redundant Magic Number when payback and ratio both clear, a
cohort/channel-normalized LTV input, and an explicit healthy/watch/
critical verdict scoped to the confirmed segment.

## Decision rules

- **ADDITION**: when a company's motion is PLG/self-service, target a
  CAC band near $420 rather than applying a blended-company average —
  use the motion-specific band (self-serve ~$420, mid-market/blended
  ~$1,680, enterprise sales-led ~$9,400) instead of one company-wide
  CAC target. source: https://saasgoodies.com/saas-cac-ltv-statistics/
  (2026 CAC-by-motion benchmarks).

- **ADDITION**: for an investor-facing efficiency claim, cite the 3:1
  LTV:CAC ratio only alongside the fact that just 44% of SaaS companies
  clear it — presenting 3:1 as a norm rather than a top-quartile bar
  overstates how common it is. source:
  https://www.saashero.net/strategy/b2b-saas-ltv-cac-ratio/ (44% of
  SaaS companies hit the textbook 3:1 ratio).

- **REMOVAL**: when LTV:CAC and payback both clear their bar, cut the
  Magic Number from the same headline table instead of adding it — a
  healthy payback+ratio pair already establishes efficiency,
  and stacking a third redundant metric under a 0.6 median benchmark
  invites the wrong comparison for a company whose growth stage doesn't
  match the Magic Number's assumptions. source:
  https://www.digitalapplied.com/blog/saas-unit-economics-2026-cac-ltv-payback-reference
  (Magic Number median fell below 0.6 for early/mid-stage SaaS in 2026).

- **ADDITION**: when the LTV input feeding the ratio is computed,
  require it to be normalized to a fixed time-window since acquisition
  (e.g. Day-90 or Day-365 cumulative value) rather than cumulative-to-
  date revenue, and computed per cohort/acquisition-channel before it
  is blended into one number — a to-date figure structurally favors
  older cohorts, and a blended figure can hide an unprofitable channel
  behind a profitable one; when only a single cohort/channel exists,
  the segmentation requirement is satisfied vacuously, not skipped.

- **ADDITION**: before scoring an LTV:CAC verdict, confirm and record
  which target segment/stage the company's motion actually is
  (self-serve/PLG, mid-market, or enterprise sales-led), and report the
  verdict as one of three explicit states — healthy, watch, or critical
  — rather than a binary pass/fail; a ratio that looks weak against a
  blended-market benchmark can be a normal watch-tier reading for an
  early-stage self-serve motion, and collapsing that into pass/fail
  loses the distinction a reader needs to act on.

## Notes

LTV:CAC is a magnitude metric, not a speed metric — see cac-payback.md
for the speed-side complement; a proposal that cites only one of the
two is incomplete per finance-proposal-shape.md.
