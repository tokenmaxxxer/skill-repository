---
name: ux-engineering-service-design-touchpoint-channel-mapping
description: Use when identifying and sequencing the touchpoints a customer encounters across channels for one journey, or judging whether a journey's channel set is omnichannel/cross-functional enough to warrant escalating to a full service blueprint.
metadata:
  axis: touchpoint-channel-mapping-vs-blueprint-escalation
  rule_count_floor: 4
---

# Touchpoint and channel mapping

Decision rules for mapping the touchpoints and channels a customer
encounters across one journey, and for judging when that mapping
should escalate into full service-blueprint construction — sourced
from NN/g's service-blueprinting guidance and the frontstage/backstage
touchpoint-definition literature, per issue #74's phase-1 survey
(`docs/issue-74/reports/ux-engineering/survey.md`, 2026-08-22).

## Trigger

Apply this skill when identifying and sequencing the touchpoints
(people, props, processes tied to a customer interaction moment) a
customer encounters across channels for one journey, or when judging
whether a journey's channel set is omnichannel or cross-functional
enough to warrant escalating to a full service blueprint. Do not use it
once a full blueprint is already being constructed — at that point the
touchpoints are already being laid into the blueprint's own layers, so
apply `ux-engineering-service-design-blueprint-construction` instead.

## Procedure

1. Choose which experience, segment, or journey to map before
   enumerating any touchpoint (rule 1).
2. Identify each touchpoint as people plus props/evidence plus process
   tied to one interaction moment (rule 2).
3. Sequence the identified touchpoints in the order the customer
   actually encounters them across channels (rule 3).
4. Test whether the mapped journey is omnichannel, multi-touchpoint, or
   cross-functional enough to escalate to a full blueprint (rule 4).

## Output shape

A sequenced touchpoint/channel map for one scoped journey, each
touchpoint identified by its people/props/process components, plus an
explicit escalate-or-stand-alone verdict against the blueprint trigger
test.

## Decision rules

1. Before enumerating touchpoints, choose which experience, segment, or
   journey is being mapped — the same scoping discipline NN/g names as
   a distinct step before blueprinting starts applies equally before
   touchpoint mapping starts, since an unscoped map sprawls across
   unrelated journeys.
   source: https://www.nngroup.com/articles/service-blueprints-choose-what-experience/
   counter-example: do not map "all touchpoints for the product" as one
   undifferentiated list — scope to one journey or segment first, the
   same way blueprint construction does.

2. Identify each touchpoint as the combination of people, props
   (physical or digital evidence), and process tied to one specific
   customer interaction moment — not a bare channel name (e.g. "email")
   with no interaction-moment content attached.
   source: https://ixdf.org/literature/topics/frontstage-and-backstage ,
   https://www.nngroup.com/articles/service-blueprints-definition/
   counter-example: do not list a channel like "mobile app" as a single
   touchpoint if the customer actually encounters three distinct
   interaction moments within it (e.g. browse, checkout, support chat)
   — split into separate touchpoints, each with its own
   people/props/process.

3. Sequence the identified touchpoints in the order the customer
   actually encounters them across channels, since the mapping's value
   is in revealing cross-channel handoffs and gaps, not an unordered
   inventory.
   source: https://www.nngroup.com/articles/service-blueprinting-faq/
   counter-example: do not group touchpoints by channel/department
   instead of by encounter order — grouping by channel hides the
   cross-channel handoff points the mapping exists to surface.

4. Test the mapped journey against the omnichannel/multi-touchpoint/
   cross-functional trigger: when the journey crosses multiple channels
   or requires coordination across departments, escalate to a full
   service blueprint via
   `ux-engineering-service-design-blueprint-construction`; when it does
   not, the touchpoint/channel map stands alone as its own artifact.
   source: https://www.nngroup.com/articles/service-blueprinting-faq/
   counter-example: do not escalate a single-channel, single-department
   journey to a full blueprint just because it has multiple sequential
   touchpoints within that one channel — touchpoint count alone does
   not trigger escalation; channel/department crossing does.

## Related skills

- [ux-engineering-service-design-blueprint-construction](../ux-engineering-service-design-blueprint-construction/SKILL.md) — the fuller artifact this skill's mapping escalates into when the omnichannel/cross-functional trigger fires.
- [design-artifact-user-scenario](../design-artifact-user-scenario/SKILL.md) — holds the cross-channel emotional/narrative journey content that `design-artifact-user-flow` excludes, alongside this skill's touchpoint sequencing for the same journey.
