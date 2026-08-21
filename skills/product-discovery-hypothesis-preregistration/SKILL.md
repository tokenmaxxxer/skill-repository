---
name: product-discovery-hypothesis-preregistration
description: Use when a hypothesis needs its primary metric, numeric threshold, and decision rule fixed before any data collection begins, or when ranking candidate hypotheses to register next. Applies to the hypothesis-preregistration axis.
axis: hypothesis-preregistration
rule_count_floor: 10
---

# Hypothesis pre-registration (metric, threshold, decision rule fixed before data)

Research trail: pre-registration and metric-hierarchy practice fetched this session via Atticus Li's pre-registration glossary, Optibase and AB Test Pro guardrail/measurement-plan guides, and Statsig's guardrail-metric explainer; converged with this role's own binding rule that the verdict is the mechanical application of a rule fixed before data collection.

## Trigger

Apply this skill before any data collection begins on a hypothesis: when
writing its primary metric, numeric threshold, and decision rule; when
several candidate assumptions compete for which hypothesis to register
next; or when a stakeholder proposes changing the registered package
once the test is already running.

## Procedure

1. Name a single primary metric with a numeric threshold and decision
   rule before data collection starts (rule 1), combining the
   statistical test and the practical-significance bar in one explicit
   ship criterion (rule 2), and register the sample size and test
   duration needed to reach it (rule 3).
2. At the same moment, name at least one guardrail metric with a bounded
   degradation limit, not a bare metric name (rules 4-5).
3. At measurement time, apply the registered decision rule mechanically
   to the collected data (rule 7); record a primary-metric win alongside
   a breached guardrail as a breach, not an unqualified win (rule 6);
   refuse any mid-flight change to metric, threshold, or decision rule
   (rule 8).
4. Strip a metric with prose intent but no attached number from the
   registered list (rule 9), and strip "registered" status from a
   package with no defined sample size, duration, or interim-peeking
   policy (rule 10).
5. When several assumptions compete for the next registration slot,
   rank them by impact-times-risk and register the highest-ranked one
   first, naming the experiment that would falsify it (rule 11).

## Output shape

A registered hypothesis package: primary metric, numeric threshold,
decision rule, sample size/duration, and at least one bounded guardrail
metric, all fixed before data collection — plus, at measurement time, a
mechanically-applied verdict that respects any guardrail breach.

## Rules

1. When a hypothesis is written for a go/kill/pivot decision, name a single primary metric with a numeric threshold and a decision rule before any data collection begins (e.g. "adding a progress bar will increase completion rate by 5%... ship criterion: p<0.05 AND relative lift >= 3%") — pre-registration requires the hypothesis, primary metric, and ship criterion be written "before launch," so a threshold added after results are visible is not a registration, it is post-hoc rationalization wearing the same format. source: https://atticusli.com/behavioral-science-glossary/pre-registration/

2. When writing the ship criterion, combine the statistical test and the practical-significance bar in one explicit rule (e.g. "p<0.05 AND relative lift >= 3% AND no guardrail degradation >= 2%"), not a bare significance test alone — the documented best-practice ship criterion binds all three conditions together precisely so a statistically-significant-but-practically-trivial result cannot pass as a win. source: https://atticusli.com/behavioral-science-glossary/pre-registration/

3. When a threshold is registered, also register the sample size and test duration needed to reach it (e.g. "40,000 per arm... 14-28 days") before launch — an undersized or open-ended test lets a team peek at results and stop early once the number looks favorable, which is the exact behavior pre-registration exists to prevent. source: https://atticusli.com/behavioral-science-glossary/pre-registration/

4. When the hypothesis package is written, name at least one guardrail metric distinct from the primary metric at the same moment the primary metric is registered, not added later once results start coming in — the complete metric hierarchy (primary, secondary, guardrail, and each guardrail's maximum acceptable degradation threshold) must be "documented in writing before the test is activated" to remain the binding decision framework. source: https://atticusli.com/behavioral-science-glossary/pre-registration/

5. When registering a guardrail threshold, state it as a bounded degradation limit, not a bare metric name (e.g. "revenue per visitor must not drop more than 2% with statistical significance," not just "watch revenue") — a guardrail metric without a numeric bound cannot mechanically trip, so at decision time the team would be doing fresh judgment instead of applying the registered rule. source: https://www.optibase.io/glossary/guardrail-metric

6. When the primary metric shows a win but a registered guardrail has degraded past its threshold, record the result as a guardrail breach, not an unqualified win — "a test is only a real win when the primary metric improves and every guardrail stays inside its safe range," so a win recorded without checking guardrail status overstates the result's trustworthiness. source: https://abtestresult.com/articles/guardrail-metrics

7. When applying the decision rule at measurement time, apply it mechanically to the collected numbers as registered — do not re-derive a new threshold or apply fresh judgment once results are visible; the guardrail rule is explicitly "even if the primary metric is winning," which only holds meaning if the rule was fixed before the primary metric's result was known. source: https://www.optibase.io/glossary/guardrail-metric

8. When a test is running and a stakeholder proposes changing the metric, threshold, or decision rule mid-flight because early results look different than expected, refuse the change and finish the test against the originally registered rule — pre-registration's entire function is removing "subjective post-hoc interpretation," so a mid-test threshold change reintroduces exactly the bias the registration was meant to prevent. source: https://atticusli.com/behavioral-science-glossary/pre-registration/

9. **REMOVAL**: When a hypothesis package states a metric with prose intent but no number attached ("we believe this will improve retention"), remove it from the registered hypothesis list until a numeric threshold and decision rule are attached — "prose without a number is not a registration," so an unnumbered belief statement must be reworked or dropped, never carried forward as if it were pre-registered.

10. **REMOVAL**: When a stopping rule is absent from an otherwise-complete hypothesis package (metric and threshold present but no defined sample size/duration or interim-peeking policy), strip the package of "registered" status and route it back to registration rather than allowing measurement to begin — an incomplete stopping rule leaves room for early-stop cherry-picking, which defeats the same purpose the numeric threshold rule exists to serve. source: https://atticusli.com/behavioral-science-glossary/pre-registration/

11. When several assumptions are candidates for the next registered hypothesis and time only allows testing one, rank them by impact-times-risk (how much of the plan breaks if the assumption is wrong, times how little evidence currently supports it) and register the highest-ranked one first, with the specific experiment that would falsify it named in the same registration step — a hypothesis list ranked by ease of testing or by whoever raised it first quietly defers the assumption that could most cheaply kill the whole plan, which is the opposite of what pre-registration is supposed to force to the front.
