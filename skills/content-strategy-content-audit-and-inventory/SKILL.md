---
name: content-strategy-content-audit-and-inventory
description: Use when starting a content audit, building a content inventory, or deciding whether a content-assessment task needs quantitative enumeration, qualitative judgment, or both in sequence.
axis: enumeration-vs-judgment-task-type
rule_count_floor: 2
---

# Content audit and inventory

Issue: tokenmaxxxer/skill-repository#82 (professional-discipline gap #4,
content-strategy family). Research trail:
docs/issue-82/reports/content-design/survey.md, Angle 2 (content-audit
method: quantitative inventory vs. qualitative audit).

## Trigger

Apply this skill when starting a content audit, building a content
inventory, or deciding whether a content-assessment task needs
quantitative enumeration, qualitative judgment, or both, and in what
order.

## Procedure

1. Classify the task first: enumeration-shaped (inventory) or
   judgment-shaped (audit) — do not let one stand in for the other
   (rule 1).
2. If both are needed, run the quantitative inventory before the
   qualitative audit, never the reverse (rule 2).

## Output shape

A task classification: inventory, audit, or both in sequence, plus the
concrete first step (enumerate, or judge against a named criterion).

## Rules

1. A content inventory is quantitative — an accounting of every
   published content asset (URL, type, owner, last-updated date), no
   judgment calls — while a content audit is qualitative — an
   assessment of quality, structure, voice/tone fit, and usefulness,
   requiring human judgment. "The key distinction between quantitative
   inventories and qualitative audits is human judgement. Qualitative
   content audits are a robot-free zone." Classify which task type is
   actually being requested before starting, and do not let a
   quantitative crawl stand in for a qualitative quality assessment.
   source: https://www.peachpit.com/articles/article.aspx?p=1388961&seqNum=3

2. Run the quantitative inventory before the qualitative audit, never
   the reverse — a qualitative judgment on an unenumerated asset set is
   ungrounded, since you cannot assess whether a set is complete or
   representative without first knowing what exists in it. source:
   https://en.wikipedia.org/wiki/Content_audit

## Related-skills

- `content-strategy-content-governance-ownership` — an audit that
  surfaces an unowned or orphaned asset routes the ownership question
  there, not into the audit's own scoring.
- `devrel-content-comprehensibility` — when the audited asset is
  developer-facing content, route comprehensibility scoring there.
