---
name: technical-writing-doc-type-selection
description: >-
  Use when choosing which Diátaxis quadrant a deliverable should be, or auditing
  a draft that mixes more than one quadrant's content. Applies to the
  doc-type-selection axis. Trigger on requests like "tutorial vs how-to 뭐로 써야
  해", "which doc type is this", "Diátaxis quadrant", "this draft mixes reference
  and tutorial". Do NOT use for deciding what to cut once the doc-type is fixed
  (use technical-writing-minimalism-scoping); for routing general prose style by
  reader background knowledge rather than picking a documentation quadrant,
  prose-modes is the alternative.
metadata:
  axis: doc-type-selection
  rule_count_floor: 12
---

# Doc-type selection (Diátaxis)

Decision rules for choosing exactly one Diátaxis quadrant per deliverable
(this rulebook's own `produces.doc-type` field). Research trail: layer 2
(named methodology, Diátaxis, verified at source) plus layer 1
(practitioner usage patterns as documented by the framework's own
maintainers and adopting orgs).

## Trigger

Apply this skill when choosing which Diátaxis quadrant (tutorial,
how-to guide, reference, explanation) a deliverable — or a diagram
inside one — should be, or when auditing a draft whose outline mixes
more than one quadrant's content, distinguishing it from
minimalism-scoping (what to cut once the doc-type is fixed) and
structure-comprehension (how to organize within the chosen type).

## Procedure

1. Identify the reader's stated goal (learn by doing, do a concrete
   task, look up a fact, or understand why) and map it to a quadrant:
   learn-by-doing → tutorial (rule 1), concrete task → how-to guide
   (rule 2), lookup → reference (rule 3), why → explanation (rule 4).
2. If a deadline constraint (e.g. "first successful call in under 10
   minutes") is stated, override toward tutorial rather than reference
   for a brand-new reader (rule 5).
3. If a single outline mixes conceptual "why" prose with numbered
   action steps, split it into two documents and cut the half that
   doesn't match each file's own doc-type (rule 6).
4. If the reader already knows the tool, drop narrative framing and
   answer as reference, not tutorial (rule 7).
5. If review shows a drafted tutorial's audience already has working
   knowledge, reclassify to how-to and remove "on rails" framing (rule
   8).
6. As a user's competence grows within a product, expect and plan for
   separate documents per stage rather than one document serving all
   stages (rule 9).
7. If a topic already has both a how-to guide and a reference entry
   for the same operation, delete an overlapping "overview" draft
   rather than trim it (rule 10).
8. When a deliverable would benefit from a diagram, name explicitly
   whether it optimizes for visual polish or update-cheapness before
   drafting (rule 11), and treat generation format and visual style as
   separable steps when both are in play (rule 12).

## Output shape

One doc-type classification (tutorial, how-to guide, reference, or
explanation) per deliverable, or a split into multiple deliverables
when rule 6 or rule 10 fires, plus — when a diagram is involved — an
explicit polish-vs-update-cheapness choice recorded in the outline.

## Related skills

- [technical-writing-structure-comprehension](../technical-writing-structure-comprehension/SKILL.md) — once a doc's Diátaxis quadrant is chosen, structure-comprehension governs sentence/paragraph-level shape within it.

## Rule index

Full rule text, citations, and counter-examples:
`references/rules.md` in this skill's directory — read it when a
matched rule's detail is needed.

- 1.1 — When the reader's stated goal is "I want to learn by doing and have no working knowledge yet," choose **tutorial** — a tutorial puts the reader "on rails" toward one fix…
- 1.2 — When the reader already has baseline competence and states a concrete task ("how do I do X"), choose **how-to guide**, not tutorial — how-to guides "help the reader reac…
- 1.3 — When the reader is mid-task and needs to look up a fact (a flag, a parameter, a field, a limit) rather than be taught, choose **reference** — reference is "factual, prec…
- 1.4 — When the reader asks "why does it work this way" rather than "how do I do X," choose **explanation** — explanation is the only quadrant whose job is background/rationale…
- 1.5 — Under a stated deadline of "first successful call in under 10 minutes" (an onboarding artifact), choose **tutorial**, not reference — reference material assumes the read…
- 1.6 — When a single draft's outline mixes conceptual "why" prose with numbered action steps, split it into two documents (explanation + how-to/tutorial) rather than keep the m…
- 1.7 — When the reader already knows the tool and just needs a parameter's exact type/default/range, do not answer with a tutorial-style walkthrough — pick reference and drop a…
- 1.8 — When a document was drafted as a tutorial but review shows the audience is not actually first-time users (e.g. it's gated behind an account they already have), reclassif…
- 1.9 — When users progress through a product over time (new → competent → expert), do not try to serve every stage from the same document — users naturally move tutorial → how-…
- 1.10 — **REMOVAL**: when a topic already has both a how-to guide and a reference entry for the same operation, do not add a third "overview" doc that restates both — merging du…
- 1.11 — When a deliverable would benefit from a diagram, name explicitly whether it optimizes for visual polish (editorial, hand-placed, infrequently updated) or for update-chea…
- 1.12 — When a diagram's generation format and its visual style are both in play (e.g. a generated diagram that also needs editorial polish), treat generation and style as separ…
