---
name: technical-writing-style-guide-compliance
description: >-
  Use when reviewing or drafting prose for Google Developer Documentation Style
  Guide compliance — mood, voice, person, tone, word choice. Applies to the
  style-guide-compliance axis — imperative mood in steps, active voice with
  named actors, second person present tense, "please" stripping, first-use
  jargon glosses. Trigger on requests like "구글 스타일 가이드에 맞춰줘", "style guide
  compliance check", "imperative mood로 고쳐줘", "active voice pass". Do NOT use for
  sentence-length and chunking decisions driven by cognitive load rather than
  guide conformance (use technical-writing-structure-comprehension).
metadata:
  axis: style-guide-compliance
  rule_count_floor: 11
---

# Style-guide compliance (Google Developer Documentation Style Guide)

Decision rules for the `produces.style-guide compliance note` field.
Research trail: layer 2 (named standard, verified at source:
developers.google.com/style, plus the Federal plain-language guidelines
as a second named standard for corroboration/conflict-checking).

## Trigger

Apply this skill when writing or reviewing prose for compliance with
the Google Developer Documentation Style Guide (mood, voice, person,
tone, word choice, formatting of complex material), distinguishing it
from structure-comprehension, which governs sentence/section shaping
for cognitive load rather than style-guide conformance.

## Procedure

1. Check instruction steps for imperative mood, not descriptive mood
   (rule 1); check actor-driven sentences for active voice with the
   actor as subject (rule 2).
2. Check reader address for second person, present tense (rule 3).
3. Check word choice against the guide's preferred/discouraged word
   list (rule 4); check tone for the "knowledgeable friend" register,
   flagging both stiff/formal and overly playful extremes (rule 5).
4. Check instructions for unnecessary "please" padding and strip it
   from routine steps, keeping it only for real-cost/destructive
   actions (rule 6).
5. For a legal/government-adjacent doc, cross-check active-voice
   enforcement against the Federal Plain Language Guidelines and
   record convergence (rule 7).
6. Restructure material with more than ~3 parallel conditions or
   options as a bulleted list or table (rule 8).
7. When a passive-voice sentence with no named actor is found, rewrite
   to name the actor rather than partially soften it (rule 9).
8. When a necessary term is jargon to the target reader, keep it but
   add a first-use gloss (rule 10).
9. Where the repo has an executable style check (a linter rule, a CI
   lint config), cite it over a prose-only compliance claim; name the
   gap explicitly when none exists (rule 11).

## Output shape

A style-guide compliance note per reviewed passage: pass/fail per rule
category (mood, voice, person, tone, word choice, formatting), with
flagged deviations rewritten rather than merely noted, and — where
available — a pointer to the executable check backing the claim.

## Rules

1. When writing an instruction step, use imperative mood ("Click
   Submit"), not descriptive mood ("You should click Submit" / "The
   user clicks Submit") — the style guide instructs writers to "use the
   imperative mood to guide the reader effectively." source:
   https://developers.google.com/style

2. When a sentence has an actor performing an action, write it in
   active voice with the actor as subject — "use active voice: make
   clear who's performing the action" — because passive voice hides the
   actor exactly where a reader needs to know who/what does the work.
   source: https://developers.google.com/style

3. When addressing the reader, use second person ("you") and present
   tense, not third person or future tense — this is a named,
   consistent convention across the guide's person/tense sections, and
   switching person mid-doc is a compliance deviation to flag. source:
   https://developers.google.com/style/person?hl=en

4. When choosing a term that has a preferred/discouraged pair in the
   guide's word list (e.g. avoid ableist or unclear terms), use the
   word-list entry's preferred form — the word list exists specifically
   so writers don't re-derive terminology choices per document. source:
   https://developers.google.com/style/word-list

5. When tone risks becoming either stiff/formal or overly playful,
   target "conversational, friendly, and respectful without... slang or
   being overly colloquial" — like "a knowledgeable friend," not
   "pedantic or pushy" and not "super-entertaining." Both extremes are
   named failure modes, not just "be more casual." source:
   https://developers.google.com/style/tone

6. When an instruction could be phrased as a request ("Please click
   Submit") or a direct command ("Click Submit"), prefer the direct
   command and drop "please" — the guide calls for "ensur[ing]
   politeness without overusing 'please' in instructions," so
   politeness padding on every step is itself a deviation. **REMOVAL**:
   strip "please" from routine steps; keep it only where an action has
   real cost to the reader (e.g. destructive operations). source:
   https://developers.google.com/style/tone

7. When a legal/government-adjacent doc needs a second corroborating
   source for active-voice enforcement, cross-check against the Federal
   Plain Language Guidelines: "in an active sentence, the person or
   agency that's acting is the subject," matching Google's own rule —
   record convergence (no conflict) rather than picking one arbitrarily
   when both style authorities agree. source:
   https://github.com/GSA/plainlanguage.gov/blob/main/_pages/guidelines/conversational/use-active-voice.md

8. When complex material has more than ~3 parallel conditions or
   options, restructure it as a bulleted list or table rather than a
   run-on sentence — plain-language guidance names "bullets and tables"
   for "complex material" as a distinct design feature, not just a
   formatting preference. source: https://digital.gov/guides/plain-language

9. **REMOVAL**: when a passive-voice sentence is found in review and no
   actor is named, do not just "soften" it — rewrite to name the actor
   and delete the passive construction outright; a partial fix (passive
   sentence trimmed for length but left passive) does not satisfy this
   axis's rule 2. source: https://developers.google.com/style

10. When a term is genuinely necessary but jargon to the target reader
    (per the target-reader note), keep the term but add a first-use
    gloss rather than either (a) silently using it unglossed or (b)
    avoiding the correct technical term altogether — "common, everyday
    words except for necessary technical terms" licenses jargon only
    when paired with explanation, not as an either/or choice. source:
    https://digital.gov/guides/plain-language

11. When the accuracy-review-evidence field would otherwise stay
    advisory prose only, prefer citing or pointing to an executable
    check (a style-linter rule file, a lint config run in CI) over a
    prose-only compliance claim, where the repo has one; name the gap
    explicitly when it doesn't. A style guide compiled into
    machine-checkable rules run in CI is strictly stronger evidence
    than a reviewer's prose assertion, because it re-verifies on every
    change instead of only at review time — the same "compile the
    rule instead of restating it" move this axis's other rules already
    apply to word-list and tone judgments. Evidence trail:
    docs/issue-1199/reports/technical-writing.md (on-the-record).
