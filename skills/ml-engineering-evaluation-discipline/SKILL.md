---
name: ml-engineering-evaluation-discipline
description: Use when you need guidance on Evaluation discipline: offline vs online. Applies to the evaluation-discipline axis.
axis: evaluation-discipline
rule_count_floor: 5
---

# Evaluation discipline: offline vs online

Research trail: Kohavi, Tang & Xu's trustworthy-online-controlled-experiments literature (primary named methodology for online evaluation trust) and a follow-up paper on automated Sample Ratio Mismatch detection; Qwak's shadow-vs-canary-vs-A/B comparison for method selection. Fetched this session.

## Rules

1. When reporting model quality prior to launch, report offline evaluation (metric, specific holdout/backtest dataset identity, result vs. threshold) as its own section, distinct from any online result — never let one substitute for the other, since offline plausibility and online-observed impact answer different questions. source: https://exp-platform.com/Documents/2017-05-17EmetricsControlledExperimentsPitfallsKohaviNR.pdf

2. When designing an online evaluation, run a Sample Ratio Mismatch (SRM) check via chi-square on the actual arm split before trusting any comparison metric from it — an unchecked SRM silently invalidates the result even when the headline comparison looks statistically significant. source: https://arxiv.org/pdf/2208.07766

3. When choosing among A/B, shadow, or canary as the online evaluation method, use A/B specifically when the goal is measuring business/outcome impact across a randomized population; reserve shadow for validating serving-pipeline correctness with zero user-facing risk, and canary for controlled risk exposure during rollout. source: https://www.qwak.com/post/shadow-deployment-vs-canary-release-of-machine-learning-models

4. When defining the promote/rollback decision rule for an online evaluation, pre-register the comparison metric and its decision threshold before launching the test, rather than choosing the metric or threshold after seeing results — trustworthy experimentation requires the rule to be fixed in advance of the data. source: https://exp-platform.com/Documents/2017-05-17EmetricsControlledExperimentsPitfallsKohaviNR.pdf

5. **REMOVAL**: When an online evaluation's traffic or duration is too small to reach the pre-registered decision threshold's required sample size, drop the online-only launch path and fall back to extending the test window or using an extended canary ramp instead of declaring a decision on an underpowered result. source: https://exp-platform.com/Documents/2017-05-17EmetricsControlledExperimentsPitfallsKohaviNR.pdf
