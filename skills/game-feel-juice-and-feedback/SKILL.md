---
name: game-feel-juice-and-feedback
description: Use when deciding whether a build is ready to receive juice, choosing what feedback an input needs, adding or capping a juice effect (screen shake, squash-and-stretch, anticipation), or pruning a stack of effects that has stopped reading clearly. Applies to the juice-and-feedback axis.
metadata:
  axis: juice-and-feedback
  rule_count_floor: 4
---

# Game feel, juice, and feedback

Decision rules for staging juice work, giving player actions readable
feedback, and layering effects without losing meaning, sourced from
Jonasson & Purho's and Nijman's practitioner talks and MDN's
accessibility documentation, gathered for issue #90's game-development
research pass (2026-08-23).

## Trigger

Apply this skill when deciding whether a build is ready for juice
work, choosing what feedback an input or event needs, adding or
tuning a specific juice effect (screen shake, squash-and-stretch,
anticipation, particles, sound), or pruning an effect stack that no
longer reads clearly. Distinguish it from
game-design-core-loop-and-progression (whether the underlying action
is worth taking at all) and html5-game-rendering-loop (how frames get
drawn and timed, not what plays on top of them).

## Procedure

1. Confirm the build already works at the layout-and-animation stage
   before adding any juice effect on top of it (rule 1).
2. For every player action, attach feedback that appears in the same
   frame the input is accepted (rule 2).
3. Add each juice effect as an independently removable layer on the
   working prototype, never as a rewrite of it (rule 3).
4. Reserve screen shake for events the design wants read as
   impactful, and cap its magnitude and frequency (rule 4).
5. Use squash-and-stretch and anticipation on state changes that
   benefit from a readable transition, not on every transition (rule
   5).
6. When several effects fire on one event and the event's meaning is
   no longer readable, cut back to the one effect that carries the
   meaning (rule 6).
7. Before shipping any motion effect, provide a reduced-motion path
   and hop to accessibility-aria-and-contrast-rules for the general
   contrast/motion accessibility contract (rule 7).

## Output shape

A juice plan: which stage the build is at (layout / animation /
juice), which effect attaches to which event, its magnitude/cap, and
its reduced-motion fallback — plus, where rule 6 fires, a flagged
over-stacked event trimmed back to one carrying effect.

## Decision rules

