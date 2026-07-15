# Gate Criteria — the objective tests behind each judgment

Every gate in the procedure hides a judgment call. This file gives the researched, objective criterion for each, so the call is transparent and reviewable rather than a matter of taste. Evidence strength is graded:

- **●●●** — first-tier academic source + quantitative (trust it)
- **●●○** — semi-academic or industry standard
- **●○○** — management folklore / unclear origin (use, but know it's soft)

A meta-point worth remembering: the most rigorous criteria here (measurement-systems analysis, the ASA statement on p-values) explicitly warn against judging by a single number. These criteria discipline judgment; they don't replace it.

## Contents

1. G0 — is this the right problem?
2. G0.5 — is analysis the right mode?
3. G1 — is it confirmed in data?
4. G2 — is the cause verified?
5. G2-aux — is this a real signal or noise?
6. G3 — is it time to decide, and how reversible?
7. G5 — did it actually improve?

---

## G0 — "Are we solving the right problem?"

**Problem-statement form (●●○).** Six Sigma practice specifies what a good problem statement includes and excludes. Include 5W2H — what / when / where / how much, plus quantified impact. The critical part is what it must *exclude*: a root-cause guess, a solution, or blame. "It's slow because there's no cache" (cause), "we need to automate this" (solution), and "team A messed up" (blame) all fail the gate.

**Goal statement — SMART (●●○).** Doran's 1981 original: Specific, Measurable, Assignable (note: the original A was *Assignable* — clear ownership — not today's "Achievable"), Realistic, Time-related. McKinsey reworks A into Action-oriented for consulting use.

**Hypothesis falsifiability (●●○).** Popper: a hypothesis no evidence could refute is faith, not analysis. Practical rule — when stating a candidate cause, write down "if this is wrong, what would we observe?" A hypothesis whose disconfirming evidence you can't name doesn't go to the verification stage.

**Metric soundness — Goodhart / Campbell (●●○).** "When a measure becomes a target, it ceases to be a good measure." Under pressure people game the proxy instead of improving the real thing (emergency dispatchers logging false calls to hit response-time targets). Defense: don't tie rewards to a single proxy; pair a leading indicator (early warning) with a lagging one (final confirmation); treat metrics as signals, not targets, and revisit them.

**Pass conditions:** no solution/cause/blame in the statement; a third party could judge success; stakeholders agree; the goal is SMART; hypotheses are falsifiable; the metric isn't a single gameable proxy.

---

## G0.5 — "Is analysis the right mode?" (situation classification)

From Cynefin (Kurtz & Snowden 2003). The classification is qualitative but operational.

**The litmus question:** *would an expert analyzing this reliably produce the answer?*
- Yes, and it's repeatable/predictable → **Obvious**, apply best practice, skip the procedure.
- Yes, but it needs expertise → **Complicated**, run the analysis track.
- No — "we can only tell in retrospect" → **Complex**. This is **retrospective coherence**: cause is coherent looking back but gave no foresight. Switch to safe-to-fail experiments.
- Cause not perceivable, actively failing → **Chaotic**, stabilize first.

**Retrospective coherence is the sharp tool here (●●○):** hindsight ≠ foresight. If you find yourself saying "now that we understand last time's failure, we can just make a rule," and the domain is complex, the rule will generate new failures via unintended consequences.

**4-points contextualisation (workshop method):** rather than classifying by abstract definition, place four of your *own* real cases at the extremes of the four domains, then position new cases relative to them. Ambiguous ones sit in "Disorder" until sub-divided.

**Alternative — Stacey Matrix:** two axes, certainty (can past experience predict cause→effect?) and agreement (does the team concur?). Simpler for a quick workshop; Cynefin is theoretically richer.

**Complex-system markers (no quantitative threshold exists):** emergence, nonlinearity (small change → big result), adaptation, feedback loops, interaction density, path dependence. There is no standard "N markers = complex" rule — hence the escape hatch below.

