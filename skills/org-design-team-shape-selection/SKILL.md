---
name: org-design-team-shape-selection
description: Use when deciding what kind of team a new or restructuring team should be, or what interaction mode two teams should use and for how long. Do NOT use for measuring an existing team's psychological safety (route to team-safety-measure) or for defining the competencies of a role once the team's type is chosen (route to org-design-role-competency-definition).
axis: team-type-and-interaction-mode-by-cognitive-load
rule_count_floor: 3
---

# Team-shape selection

Decision rules for selecting a team's type and its interaction mode
with other teams, sourced from Skelton & Pais's *Team Topologies*, per
issue #77's phase-1 survey
(`docs/issue-77/reports/knowledge-management/survey.md`, 2026-08-22).

## Trigger

Apply this skill when deciding what kind of team a new or
restructuring team should be, or what interaction mode two teams should
use and for how long. Do not use it to measure whether an existing
team already feels psychologically safe — that symptom routes to
`team-safety-measure`'s measurement scope, not to a reshape decision.
Do not use it to define the competencies of the roles inside a team
once its type is chosen — apply
`org-design-role-competency-definition` after this skill's type
decision, against the chosen type's accountabilities.

## Procedure

1. Classify the team against the four fundamental team types by what
   it owns end-to-end and whose cognitive load it exists to reduce
   (rule 1).
2. Classify each cross-team interaction as collaboration,
   X-as-a-Service, or facilitating (rule 2).
3. Treat collaboration and facilitating modes as time-bounded by
   design, and read a facilitating relationship that never ends as a
   signal the receiving team's shape is wrong (rule 3).

## Output shape

A team-type classification (stream-aligned, enabling,
complicated-subsystem, or platform) with its cognitive-load rationale,
plus an interaction-mode classification for each team it works with,
including an explicit time-bound or end condition for any collaboration
or facilitating mode.

## Decision rules

1. Classify the team as one of the four fundamental team types —
   stream-aligned (owns end-to-end delivery for one business
   domain/product/customer need, minimal external dependencies),
   enabling (builds missing capability in other teams, aims at their
   autonomy), complicated-subsystem (isolates genuinely hard
   specialist work so it doesn't tax stream-aligned teams' cognitive
   load), or platform (provides internal services so stream-aligned
   teams self-serve with reduced cognitive load) — by what the team
   owns and whose cognitive load it reduces, not by org-chart
   convenience or a pre-existing skill silo.
   source: https://teamtopologies.com/key-concepts
   counter-example: do not classify a team as "platform" just because
   it is centralized or shared — if it doesn't reduce another team's
   cognitive load through a self-service internal product, it may
   actually be a complicated-subsystem or enabling team wearing a
   platform org-chart label.

2. Classify every interaction between two teams as exactly one of:
   collaboration (close joint work on an evolving problem,
   intentionally short-lived and high-bandwidth), X-as-a-Service (one
   team consumes another's output with minimal communication
   overhead), or facilitating (one team helps another overcome a gap,
   aiming at the facilitation ending).
   source: https://teamtopologies.com/key-concepts
   counter-example: do not leave a cross-team relationship
   unclassified as "we just talk sometimes" — an unclassified
   interaction mode hides whether the ongoing communication overhead is
   intentional (collaboration) or a symptom of a gap that facilitation
   should be closing.

3. Treat collaboration and facilitating interaction modes as
   time-bounded by design; when a facilitating relationship has been
   running indefinitely, treat that as a signal the receiving team's
   shape or capability gap is wrong, not as a reason to keep
   facilitating indefinitely.
   source: https://calade.de/en/glossary/what-are-team-topologies
   counter-example: do not accept "Team A has been facilitating Team B
   for two years and it's working fine" as a stable end-state — surface
   it as a signal to re-evaluate Team B's shape (e.g., does it need an
   enabling-team engagement of defined scope, or a capability it should
   own itself) rather than normalizing permanent facilitation.

## Related skills

- [team-safety-measure](../team-safety-measure/SKILL.md) — if the actual complaint is "this team doesn't feel safe," route to the measurement skill rather than treating it as a reshape decision.
- [org-design-role-competency-definition](../org-design-role-competency-definition/SKILL.md) — once a team's type is chosen here, define the roles inside it against that type's accountabilities using this skill.
