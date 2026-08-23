---
name: user-discovery-saturation-stopping-rule
description: >-
  Use when deciding how many discovery interviews to run or when to stop a round — sizing
  the initial batch, tracking a new-theme counter, applying a three-consecutive-dry stopping
  rule, and recording the saturation decision with its evidence. Trigger on requests like
  "인터뷰 몇 명이면 충분해", "have we reached saturation", "should we stop interviewing", "plan the
  interview count for this round". Do NOT use for how the final count feeds a pain-confirmed
  verdict (use user-discovery-verdict-prevalence-reporting).
metadata:
  axis: saturation-stopping-rule
  rule_count_floor: 8
---

# Saturation: when to stop interviewing

Research trail: qualitative-research saturation systematic review (ScienceDirect 2021), sample-size-to-saturation empirical studies (PMC/PubMed secondary analyses), Torres' continuous-discovery weekly-interview cadence. All searched this session.

## Trigger

Apply this skill when planning the interview count for a discovery
round, or deciding whether to stop or continue an in-progress round —
distinct from how the resulting count feeds a prevalence verdict
(verdict-prevalence-reporting).

## Procedure

1. For a narrow hypothesis and homogeneous population, plan an initial
   batch of 9-12 interviews before the first saturation check (rule 1).
2. For a diverse population or complex multi-part hypothesis, extend the
   planned count beyond that range rather than reusing 9-12 (rule 2).
3. Track a running new-theme counter per interview rather than only a
   total-interview count (rule 3).
4. Treat three consecutive interviews with a zero new-theme count as the
   saturation stopping point (rule 4).
5. If a new theme appears mid-check, reset the consecutive-dry counter
   to zero rather than only decrementing a fixed budget (rule 5).
6. Record the initial plan, the stopping criterion actually used, and
   the interview count at which it was met (rule 6).
7. For an ongoing/continuous discovery practice, run interviews on a
   fixed weekly cadence and re-evaluate saturation per theme rather than
   once for the whole practice (rule 7).
8. Drop any "saturation reached" claim from a below-range small sample
   that has no new-theme tracking evidence (rule 8).
9. Drop any fixed a-priori interview quota used as the sole stopping
   rule with no theme-tracking component (rule 9).

## Output shape

A saturation decision recording the initial interview-count plan, the
stopping criterion applied (e.g. three consecutive dry interviews), and
the interview count at which it was met — never a bare "saturation
reached" assertion with no supporting count.

## Rules

1. When starting a discovery round on a narrowly defined hypothesis with a relatively homogeneous target population, plan an initial batch of 9-12 interviews before the first saturation check — empirical studies found saturation reached within a 9-17 interview range for homogeneous populations with narrow objectives, so budgeting far below that range risks stopping before any real saturation signal appears. source: https://www.sciencedirect.com/science/article/pii/S0277953621008558

2. When the interviewee population is diverse or the hypothesis spans a complex, multi-part problem, extend the planned interview count beyond the narrow-population range (rule 1) rather than reusing the same 9-12 budget — more interviews may be needed if users are diverse or the topic is complex, and a fixed count regardless of population diversity is not evidence-grounded. source: https://heymarvin.com/resources/saturation-in-qualitative-research

3. When running interviews, track a running "new-theme" counter per interview (does this interview surface a theme/claim not already logged) rather than only counting total interviews — saturation is defined by the point new perspectives stop appearing, not by hitting a raw interview count, so a count-only stopping rule can halt too early or too late relative to the actual signal. source: https://heymarvin.com/resources/saturation-in-qualitative-research

4. When the new-theme counter hits zero for three consecutive interviews, treat that as the saturation stopping point and close the round — a validated practical strategy runs interviews until three consecutive sessions yield nothing new, then stops; fewer than three dry interviews in a row is not yet a reliable saturation signal. source: https://heymarvin.com/resources/saturation-in-qualitative-research

5. When a new theme appears after what looked like a saturation run (e.g. dry interview #2 of a planned 3), reset the consecutive-dry counter to zero rather than only decrementing a remaining-interviews budget — a genuinely new theme mid-check invalidates the prior dry streak's saturation claim, and continuing to count down a fixed budget around it would ignore the very signal saturation is meant to detect. source: https://heymarvin.com/resources/saturation-in-qualitative-research

6. When recording the saturation decision in the evidence log, state the initial interview-count plan, the stopping criterion actually used (e.g. "three consecutive dry interviews"), and the interview count at which it was met — saturation should be explained (documented sampling decisions with rationale), not merely asserted as a bare "saturation reached" line with no supporting count. source: https://www.tandfonline.com/doi/full/10.1080/08911762.2025.2590757

7. When a discovery effort is ongoing/continuous rather than a single bounded round (e.g. a standing product-discovery practice), run interviews on a fixed weekly cadence and re-evaluate saturation per theme/opportunity rather than declaring the whole practice saturated once — a continuous-discovery cadence treats saturation as a per-topic checkpoint, not a one-time terminal state for the entire practice. source: https://www.lennysnewsletter.com/p/teresa-torres-on-how-to-interview

8. **REMOVAL**: When a small-sample discovery round (fewer than the population-appropriate range from rules 1-2) reports "saturation reached" with no new-theme tracking evidence, drop that saturation claim from the verdict — a bare small-N claim of saturation with no per-interview new-theme log is an assertion, not the evidenced stopping criterion rules 3-6 require. source: https://www.tandfonline.com/doi/full/10.1080/08911762.2025.2590757

9. **REMOVAL**: When a fixed a-priori interview quota (e.g. "always do exactly 5 interviews") is used as the sole stopping rule regardless of what the new-theme counter shows, drop the fixed-quota-only stopping rule — a quota with no theme-tracking component can stop mid-saturation-check (too early, missing rule 4's three-dry-in-a-row bar) or continue well past saturation (too late, wasting interview budget on redundant data), neither of which the evidence-grounded rules above permit. source: https://heymarvin.com/resources/saturation-in-qualitative-research
