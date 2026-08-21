---
name: issue-retrospective-timeline-comprehensibility-and-subtraction-rules
description: Use when composing or reading a records-only cross-role retrospective for a subject issue — drafting its Timeline, Contributing factors, or Action items, or judging whether a draft section restates background instead of citing it.
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

## Rules

1. When starting record composition, write the Timeline section from the
   subject's other-role records first, before drafting any Contributing
   factors or What-we-learned language — Google SRE's postmortem template
   documents "an accurate timeline reconstructed from system data" ahead of
   causal analysis, and SRE workbook practice treats timeline-before-judgment
   as the mechanism that keeps causal claims falsifiable against the record.
   source: https://sre.google/workbook/postmortem-culture/

2. When a contributing-factor sentence is about to name a person or a role's
   choice as the explanation, rewrite it to name the structural gap (process,
   tool, documentation, or interface absence) that let that choice go wrong —
   blameless-postmortem practice assumes everyone acted in good faith with
   the information they had, so the record's causal language must point at
   the system, not the actor. source: https://sre.google/sre-book/postmortem-culture/

3. When the contributing-factors list is being drafted, cap it at 2-5
   systemic items and never collapse it to one "root cause" line — SRE and
   incident.io postmortem practice both define contributing factors as a
   plural set of causes that let a failure cascade, not a single point of
   attribution. source: https://incident.io/blog/sre-incident-postmortem-best-practices

4. When drafting Action items, give each one a named owner (a person or
   role, never "the team") and phrase it as a checkable change, and mark
   whether it fixes this instance or the class of failure — PagerDuty's
   postmortem documentation separates "fixes to prevent the contributing
   factor" from "preparedness tasks" and requires owners on both.
   source: https://www.pagerduty.com/resources/insights/learn/how-to-write-postmortem/

5. When the record will be read by a session or reviewer unfamiliar with the
   subject issue's jargon (role names, internal gate names, tool acronyms),
   define the term at its first use in the record rather than assuming
   context — PagerDuty's guide flags that postmortem readers are often
   newcomers to the incident and terminology must be defined for them.
   source: https://www.pagerduty.com/resources/insights/learn/how-to-write-postmortem/

6. When a paragraph is doing double duty — describing what happened and
   proposing how to fix it in the same sentence — split it: keep the
   Impact-summary/Contributing-factors description of what happened separate
   from the What-we-learned/Action-items discussion of what to do about it —
   postmortem-writing practice treats mixing description and remedy as what
   makes a record hard to audit later. source: https://www.pagerduty.com/resources/insights/learn/how-to-write-postmortem/

7. When another role's record is silent on a section this role's contract
   requires reading (e.g., no Impact summary in an implementation record),
   record that silence itself as a finding ("record too thin to
   retrospective on") rather than inferring the missing content from the
   running system — the records-only constraint is this role's own
   convention, and SRE practice's rule that a postmortem is only as good as
   the data it draws from applies the same way to records as to system logs.
   source: https://sre.google/workbook/postmortem-culture/

8. **REMOVAL**: When a draft record section restates background already
   established by the linked issue, proposal, or another role's record
   (e.g., a "Context" section re-explaining the subject issue), delete it
   and cite the source instead of restating it — subtraction-neglect
   research shows people default to additive edits and must be prompted to
   actively search for removable content, so treat "can this section be a
   citation instead of prose" as a mandatory check on every draft, not an
   optional trim. source: https://www.nature.com/articles/s41586-021-03380-y

9. **REMOVAL**: When the contributing-factors list grows past 5 items, cut
   it down to the factors that actually explain the cascade and drop items
   that are just downstream restatements of another factor already listed —
   the additive bias documented in Adams et al. means a first-pass list
   tends to over-include; the subtraction step is a required second pass,
   not a sign the first pass was wrong. source: https://www.nature.com/articles/s41586-021-03380-y

10. **REMOVAL**: When an Action item is vague, unowned, or duplicates an
    item already tracked elsewhere, delete it rather than keep it as filler
    — the Action items section is structurally required to exist but its
    content is advisory-only, so an empty section is a correct outcome and a
    padded section is the actual defect (mirrors this repo's own
    record-tiering convention for "What did not work": bare `None.` beats a
    restated-summary body). source: https://www.nature.com/articles/s41586-021-03380-y

11. **REMOVAL**: When a Timeline entry does not change the reader's
    understanding of the impact or the causal cascade (e.g., a routine
    status ping with no decision attached), cut it — plain-language
    brevity practice ("write briefly and clearly") and the subtraction-
    neglect finding both point the same direction here: a longer timeline
    is not a more useful one, and length must be actively pruned rather than
    left as a byproduct of thorough note-taking.
    source: https://digital.gov/guides/plain-language/principles

12. When writing any record sentence, default to active voice, short
    sentences, and everyday words over technical phrasing, using bullet or
    numbered lists for multi-item material (a contributing-factors set, an
    action-item list) instead of a dense paragraph — Federal Plain Language
    Guidelines name these as the concrete techniques that make comprehension
    fast rather than merely possible. source: https://digital.gov/guides/plain-language/principles

13. When laying out the record as a whole, keep the five required sections
    in a fixed order (Timeline, Impact summary, Contributing factors, What
    we learned, Action items) even when a section is thin or empty, rather
    than reordering per-issue for narrative flow — plain-language practice's
    "organize content logically" principle and Google SRE's fixed postmortem
    template both treat a predictable structure as what lets a
    zero-context reader navigate without re-deriving the record's shape
    each time. source: https://sre.google/sre-book/example-postmortem/

14. When any sibling role record for the subject is still at a
    non-terminal loop_state at the moment this role reads it, say so
    plainly in the Timeline (or a dedicated note next to the sibling
    citation) instead of drafting the rest of the record as if the full
    picture were already settled — a retrospective built over an
    incomplete input set is itself provisional, and that provisionality
    is a fact about the record's own basis, not a detail to omit for
    narrative smoothness.

15. When drafting Action items, add a one-clause stated Impact (what
    measurably improves if the item is done) next to the owner and the
    checkable phrasing already required by rule 4; and scale how much
    Timeline/sibling-record depth this role reads to the subject's actual
    footprint — a subject with two sibling records needs a light pass,
    one with a dozen needs proportionally more — rather than applying one
    fixed reading depth regardless of how large the subject actually is.
