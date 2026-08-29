---
name: technical-writing-minimalism-scoping
description: >-
  Use when deciding what to cut vs. keep in a draft section, or auditing an
  over-long doc for redundant or unrequested content. Applies to the
  minimalism-scoping axis — subtraction-first passes, duplicate removal,
  collapsing edge cases, with error-recovery content as the named exception.
  Trigger on requests like "문서 너무 길어, 줄여줘", "cut this doc down", "subtraction
  pass", "remove redundant sections". Do NOT use for choosing which Diátaxis
  quadrant the doc belongs to (use technical-writing-doc-type-selection) or for
  how surviving content is structured sentence by sentence (use
  technical-writing-structure-comprehension).
metadata:
  axis: minimalism-scoping
  rule_count_floor: 11
---

# Minimalism / scoping

Decision rules for what to include vs. cut per section (this skill spec's
`produces.minimalism check` field). Research trail: layer 1 (practitioner
depth per John Carroll's minimalist-instruction canon) plus layer 3
(academic: subtraction neglect, cognitive-load/extraneous-load theory).

## Trigger

Apply this skill when deciding what to include vs. cut in a draft
section, or when a doc has grown over-long and needs a subtraction
pass, distinguishing it from doc-type-selection (which quadrant a doc
belongs to) and structure-comprehension (how kept content is
organized).

## Procedure

1. Scan for restated information already stated earlier in the doc or
   a linked doc; remove the restatement and link instead (rule 1).
2. Scan for background the reader doesn't need for the immediate task;
   move it to an explanation doc or a collapsed aside (rule 2).
3. When drafting a first version, write task-oriented steps first and
   add explanation only where a reviewer flags a specific gap (rule
   3).
4. Group advanced/edge-case options behind a labeled, collapsed
   subsection rather than inlining them into the main procedure (rule
   4).
5. When shortening an over-long draft, run a dedicated cut-search pass
   before or separate from a compression/line-edit pass (rule 5).
6. Delete purely definitional sections with no attached task or
   decision (rule 6).
7. When both a subtractive and an additive fix are available for the
   same comprehension problem, evaluate the subtractive option first
   (rule 7).
8. Centralize recurring boilerplate in one linked location instead of
   duplicating it across docs (rule 8).
9. Cut a paragraph that took effort to write but doesn't change what
   the reader does next (rule 9).
10. Add missing error-recovery content even though this axis otherwise
    biases toward cutting — name it as the deliberate exception (rule
    10).
11. When producing an editorial-style diagram, cap it to one accent
    color, 1-2 focal elements, and a small fixed typeface set (rule
    11).

## Output shape

A scoped section or doc with duplicate/unrequested/definitional
content removed, boilerplate centralized, and — per rule 10 — any
missing error-recovery content added as the named exception to the
otherwise cut-biased pass.

## Rules

1. When a draft section restates information already stated earlier in
   the same doc or in a linked doc, **REMOVE** the restatement and link
   instead — duplicate information "makes the page more dense with text
   but not with information," and progressive disclosure's value is
   destroyed once duplicated content forces the reader to re-verify
   which copy is current. source:
   https://www.algolia.com/blog/ux/information-density-and-progressive-disclosure-search-ux

2. When a section explains background the reader does not need to
   complete the immediate task, move it to an explanation doc or a
   collapsed/linked aside rather than inline it — Carroll's minimalism
   principle is "the smallest amount of information necessary to
   achieve the reader's goals," and unrequested background is exactly
   the surplus that principle targets. source:
   https://en.wikipedia.org/wiki/Minimalism_(technical_communication)

3. When drafting a first version of any procedure, default to writing
   the task-oriented steps first and add explanatory prose only where a
   reviewer flags a specific comprehension gap — Carroll found
   "training materials should present short task-oriented chunks, not
   lengthy, monolithic documentation," so explanation should be pulled
   in reactively, not drafted in by default. source:
   https://www.researchgate.net/publication/3229757_John_Carroll's_The_Nurnberg_Funnel_and_Minimalist_Documentation

4. When advanced/edge-case options exist alongside a common path, do not
   inline them into the main procedure — group them behind a labeled,
   collapsed subsection (progressive disclosure) so the common path
   stays short; multiple advanced-feature levels should nest into
   meaningful categories rather than flatten into one long list. source:
   https://www.webfx.com/blog/web-design/progressive-disclosure-in-user-interfaces/

5. When you are deciding how to shorten an over-long draft, actively
   search for content to CUT, not just content to compress — people
   "systematically default to searching for additive transformations
   and consequently overlook subtractive transformations," and this
   default gets worse "under higher cognitive load" (i.e., exactly when
   editing a dense draft), so cutting must be a deliberate, separate
   pass, not a byproduct of line-editing. source:
   https://www.nature.com/articles/s41586-021-03380-y

6. **REMOVAL**: when a draft outline has a section whose only content is
   definitional ("X is a mechanism that...") with no task or decision
   attached to it, delete the section rather than shrink it — a
   glossary-shaped paragraph inside a task-oriented doc adds surface
   area without adding actionable information, the same defect this
   program's depth-gate rejects in playbook rule blocks. source:
   https://www.researchgate.net/publication/3229757_John_Carroll's_The_Nurnberg_Funnel_and_Minimalist_Documentation

7. When a subtractive edit is available (delete a redundant paragraph)
   and an additive edit is also available (add a clarifying sentence)
   for the same comprehension problem, evaluate the subtractive option
   first and explicitly — explicitly reminding yourself that subtraction
   is on the table, or "putting a cost on adding parts while making
   removing parts free," measurably increases the rate at which
   subtractive fixes actually get chosen. source:
   https://sciencedaily.com/releases/2021/04/210407135801.htm

8. When boilerplate content (standard disclaimers, repeated setup steps)
   recurs across many docs, **REMOVE** it from each doc and centralize it
   in one linked location instead of leaving N copies — "consolidating
   redundant instructions and filtering recurring boilerplate content"
   is named directly as an extraneous-cognitive-load fix. source:
   https://arxiv.org/pdf/2605.19174

9. When a review finds a paragraph that took effort to write but does
   not change what the reader does next, cut it even though cutting
   feels like a loss of invested effort — minimalism's target is
   reader-goal alignment, not authorial completeness; the doc's
   quality bar is what remains being justified by the target-reader
   note, not by how much was written. source:
   https://en.wikipedia.org/wiki/Minimalism_(technical_communication)

10. When error-recovery content is missing (the user hits a failure and
    the doc has no path back), add it even though this axis otherwise
    biases toward cutting — Carroll's principle set explicitly requires
    "training materials and activities... provide for error recognition
    and recovery," so this is the one place the minimalism axis calls
    for addition, and it should be named as the deliberate exception
    rather than silently contradicting rules 1-9. source:
    https://www.instructionaldesign.org/theories/minimalism/

11. When producing an editorial-style diagram (doc-type-selection.md
    rule 11's polish branch), cap it to one accent color and 1-2 focal
    elements, hold to a small fixed set of typefaces, and avoid
    decorative shadow/gradient noise — visual-discipline constraints
    like these exist to suppress diffuse, over-decorated output, and
    the same over-decoration failure mode applies to any editorial
    diagram this skill produces; minimalism applies to visual surface
    the same way it applies to prose. Evidence trail:
    docs/issue-1199/reports/technical-writing.md (on-the-record).
