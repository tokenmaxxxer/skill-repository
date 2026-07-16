---
name: usability-eval
description: >-
  A design-and-analysis harness for evaluative UX research and product experiments: it designs
  the right test (formative usability, benchmark, heuristic eval, A/B) with correct sample sizes,
  then analyzes results with proper statistics — standardized scales, task-success confidence
  intervals, and honest significance. Use whenever the user wants to check whether an existing
  design/feature actually works — "사용성 테스트 설계해줘", "usability test for this flow", "how many
  users do I need to test", "analyze these usability findings", "is this SUS/task-success score
  good", "design an A/B test", "run a heuristic evaluation", "accessibility check", "did this
  change actually improve things". Trigger it when someone is judging a built thing by opinion or
  a too-small/too-large sample. Do NOT use for discovering unmet needs before building
  (user-discovery), market/competitor research (market-recon), or internal performance debugging
  (diagnose-first).
---

# Usability Eval — a design & analysis harness for evaluative research

You can't recruit the users yourself — but you can design the evaluation so its verdict is trustworthy, and analyze the results so "better" means better, not noise. The failure mode this prevents: shipping on a designer's confidence, or on a test whose sample was wrong for the question — five users to compare two conversion rates (hopeless), or forty to find obvious layout bugs (wasteful).

## First: is this the right harness, and which test?

- Discovering needs *before* building → `user-discovery`. Sizing a market → `market-recon`. Debugging why the system is slow → `diagnose-first`.
- The pivotal split that sets everything else: **finding problems (formative)** vs **measuring/comparing numbers (summative/benchmark/A-B)**. They need completely different sample sizes, and misapplying the "5 users" rule to a metric comparison is the single most common error in this field. Name which you're doing first.

## The one rule that carries the most weight

**Match the sample to the question, because they diverge by an order of magnitude.** Finding usability problems: small iterative rounds (~5 users catch most *surface* problems in a homogeneous flow) — but that number is a cost-benefit heuristic, not a guarantee, and it collapses for open-ended tasks, heterogeneous users, or low-frequency problems. Comparing metrics (success rate, conversion, satisfaction): you need enough power to detect the effect — roughly ~40 for a binary metric at typical precision, more for tight bounds — and you compute it up front, don't peek and stop early. Using the wrong regime doesn't just waste effort; it produces confident wrong conclusions.

## Designing the evaluation

Pick the method by the question:

- **Formative usability test** — where does the design break? 5-8 users per round, iterate. Use **think-aloud**: concurrent captures in-the-moment reasoning (but can slow the task); retrospective avoids interference (but risks post-hoc rationalization). Ask users to verbalize what they're doing, not to justify — justification changes behavior.
- **RITE** (fix-as-you-go) when problems are obvious, the decision-maker is in the room, and the build allows rapid change — fix after even one observation, re-test the change. Not for when causes are unclear or rare problems matter (changing the UI mid-study breaks the controlled condition).
- **Benchmark/summative** — how good is it, on a scale? Standardized instruments so results are comparable: SUS (whole-experience, 0-100), SEQ (per-task ease), task-success rate. Size for the precision you need.
- **Heuristic evaluation** — expert inspection against Nielsen's 10 heuristics, **3-5 evaluators** because any one evaluator finds only ~35% of problems (the evaluator effect) and no one evaluator is reliably best.
- **A/B test** — does the change move the metric? Pre-declare the primary metric, minimum detectable effect, and required sample from a power calculation; no peeking. (The stats live in diagnose-first's criteria too.)
- **Accessibility** — WCAG conformance level (AA is the usual legal/industry bar). Automated tools are a first pass only: they catch a *minority* of issues (commonly cited ~30-40%, though volume-based studies argue higher) — the semantic judgments (alt-text quality, heading logic, link context, screen-reader experience) require manual testing regardless.

## Analyzing the results

- **Standardized scores against benchmarks.** SUS mean is 68 (500+ studies); convert to a letter grade rather than reporting a bare number. Task success benchmark median ~78%. Report against the benchmark, not in a vacuum.
- **Confidence intervals on small samples.** "5 of 5 succeeded" is not "100% success" — the naive interval badly overstates certainty at small n. Use the adjusted-Wald interval (add ~2 successes and 2 failures, then compute) so completion-rate claims carry honest bounds.
- **Significance vs. meaning.** A statistically significant difference can be trivial; report the effect size and whether it clears a threshold that matters, not just p < 0.05. And subjective satisfaction (SUS) correlates only modestly with objective success — report both, don't let one stand for the other.
- **Problem findings by severity, not count.** Rank issues by impact × frequency; a single-user showstopper outranks a cosmetic issue five users mentioned.

## Why this exists (the meta-evidence)

Even elite teams with mature experimentation find only a minority of ideas actually improve the metric — roughly a third of Microsoft's experiments move the target (a third do nothing, a third hurt), and ~90% of Booking.com's fail. Seniority doesn't make the intuition more accurate. That is the empirical case for this whole skill: "we're confident it's better" is not evidence; a defined measurement is. Design so the verdict can come back *negative* and be believed.

## The deliverable

Test designs ship as: which test and why, sample size with its justification, tasks/metrics/instruments, and the success criteria set *before* running. Analyses ship as: scores against benchmarks with confidence intervals, findings ranked by severity, honest significance, and a clear verdict — including "no significant improvement" when that's the answer — plus the next iteration or the decision it unblocks.

## References

Read `references/criteria.md` for a high-stakes eval needing the precise numbers and sources — the 5-user model and its rebuttals, SUS scoring/grade bands, task-success CIs (adjusted Wald), quantitative sample-size tables, think-aloud reactivity, evaluator effect, RITE conditions, WCAG levels and automated-detection studies, experiment success-rate data. Light checks never need it.