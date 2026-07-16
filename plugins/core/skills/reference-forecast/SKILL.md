---
name: reference-forecast
description: >-
  Correct schedule/cost/effort forecasts by anchoring them to the measured outcome distribution
  of comparable past projects (the external approach) instead of building the number up from the
  case's own components (the internal approach). Use this whenever someone needs to produce or
  audit a duration, cost, or effort estimate and comparable completed cases plausibly exist — e.g.
  "이거 얼마나 걸릴까", "일정 추정해줘", "예산 얼마나 잡아야 해", "우리 추정이 맞는지 점검해줘", "낙관 편향 보정", "how long will
  this actually take", "estimate the budget for this project", "sanity-check our schedule
  estimate", "correct for optimism bias", "reference class forecasting". Trigger it whenever a
  quantitative forecast is about to be built bottom-up from task breakdowns, or an existing
  bottom-up estimate needs auditing against outside evidence. Do NOT use it for one-of-a-kind work
  with no conceivable comparable case (state the internal estimate as uncorrected instead), for
  trivial small tasks where estimation overhead exceeds the stake, or for qualitative
  prioritization/preference calls with no quantitative forecast at their center (route those
  elsewhere).
---

# Reference Class Forecasting

## First: does this even need the procedure?

Run this gate before writing any estimate — the whole point of this skill is external correction, and forcing it onto forecasts with nothing to correct against just produces a fake distribution dressed up as data.

- **Is there an actual quantitative forecast to make or audit** — a duration, a cost, or an effort figure — as opposed to a qualitative judgment call? If nothing numeric is being predicted, this skill does not apply.
- **Do comparable completed cases plausibly exist?** If the work is genuinely one-of-a-kind (a first-of-its-kind technology, a rare project type like a novel nuclear plant, a small organization with no history of similar work), no reference class can be built. Exit: deliver the internal estimate, but flag it explicitly as **uncorrected and low-reliability** — state this limit honestly rather than inventing a class.
- **Is the stake big enough to justify the overhead?** For trivial small tasks, the cost of building a reference class exceeds the value of correcting the estimate. Exit and just estimate directly.

Everything below applies only once a genuine quantitative forecast is on the table and comparable cases plausibly exist.

## Evidence grade — read before citing this to anyone

