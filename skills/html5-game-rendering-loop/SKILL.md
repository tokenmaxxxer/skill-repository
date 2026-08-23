---
name: html5-game-rendering-loop
description: Use when structuring or reviewing a game's frame loop, timestep, or render/logic separation — choosing a single requestAnimationFrame driver, a fixed-timestep accumulator, state interpolation, delta clamping, or tab-visibility handling. Applies to the rendering-loop axis.
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

## Decision rules

1. When anything on screen animates over time, drive every visual
   update from a single requestAnimationFrame loop that re-schedules
   itself, rather than triggering draws directly from input events,
   timers, or network callbacks — a single scheduler is the only way
   to guarantee frame-consistent updates and avoid redundant draws.
   source: MDN, "Anatomy of a video game" (https://developer.mozilla.org/en-US/docs/Games/Anatomy): "window.requestAnimationFrame() ... Modern web games should leverage requestAnimationFrame() as the primary timing mechanism," calling requestAnimationFrame(main) again from within main to continue the cycle.
   counter-example: a static UI change with no animation (e.g. a
   one-time score label update on game-over) does not need to route
   through the frame loop — a direct DOM/canvas write is fine when
   nothing is animating.

2. When a game has any physics, movement, or timing-sensitive logic,
   advance that logic on a fixed timestep consumed from an
   accumulator, rather than passing the raw variable per-frame delta
   straight into the simulation — simulation code is tuned against a
   constant step and produces different, unstable results at
   different step sizes.
   source: Gaffer On Games, "Fix Your Timestep!" (https://gafferongames.com/post/fix_your_timestep/): "the behavior of your physics simulation depends on the delta time you pass in" and the accumulator pattern has the renderer "produce time" that physics "consumes" in fixed-size steps.
   counter-example: a game with no time-dependent logic at all (e.g. a
   purely turn-based board game whose only animation is cosmetic
   tweening) does not need an accumulator — advancing state on
   discrete player actions is already deterministic.

3. When writing the render step of the loop, treat it as read-only:
   it may compute an interpolated or effect-only representation of
   state to draw, but it must never write back into the logic/model
   state that the fixed-timestep update owns — otherwise the visible
   frame rate leaks into game behavior.
   source: MDN, "Anatomy of a video game" (https://developer.mozilla.org/en-US/docs/Games/Anatomy), describing the separated-update-and-render approach where "simulation to run at consistent 20Hz (50ms) independent of display refresh rate" while render only reads that state to interpolate or extrapolate.
   counter-example: input capture (recording a keypress or click) is
   allowed to happen inside the render-frequency callback, since input
   sampling isn't logic mutation — it should just be applied to state
   during the next fixed update, not immediately drawn as if applied.

4. When the render rate is higher than the fixed tick rate, interpolate
   the drawn value between the previous and current logic state using
   `alpha = accumulator / dt` as the blend factor; when a value is
   discrete or non-interpolable (e.g. which tile a piece occupies, a
   boolean visibility flag), snap to the current state instead of
   blending it.
   source: Gaffer On Games, "Fix Your Timestep!" (https://gafferongames.com/post/fix_your_timestep/): "the article recommends interpolating between previous and current physics states using the accumulator as a blend factor: alpha = accumulator / dt."
   counter-example: do not interpolate a value whose intermediate
   states are meaningless (e.g. a card's face-up/face-down state, or
   which player's turn it is) — blending those produces a nonsense
   halfway frame instead of a clean snap.

5. When a visual effect is short-lived and purely cosmetic (particle
   burst, highlight flash, floating damage text), draw it on a
   separate effect layer or canvas from the static board/scene, so
   that layer alone can be cleared and redrawn each frame without
   re-rendering content that hasn't changed.
   source: MDN, "Anatomy of a video game" (https://developer.mozilla.org/en-US/docs/Games/Anatomy), noting the loop should "consider throttling expensive non-time-sensitive tasks" and separate concerns between simulation and drawing; extended here to layering the effect surface apart from the static board for the same reason full redraws are wasteful.
   counter-example: an effect that permanently changes the board's
   appearance (e.g. a captured piece's tile recoloring) belongs on the
   board layer itself, not the transient effect layer, since it must
   persist rather than clear each frame — see
   game-feel-juice-and-feedback for effect-content decisions once the
   layer is chosen.

6. When computing the delta time to feed the accumulator, clamp it to
   a maximum value (e.g. a few simulation steps' worth) before adding
   it in, rather than accumulating the raw elapsed time verbatim —
   an unclamped delta after a stall causes the accumulator to demand
   many catch-up steps in one frame, which take even longer and stall
   it further.
   source: Gaffer On Games, "Fix Your Timestep!" (https://gafferongames.com/post/fix_your_timestep/): "When physics updates take longer than the time they simulate, the system falls behind and must simulate more steps to catch up, creating a death spiral. The solution involves either maintaining significant headroom or clamping maximum steps per frame."
   counter-example: do not clamp so aggressively that normal frame
   jitter (a single dropped frame at 60Hz) starts dropping simulated
   time — the clamp should only cut off pathological stalls (tab
   suspend, GC pause), not ordinary variance.

7. When a tab becomes hidden, pause simulation stepping on the
   visibilitychange event rather than letting requestAnimationFrame
   keep silently throttling in the background; on resume, discard or
   clamp the elapsed time since hide rather than feeding the browser's
   full suspended duration into the accumulator.
   source: MDN, Page Visibility API (https://developer.mozilla.org/en-US/docs/Web/API/Page_Visibility_API): "document.hidden ... visibilitychange event ... Prevents unnecessary tasks from consuming resources in background tabs," combined with MDN requestAnimationFrame (https://developer.mozilla.org/en-US/docs/Web/API/Window/requestAnimationFrame): "requestAnimationFrame() calls are automatically paused when running in background tabs."
   counter-example: a game with server-authoritative real-time state
   (e.g. a live multiplayer match) should not silently discard elapsed
   background time on its own client simulation — it must instead
   resync from the server on resume rather than pretend no time
   passed.

8. REMOVAL: when a codebase has more than one requestAnimationFrame
   loop running concurrently (e.g. one for the board, a second one
   independently animating effects or a UI overlay), cut it down to
   the single driving loop and fold the other work into that loop's
   update/render steps — two independent loops drift out of phase and
   can double-schedule work on the same frame.
   source: MDN, requestAnimationFrame (https://developer.mozilla.org/en-US/docs/Web/API/Window/requestAnimationFrame): "requestAnimationFrame() is one-shot — it only schedules a single callback. To create a continuous animation loop, you must call requestAnimationFrame() again from within your callback," implying one call site should own the recursive scheduling, not several independent ones.
   counter-example: a genuinely independent overlay that must keep
   animating while the main game loop is paused (e.g. a pause-menu
   spinner) can legitimately run its own short-lived loop — the
   removal rule targets loops competing to drive the same live game
   state, not an intentionally decoupled paused-state overlay.

9. REMOVAL: when a frame redraws the entire scene every tick but only
   a small region actually changed (e.g. one tile flipped, one token
   moved), cut the full-scene redraw down to a dirty-region redraw or
   a static pre-rendered layer for the unchanged parts, recombining
   only the changed region each frame.
   source: MDN, "Anatomy of a video game" (https://developer.mozilla.org/en-US/docs/Games/Anatomy): the article's guidance to "consider throttling expensive non-time-sensitive tasks to lower frequencies," applied here to redrawing static scene content only when it actually changes rather than every frame.
   counter-example: a scene where most pixels genuinely change every
   frame (e.g. a full-screen particle field or continuous camera pan)
   gets no benefit from dirty-region tracking — the bookkeeping cost
   exceeds the redraw it would save, so a full redraw stays correct.

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
