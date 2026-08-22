---
name: org-design-role-competency-definition
description: Use when writing or reviewing a role's competency list, a job description's requirements section, or a promotion/leveling criterion. Do NOT use for designing the interview questions that assess a role once its competencies are defined (route to org-design-hiring-rubric-structured-interview) or for choosing what shape a team should be (route to org-design-team-shape-selection).
axis: threshold-vs-differentiating-competency
rule_count_floor: 3
---

# Role and competency definition

Decision rules for writing or reviewing a role's competency list,
sourced from McClelland (1973) and Boyatzis (1982)'s
threshold/differentiating competency distinction, with a falsifiable
goal-statement convention borrowed from Doran (1981) SMART and
Grove/Doerr's OKR lineage, per issue #77's phase-1 survey
(`docs/issue-77/reports/knowledge-management/survey.md`, 2026-08-22).

## Trigger

Apply this skill when writing or reviewing a role's competency list, a
job description's requirements section, or a promotion/leveling
criterion. Do not use it to design the interview questions used to
assess a role once its competencies exist — that is
`org-design-hiring-rubric-structured-interview`'s scope, which should
draw its questions from this skill's output. Do not use it to decide
what kind of team a role sits inside — that is
`org-design-team-shape-selection`'s scope; apply this skill afterward,
against the chosen team type's accountabilities.

## Procedure

1. Tag every listed competency as threshold or differentiating before
   finalizing the list (rule 1).
2. Reject an untagged flat list of trait adjectives as an authoring
   error, not an acceptable shorthand (rule 2).
3. State each competency's performance expectation in falsifiable
   form, using an Objective/Key-Result or SMART-style split (rule 3).

## Output shape

A role/competency list where every entry is explicitly tagged
threshold or differentiating, and every entry's performance expectation
is stated as a falsifiable measure rather than an unmeasurable trait
adjective.

## Decision rules

1. Every listed competency must be tagged threshold (necessary for
   minimally adequate performance) or differentiating (separates
   superior from average performers) — these are not the same
   category, and a role definition that doesn't distinguish them
   cannot be used to decide what "meets bar" versus "exceeds bar"
   means for that role.
   source: http://www.iosrjournals.org/iosr-jbm/papers/Vol16-issue1/Version-1/C016111422.pdf
   counter-example: do not list "communication skills, ownership,
   technical depth" as one undifferentiated bullet list — tag each as
   threshold or differentiating, since a candidate lacking a threshold
   competency should be rejected outright while lacking a
   differentiating one only affects leveling.

2. Treat an untagged flat competency list as an authoring defect to be
   fixed, not a stylistic choice — the practice literature surveyed
   identifies conflating threshold and differentiating competencies as
   the most common competency-model authoring error.
   source: http://www.iosrjournals.org/iosr-jbm/papers/Vol16-issue1/Version-1/C016111422.pdf
   counter-example: do not accept "we'll figure out which ones matter
   more later" as a reason to skip tagging at authoring time — leaving
   the list untagged pushes the threshold/differentiating judgment onto
   whoever reads the list later, inconsistently, per reader.

3. State each competency's performance expectation so it is
   falsifiable: split it into a qualitative Objective and one or more
   quantitative, checkable Key Results (or an equivalent SMART-style
   measurable criterion), rather than an unmeasurable trait adjective
   like "strong" or "excellent."
   source: https://www.whatmatters.com/articles/the-origin-story , https://www.collective-genius.com/blog/the-history-of-smart-goals-and-okrs
   counter-example: do not write a competency as "demonstrates strong
   ownership" with no attached measure — state what observable,
   checkable result would confirm or refute that the competency was
   met (an Objective+Key-Result pair, or an equivalently measurable
   SMART-style criterion).

## Related skills

- [org-design-hiring-rubric-structured-interview](../org-design-hiring-rubric-structured-interview/SKILL.md) — a hiring rubric's questions should be drawn from this skill's competency definitions, not invented ad hoc.
- [org-design-team-shape-selection](../org-design-team-shape-selection/SKILL.md) — once a team's type is chosen there, the roles inside it should be defined against that type's accountabilities using this skill.
- [partnerships-bd-negotiation-positioning](../partnerships-bd-negotiation-positioning/SKILL.md) — where a role's competency definition covers an externally-facing BD/partnerships seat, chain to that skill's negotiation-positioning content rather than duplicating it here.
