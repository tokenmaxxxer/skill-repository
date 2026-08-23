---
name: issue-retrospective-timeline-comprehensibility-and-subtraction-rules
description: >-
  Use when composing or reading a records-only cross-role retrospective for a subject issue
  — drafting its Timeline, Contributing factors, or Action items, or judging whether a draft
  section restates background instead of citing it. Trigger on requests like "write the
  issue retrospective", "회고 타임라인 정리해줘", "trim this retrospective draft", "does this section
  restate the record". Adjacent to blameless-postmortem, which owns declared-incident
  postmortems rather than per-issue records-only retrospectives.
metadata:
  axis: convention, subtraction, comprehensibility
  rule_count_floor: 8
  axes: convention,subtraction,comprehensibility
---

# Retrospective-record convention, subtraction, and comprehensibility rules

Research trail (fetched this session, 2026-08-13): Google SRE's postmortem-culture
page and SRE workbook chapter on postmortem practices, PagerDuty's Postmortem
Documentation Guide and postmortem template, incident.io's SRE postmortem
best-practices post, and — for the academic layer — Adams, Converse, Hales &
Klotz, "People systematically overlook subtractive changes," *Nature* 592
(2021), plus the Federal Plain Language Guidelines / plainlanguage.gov
principles for the comprehensibility axis. Domain classification: moderate —
an established public postmortem canon exists (Google SRE, PagerDuty) but this
role's specific object (a *records-only* cross-role retrospective, not a live
incident postmortem) is a narrower analogy than the source literature, flagged
as such rather than presented as retrospective-native research.

## Trigger

Use this skill when composing or reading a records-only cross-role
retrospective for a subject issue — this is the records-only
retrospective moment, distinct from adjacent record-writing moments
such as mid-incident postmortem drafting or a single role's own
implementation record:
- starting or continuing composition of the retrospective record from
  another role's records (Timeline, Contributing factors, What we
  learned, Action items sections).
- drafting or reviewing a contributing-factor or causal-language
  sentence for whether it names a person/choice instead of a structural
  gap.
- drafting, reviewing, or pruning the contributing-factors list or the
  Action items list.
- laying out or checking the record's overall section order and
  completeness.
- judging whether a draft section restates background already
  established elsewhere instead of citing it.

## Procedure

1. Draft the Timeline section first, from the subject's other-role
   records, before drafting Contributing factors or What we learned
   (rule 1).
2. While drafting or reviewing Contributing factors, rewrite any
   sentence that names a person or role's choice as the explanation so
   it instead names the structural gap that let the choice go wrong
   (rule 2).
3. Cap the Contributing factors list at 2-5 systemic items; run the
   removal pass to cut items that are downstream restatements of one
   already listed (rules 3, 9).
4. Draft each Action item with a named owner, checkable phrasing, and a
   one-clause stated Impact; delete any item that stays vague, unowned,
   or duplicative rather than keeping it as filler (rules 4, 10, 15).
5. Lay out the record in the fixed five-section order — Timeline, Impact
   summary, Contributing factors, What we learned, Action items — even
   when a section is thin or empty (rule 13).
6. Before finalizing, run the two subtraction passes: cut any section
   restating background already established by the issue, a proposal,
   or another role's record in favor of a citation (rule 8), and cut any
   Timeline entry or Contributing-factor/Action-item content that does
   not change the reader's understanding (rules 9, 10, 11).

## Output shape

A five-section retrospective record body — Timeline, Impact summary,
Contributing factors, What we learned, Action items — in that fixed
order, with contributing factors capped at 2-5 systemic items, each
Action item owned and checkable with a stated Impact, and no section
restating background available elsewhere by citation.

## Rule index

Full rule text, citations, and counter-examples:
`references/rules.md` in this skill's directory — read it when a
matched rule's detail is needed.

- 1.1 — When starting record composition, write the Timeline section from the subject's other-role records first, before drafting any Contributing factors or What-we-learned lan…
- 1.2 — When a contributing-factor sentence is about to name a person or a role's choice as the explanation, rewrite it to name the structural gap (process, tool, documentation,…
- 1.3 — When the contributing-factors list is being drafted, cap it at 2-5 systemic items and never collapse it to one "root cause" line — SRE and incident.io postmortem practic…
- 1.4 — When drafting Action items, give each one a named owner (a person or role, never "the team") and phrase it as a checkable change, and mark whether it fixes this instance…
- 1.5 — When the record will be read by a session or reviewer unfamiliar with the subject issue's jargon (role names, internal gate names, tool acronyms), define the term at its…
- 1.6 — When a paragraph is doing double duty — describing what happened and proposing how to fix it in the same sentence — split it: keep the Impact-summary/Contributing-factor…
- 1.7 — When another role's record is silent on a section this role's contract requires reading (e.g., no Impact summary in an implementation record), record that silence itself…
- 1.8 — **REMOVAL**: When a draft record section restates background already established by the linked issue, proposal, or another role's record (e.g., a "Context" section re-ex…
- 1.9 — **REMOVAL**: When the contributing-factors list grows past 5 items, cut it down to the factors that actually explain the cascade and drop items that are just downstream…
- 1.10 — **REMOVAL**: When an Action item is vague, unowned, or duplicates an item already tracked elsewhere, delete it rather than keep it as filler — the Action items section i…
- 1.11 — **REMOVAL**: When a Timeline entry does not change the reader's understanding of the impact or the causal cascade (e.g., a routine status ping with no decision attached)…
- 1.12 — When writing any record sentence, default to active voice, short sentences, and everyday words over technical phrasing, using bullet or numbered lists for multi-item mat…
- 1.13 — When laying out the record as a whole, keep the five required sections in a fixed order (Timeline, Impact summary, Contributing factors, What we learned, Action items) e…
- 1.14 — When any sibling role record for the subject is still at a non-terminal loop_state at the moment this role reads it, say so plainly in the Timeline (or a dedicated note…
- 1.15 — When drafting Action items, add a one-clause stated Impact (what measurably improves if the item is done) next to the owner and the checkable phrasing already required b…
