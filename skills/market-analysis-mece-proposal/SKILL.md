---
name: market-analysis-mece-proposal
description: >-
  Use when structuring a phase-1 proposal's required elements to check for content overlap
  between sections, choosing a MECE split for the analysis, or verifying the section set is
  collectively exhaustive against the rulebook's required-elements field. Applies to the
  mece-proposal axis. Trigger on requests like "제안서 섹션 구조 MECE하게 잡아줘", "do these sections
  overlap", "is the proposal missing a required element", "re-cut this issue tree". Do NOT
  use for judging whether the claims inside a section are properly sourced (use
  market-analysis-evidence-rigor).
metadata:
  axis: mece-proposal
  rule_count_floor: 10
---

# MECE-structuring rules (phase-1 proposal)

Decision rules for structuring the phase-1 proposal's 5 required
elements (decision framed, frameworks selected + why, evidence plan,
adoption rationale, plugin-reflection plan) so the set is mutually
exclusive and collectively exhaustive. Research trail: layer 2 (Barbara
Minto's MECE principle, verified at source) plus layer 1 (practitioner
issue-tree structuring practice).

## Trigger

Apply this skill when drafting or reviewing a phase-1 proposal's
section structure, choosing how to split the analysis, or checking the
proposal against the rulebook's 5 required elements for overlap or
gaps.

## Procedure

1. When drafting the section list, check each pair of sections for
   content overlap and merge or reassign overlapping facts rather than
   let them be restated in two places (rule 1).
2. When a frameworks-selected section lists a framework with no "why,"
   treat that as an exhaustiveness gap, not a style nit (rule 2).
3. When choosing how to split the analysis, prefer a fastest reliable
   MECE split (two-part, formula-based, process-step, or explicit
   "other" bucket) over an ad hoc list (rule 3).
4. When the same source justifies claims in two sections, cite it once
   in the owning section and cross-reference by name rather than
   duplicate the citation (rule 4).
5. When structuring as an issue tree, keep sibling branches independent
   and re-cut the structure if one sub-question needs another's answer
   first (rule 5).
6. When the plugin-reflection element has no corresponding gate or
   plugin named elsewhere in the proposal, flag it as a collective-
   exhaustiveness gap (rule 6).
7. When a draft section restates a decision already framed earlier, cut
   the restatement rather than keep it for emphasis (rule 7).
8. When two required elements genuinely share unavoidable context, do
   not force an artificial split — state the shared dependency once and
   reference it (rule 8).
9. When checking collective exhaustiveness, verify against the
   rulebook's own PRODUCES field's 5 named elements, not against
   recollection (rule 9).
10. When an "other" bucket accumulates more than a small fraction of
    content, split it into properly named sub-elements rather than
    leave it as a catch-all (rule 10).

## Output shape

A proposal whose sections carry no cross-section content overlap, each
required element paired with its rationale, an explicit MECE split
choice, and full coverage of the rulebook's 5 named elements verified
against the PRODUCES field.

## Rules

1. When drafting the proposal's element list, check each pair of
   sections for content overlap first — if the same fact or judgment
   would need to be restated in two sections, merge them or move the
   fact to whichever section owns it, because overlapping buckets is
   exactly what "mutually exclusive" forbids. source:
   https://en.wikipedia.org/wiki/MECE_principle
2. When a proposal's frameworks-selected section lists a framework with
   no accompanying "why," treat that as a MECE-exhaustiveness gap, not a
   style nit — the required element is "frameworks selected + why," and
   a bare list without rationale does not satisfy the "why" half of the
   pairing. source: docs/issue-1174/proposals/operational-playbook-program.md
   (this rulebook's own governing role-directive, `PRODUCES` field)
3. When choosing how to split the analysis into sections, prefer the
   fastest reliable MECE splits named in practitioner guidance —
   two-part splits, formula-based splits (e.g. TAM = SAM + SOM),
   process-step splits, or an explicit "other" bucket — over an ad hoc
   list assembled from whatever facts were gathered first.
   source: https://slideworks.io/resources/mece-mutually-exclusive-collectively-exhaustive
4. When the evidence plan section and the adoption-rationale section
   both cite the same source to justify different claims, do not
   duplicate the citation block — cite it once in whichever section the
   claim primarily belongs to and cross-reference by name from the
   other, keeping each section's content mutually exclusive.
   source: https://en.wikipedia.org/wiki/MECE_principle
5. When building the proposal as an issue tree (decision → sub-questions
   → evidence), keep sibling branches independent of each other — if
   answering one sub-question requires knowing another sibling's answer
   first, they are not properly separated and the branch structure needs
   re-cutting before drafting prose. source:
   https://caseinterview.com/mece
6. When the "plugin-reflection plan" element has no corresponding gate
   or plugin named anywhere else in the proposal, flag the proposal as
   not collectively exhaustive — reflection is one of the 5 required
   elements and an empty or vague plan leaves a gap in the coverage,
   not just a thin section. source:
   docs/issue-1174/proposals/operational-playbook-program.md
7. **REMOVAL**: when a draft section restates the decision already
   framed in the "decision framed" element using different words later
   in the document (e.g. a redundant "why this matters" paragraph before
   the evidence plan), cut the restatement rather than keep it for
   emphasis — MECE structuring treats restating an already-covered
   bucket as exactly the redundancy the principle exists to eliminate.
   source: https://strategyu.co/wtf-is-mece-mutually-exclusive-collectively-exhaustive/
8. When perfect MECE cannot be achieved because two required elements
   genuinely share unavoidable context (e.g. evidence plan and adoption
   rationale both depend on the same market-data source), do not force
   an artificial split — practitioner guidance treats perfect MECE as an
   aspiration, not an absolute; state the shared dependency once and
   reference it, rather than duplicating or awkwardly forcing exclusivity.
   source: https://www.myconsultingoffer.org/case-study-interview-prep/mece/
9. When checking collective exhaustiveness, verify against the
   rulebook's own `PRODUCES` field (the 5 named elements) as the
   checklist, not against whatever the analyst remembers writing —
   a proposal missing one of the 5 named elements fails exhaustiveness
   even if every present section is well-written. source:
   docs/issue-1174/proposals/operational-playbook-program.md
10. When an "other" or miscellaneous bucket accumulates more than a
    small fraction of the proposal's content, treat that as a signal the
    real categories were mis-cut — split the miscellaneous bucket into
    properly named sub-elements rather than leaving it as a catch-all,
    since a bloated "other" bucket is the practitioner-named failure mode
    of a MECE split done too coarsely. source:
    https://slideworks.io/resources/mece-mutually-exclusive-collectively-exhaustive