**Escape hatch:** if the analysis track fails to narrow the cause after two honest attempts, re-classify as complex and switch to experiments. This corrects an initial misclassification from the back end.

---

## G1 — "Is it confirmed in data?"

**Measurement-system trust — MSA / Gage R&R (●●○).** Before trusting the numbers, check the instrument. %GRR (measurement error as a share of total variation) < 10% good, 10–30% conditional, > 30% unusable; number of distinct categories ≥ 5. The AIAG manual itself says these thresholds aren't a mechanical pass/fail — weigh the purpose (pass/fail inspection vs. improvement). The software analogue: does this instrumentation have the resolution to separate signal from noise?

**Performance-measurement rigor (●●●).** One benchmark run is not evidence (JIT/warmup make single runs unreliable — Georges et al., OOPSLA 2007). Rules: enough warmup then multiple independent runs; report confidence intervals, not a single mean; significance-test A vs B before concluding. Report **p95/p99 percentiles**, not averages — perceived quality is set by the worst experiences. Watch for **coordinated omission**: sequential-request benchmark tools drop the requests that would have landed during a stall, hiding the tail latency (one case: p99 measured 249µs, was actually 665ms after correction). Use open-loop, target-throughput measurement with latency correction.

**Pass condition:** the problem is reproduced in data and the baseline is recorded. If measurement doesn't show the problem, return to G0 — the definition is likely wrong.

---

## G2 — "Is the cause verified?" (the most important gate)

Every serious attempt to objectify causal verification converges on four axes. A candidate cause should pass as many as apply.

**Axis 1 — Temporality (●●●).** Cause precedes effect. Of Bradford Hill's nine criteria, this is the only absolute necessity; the other eight (strength, consistency, dose-response, etc.) raise plausibility but are individually defeasible. Hill himself insisted these are a lens for thinking, not a scorecard.

**Axis 2 — Interventional counterfactual (●●●).** The strongest test: "if the cause were absent, would the effect be absent?" — checked by actual intervention. The same logic recurs across fields: Koch's postulates (remove the pathogen → no disease; reintroduce → disease returns), Pearl's do-calculus (distinguishing *seeing* from *doing*), the legal but-for test, A/B tests, and rollback/canary deploys. Practical rule: **write down "if this cause is real, removing/rolling-it-back should change the result thus" in advance, then intervene and compare.** Stating the prediction before the intervention is what promotes correlation to causation.

**Axis 3 — Contrastive explanatory power (●●○).** The real cause explains, in one hypothesis, both where the problem occurs and where it doesn't. Kepner-Tregoe's IS / IS-NOT matrix: a hypothesis that can't account for the near-miss situations that *didn't* fail is rejected. Forces a control comparison, filtering out correlation errors.

**Axis 4 — Necessity stated explicitly — Five Rules of Causation (●●○).** From the VA National Center for Patient Safety, adopted by many hospitals: show cause→effect clearly; use specific descriptors, not "poor/inadequate"; human error must have a preceding cause ("the person made a mistake" is not an endpoint); procedure violations must have a root cause; a "failure to X" claim holds only if there was a pre-existing duty to do X.

**The Amdahl check (●●●):** even a verified cause isn't worth fixing if its share of the whole is small. Compute "removing this improves the total by at most N%." Small N → move to a bigger bottleneck.

**Honest limit:** in complex systems (software outages, industrial accidents) a single "the root cause" usually doesn't exist — failures are the product of "each necessary, but only jointly sufficient" contributors (Cook, Allspaw). The NTSB withholds a probable-cause finding when evidence isn't conclusive (it still issues safety recommendations). The pass condition is not "found the one cause" but "the set of necessary causes is evidenced, and shown jointly sufficient by intervention."

---

## G2-aux — "Is this a real signal or noise?" (statistical gate)

Before attaching a cause to a swing, confirm the swing warrants a response.

