---
name: html5-game-rendering-loop
description: >-
  Use when structuring or reviewing a game's frame loop, timestep, or render/logic separation
  — choosing a single requestAnimationFrame driver, a fixed-timestep accumulator, state
  interpolation, delta clamping, or tab-visibility handling. Trigger on requests like
  "requestAnimationFrame game loop", "fixed timestep accumulator", "delta time clamping", "게임
  루프 구조 잡아줘". Do NOT use for the content of transient effects like shake or particles (use
  game-feel-juice-and-feedback).
metadata:
  axis: rendering-loop
  rule_count_floor: 5
---

# Rendering loop

Decision rules for driving a web game's frame loop, timestep, and
render/logic separation, sourced from Gaffer On Games' fixed-timestep
writeup and MDN's game-loop and requestAnimationFrame documentation,
gathered for issue #90's game-development research pass (2026-08-23).

## Trigger

Apply this skill when deciding how a game advances state per frame:
choosing the loop driver, splitting update from render, timestepping
logic, interpolating or snapping rendered state, clamping frame delta,
or handling a backgrounded tab. Distinguish it from
game-feel-juice-and-feedback (the content of a transient effect, not
the loop that drives it) and game-ui-board-and-lane-layout (static
layout, not per-frame motion).

## Procedure

1. Drive all animation from one requestAnimationFrame loop that
   re-schedules itself each callback; never trigger a draw from a
   click handler, timer, or other ad hoc event once anything animates
   (rule 1).
2. Split the loop into an update step (game logic) and a render step
   (drawing), and advance update on a fixed timestep via an
   accumulator rather than the raw per-frame delta (rule 2).
3. Keep the render step read-only with respect to game/logic state:
   it may read state and draw an interpolated or effect-layer
   representation of it, but must not mutate it (rule 3).
4. When render rate exceeds tick rate, interpolate between the
   previous and current logic state using the accumulator remainder;
   snap directly to current state only for values that are inherently
   discrete or non-interpolable (rule 4).
5. Render short-lived, purely visual effects on a separate effect
   layer or canvas so that layer can be cleared and redrawn without
   re-rendering the static board (rule 5).
6. Clamp the per-frame delta fed to the accumulator to a maximum
   value before accumulating it (rule 6).
7. Pause simulation work on visibilitychange when the tab is hidden,
   and resume with a clamped/discarded catch-up delta rather than a
   raw elapsed-time jump (rule 7).
8. REMOVAL: cut a second, competing requestAnimationFrame loop
   (e.g. one for effects, one for the board) down to the single
   driving loop from rule 1 (rule 8).
9. REMOVAL: cut a per-frame full-scene redraw down to a dirty-region
   or static-layer redraw wherever most of the scene did not change
   between frames (rule 9).

## Output shape

A loop spec: the single rAF driver, the fixed update rate and
accumulator, which state is interpolated vs. snapped, the effect-layer
split, the delta clamp value, and the visibilitychange handling — plus,
where rule 8 or 9 fires, a flagged competing loop or redundant
full-redraw to remove.

## Related skills

- game-design-core-loop-and-progression: hop there for what the game
  loop's actions and pacing should be, not how a frame is scheduled.
- game-feel-juice-and-feedback: hop there for what content an effect
  layer (rule 5) should contain and how it should read, once this
  skill has established the layer split.
- game-ui-board-and-lane-layout: hop there for static board/lane
  layout decisions, distinct from the per-frame motion this skill
  governs.
- implementation-performance-data-structure-choice: hop there when a
  dirty-region or effect-layer decision (rules 5, 9) turns into a
  broader data-structure or algorithmic choice.
- ux-engineering-color-visibility / accessibility-aria-and-contrast-rules:
  hop there for the visual/contrast content of a rendered frame, not
  the loop that produces it.

## Rule index

Full rule text, citations, and counter-examples:
`references/rules.md` in this skill's directory — read it when a
matched rule's detail is needed.

- 1.1 — When anything on screen animates over time, drive every visual update from a single requestAnimationFrame loop that re-schedules itself, rather than triggering draws dir…
- 1.2 — When a game has any physics, movement, or timing-sensitive logic, advance that logic on a fixed timestep consumed from an accumulator, rather than passing the raw variab…
- 1.3 — When writing the render step of the loop, treat it as read-only: it may compute an interpolated or effect-only representation of state to draw, but it must never write b…
- 1.4 — When the render rate is higher than the fixed tick rate, interpolate the drawn value between the previous and current logic state using `alpha = accumulator / dt` as the…
- 1.5 — When a visual effect is short-lived and purely cosmetic (particle burst, highlight flash, floating damage text), draw it on a separate effect layer or canvas from the st…
- 1.6 — When computing the delta time to feed the accumulator, clamp it to a maximum value (e.g. a few simulation steps' worth) before adding it in, rather than accumulating the…
- 1.7 — When a tab becomes hidden, pause simulation stepping on the visibilitychange event rather than letting requestAnimationFrame keep silently throttling in the background;…
- 1.8 — REMOVAL: when a codebase has more than one requestAnimationFrame loop running concurrently (e.g. one for the board, a second one independently animating effects or a UI…
- 1.9 — REMOVAL: when a frame redraws the entire scene every tick but only a small region actually changed (e.g. one tile flipped, one token moved), cut the full-scene redraw do…
