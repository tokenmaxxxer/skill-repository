---
name: devrel-content-comprehensibility
description: Use when shaping developer-facing content for comprehension — sizing new-concept chunks, deciding whether to re-explain or link a foundational concept, avoiding split-attention across sources, trimming a getting-started path, choosing sample idioms for a reader's skill level, or splitting content by audience competence.
axis: content-comprehensibility
rule_count_floor: 8
---

# Content comprehensibility (cognitive load / schema theory)

## Trigger

Apply this skill when shaping developer-facing content for
comprehension — introducing a new concept in onboarding content,
deciding whether to re-explain or link a foundational concept, laying
out a tutorial that spans multiple sources, trimming a getting-started
path, choosing sample idioms for a reader's skill level, deduplicating a
concept across a tutorial and a reference page, retiring a stale code
path from a sample, or splitting content for novice vs. expert
audiences.

## Procedure

1. Present no more than about 4-7 new distinct pieces of information in
   one onboarding section; move anything past that into a separate
   step (rule 1).
2. Do not re-explain a foundational concept inline for a reader already
   fluent in it; link out instead (rule 2).
3. Consolidate a tutorial step's code block and its parameter table
   into the same place instead of cross-referencing across pages
   (rule 3).
4. Cut prerequisite and background material out of a getting-started
   path exceeding about 10 minutes to first success, moving it to an
   appendix or reference link (rule 4).
5. Use only the language idioms and API surface a first-time reader's
   stated skill level already has as schema; do not introduce an
   advanced feature and a new API concept in the same quickstart sample
   (rule 5).
6. When the same concept appears in a tutorial and a reference page,
   give the tutorial a short pointer to the reference's canonical
   definition instead of restating the explanation (rule 6).
7. Delete an older, no-longer-recommended code path from a sample
   repository rather than leaving it commented out or marked
   deprecated inline (rule 7).
8. Split content serving both a novice and an expert audience by
   competence stage instead of writing one document for both (rule 8).

## Output shape

A content-shaping decision (chunk size, re-explain-vs-link, co-location
vs. cross-reference, path length, sample idiom level, tutorial/reference
dedup, dead-path removal, or audience split) attributed to the rule
that drove it, sized to the target reader's existing schema.

Research trail: layer 3 (academic — cognitive load theory,
working-memory capacity, schema acquisition) plus layer 1 (practitioner
onboarding-speed data).

## Rules

1. When onboarding content introduces a new API concept, present no
   more than about 4-7 new distinct pieces of information (parameters,
   steps, or concepts) in one section, and move anything past that into
   a separate step — working memory reliably holds only a small number
   of discrete items at once, so a section that exceeds this range
   overloads the reader before they reach the concept the section
   exists to teach. source:
   https://www.instructionaldesign.org/theories/cognitive-load/

2. When the target reader is already fluent in the language or
   framework a sample uses, do not re-explain the foundational concept
   inline — link out to it instead. Fluent readers hold that concept as
   a schema, a single treatable unit in long-term memory, and
   re-explaining it forces working memory to reprocess knowledge that
   is already automated, which is pure extraneous load with no
   comprehension benefit. source:
   https://www.instructionaldesign.org/theories/cognitive-load/

3. When a tutorial step requires the reader to hold information from
   two separated sources at once (a code block on one page and a
   parameter table on another) to complete that step, consolidate both
   into the same place instead of cross-referencing — this is the
   split-attention effect: when related information is separated in
   space, working memory must bridge the gap itself, which measurably
   degrades comprehension versus co-located material. source:
   https://medium.com/the-comprehension-engineer/cognitive-load-theory-and-technical-writing-a-foundation-for-better-documentation-2d805fbc41e3

4. **REMOVAL**: when a getting-started guide's path to a first
   successful call takes longer than about 10 minutes of reading,
   cut prerequisite and background material out of that path and move
   it to an appendix or reference link rather than leave it inline — a
   slow first success measurably loses developers to alternatives, so
   the fastest fix is subtracting the detour, not writing a clearer
   version of it. source:
   https://www.digitalapi.ai/blogs/how-api-documentation-improves-developer-adoption

5. When writing a code sample for a first-time reader, use only the
   language idioms and API surface that reader's stated skill level
   already has as schema — do not introduce an advanced language
   feature and a new API concept in the same quickstart sample.
   Introducing two unfamiliar things at once means neither has an
   existing schema to absorb it, so both compete for the same limited
   working-memory capacity simultaneously. source:
   https://www.instructionaldesign.org/theories/cognitive-load/

6. When the same concept must appear in both a tutorial and a reference
   page, do not restate the full explanation in both — give the
   tutorial a short pointer to the reference's canonical definition.
   This is the redundancy effect from cognitive load research: repeated
   explanation across contexts does not reliably reinforce memory, it
   inflates the material the reader must process to reach the point of
   the tutorial. source:
   https://education.nsw.gov.au/content/dam/main-education/about-us/educational-data/cese/2017-cognitive-load-theory.pdf

7. **REMOVAL**: when a sample repository has accumulated an older code
   path that is no longer the recommended pattern, delete it from the
   sample rather than leave it commented out or marked "deprecated"
   inline — a first-time reader has no schema yet for distinguishing
   signal from noise, so an extraneous branch consumes working memory
   before the reader can even identify it as irrelevant. source:
   https://www.instructionaldesign.org/theories/cognitive-load/

8. When a single piece of content must serve both a novice audience and
   an expert audience, split it by competence stage (a tutorial for the
   novice path, a reference or explanation for the expert path) instead
   of writing one document to cover both — schema-holders and
   non-schema-holders need different amounts of scaffolding for the
   same material, so one document calibrated for either stage
   under-serves or overloads the other. source:
   https://www.instructionaldesign.org/theories/cognitive-load/
</content>
