---
name: experiment-trust
description: >-
  Trustworthiness gates for online controlled experiments (A/B tests): validate the experimentation
  setup and data quality BEFORE anyone interprets the result. Checks Sample Ratio Mismatch (SRM)
  via chi-square, platform A/A validation status, pre-committed design, and Twyman's-law skepticism
  on anomalous wins. Use whenever someone is about to trust, report, or act on an A/B experiment
  result — e.g. "A/B 테스트 결과 믿어도 돼?", "실험 결과 해석해줘", "can we trust this experiment", "check this
  experiment for SRM", "is our A/B testing platform reliable". Trigger BEFORE interpreting any
  variant-comparison result, especially a big win about to drive a launch decision. Companion to
  `usability-eval` (study design) and `hypothesis-testing` (decision rule). Do NOT use for
  designing a NEW experiment (route to `usability-eval` or `hypothesis-testing`), for an
  observational comparison with no random assignment, or for a qualitative usability question with
  no metric contrast.
---

# Experiment Trust

## First: does this even need the procedure?

Run this gate before touching any chi-square test or A/A record — the whole point of this skill is
to sit between "an experiment produced a number" and "someone acts on that number," and applying it
where there is no real experiment, or where the result is already settled, just produces theater.

- **Is this actually an ONLINE CONTROLLED EXPERIMENT?** Random assignment of units (users, sessions,
  devices) to two or more variants, with enough traffic to measure the target metric. If assignment
  was not random — a before/after comparison, a self-selected cohort, a regional rollout used as a
  proxy — this is an observational comparison, not an A/B test. Say so explicitly and stop; do not
  run SRM or A/A checks on data that was never randomized.
- **Is the question a metric contrast, or a qualitative usability question?** "Did conversion go up"
  is this skill. "Do users understand this flow" has no variant-count denominator to check for
  mismatch — route to `usability-eval` instead.
- **Is a design decision (sample size, metric, threshold) still open?** If nobody has written the
  metric and decision rule yet, this skill is the wrong entry point — route to `hypothesis-testing`
  first to pre-register the decision rule, then come back here to validate the run itself.
- **Has the result already been fully vetted and reported?** If SRM was already checked, the platform
  is already A/A-validated, and the verdict already cites registered thresholds vs. measured numbers,
  there is nothing left to gate — this skill exists to run those checks once, not to re-litigate a
  clean, already-reported result.

Everything below applies only once: assignment was genuinely random, there is a real control, and a
metric result exists (or is about to exist) that someone intends to interpret or act on.

## Evidence grade — read before citing this to anyone

Three lines of honesty, stated every time this skill is invoked:

- **(a) Confirmed, from primary industry-research sources (KDD / Microsoft experimentation-platform
  papers)** — real measured platform data, not RCT evidence about experimentation as a practice: SRM's
  definition, its chi-square detection method with the verified concrete examples below, its
  invalidating consequence for causal inference, and its measured platform prevalence.
- **(b) Confirmed, prescribed procedure with a checkable numeric criterion, same lineage**: the A/A
  test validation method and its ~5% false-positive-rate criterion.
- **(c) NEVER EXAMINED — a coverage gap, not a negative finding**: sample-size / power-analysis
  specifics, and the peeking (early-stopping) type-I-error-inflation literature. These were not
  refuted; no verifier ever voted on them (the research round extracted 99 claims and verified 25, so
  the remainder was never adjudicated). Do not report them as unsupported. The gates below still
  REQUIRE a pre-committed sample size and a no-peeking rule — that is a procedural design choice
  consistent with the verified A/A false-positive semantics (a fixed nominal α presumes a fixed
  horizon), not a claim this skill's research checked. For the pre-registration discipline itself — metric, threshold, decision
  rule, date-stamped before the run — route to `hypothesis-testing`; do not re-derive it here.

Additionally, at medium grade (2-1 vote each, name the grade when citing): Twyman's law as a
skepticism heuristic for anomalous results, and the base-rate reminder that most experiments do not
produce a positive significant effect.

**MUST NOT claim**: that chi-square (with KS / Anderson-Darling) is "the industry-standard
randomization-validation method used at Google, Microsoft and LinkedIn" — that broader industry-wide
framing was refuted. Chi-square for SRM specifically is confirmed via the examples in Step 4; the
broader attribution is not. No invented statistics beyond what is listed in this file.

## Procedure

### Step 1 — Scope gate

Confirm: random assignment to variants, a real control, enough traffic to measure the target metric.

**Gate (per-condition yes/no)**:
- Random assignment? If no → this is an observational comparison; say so and stop, do not proceed.
- Real control group? If no → stop, same reason.
- Metric-contrast question (not qualitative usability)? If no → route to `usability-eval`.
- Traffic horizon: does a pre-committed sample size / duration exist, and did the run reach it? If no
  → not gateable here; route to `hypothesis-testing` to register the horizon *before* any
  interpretation. (Power-analysis specifics are grade (c) below — the horizon must be *committed*,
  which is checkable; this skill does not adjudicate whether the number was correctly derived.)

Only continue if all four are yes.

### Step 2 — Platform validation (A/A check)

Before trusting ANY experiment run on this platform, has an A/A validation been performed?