1. When a build still consists of static text, placeholder buttons,
   and no animation, ship or demo it as a layout-stage build and do
   not add juice effects yet — juice tunes feedback on top of motion
   and interaction that must already exist and already read
   correctly, so juice added at the layout stage has nothing correct
   underneath it to amplify.
   source: Jonasson & Purho, "Juice it or lose it" (https://www.youtube.com/watch?v=Fy0aCDmgnxg): the talk demonstrates the same simple jump-and-collect game staged from a bare, static build up through animation and only then juice, showing each stage as a precondition for the next.
   counter-example: do not block a genuinely juice-stage build (interactions already animated and working) on further layout polish before adding juice — the staging is sequential, not a gate that reopens once passed.

2. When a player performs any action the game recognizes as input,
   attach visible or audible feedback that appears in the same frame
   the input is accepted, not on a later frame or only once the
   action's full effect resolves — feedback delayed past the input
   frame reads as unresponsiveness even if the underlying action is
   processed correctly.
   source: Jonasson & Purho, "Juice it or lose it" (https://www.youtube.com/watch?v=Fy0aCDmgnxg): the talk's core thesis is that immediate, exaggerated feedback on every action (not just the successful ones) is what makes a game feel alive, illustrated by adding instant reaction to jumps, hits, and even failed actions.
   counter-example: a purely passive background event the player did not trigger (ambient weather, a distant NPC's idle animation) does not need input-frame feedback — the rule binds to actions the player took, not to every visible change in the world.

3. When adding a new juice effect to a working prototype, implement it
   as a layer that can be disabled or removed independently of the
   underlying mechanic, never as a change that rewrites or entangles
   with the mechanic's own logic — juice is decoration on top of a
   working system, and a system that only works with its juice
   attached has lost the separation that makes juice safe to iterate
   on.
   source: Jonasson & Purho, "Juice it or lose it" (https://www.youtube.com/watch?v=Fy0aCDmgnxg): the talk repeatedly adds one juice effect at a time (screen shake, particles, squash-and-stretch, sound) to the same untouched base game, each addable or removable without touching the base mechanic.
   counter-example: a change that fixes an actual mechanical bug (wrong collision box, wrong input timing) is not a juice layer and should not be deferred to "layer it on later" — juice work assumes the mechanic underneath is already correct.

4. When an event is one the design wants the player to read as
   impactful (a heavy hit, a big explosion, a boss landing), apply
   screen shake to it and cap the shake's magnitude and trigger
   frequency so that ordinary, frequently repeated actions (walking,
   routine shooting, small pickups) never shake the screen — shake
   that fires on everything stops signaling anything and becomes pure
   noise or motion sickness risk.
   source: Nijman, "The art of screenshake" (https://www.youtube.com/watch?v=AJdEqssNZ-U): the talk frames screenshake as a tool tuned per-event for perceived impact, not a blanket effect, and shows how uncapped or overused shake degrades rather than improves feel.
   counter-example: do not apply screen shake to UI-only feedback (a menu confirmation, a inventory pickup ping) even if it is a "significant" event in game-state terms — shake is reserved for events with physical, in-world impact the camera itself would plausibly react to.

5. When an object changes state in a way the player benefits from
   reading clearly (a character landing a jump, an enemy about to
   attack, a button being pressed), apply squash-and-stretch to the
   motion and a brief anticipation beat before the action lands; do
   not apply this to every single transition an object goes through.
   why: exaggerating the run-up and follow-through of a state change
   is what separates a mechanically-identical but flat-feeling
   transition from one that reads as weighty and intentional, but
   applying it universally dilutes which transitions are actually
   meant to draw attention.
   source: Jonasson & Purho, "Juice it or lose it" (https://www.youtube.com/watch?v=Fy0aCDmgnxg): the talk's jump example is built almost entirely from squash-and-stretch and a brief pre-jump anticipation frame added on top of an otherwise unchanged jump mechanic.
   counter-example: a continuous, already-smooth motion (a projectile flying in a straight line) does not need squash-and-stretch inserted mid-flight — the technique targets the moments of state change (launch, impact), not steady-state motion.

6. REMOVAL: when several juice effects (shake, particles, sound,
   squash-and-stretch, flash) all fire on the same event and a
   playtester can no longer tell what the event was from watching it,
   cut back to the single effect that most directly carries the
   event's meaning and remove the rest, rather than tuning all of them
   down slightly.
   why: stacked effects compete for the same instant of attention;
   partial tuning of every effect still leaves several competing
   signals, while dropping to one clear signal restores readability
   immediately.
   source: Jonasson & Purho, "Juice it or lose it" (https://www.youtube.com/watch?v=Fy0aCDmgnxg): the talk's own progression shows effects added one at a time specifically so each one's individual contribution stays checkable, implying an equivalent one-at-a-time removal path when a stack becomes unreadable.
   counter-example: do not strip an event down to zero effects just because it currently has more than one — a hit event carrying both a hit-flash and a knockback nudge can legitimately need two signals (damage occurred, and direction), as long as a player can still parse both from one glance.

7. When shipping a motion-based juice effect (shake, parallax,
   scaling pulses, panning), provide a reduced-motion variant gated on
   the user's OS-level preference, and consult
   accessibility-aria-and-contrast-rules for the broader contrast and
   motion accessibility contract this rule sits inside — juice that
   ignores a stated reduced-motion preference can trigger real
   discomfort, not just an aesthetic mismatch.
   source: MDN, "prefers-reduced-motion" (https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-reduced-motion): "The setting is used to convey to the browser on the device that the user prefers an interface that removes, reduces, or replaces motion-based animations," noting scaling and panning of large objects as particularly problematic for vestibular motion disorders.
   counter-example: a purely static feedback signal with no motion component (a color flash with no scale/pan/shake) is not gated by this rule — the reduced-motion preference targets motion, not all feedback.

## Related skills

- game-design-core-loop-and-progression: hop there when the question is
  whether an action belongs in the loop at all, before deciding how it
  should feel.
- html5-game-rendering-loop: hop there for frame timing and draw-order
  mechanics that juice effects execute inside of.
- game-ui-board-and-lane-layout: hop there when the feedback in
  question is about board/lane spatial layout rather than an effect
  layered on an event.
- implementation-performance-data-structure-choice: hop there when a
  juice effect (particles, shake queues) risks a performance cliff at
  scale.
- accessibility-aria-and-contrast-rules: hop there for the general
  motion, contrast, and ARIA accessibility contract that rule 7's
  reduced-motion path sits inside.
