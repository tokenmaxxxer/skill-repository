---
Subject: issue-50
---

# Scout brief: design-artifact skill family

Mode: parallel WebSearch fan-out (4 angles: NN/g storyboards, NN/g IA,
NN/g user-flow/journey, ISO 9241-210), 1 sweep stage + 1 deepening stage
(WebFetch on the two thinnest angles + one search-only angle for
HTML-demo, which the sweep didn't cover). 2 stages total, well under
budget; stopped at saturation — a third round would not change which
axis each skill covers.

## Must-bes (category-wide, from the field)

- Storyboard: a sequence of panels chronologically mapping a user
  story's main events — not a single static screen (NN/g).
- IA: structure driven by how users actually seek information (card
  sorting / mental models), not by org chart; the "3-click rule" is a
  myth NN/g explicitly refutes — depth is fine if labels carry clear
  information scent (NN/g IA study guide).
- User flow vs. user journey are distinct artifacts, not
  interchangeable terms: flow = micro, single-product, steps+system
  responses only; journey = macro, multi-channel, includes
  emotions/thoughts over days-to-months (NN/g).
- ISO 9241-210 HCD process: context-of-use description, user-group
  profiles, and scenarios/personas are produced BEFORE design solutions
  are drafted, then requirements are refined iteratively via
  scenarios + prototypes with user feedback.
- HTML demo: semantic elements (header/nav/main/article/section/footer/
  button/a/label, single h1, no skipped heading levels) carry built-in
  accessible roles/keyboard behavior for free — this is the accessible
  default, not an add-on (MDN).

## Performance axes (2-3 the field competes on)

1. Fidelity-to-purpose: does the artifact match its intended scope
   (flow ≠ journey; storyboard ≠ wireframe) rather than being used as a
   generic catch-all.
2. Structural correctness: IA depth/breadth and labeling judged by
   findability evidence (card sort / task completion), not aesthetic
   preference; HTML demo judged by semantic-element choice, not visual
   fidelity alone.
3. Traceability to real users: scenarios/personas grounded in
   context-of-use research (ISO 9241-210), not invented personas.

## Adopt / skip

- Adopt: NN/g's flow-vs-journey scope distinction as the trigger-line
  differentiator between the user-flow and user-scenario skills (avoids
  overlap collapse the family risks).
- Adopt: ISO 9241-210's ordering (context → requirements → design →
  evaluate, iterative) as the procedural backbone for both
  user-scenario and the family's overall Output shape guidance.
- Skip: card-sorting/tree-testing as a research *method* deep-dive —
  out of scope for issue #50 (which asks for artifact-authoring rules,
  not IA research-methodology rules); the IA skill cites card sorting
  as evidence input, doesn't teach how to run one.

## Segment fit

This is an authoring-practice family (produce the artifact well),
sibling to the existing `ux-engineering-*` in-screen-decision family —
not a research-methodology family (that's `usability-eval`/
`user-discovery`).

## Gap line

Current state (`ux-engineering-*`) already meets: color/control/layout/
nav/contrast in-screen decision-making. Missing, and what this family
fills: everything upstream of "which control" — the artifacts that
decide what screens/flows exist in the first place (storyboard, IA,
user-flow, user-scenario) plus the lightweight HTML-demo construction
step between design artifact and code.

## Sources

- https://www.nngroup.com/videos/ux-storyboard/
- https://www.nngroup.com/articles/user-journeys-vs-user-flows/
- https://www.nngroup.com/articles/ia-study-guide/
- https://www.nngroup.com/reports/topic/information-architecture/
- https://richardcornish.s3.amazonaws.com/static/pdfs/iso-9241-210.pdf
- https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Accessibility/HTML