- **Theoretical origin — CONFIRMED**: Kahneman & Tversky, "Intuitive Prediction: Biases and Corrective Procedures" (1977 DTIC report, published 1979). The original distinction is between the **"internal approach"** (building the estimate from the case's own components) and the **"external approach"** (treating the case as one member of a class of similar cases and using the distribution of those cases' outcomes). The now-common labels "inside view / outside view" do **NOT** appear in the 1979 paper — that naming came later, from Lovallo & Kahneman (2003). A claim attributing the "inside/outside view" terms to the 1979 paper was checked and refuted in our verification; use "internal approach" and "external approach" for the original work. The original corrective procedure has **five steps**: (1) select a reference class; (2) obtain the class's outcome distribution; (3) make an intuitive/internal estimate; (4) assess the internal estimate's predictability; (5) correct the internal estimate toward the class mean.
- **Operationalization — CONFIRMED**: Flyvbjerg (2006, "From Nobel Prize to Project Management," *Project Management Journal* 37(3)) compressed this into three practical steps: (1) identify a reference class of past, similar projects — broad enough to be statistically meaningful, narrow enough to be genuinely comparable; (2) establish the class's outcome probability distribution from reliable empirical data on enough projects; (3) compare the project at hand with that distribution to derive the most likely outcome. Flyvbjerg's stated mechanism: anchoring the forecast to the actual performance of comparable projects bypasses **both** optimism bias (a cognitive error) **and** strategic misrepresentation (deliberate underestimation to win approval) — the method targets a cognitive problem and a political problem with the same correction.
- **Empirical base — CONFIRMED**: Flyvbjerg, Holm & Buhl (2002/2003) — 258 transport infrastructure projects, 20 countries, ~$90B (1995 prices); the first statistically significant study of cost performance in this domain. Average cost overruns: rail 45% (SD=38), bridges/tunnels 34% (SD=62), roads 20% (SD=30). Across the 70 years the dataset covers, estimation accuracy did **not** improve over time — the bias is structural, not a transient skill gap. The UK road-sector reference distribution was built from 172 completed road projects.
- **Institutional adoption — CONFIRMED, UK only**: HM Treasury's 2003 Green Book revision officially recognized systematic appraiser optimism and recommended data-based adjustment. In summer 2004 the UK Department for Transport and HM Treasury adopted reference class forecasting (as "optimism-bias uplifts") for major transport project appraisal, made mandatory for local authorities applying for transport funding from August 2004 — confirmed against the UK government's own "Supplementary Green Book Guidance: Optimism Bias" document. **Denmark's adoption was NOT confirmed** — do not assert it, and do not assert adoption elsewhere without a similarly confirmed primary source.
- **Data-quality debate — state both sides**: Love & Ahiaga-Dagbui (2018) criticized the dataset, arguing ~383 projects were needed for representativeness. Flyvbjerg et al. (2018, *Transportation Research Part A*) rebutted that once statistical significance is established (p<.05, main results p<.001), sample size is not the live issue. The dataset has since grown: 258 → 806 (Cantarelli et al. 2012a) → 2,062 (Flyvbjerg 2016). The genuinely contested points are the measurement baseline (decision-to-build vs. contract price) and cause attribution (deception vs. legitimate scope change) — the 70-year no-improvement time series itself has not been rebutted. Also disclose the **self-reference risk**: most of the empirical base originates from Flyvbjerg's own research group; it is cross-confirmed here only via UK government primary documents and independent journals, not by fully independent replication of the dataset itself.
- **Procedural limits — these drive the gate design below**: reference-class selection involves irreducible judgment (the "reference class problem" — which past projects belong is a managerial call, confirmed as a live issue in a 2025 peer-reviewed review). Rare project types or small organizations may lack enough comparable cases to build any distribution at all. This is why Step 3 below is a **judgment gate that must be externalized in writing**, with a pre-committed minimum class size as an entry condition, not an afterthought.
- **What this is NOT**: this is not RCT evidence that using reference class forecasting improves forecasting outcomes versus not using it. It is (a) a theoretical procedure from peer-reviewed judgment-and-decision-making research, plus (b) large-scale observational outcome data with a genuine, disclosed academic debate about representativeness and measurement baseline, plus (c) one confirmed instance of mandatory institutional adoption (UK transport, since 2004). The one robust, unrebuked fact worth leading with: **70 years of project estimates showed no accuracy improvement** — waiting for estimators to get better is not a plan; correcting with outside outcome data is.
- **MUST NOT appear when this skill is used**: "inside view/outside view" attributed to the 1979 paper; Denmark or any other non-UK adoption presented as confirmed; overrun percentages beyond the ones listed above; any claim that reference class forecasting is RCT-validated.

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

Report, per forecast:

- Step 1: scope gate result (proceed / exited with reason).
- Step 2: internal estimate with its date stamp.
- Step 3: written inclusion/exclusion criteria, member count, and whether it met the pre-committed floor (if not, the fallback taken).
- Step 4: the distribution table (median, spread, percentiles if available), each row sourced, exclusions justified.
- Step 5: the pre-committed percentile, and the corrected forecast with the uplift arithmetic shown.
- Step 6: the residual list of what the correction does not cover.
- The evidence-grade limits from above, restated briefly: observational data with a disclosed representativeness debate, one confirmed institutional adoption (UK transport since 2004), not RCT-validated.

Never compress this into a bare corrected number — the whole point of reference class forecasting is that the correction is traceable to a named class, a sourced distribution, and a percentile chosen before the comparison, not reverse-engineered to justify a number someone already wanted.
