# Scout brief — issue #90 game-development skill families

Mode: PARALLEL fan-out (4 concurrent WebSearch calls per stage). Stages
used: 2 of 5 (sweep + one deepening round), well inside the 3-min
budget. Stopped at saturation — a third round would not change any
authoring decision, only add restatements of the same canon.

## Category must-bes (what strong sources in this field assume)

- Progression/economy is treated as *arithmetic*, not vibes: cost curves
  and reward curves are explicit functions, and source/sink balance is
  the stated control for inflation (Schreiber Level 3; Unity economy
  guide).
- Game feel is decomposed into layered, individually-cheap effects
  applied on top of a working prototype — never as a rewrite (Juice it
  or Lose it; Art of Screenshake's ~30 discrete tweaks).
- Loop discipline assumes a fixed simulation step decoupled from a
  variable render rate, with interpolation via an accumulator remainder
  (Fiedler; MDN Anatomy of a video game).
- Touch surfaces assume a minimum target size and a non-drag alternative
  for any drag-operated function (WCAG 2.2 SC 2.5.8 / 2.5.7; NN/g).

## Performance axes the field competes on

1. Determinism/reproducibility of the simulation (fixed step, seeded
   randomness) vs. raw frame smoothness.
2. Feedback density per player action (readability of a hit/merge) vs.
   restraint — screenshake and particles degrade fast when over-applied.
3. Legibility at the smallest shipped token size vs. information density
   on the board.

## Adopt / skip

- ADOPT: the accumulator + interpolation formulation, stated as a rule
  with the "render must not mutate logic state" corollary — it is the
  exact risk the interaction-design consult flagged in the dogfood.
- ADOPT: layered-juice staging (layout -> animation -> juice) as an
  ordering rule, since the operator-rejected "text + buttons" build is
  precisely a stage-1-only ship.
- SKIP: cloning "30 tricks" as a checklist. The repo's format wants
  condition -> choice -> source rules; a trick list has no condition
  column and would fail the decision-rule bar.
- SKIP: full economy simulation tooling (Machinations-style modelling) —
  out of scope for a skill, and unciteable as a rule.

## Segment fit

These four are decision-point skills for a small-team HTML5/canvas
game, matching the repo's existing `<discipline>-<axis>` sparse-tier
skills — not textbook overviews.

## Gap line

Already met by current state: contrast floors and generic control
choice (`accessibility-aria-and-contrast-rules`,
`ux-engineering-*`); algorithmic performance cliffs
(`implementation-performance-data-structure-choice`). MISSING entirely:
progression/economy math, feedback/juice staging, frame-loop and
state/render separation, and spatial board/lane/token composition with a
merge-gesture fallback.

Sources:
- https://gamebalanceconcepts.wordpress.com/2010/07/21/level-3-transitive-mechanics-and-cost-curves/
- https://unity.com/how-to/design-balanced-in-game-economy-guide-part-3
- https://www.youtube.com/watch?v=Fy0aCDmgnxg (Jonasson & Purho, "Juice it or lose it")
- https://www.youtube.com/watch?v=AJdEqssNZ-U (Nijman, "The art of screenshake")
- https://gafferongames.com/post/fix_your_timestep/
- https://developer.mozilla.org/en-US/docs/Games/Anatomy
- https://developer.mozilla.org/en-US/docs/Web/API/Window/requestAnimationFrame
- https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html
- https://www.w3.org/WAI/WCAG22/Understanding/dragging-movements.html
- https://www.nngroup.com/articles/touch-target-size/

Note: the "Juice it or lose it" URL above is the canonical talk ID as
commonly cited; phase 2 must re-verify every URL live before it lands in
a `source:` line, since `check_skill_conformance.py` gates on the
presence of the citation but not its liveness.
