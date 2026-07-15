# Usability Eval — objective criteria and their sources

Grades: ●●● peer-reviewed/quantitative · ●●○ industry standard · ●○○ folklore.

## The 5-user model and its limits (●●●, contested)

Nielsen & Landauer (1993): problems found = 1−(1−L)ⁿ, L≈31% per user (Poisson model); Virzi (1992) similar (p≈0.32, ~80% in first 4-5). It's a *cost-benefit* heuristic for formative problem-finding, not a law. Rebuttals: Spool & Schroeder (2001) — open-ended websites keep surfacing serious problems well past 5; Woolrych & Cockton (2001) — uniform-probability assumption is wrong, problems hit users unevenly, so the model underestimates; Faulkner (2003) — random 5-user draws found 55-99% of problems (mean 85%, high variance). 5 users is insufficient for: open-ended tasks, heterogeneous users, low-frequency problems, and any *metric comparison* (different statistical regime entirely).

## Formative vs summative sample sizes (●●●/●●○)

Problem-finding (formative): 5-8/round, iterate. Metric comparison (summative/benchmark): size for power. Binary metrics (success/conversion): ~40 for 95% confidence ±15% margin; ~28 at 90%/±15%; ~15 at 90%/±20% (Sauro/Lewis via NN/g). Continuous metrics (time, score): ~47 at 95%/±15% assuming SD≈52% of mean. Compute up front; no optional stopping/peeking (inflates false positives — see diagnose-first G2-aux for power/MDE mechanics).

## SUS (●●●)

10 items, alternating positive/negative, 5-point. Score: odd items (response−1), even items (5−response), sum ×2.5 → 0-100. Benchmark mean **68** (Sauro & Lewis, 500+ studies, 5,000+ scores). Grade bands: ≥80.8 = A, 68-ish = C (50th pct), <51.7 = F. Cronbach's α≈0.91. Two factors (items 4,10 = learnability). Correlates only modestly with objective task performance (r≈.24) — subjective ≠ objective, report both.

## Other scales (●●●/●●○)

SEQ (single ease question, 7-pt, per-task) — strong properties despite one item; ~71% avg success correspondence. UMUX-Lite (2 positive items) predicts SUS at r≈.83. NASA-TLX (6 workload subscales) for cognitively demanding/mission-critical flows. NPS — arbitrary 0-6/7-8/9-10 cutoffs, modest predictive validity; "qualified, not discredited" is the academic verdict — don't treat it as a usability measure.

## Task success + confidence intervals (●●●)

Binary success is standard (success=1, fail=0; define completion state up front). Benchmark median ~78% (Sauro; 115 tests, 3,472 users — lab-skewed optimistic). Small-sample CIs: naive Wald badly under-covers at small n / extreme rates (5/5 ≠ true 100%). **Adjusted-Wald** (Sauro & Lewis 2005): add 2 successes + 2 failures, then Wald — Monte-Carlo coverage 96.7% vs nominal 95%. Use it for any completion-rate claim.

## Think-aloud (●●●)

Ericsson & Simon (1980/1993): concurrent verbalization of working-memory contents doesn't distort the process *if* you ask users to state what they're doing (Level 1/2), not to explain/justify (Level 3, which changes behavior). Concurrent = in-the-moment, no recall loss, but can slow the task; retrospective = no task interference, but recall gaps / post-hoc rationalization. Van den Haak (2003): both find similar problem counts, retrospective slightly more, concurrent lengthens task time. Meta-analysis (ACM TOCHI 2024): reactivity is real but varies by task.

## Heuristic evaluation (●●●/●●○)

Nielsen's 10 heuristics. Evaluator effect: a single evaluator finds ~35% of problems; substantial non-overlap between evaluators; none consistently best (Nielsen's 19-evaluator study). 3-5 evaluators is the cost-benefit sweet spot (benefit/cost ~62:1 at ~4 evaluators in Nielsen's example); diminishing returns beyond.

## RITE (●●○, single case study)

Rapid Iterative Testing & Evaluation (Medlock et al., MS Game Studios): fix as soon as a problem and its solution are clear (even after 1 user), decision-maker on the team, re-test the fix. Age of Empires II case: 30/31 problems fixed across 6 rounds. Fits: obvious problems, empowered decision-maker, fast-change build, skilled researcher. Unfit: unclear cause/solution, rare-problem detection matters (mid-study changes break the controlled condition), low domain expertise. Single uncontrolled case — present as conditions, not proven superiority.

## Accessibility (●●●/●○○)

WCAG 2.x levels A / AA (legal & industry bar) / AAA (not expected site-wide). Automated tools: commonly-cited ~30-40% of issues detected (●○○, origin unclear); Deque's 2,000-audit study argues 57% by issue *volume* (●●○) — the gap is measurement method (per-success-criterion vs per-issue). Either way, semantic checks (alt-text meaning, heading logic, link-text context, screen-reader quality, dynamic content) structurally require manual testing.

## Why measure at all (●●●/●●○)

Microsoft (Kohavi): ~⅓ of experiments produce a significant positive effect, ⅓ flat, ⅓ negative — "most experiments fail to move the metric they targeted"; Bing's rate is lower. Booking.com: ~90% of experiments fail to ship; C-level title doesn't improve the hit rate. Elite teams, mature infra — 70-90% of ideas still don't work. Therefore intuition is not a reliable pre-filter, and "did it actually improve" is a mandatory separate step, judged by a defined metric, not by confidence.