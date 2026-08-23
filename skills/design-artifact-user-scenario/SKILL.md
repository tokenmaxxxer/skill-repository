---
name: design-artifact-user-scenario
description: >-
  Use when writing a user scenario, persona, or cross-channel journey map — a macro-scope
  narrative of a user's experience over time, including emotions and context, grounded in real
  user research. Trigger on requests like "persona journey map", "narrative scenario for this
  user", "journey mapping over weeks", "사용자 시나리오 써줘". Do NOT use for a micro-scope
  single-product step sequence (use design-artifact-user-flow).
metadata:
  axis: scenario-grounding-vs-invented-persona
  rule_count_floor: 3
---

# Scenario grounding vs. invented persona

Decision rules for writing user scenarios, personas, and journey maps as
macro-scope, emotion-and-context-bearing narratives grounded in real
context-of-use research, distinguishing them from design-artifact-user-flow's
micro-scope, step-and-system-response artifacts.

## Trigger

Apply this skill when writing a user scenario, persona, or cross-channel
journey map — a narrative of a user's experience over time that includes
emotions and context and can span multiple channels or days-to-months.
Distinguish this from design-artifact-user-flow, which covers the narrower,
micro-scope, single-product sequence of steps and system responses with no
emotional layer.

## Procedure

1. Before drafting any scenario or persona, gather context-of-use research —
   interviews, observed behavior, contextual inquiry — covering the intended
   user group (rule 1).
2. Draft the scenario/persona/journey map at macro scope: multi-channel,
   spanning the relevant timeframe, annotated with emotions and context at
   each stage (rule 2).
3. REMOVAL: when a draft persona or scenario has no traceable link to
   research, reject or flag it rather than publishing it as if grounded
   (rule 3).
4. When a journey map has been reduced to bare steps with no emotional or
   context layer, flag the collapse and restore the layer rather than
   treating it as a completed journey map (rule 4).
5. Refine the scenario/persona iteratively alongside prototypes and user
   feedback rather than freezing it after the first draft (rule 5).

## Output shape

A scenario, persona, or journey-map document spanning the relevant
timeframe and channels, structured as a stage-by-stage narrative annotated
with the user's emotional state, thoughts, and context at each stage, with
each claim traceable back to the specific research (interview, observation)
that grounds it, and marked as a living document subject to revision as
research and prototypes evolve.

## Decision rules

1. When starting a scenario, persona, or journey map, first produce a
   context-of-use description and user-group profile from real research —
   interviews, field observation, contextual data — before drafting any
   narrative content, rather than starting from an assumed or idealized user.
   source: ISO 9241-210, Ergonomics of human-system interaction — Human-
   centred design for interactive systems
   (https://richardcornish.s3.amazonaws.com/static/pdfs/iso-9241-210.pdf):
   the human-centred design process requires "understand and specify the
   context of use" as an activity that produces the context-of-use
   description and user-group profile, positioned before "design solutions"
   are produced.
   counter-example: do not skip straight to writing persona traits ("busy
   parent, impatient, prefers mobile") from stakeholder assumption in a
   kickoff meeting — that produces a plausible-sounding but ungrounded
   character that HCD's process explicitly places research ahead of.

2. When scoping a user scenario or journey, write it as macro-scope —
   multi-channel, spanning days to months where the real experience does,
   and annotated with the user's emotions and thoughts at each stage —
   rather than collapsing it to a single-product sequence of steps and
   system responses, which belongs to design-artifact-user-flow instead.
   source: Nielsen Norman Group, "User Journeys vs. User Flows: Two
   Different Ways to Map the User Experience"
   (https://www.nngroup.com/articles/user-journeys-vs-user-flows/): user
   journeys are "macro" and can include "emotions, thoughts, and pain
   points" across "multiple channels" over an extended timeframe, whereas
   user flows are "micro," single-product, and limited to steps and system
   responses without emotional context.
   counter-example: do not write a "journey map" that is actually a
   product's screen-by-screen click path with no cross-channel or emotional
   content — route that content to design-artifact-user-flow, the sibling
   skill scoped for exactly that micro-level artifact.

3. REMOVAL: when a persona or scenario in a draft has no citation back to an
   interview, observation, or other context-of-use research artifact — it
   was written from assumption, a stakeholder's mental model, or a
   composite of "best guesses" — reject it or flag it explicitly as
   unvalidated rather than presenting it as a grounded persona.
   source: ISO 9241-210
   (https://richardcornish.s3.amazonaws.com/static/pdfs/iso-9241-210.pdf):
   the standard specifies that user-group profiles and context-of-use
   descriptions are outputs of the "understand and specify the context of
   use" activity, meaning they are derived from evidence gathered in that
   activity, not authored independently of it.
   rationale: an invented persona still looks and reads like a grounded one
   — same format, same confident tone — so the failure mode is silent; the
   only reliable defense is checking for a traceable research citation on
   each persona claim, and removing or flagging the ones that have none.

4. When a journey map under review contains only a sequence of steps with no
   annotated emotional state or situational context at any stage, treat
   that as a collapsed artifact — flag it and restore the emotion/context
   layer — rather than accepting it as a finished journey map.
   source: Nielsen Norman Group, "User Journeys vs. User Flows"
   (https://www.nngroup.com/articles/user-journeys-vs-user-flows/): the
   article's core distinction is that journeys carry "emotions, thoughts,
   and pain points" and cross-channel context that flows deliberately omit;
   a journey map stripped of that layer is functionally a user flow wearing
   a journey map's label.
   counter-example: do not flag a legitimately flow-scoped artifact (one
   correctly labeled and used as a user flow, single product, steps and
   system responses only) as a "collapsed journey map" — the rule targets
   artifacts labeled and used as journey maps that have lost the layer that
   justifies that label, not flows that were never meant to carry it.

5. When a scenario or persona has already been published, keep refining it
   iteratively alongside prototypes and user feedback as research
   continues, rather than treating the first draft as final and immutable.
   source: ISO 9241-210
   (https://richardcornish.s3.amazonaws.com/static/pdfs/iso-9241-210.pdf):
   the human-centred design process is iterative — "evaluate the design
   against requirements" feeds back into "produce design solutions" and
   the context-of-use understanding, meaning scenarios and personas
   produced early are expected to be revised as prototypes and feedback
   accumulate, not frozen after one pass.
   counter-example: do not re-litigate a well-validated persona's core
   traits on every minor feedback item — iterate on the persona/scenario
   when feedback surfaces a material mismatch with real context of use, not
   on every superficial suggestion unrelated to that grounding.