Verified criterion: if the experimentation system operates correctly, comparing IDENTICAL variants
should reach statistical significance only ~5% of the time — the false-positive rate implied by a
nominal α. The prescribed procedure is running on the order of 1,000 A/A tests and checking that the
resulting p-value distribution is uniform. This is not cosmetic: Kohavi reports this exact check
caught real bugs in Skype metrics that had to be corrected.

**Gate**: exactly one of three states must be named explicitly in the report — existence of a record is
not enough; its *values* decide —
1. **Validated** — a record exists AND its observed false-positive rate is consistent with ~5% AND its
   p-value distribution is uniform.
2. **Failed validation** — a record exists but fails either check (e.g. a 30% observed false-positive
   rate, or a visibly non-uniform p-value distribution) → **"platform failed A/A validation — no result
   from this platform is interpretable until the defect is found and the platform re-validated."**
   Treat this as a hard stop of the same class as Step 4; this is precisely the state that surfaced the
   Skype metric bugs.
3. **Unvalidated** — no record exists → flag **"platform unvalidated — results carry unknown
   false-positive rate."**

Never silently assume the platform is sound because no one raised a concern.

### Step 3 — Pre-commit design (cross-reference `hypothesis-testing`)

Confirm sample size / duration, the primary metric, and the decision rule were written down and
date-stamped BEFORE the run started. This skill does not re-derive the registration form —
`hypothesis-testing` Step 4 owns that content.

**Gate**: all of sample size/duration, primary metric, and decision rule are present and dated before
the run's start date. The no-peeking rule is recorded as an explicit commitment: no decision on the
primary metric before the pre-committed horizon. If the team wants interim looks, they must name a
specific sequential method in advance — this skill does not bless ad-hoc peeking, and "we looked
early but only decided at the end" does not pass this gate if the look influenced any action.

### Step 4 — SRM gate (the hard, numeric one — run BEFORE looking at any result metric)

Compute the chi-square test of observed vs. expected variant counts.

**Gate**: state side by side — the expected split, the observed counts, and the chi-square p-value.
If SRM is detected, **STOP**: the result is not interpretable. Investigate the assignment/logging
pipeline before doing anything else. Do not report "the treatment won/lost" from an SRM-flagged run
under any circumstance, regardless of how compelling the metric movement looks.

Reference points to calibrate judgment, not to be reused as this run's numbers:
- A split that "looks fine" on its face can still be a real SRM: 821,588 vs. 815,482 users (50.2% /
  49.8% against a designed 50.0% / 50.0%) yields chi-square p = 1.8e-6 — a split that extreme would
  occur by chance less than 1 in 500,000 times. Kohavi reports SRMs of this kind are detected "every
  week" at Microsoft.
- A more visibly broken case: an expected 50/50 split instead producing an observed ratio of 2/3
  (2,108 test vs. 3,183 control triggered users out of 10,000 total).
- Prevalence, so a flagged run is not treated as a freak occurrence: ~6% of experiments at Microsoft
  exhibit an SRM (varies by product); ~10% of triggered analyses at LinkedIn (per cited prior work).
  At scale, a product running 10,000 experiments/year can expect at least one SRM per day.

### Step 5 — Result interpretation with Twyman's law (medium grade)

An anomalous or too-good-to-be-true effect is treated as a suspected instrumentation error until an
independent check clears it — not celebrated on sight.

**Gate**: any effect size that would be a record-breaker for the product must be accompanied by at
least one named independent validation (a logging cross-check, a segment-consistency check, or a
re-run) before it is reported as real. No named independent check → the effect is reported as
"unconfirmed, pending validation," not as a result.

### Step 6 — Report

Assemble the report at the depth the decision warrants. Every item below must appear; the difference is in the verbosity:

- **Launch-blocking / high-stakes**: full detail — every deviation individually named, SRM with split+counts+p-value, platform status with false-positive rate, effect with CI, base-rate reminder cited with grade.
- **Directional / internal check**: condensed — SRM pass/fail with p-value only (counts summarized), platform status as validated/unvalidated (rate only when relevant), effect with CI, base-rate reminder as one-line note. Deviations grouped by type rather than individually named.

Required in all reports:
- Pre-committed design vs. what actually ran, with deviations accounted for (individually or grouped by type per depth level above).
- The SRM verdict, with its expected split, observed counts, and p-value stated side by side (Step 4).
- The A/A platform status: validated, failed validation, or unvalidated (Step 2).
- The effect, with its confidence interval — **only if Step 4 passed**. An SRM-flagged run's report contains no effect estimate, no confidence interval, and no direction: only the SRM verdict and the pipeline-investigation status.
- The base-rate reminder: most product ideas do not produce a positive significant effect, and a flat result is the norm, not a failure of execution.

## Verdict

Report, per experiment reviewed:

- Step 1: scope gate result (proceed / routed elsewhere, with reason).
- Step 2: A/A platform status — validated (rate + distribution check) or flagged unvalidated.
- Step 3: pre-commit design fields present and dated, or gate violation named.
- Step 4: SRM verdict — expected split, observed counts, chi-square p-value, pass/fail, and STOP if
  failed.
- Step 5: Twyman's-law check — named independent validation, or "unconfirmed, pending validation."
- Step 6: full report as specified above.

Never report a treatment win or loss from a run that failed Step 4, and never report a platform as
trustworthy by default when Step 2 found no A/A record.