**Common vs special cause — Shewhart control chart (●●●).** Split variation into system-inherent randomness (common cause) and identifiable external anomaly (special cause). Control limits are centerline ± 3 sigma; the "3" is an economic balance of investigation cost vs miss cost, not a precise probability (a 3-sigma excursion happens by chance about 1 in 370 points). Deming's **funnel experiment** proved that intervening on every individual result of a stable process — *tampering* — provably increases variation. Evidence-based "don't intervene prematurely."

**Special-cause detection rules (●●○).** Western Electric / Nelson rules make "what counts as a signal" concrete: e.g., 1 point beyond 3σ; 9 consecutive on one side; 6 consecutive trending. More rules = more sensitivity but more false alarms; the tradeoff is quantified, so practice usually uses rules 1–3 only.

**Significance vs effect size (●●●).** Statistically significant ≠ materially meaningful. The ASA's 2016 statement: a p-value doesn't measure effect size or importance; with a big sample, a trivial difference clears p<0.05. Judge effect size separately (Cohen's d: 0.2 small, 0.5 medium, 0.8 large). Pre-compute the minimum data needed from power (conventionally 80%) and minimum detectable effect; don't peek and stop early. Bayesian alternative: grade evidence by Bayes factor (3–10 moderate, 10–30 strong, >100 decisive).

**When to respond, objectified (●●●).** Google SRE error budgets and multi-window multi-burn-rate alerts convert "should we respond?" into the calculable rate at which the error budget is burning; alert only when a long and short window are both exceeded, catching both false alarms and late alerts.

---

## G3 — "Is it time to decide, and how reversible?"

**Value of further analysis — EVPI (●●●).** Whether to keep analyzing is calculable, not a gut call. Expected value of perfect information = (expected value with perfect info) − (current expected value); it's the ceiling on what information is worth. Rule: **gather more only if the cost of doing so is below EVPI.** If EVPI is below the cost of the study, stop analyzing and decide. The theoretical antidote to analysis paralysis.

**Stopping math — 37% rule (●●● as math / ●○○ applied).** For sequential, irreversible choices: observe ~37% (1/e) of options without picking, then take the first that beats everything seen so far. Holds only under strict assumptions (known N, random order, no going back). The looser Powell 40-70 heuristic (act on 40–70% of info) is folklore (●○○). Simon's **satisficing** is the sturdier basis (●●●, Nobel): factoring in the cost of computation, stopping at "good enough" can be the true optimum.

**Decision reversibility (●●○ / ●○○).** Bezos's one-way vs two-way door: the criterion is not absolute reversibility but the *cost of reversal*. Operationalized by later frameworks: estimate the time, money, and opportunity cost of reversing — if all three are small, it's two-way; decompose an apparently one-way decision into checkpointed stages (decision stacking) to make each stage two-way. Large orgs tend to overclassify two-way decisions as one-way and get slow. No standard threshold for "reversal cost" exists yet — it's a qualitative checklist.

**Estimate reliability — reference-class forecasting (●●●).** Whether a Type-1 estimate is trustworthy: replace the inside view (this project's specifics) with the outside view (the actual distribution of similar past projects). Kahneman's concept, Flyvbjerg's method, adopted by the UK Dept for Transport in 2004. Weight of evidence: Flyvbjerg's "iron law" — ~90% of megaprojects overrun. Forecaster calibration is measurable and trainable via Brier score; Tetlock's superforecaster work showed one hour of reference-class training yields accuracy gains lasting at least a year.

**Pre-mortem (●●○).** Before choosing, assume "it's six months later and this failed" and list the causes. Mitchell, Russo & Pennington (1989) reported prospective hindsight raises cause identification ~30% (the figure is widely cited; original design details bear checking). Gate discipline: if sunk cost enters the argument ("we've come this far"), that's a violation.

---

## G5 — "Did it actually improve?"

Re-measurement uses the same statistical discipline as G1 — same metric, same method, effect-size gate passed, no coordinated-omission trap. Then branch: improved but short of target → the constraint has moved (Theory of Constraints stage 5: beware inertia), return to Stage 1; no improvement → the G2 cause was wrong, widen candidates and redo Stage 2.