---
name: technical-writing-doc-type-selection
description: Use when you need guidance on Doc-type selection (Diátaxis). Applies to the doc-type-selection axis.
axis: doc-type-selection
rule_count_floor: 12
---

# Doc-type selection (Diátaxis)

Decision rules for choosing exactly one Diátaxis quadrant per deliverable
(this rulebook's own `produces.doc-type` field). Research trail: layer 2
(named methodology, Diátaxis, verified at source) plus layer 1
(practitioner usage patterns as documented by the framework's own
maintainers and adopting orgs).

## Rules

1. When the reader's stated goal is "I want to learn by doing and have
   no working knowledge yet," choose **tutorial** — a tutorial puts the
   reader "on rails" toward one fixed destination with exact steps and
   no decision points, because a beginner cannot yet evaluate branches.
   source: https://diataxis.fr/start-here/

2. When the reader already has baseline competence and states a
   concrete task ("how do I do X"), choose **how-to guide**, not
   tutorial — how-to guides "help the reader reach a destination of
   their choosing" rather than a fixed one, so branching and
   prerequisites are acceptable where a tutorial would forbid them.
   source: https://diataxis.fr/

3. When the reader is mid-task and needs to look up a fact (a flag, a
   parameter, a field, a limit) rather than be taught, choose
   **reference** — reference is "factual, precise, and structured to
   help find specific details quickly," organized by the product's own
   structure, not by the reader's task sequence. source:
   https://diataxis.fr/

4. When the reader asks "why does it work this way" rather than "how do
   I do X," choose **explanation** — explanation is the only quadrant
   whose job is background/rationale rather than action, and mixing
   task steps into it re-creates the how-to/explanation confusion the
   framework exists to prevent. source: https://diataxis.fr/

5. Under a stated deadline of "first successful call in under 10
   minutes" (an onboarding artifact), choose **tutorial**, not
   reference — reference material assumes the reader can already
   navigate the product's structure, which a brand-new reader cannot;
   documentation that fails this window measurably loses developers to
   alternatives. source:
   https://www.digitalapi.ai/blogs/how-api-documentation-improves-developer-adoption

6. When a single draft's outline mixes conceptual "why" prose with
   numbered action steps, split it into two documents (explanation +
   how-to/tutorial) rather than keep the mixed draft as one — Diátaxis
   treats action-oriented and cognition-oriented content as
   orthogonal axes precisely because a reader mid-task cannot
   efficiently filter out background prose, and a reader seeking
   understanding cannot efficiently filter out step numbering. **REMOVAL**:
   cut whichever half doesn't match the file's own doc-type before
   publishing, don't keep both halves "for completeness." source:
   https://diataxis.fr/

7. When the reader already knows the tool and just needs a parameter's
   exact type/default/range, do not answer with a tutorial-style
   walkthrough — pick reference and drop any narrative framing
   ("First, let's..."), because reference's value is being scannable,
   and narrative framing forces linear reading against the reader's
   actual lookup behavior. source: https://diataxis.fr/

8. When a document was drafted as a tutorial but review shows the
   audience is not actually first-time users (e.g. it's gated behind an
   account they already have), reclassify to how-to and **REMOVE** the
   "on rails"/single-path framing — retaining tutorial framing for an
   audience that already has working knowledge produces exactly the
   condescension the style-guide-compliance axis flags separately.
   source: https://diataxis.fr/start-here/

9. When users progress through a product over time (new → competent →
   expert), do not try to serve every stage from the same document —
   users naturally move tutorial → how-to → reference → explanation as
   competence grows, so a single "one true doc" for a topic under-serves
   both ends; split by stage instead of merging. source:
   https://diataxis.fr/

10. **REMOVAL**: when a topic already has both a how-to guide and a
    reference entry for the same operation, do not add a third
    "overview" doc that restates both — merging duplicate framing
    across quadrants is the specific redundancy the minimalism axis's
    rule 1 also flags; the fix here is to delete the overlapping
    overview draft entirely rather than trim it, since its entire
    content already exists in the other two quadrants. source:
    https://diataxis.fr/ (four-quadrant orthogonality implies no
    quadrant should duplicate another's content)

11. When a deliverable would benefit from a diagram, name explicitly
    whether it optimizes for visual polish (editorial, hand-placed,
    infrequently updated) or for update-cheapness (as-code,
    regenerated whenever the underlying structure changes) — never
    silently default to one. A polish-optimized diagram earns its cost
    only when the underlying structure is stable enough that
    hand-placement won't go stale before the next edit; an
    update-cheap diagram earns its cost whenever the structure is
    still moving. Record the choice in the doc outline before
    drafting, not after a diagram is already placed. Evidence trail:
    docs/issue-1199/reports/technical-writing.md (on-the-record).

12. When a diagram's generation format and its visual style are both
    in play (e.g. a generated diagram that also needs editorial
    polish), treat generation and style as separable steps rather than
    assuming one tool or pass must do both — a diagram can be
    generated in one representation and redrawn into a differently
    constrained visual vocabulary without the two concerns being
    coupled. This is the operational detail for applying rule 11's
    choice when both tradeoffs collide on one deliverable. Evidence
    trail: docs/issue-1199/reports/technical-writing.md
    (on-the-record).
