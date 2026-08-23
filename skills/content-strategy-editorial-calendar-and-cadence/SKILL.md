---
name: content-strategy-editorial-calendar-and-cadence
description: Use when planning or reviewing an editorial calendar, committing to a publishing cadence, or deciding a content asset's lifecycle stage (create, update, retire).
metadata:
  axis: lifecycle-and-cadence-planning
  rule_count_floor: 2
---

# Editorial calendar and cadence

Issue: tokenmaxxxer/skill-repository#82 (professional-discipline gap #4,
content-strategy family). Research trail:
docs/issue-82/reports/content-design/survey.md, Angle 1 (Halvorson/Rach
core discipline definition).

## Trigger

Apply this skill when planning or reviewing an editorial calendar,
committing an organization to a publishing cadence, or deciding a
content asset's lifecycle stage — whether it should be created, updated
in place, or retired.

## Procedure

1. Before adding a calendar entry, check that it carries a lifecycle
   plan, not just a publish date: a review or retirement point, not
   only a "when it goes live" date (rule 1).
2. When drafting or reviewing the actual wording, tone-of-voice, or
   plain-language quality of a calendar entry's copy, route that
   decision to `content-design-operational-playbook` rather than
   deciding it here — this skill owns *when and whether*, not *how it
   reads* (rule 2).

## Output shape

A calendar decision: the applicable rule number, the calendar entry
affected, and the lifecycle action (schedule with a review/retirement
date attached, or route the wording decision elsewhere).

## Rules

1. Editorial strategy "defines the guidelines by which all online
   content is governed: values, voice, tone, legal and regulatory
   concerns, user-generated content... and also defines an
   organization's online editorial calendar, including content life
   cycles." A calendar entry with no retirement or review date is an
   incomplete lifecycle plan, not just a scheduling gap — every entry
   must carry a create/update/retire decision, not only a publish date.
   source: https://alistapart.com/article/thedisciplineofcontentstrategy/

2. **REMOVAL**: Sentence-level wording, tone-of-voice-per-string, and
   plain-language decisions are out of scope for calendar planning —
   route them to `content-design-operational-playbook` instead of
   re-deciding them here, since that skill already owns the
   sentence/string-level craft layer and duplicating its rules here
   would let a calendar entry ship with untested wording assumptions.
   source: https://alistapart.com/article/thedisciplineofcontentstrategy/

## Related-skills

- `content-design-operational-playbook` — wording, tone-of-voice, and
  plain-language decisions once a calendar slot is confirmed.
- `marketing-channel-selection` — channel choice for a calendar entry
  that spans marketing content.
- `content-strategy-content-governance-ownership` — when a calendar
  entry has no owner committed to the cadence, resolve ownership there
  before scheduling.
