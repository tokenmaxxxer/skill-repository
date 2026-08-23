---
name: technical-writing-structure-comprehension
description: Use when drafting or editing sentence, paragraph, or section structure for reader comprehension and cognitive load. Applies to the structure-comprehension axis.
metadata:
  axis: structure-comprehension
  rule_count_floor: 10
---

# Structure for comprehension (cognitive load)

Decision rules for sentence/paragraph/section structure. Research trail:
layer 3 (academic: cognitive load theory applied to sentence
comprehension, working-memory constraints on reading).

## Trigger

Apply this skill when drafting or editing sentence, paragraph, or
section structure for reader comprehension, distinguishing it from
minimalism-scoping (what content survives) and doc-type-selection
(which quadrant it belongs to) — this axis governs how surviving
content is structured, not what is kept.

## Procedure

1. Target 15-20 words per instructional sentence (rule 1); split a
   sentence carrying more than one independent clause plus a
   conditional (rule 2).
2. Allow a longer sentence where technical detail (a caveat, a
   condition, a threshold) requires it, keeping surrounding sentences
   short (rule 3); bias toward the short end of the range for
   accessibility-sensitive audiences (rule 4).
3. Insert a break (list item, subheading, sentence split) before a
   chunk exceeds ~130-150 characters of new information (rule 5).
4. When editing a long sentence, first try deleting subordinate
   clauses that don't change what the reader does next, before
   restructuring into multiple sentences (rule 6).
5. Group a procedure of more than ~7 sequential steps under
   subheadings by phase rather than one flat list (rule 7).
6. When subject and main verb are separated by a long embedded clause,
   rewrite so they sit close together (rule 8).
7. Substitute a common synonym for a rare/technical word with no loss
   of precision (rule 9).
8. Delete hedge or filler clauses outright rather than compress them,
   as a separate pass from rule 6's clause deletion (rule 10).

## Output shape

A structurally revised passage: sentences within the target length
range, chunks broken at the size threshold, long procedures grouped by
phase, and filler/subordinate clauses removed per the applicable
rules.

## Rules

1. When drafting an instructional sentence, target roughly 15-20 words —
   "the Oxford guide to plain English recommends sentences of 15 to 20
   words," and sentence length in words correlates negatively with
   readability across a century of studies. source:
   https://www.trinka.ai/blog/how-sentence-length-variation-improves-academic-readability/

2. When a sentence carries more than one independent clause plus a
   conditional, split it into two sentences — "longer sentences can be
   harder to process because they contain more ideas, clauses, and
   complex structures," and working memory is the bottleneck cognitive
   load theory identifies, not vocabulary difficulty alone. source:
   https://readabilityformulas.com/how-to-measure-cognitive-reading-load-to-improve-readability-of-any-text/

3. When a passage must carry technical detail (a caveat, a condition, a
   numeric threshold), allow a longer sentence there but keep the
   surrounding sentences short — sentence-length variation "supports
   chunking, with shorter sentences giving clean stopping points," so
   uniform shortening isn't the goal, controlled variation is. source:
   https://www.trinka.ai/blog/how-sentence-length-variation-improves-academic-readability/

4. When writing for readers who may be non-native speakers, using
   assistive tech, or have attention/reading disabilities, bias toward
   the short end of the 15-20 word range — shorter sentences
   "particularly benefit[] people with dyslexia, ADHD, non-native
   English speakers, and screen reader users," so accessibility need
   tightens this rule rather than relaxing it. source:
   https://www.siteimprove.com/blog/readability-plain-language-wcag/

5. When a single paragraph or chunk risks holding more than
   ~130-150 characters of new information before the next natural
   break, insert a break (list item, subheading, or sentence split) —
   text chunks in that range were found "the most appropriate length to
   enhance learners' text comprehension," correlated with working-memory
   capacity limits. source:
   https://readabilityformulas.com/how-to-measure-cognitive-reading-load-to-improve-readability-of-any-text/

6. **REMOVAL**: when editing a long sentence for comprehension, first try
   deleting subordinate clauses that don't change what the reader does
   next, before restructuring the sentence into multiple shorter ones —
   the cognitive-load fix is fewer ideas per sentence, and deletion
   reduces idea-count without adding new sentences to track. source:
   https://readabilityformulas.com/how-to-measure-cognitive-reading-load-to-improve-readability-of-any-text/

7. When a procedure has more than ~7 sequential steps, group them under
   subheadings by phase rather than leave one flat numbered list — this
   mirrors the same chunking rationale as rule 5 applied at the
   section level, not just the sentence level: working memory is the
   limiting resource at every granularity of the document. source:
   https://readabilityformulas.com/how-to-measure-cognitive-reading-load-to-improve-readability-of-any-text/

8. When a sentence's syntactic subject and its main verb are separated
   by a long embedded clause (long linear distance / high structural
   density), rewrite so subject and verb sit close together — memory
   load in sentence comprehension is driven by both linear distance and
   structural density between dependent elements, not sentence length
   alone. source: https://arxiv.org/pdf/2509.20916

9. When a draft uses a rare or highly technical word where a common
   synonym exists with no loss of precision, substitute the common
   word — "familiar words reduce processing time," an independent lever
   from sentence length. source:
   https://www.siteimprove.com/blog/readability-plain-language-wcag/

10. **REMOVAL**: when a sentence contains a hedge or filler clause ("it
    should be noted that," "in order to") that adds words without adding
    an idea, delete it outright rather than compress it — this is
    distinct from rule 6 (structural clause deletion): rule 6 targets
    subordinate content clauses, this targets zero-information filler
    phrasing, so both passes are needed on a dense draft. source:
    https://www.trinka.ai/blog/how-sentence-length-variation-improves-academic-readability/

## Related skills

- [technical-writing-doc-type-selection](../technical-writing-doc-type-selection/SKILL.md) — structure rules assume the doc-type quadrant was already fixed by doc-type-selection.
