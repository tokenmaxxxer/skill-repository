---
name: reference-forecast
description: >-
  Use whenever someone needs to build or audit a duration, cost, or effort estimate and comparable
  completed cases exist: correct the forecast by anchoring it to the measured outcome distribution
  of comparable past projects (the external view) instead of building the number up from the
  case's own components. Trigger on requests like "이거 얼마나 걸릴까", "일정 추정해줘", "예산 얼마나 잡아야 해", "how
  long will this actually take", "sanity-check our schedule estimate", "correct for optimism
  bias", "reference class forecasting" — whenever a quantitative forecast is about to be built
  bottom-up, or an existing bottom-up estimate needs auditing against outside evidence. Do NOT use
  for one-of-a-kind work with no comparable case (state the internal estimate as uncorrected), for
  trivial tasks where estimation overhead exceeds the stake, for qualitative calls with no
  quantitative forecast, or for infrastructure demand forecasting (use capacity-planning-demand-
  shape-and-forecast-method).
---

# Reference Class Forecasting

## First: does this even need the procedure?

Run this gate before writing any estimate — the whole point of this skill is external correction, and forcing it onto forecasts with nothing to correct against just produces a fake distribution dressed up as data.

- **Is there an actual quantitative forecast to make or audit** — a duration, a cost, or an effort figure — as opposed to a qualitative judgment call? If nothing numeric is being predicted, this skill does not apply.
- **Do comparable completed cases plausibly exist?** If the work is genuinely one-of-a-kind (a first-of-its-kind technology, a rare project type like a novel nuclear plant, a small organization with no history of similar work), no reference class can be built. Exit: deliver the internal estimate, but flag it explicitly as **uncorrected and low-reliability** — state this limit honestly rather than inventing a class.
- **Is the stake big enough to justify the overhead?** For trivial small tasks, the cost of building a reference class exceeds the value of correcting the estimate. Exit and just estimate directly.

Everything below applies only once a genuine quantitative forecast is on the table and comparable cases plausibly exist.

## Evidence grade

70 years of project estimates showed no accuracy improvement (Flyvbjerg et al.; 258→2,062 infrastructure projects). One confirmed institutional adoption (UK transport, since 2004). Not RCT-validated; representativeness debate is live and disclosed. Full evidence base in `references/evidence.md`.

## Procedure

### Step 1 — Scope gate

Confirm: is there a quantitative forecast to make or audit (duration, cost, or effort), and do comparable completed cases plausibly exist?

**Gate**: if the work is genuinely one-of-a-kind with no conceivable reference class, exit — deliver the internal estimate flagged explicitly as uncorrected and low-reliability, stating the rare-project limit honestly. If the task is trivial, exit — estimation overhead exceeds the stake. Only continue if a real forecast is on the table and a class plausibly exists.

### Step 2 — Internal estimate first, recorded

Write down the team's own bottom-up estimate **before** looking at any reference-class data, with a date stamp. This mirrors the original Kahneman & Tversky step order and keeps the internal and external estimates independent so they can actually be compared — if reference data contaminates the internal estimate before it's written, there is nothing left to correct.

**Gate**: a written internal estimate exists, dated, and its date precedes the start of Step 3. An internal estimate written or revised after reference data has been seen fails this gate and must be redone or flagged as contaminated.

### Step 3 — Reference class definition (the externalized judgment)

Write the inclusion/exclusion criteria — project type, size band, technology novelty, team/organizational context — **before** querying for class members. Then enumerate the actual class members with their real outcomes. Pre-commit the minimum class size required to proceed; the user sets this floor and writes it down (this skill does not impose a universal N).

**Gate**: written criteria precede the member list. The member count is stated explicitly. If the count is below the pre-committed floor, **stop** — fall back to Step 1's flagged, uncorrected internal estimate. Do not fabricate a distribution from too few cases.

### Step 4 — Outcome distribution

Compute the class's outcome ratios (actual ÷ estimated), at minimum the median and a spread measure, plus percentiles if the class is large enough to support them. Every member's numbers must cite a source.

**Gate**: a distribution table exists; every row has a cited source; no member is silently dropped — any exclusion carries a written reason tied back to the Step 3 criteria.

### Step 5 — Position and correct

Pre-commit the risk-tolerance percentile **before** seeing where the internal estimate falls on the distribution (e.g., budget to the 50th percentile vs. the 80th — matching the UK uplift practice). Then locate the internal estimate against the distribution and apply the implied uplift.

**Gate**: the percentile choice is recorded before the comparison is made. The corrected forecast shows its arithmetic explicitly (internal estimate × uplift = corrected forecast) — no unexplained final number.

### Step 6 — Report

Compile: the internal estimate, the class definition and size, the distribution, the chosen percentile, the corrected forecast, and a residual list — what the correction does **not** cover (scope changes after the decision point, the irreducible class-selection judgment call, and the open debate over cause attribution).

**Gate**: all six elements are present; the residual list is non-empty and specific, not a generic disclaimer.

## Report format

Classify the stakes before reporting depth. Write the classification in the report so it's auditable.

**High-stakes** (budget commitment, contract bid, public deadline): full report with all six steps — scope gate result, internal estimate with date stamp, written criteria with member count and floor check, sourced distribution table with justified exclusions, pre-committed percentile with uplift arithmetic shown, and residual list. Include the evidence-grade limits restated briefly: observational data with a disclosed representativeness debate, one confirmed institutional adoption (UK transport since 2004), not RCT-validated.

**Directional / internal planning**: corrected number + distribution + class description only. Report the corrected forecast with the uplift arithmetic, the distribution's median and spread, and the class name and size. Omit the full member list and the percentile-negotiation transcript. The full trace is kept in the registration form; the directional report does not reprint it.

If stakes are unclear, default to full reporting.
