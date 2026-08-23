---
name: org-design-hiring-rubric-structured-interview
description: Use when designing or reviewing a hiring interview rubric, or judging whether an interview process is structured enough to trust its validity claim. Do NOT use for measuring an existing team's psychological safety (route to team-safety-measure) or for defining what a role's competencies are (route to org-design-role-competency-definition).
metadata:
  axis: interview-structure-vs-validity-tradeoff
  rule_count_floor: 3
---

# Hiring rubric and structured-interview design

Decision rules for designing or reviewing a hiring interview rubric,
sourced from Schmidt & Hunter (1998)'s meta-analysis of 85 years of
personnel-selection research, per issue #77's phase-1 survey
(`docs/issue-77/reports/knowledge-management/survey.md`, 2026-08-22).

## Trigger

Apply this skill when designing or reviewing a hiring interview rubric,
or when judging whether an interview process is "structured enough" to
trust the validity figures commonly cited for it. Do not use it to
measure whether an existing team feels psychologically safe (that is
`team-safety-measure`'s scope) or to decide what a role's competencies
should be in the first place (that is
`org-design-role-competency-definition`'s scope — draw the rubric's
questions from that skill's output rather than inventing criteria here).

## Procedure

1. Confirm the rubric uses a fixed question set, behaviorally anchored
   rating scales, and systematic scoring before calling it "structured"
   (rule 1).
2. State the validity figure the rubric is entitled to claim, matched
   to whether it is actually structured or not (rule 2).
3. Check whether a work-sample or general-ability measure is available
   alongside the interview, and if so, position the interview as a
   complement rather than a sufficient stand-alone signal (rule 3).

## Output shape

A hiring rubric (or a review verdict on an existing one) that names its
fixed question set, anchored rating scale, and scoring method
explicitly, states the validity figure it can honestly claim, and notes
whether it is paired with a work-sample/ability measure.

## Decision rules

1. A rubric may only be called "structured" — and inherit the higher
   validity figure associated with that term — if it has all three of:
   a standardized question set asked of every candidate, behaviorally
   anchored rating scales, and systematic (not holistic/gut-feel)
   scoring. Absent any one of these three, treat and label it as
   unstructured.
   source: https://firstpersonnel.org/wp-content/uploads/2013/10/Summary-Schmidt-Hunter-1998.pdf
   counter-example: do not call a rubric "structured" just because
   interviewers are handed the same list of topics to "cover somehow"
   — without fixed questions, anchored scales, and systematic scoring,
   it is a structured *topic list*, not a structured interview, and
   must not borrow the structured interview's validity figure.

2. State the interview's expected operational validity honestly: a
   genuinely structured interview supports r ≈ .51; an unstructured
   interview (including a "structured topic list" per rule 1) supports
   only r ≈ .38. Never present the higher figure for a process that
   fails rule 1's structure test.
   source: https://www.plum.io/blog/schmidt-hunter-meta-analysis
   counter-example: do not cite "structured interviews predict job
   performance at r=.51" as a blanket justification for an interview
   process that was never checked against rule 1's three-part
   definition — the number is conditional on the format, not a
   property of "having an interview."

3. Where a work-sample test or general-mental-ability (GMA) measure is
   available for the role, design the rubric to complement it rather
   than replace it — combined GMA+structured-interview validity (r ≈
   .63) exceeds either alone, so a rubric review should flag a
   hiring process that relies on the interview as its sole
   measurement when a work-sample or ability measure could be added.
   source: https://firstpersonnel.org/wp-content/uploads/2013/10/Summary-Schmidt-Hunter-1998.pdf
   counter-example: do not treat a well-structured interview as
   sufficient justification to skip a feasible work-sample or ability
   measure — the evidence supports pairing, not substitution, wherever
   pairing is practical for the role.

## Related skills

- [org-design-role-competency-definition](../org-design-role-competency-definition/SKILL.md) — a hiring rubric's questions should be drawn from an existing competency definition, not invented ad hoc.
- [team-safety-measure](../team-safety-measure/SKILL.md) — if the actual question is whether a candidate or team member feels safe disagreeing, route the measurement question there rather than folding it into a hiring rubric.
