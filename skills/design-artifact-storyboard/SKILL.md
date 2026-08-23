---
name: design-artifact-storyboard
description: Use when authoring a sequence-of-panels storyboard for a user story or workflow, one that maps chronological events rather than a single static screen.
metadata:
  axis: storyboard-sequence-vs-single-screen
  rule_count_floor: 3
---

# Storyboard sequence vs. single screen

Decision rules for authoring a storyboard as a chronological sequence
of panels depicting a user's experience over time — a beginning,
middle scenario context, and end/outcome — rather than a single static
screen or wireframe, sourced from NN/g storyboard guidance and
ISO 9241-210's context-of-use framing.

## Trigger

Apply this skill when authoring a storyboard for a user story or
workflow: a sequence of panels that maps the chronological events of a
user's experience, distinguishing it from design-artifact-user-flow
(a step-by-step interaction path through an existing UI) and
design-artifact-user-scenario (narrative/persona-based scenario text
with no panel sequence), and distinguishing a storyboard panel from a
single static screen mockup or wireframe.

## Procedure

1. Establish the beginning panel: the user's context and trigger
   before any UI exists, not a screen (rule 1).
2. Add middle panels for the scenario's key events/decision points,
   showing the user's environment and behavior, not just app state
   (rule 2).
3. Close with an end/outcome panel showing the result of the workflow
   for the user, not the final screen state alone (rule 3).
4. When a candidate panel would only show a static screen with no
   change in scene, actor state, or context, don't add it as a
   storyboard panel (rule 4).
5. REMOVAL: when two adjacent panels depict the same scene and context
   with no change in the user's action, decision, or outcome between
   them, merge or drop the redundant panel (rule 5).
6. Judge storyboard completeness by whether the sequence explains why
   a design solution is needed, not by hitting a fixed panel count
   (rule 6).

## Output shape

An ordered sequence of panels (typically 3-6), each depicting a
distinct scene: the user, their context/environment, and what they are
doing or experiencing at that point in time — with a beginning panel
(pre-trigger context), one or more middle panels (scenario events and
decision points), and an end panel (outcome/result). No panel is a
static screen mockup or wireframe; panels may precede any UI design
existing at all. The sequence reads as a narrative arc, not a UI spec.

## Decision rules

1. When authoring a storyboard's opening panel, depict the user's
   real-world context and the trigger that starts their need — not a
   screen or app UI, which may not exist yet — because storyboards are
   meant to explore context and motivation before a design solution is
   proposed.
   source: NN/g, "UX Storyboards" (https://www.nngroup.com/videos/ux-storyboard/):
   storyboards show a sequence of scenes/panels depicting a user's
   experience over time, and are used early, before UI exists, to
   explore the context surrounding a need.
   counter-example: do not open with a login screen or dashboard panel
   just because that's where the eventual product starts — if the
   real trigger is, e.g., a user noticing a problem at their desk
   before opening any app, that pre-app moment is the correct opening
   panel.

2. When adding middle panels, ground each one in the actual context of
   use — the user's environment, constraints, and goals at that
   moment — rather than jumping straight to interface details, because
   context-of-use is what justifies why a particular design response
   is needed at all.
   source: ISO 9241-210 context-of-use framing
   (https://richardcornish.s3.amazonaws.com/static/pdfs/iso-9241-210.pdf),
   which frames usability and design decisions as inseparable from the
   users, tasks, equipment, and physical/social/organizational
   environment in which a product is used.
   counter-example: do not pad the middle with panels that only show
   UI screens in isolation, stripped of the surrounding environment —
   a storyboard for a field-service app that never shows the noisy,
   gloved-hands context loses the reason a design choice (e.g. large
   touch targets) was made.

3. When closing a storyboard, depict the outcome for the user — what
   changed in their situation, task, or feeling — not merely the final
   screen state, because the storyboard's purpose is to communicate
   the value delivered across the whole experience, not just the last
   UI frame.
   source: NN/g, "UX Storyboards" (https://www.nngroup.com/videos/ux-storyboard/):
   storyboards map a story's main events across a beginning, middle,
   and end to show the user's experience over time, culminating in a
   resolution to their need.
   counter-example: do not end on a "success" toast/confirmation
   screen alone if the real outcome is a downstream, off-screen
   consequence (e.g. the user leaves for their next task with time
   saved) — show that consequence as the end panel, even if it has no
   corresponding UI.

4. When a candidate panel would show nothing but a static screen with
   no change in scene, actor state, or context from the panel before
   it, don't add it as a storyboard panel — it duplicates what a
   single wireframe already communicates and adds no chronological
   information.
   source: NN/g, "UX Storyboards" (https://www.nngroup.com/videos/ux-storyboard/):
   distinguishes a storyboard (sequence of scenes over time) from a
   single static screen or wireframe, which the video calls
   insufficient for capturing an experience that unfolds over time.
   counter-example: do not drop a panel just because it shows the same
   physical location as the previous one — if the user's action,
   decision, or emotional state changed even though the setting is
   identical, that is still a new chronological event worth a panel.

5. REMOVAL: when two adjacent panels depict the same scene and context
   with no change in the user's action, decision, or outcome between
   them, merge or drop the redundant panel — storyboards accrete
   near-duplicate panels as scenario detail is added incrementally,
   and an unreviewed panel that repeats the prior one's information
   adds length without adding story.
   source: Adams, Converse, Hales & Klotz, "People systematically
   overlook subtractive changes," Nature 592 (2021), summarized at
   https://phys.org/news/2021-04-brains-opportunities.html — applied
   to storyboards that grow panel-by-panel through additive edits
   without anyone later checking whether a given panel still earns its
   place once it no longer marks a distinct story beat.
   counter-example: do not merge two panels that look visually similar
   but mark a meaningful time gap or a repeated attempt that itself is
   part of the story (e.g. "user tries again after failing") — the
   removal rule targets true redundancy, not a deliberate beat that
   happens to reuse the same setting.

6. Judge storyboard completeness by whether the finished sequence
   explains why a proposed design solution is needed — i.e. whether a
   reader unfamiliar with the project can see the problem and its
   context from the panels alone — rather than by hitting a fixed
   panel count or matching a template's number of boxes.
   rationale: panel count is a proxy; a 3-panel storyboard that clearly
   establishes context, conflict, and resolution does its job, while a
   6-panel storyboard that never leaves the UI can fail even with more
   panels — the standard is whether the "why" is legible, not how many
   boxes are filled.
   counter-example: do not force a scenario into a fixed template of
   exactly N panels if the story's context and outcome are already
   clear in fewer — padding to hit a count reintroduces the
   single-static-screen problem one panel at a time.
