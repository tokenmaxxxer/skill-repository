---
name: knowledge-management-structure-findability
description: Use when filing a new entry, naming a file or title, or structuring content for retrieval — classifying it as tutorial-, how-to-, reference-, or explanation-shaped per Diátaxis.
metadata:
  axis: structure-findability
  rule_count_floor: 10
---

# Structure and findability (Diátaxis-informed)

Research trail: diataxis.fr (the Diátaxis framework's own reference site), Ubuntu/Canonical's "Diátaxis, a new foundation for Canonical documentation", I'd Rather Be Writing's Diátaxis explainer, and bssw.io's "Diátaxis: A Systematic Approach to Technical Documentation Authoring", all fetched this session.

## Trigger

Apply this skill when filing a new entry, naming a file or entry title,
splitting or combining content by reader need, structuring content for
a search/RAG pipeline, or cross-linking entries.

## Procedure

1. Classify a new entry by the reader need it serves (tutorial, how-to,
   reference, or explanation) and store it under that type rather than
   one flat bucket (rule 1).
2. Recognize a pattern-library entry (per
   [[knowledge-management-pattern-extraction]]) as reference-shaped and
   write/title it for scanning, not narrative flow (rule 2).
3. Name a file or entry so the name states the condition or topic a
   searcher would query for (rule 3).
4. Split a topic that requires both a how-to and an explanation into
   two cross-linked entries rather than one combined document (rule 4).
5. Keep the four Diátaxis quadrants as separate top-level directories or
   clearly distinguishable path prefixes for retrieval-system readers
   (rule 5).
6. Prefer a specific condition-led title over a broad topic-only title
   (rule 6).
7. Cross-link entries at the point where the connection is load-bearing
   for the current rule, not as a bottom-of-file "see also" list
   (rule 7).
8. Keep reference-shaped entries short and self-contained so one entry
   answers one query (rule 8).
9. Strip narrative prose out of a reference-shaped entry into a separate
   explanation-type entry, or drop it if it adds no retrievable fact
   (rule 9).
10. Flatten headings nested more than two or three levels deep purely to
    preserve narrative order, unless the nesting reflects a real
    broader/narrower relationship per
    [[knowledge-management-taxonomy-tagging]] (rule 10).
11. State a fact needed in both a how-to and a reference once, in the
    reference entry, and link to it from the how-to rather than
    duplicating it (rule 11).

## Output shape

A Diátaxis-classified entry (tutorial/how-to/reference/explanation),
condition-led title, placed under its type's path, with load-bearing
cross-links inline rather than a bottom "see also" list.

## Rules

1. When filing a new entry, first classify it by the reader's need it serves (tutorial-shaped: learning by doing; how-to-shaped: achieving a specific task; reference-shaped: looking up a fact; explanation-shaped: understanding why) and store it under that type, rather than one flat "docs" or "notes" bucket — Diátaxis's core claim is that these four needs require different content shapes, and mixing them in one document degrades both the writer's ability to write it well and the reader's ability to find it. source: https://diataxis.fr/

2. When a pattern-library entry (per [[pattern-extraction]]) is being filed, recognize it as reference-shaped, not explanation-shaped — a pattern is looked up by a practitioner mid-task who needs the condition→choice fact quickly, not read start-to-end for understanding; write and title it for scanning (a clear condition-led heading), not for narrative flow. source: https://diataxis.fr/

3. When naming a file or entry, make the name itself state the condition or topic a searcher would query for (e.g. `supersession-lifecycle.md`, not `notes2.md` or `misc-thoughts.md`) — Diátaxis-adjacent practice ties predictable naming directly to retrieval, and this holds doubly for RAG/search-driven retrieval, where the filename and heading are often the only signal a ranking system has before opening the file. source: https://idratherbewriting.com/blog/what-is-diataxis-documentation-framework

4. When a topic requires both a how-to and an explanation (e.g. "how to write a pattern entry" and "why patterns beat raw anecdotes"), split them into two entries with a cross-link rather than one combined document — Diátaxis explicitly warns that combining task-oriented and understanding-oriented content in one place serves neither reader well, since a task-focused reader has to wade past background they didn't ask for and vice versa. source: https://ubuntu.com/blog/diataxis-a-new-foundation-for-canonical-documentation

5. When structuring content for a retrieval system (search index or RAG pipeline reading this repo), keep the four Diátaxis quadrants as separate top-level directories or clearly distinguishable path prefixes rather than interleaving them — the framework's documented advantage for machine retrieval specifically depends on structural predictability being visible in the document's location/heading, not just implied by its prose style. source: https://bssw.io/items/diataxis-a-systematic-approach-to-technical-documentation-authoring

6. When an entry's title could describe either a broad topic or a specific condition, prefer the specific condition — a title that only names the topic ("Tagging") gives a searcher no way to distinguish it from five other entries about the same topic, while a condition-led title ("When two terms always co-occur, merge them") is itself a retrievable, disambiguating summary.

7. When cross-linking entries (e.g. this playbook's own `[[axis-name]]` convention), link at the point where the connection is actually load-bearing for the current rule, not as a blanket "see also" list at the bottom — a link embedded at its point of relevance survives excerpted/chunked retrieval (a RAG system reading one paragraph still sees the link), while a bottom-of-file "see also" list is frequently truncated away by chunking.

8. When an entry is reference-shaped (a rule, a fact, a lookup table), keep entries short and self-contained enough that one entry answers one query — Diátaxis's reference-mode guidance is that reference material should be structured for lookup accuracy, not readability as a whole; a long entry that answers three different questions is three retrieval failures waiting to happen, since a search hit surfaces the whole entry regardless of which question the reader had.

9. **REMOVAL**: When an existing entry mixes tutorial narrative ("first we tried X, then we learned Y") into what is otherwise a reference-shaped rule, strip the narrative out into a separate explanation-type entry (or drop it if it adds no retrievable fact) rather than leaving it inline — narrative prose inside a reference entry dilutes the keyword density a search/RAG system relies on to match the entry to a query, per the same retrieval-structure finding in rule 5. source: https://bssw.io/items/diataxis-a-systematic-approach-to-technical-documentation-authoring

10. **REMOVAL**: When a heading nests more than two or three levels deep purely to preserve an author's original narrative order, flatten it — Diátaxis-adjacent practice ties findability to "consistent formatting, clear hierarchies, and predictable naming," and deep incidental nesting (as opposed to nesting that reflects a real broader/narrower relationship per [[taxonomy-tagging]]) obscures rather than aids the hierarchy a searcher relies on. source: https://idratherbewriting.com/blog/what-is-diataxis-documentation-framework

11. When the same fact needs to appear in both a how-to (as a step) and a reference (as a standalone rule), state it once in the reference entry and link to it from the how-to rather than duplicating the text — duplicated facts drift out of sync silently, and per [[supersession-lifecycle]] rule 1, a superseded fact must be updated in exactly one place for the fix to actually propagate.
