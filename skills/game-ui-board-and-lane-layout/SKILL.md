---
name: game-ui-board-and-lane-layout
description: >-
  Use when laying out a game board's cells, lanes, and token targets, sizing drag/tap
  interaction zones on a board, or deciding how pip/token counts and lane boundaries read
  spatially. Trigger on requests like "board grid layout", "drag target size on the board",
  "pip count rendering per cell", "레인 배치 잡아줘". Do NOT use for the draw/update cadence that
  repaints the board (use html5-game-rendering-loop).
metadata:
  axis: board-and-lane-layout
  rule_count_floor: 4
---

# Board and lane layout

Decision rules for board-grid sizing, lane boundaries, and token/pip
interaction targets, sourced from WCAG 2.2 pointer-input criteria and
Nielsen Norman Group touch-target research, gathered for issue #90's
game-development research pass (2026-08-23).

## Trigger

Apply this skill when arranging a board's cells or lanes, sizing a
draggable or tappable token/pip target, deciding how a pip count
should render at a given cell size, or separating board state from
surrounding chrome — distinguishing it from game-feel-juice-and-feedback
(animation/feedback timing on a move, not where the move target sits),
html5-game-rendering-loop (draw/update cadence, not spatial layout),
and game-design-core-loop-and-progression (what the move means
mechanically, not how it is laid out).

## Procedure

1. Give every drag/merge gesture a single-pointer tap-then-tap
   alternative that reaches the same outcome (rule 1).
2. Size every interactive board cell and token to at least the 24x24
   CSS-px floor, and larger on touch-primary surfaces (rule 2).
3. Pick one grid unit and derive cell size, gutter, and board aspect
   from it so layout survives viewport change (rule 3).
4. Separate lanes from the HUD with one explicit spatial boundary,
   not an implicit color or spacing cue alone (rule 4).
5. Switch a pip/token count to a numeral once individual pips stop
   being countable at the shipped cell size (rule 5).
6. Audit boundary and grouping signals already in place before adding
   a new one; cut down to a single signal where several stack on the
   same edge (rule 6, REMOVAL).
7. Drop any lane that renders but carries no game state (rule 7,
   REMOVAL).
8. For text or icon labels placed on board cells, hand contrast and
   ARIA-role questions to ux-engineering-color-visibility and
   accessibility-aria-and-contrast-rules rather than deciding them
   here (rule 8).

## Output shape

A board/lane layout spec: grid unit and derived cell/gutter/aspect
values, per-cell and per-token target sizes at each supported input
mode, the single-pointer alternative for each drag gesture, the pip-
to-numeral switch threshold, and the boundary treatment separating
lanes from HUD — plus, where rule 6 or 7 fires, a flagged redundant
boundary signal or a flagged inert lane.

## Related skills

- ux-engineering-layout-grouping: for general field/element grouping
  and boundary-signal choices off the board (menus, forms, panels) —
  this skill only owns the board/lane/token spatial case.
- ux-engineering-color-visibility: hop there for the actual contrast
  ratios and color-pairing choices used to render a board or HUD
  boundary; this skill only says a boundary must exist.
- accessibility-aria-and-contrast-rules: hop there for ARIA roles and
  contrast minimums on board cell/token markup; this skill covers
  spatial sizing and placement, not markup or color math.
- game-feel-juice-and-feedback: hop there for how a move or merge
  animates and confirms once the target layout from this skill is
  already in place.
- html5-game-rendering-loop: hop there for how often and when the
  board redraws; this skill only fixes where things sit, not the
  draw cadence.
- game-design-core-loop-and-progression: hop there for what a board
  move means mechanically; this skill only lays out where it happens
  spatially.

## Rule index

Full rule text, citations, and counter-examples:
`references/rules.md` in this skill's directory — read it when a
matched rule's detail is needed.

- 1.1 — When a board interaction is implemented as a drag or merge gesture (e.g. dragging a token from one cell to another, or dragging one token onto another to merge them), sh…
- 1.2 — When a board cell or token is interactive (tappable, draggable, or selectable), size its hit target to at least 24x24 CSS px on any pointer-input surface, and increase t…
- 1.3 — When defining a board's grid, derive cell size, gutter width, and overall board aspect ratio from one base grid unit (e.g. all spacing and sizing are multiples of a sing…
- 1.4 — When lanes sit next to a HUD (score, timer, hand, resource counters), give the boundary between them one explicit spatial signal — a gap, a frame, or a container edge —…
- 1.5 — When a pip or token count on a cell exceeds the number a player can subitize or reliably count at speed at the shipped cell size (commonly beyond 4-6 individual marks at…
- 1.6 — REMOVAL: when a board region already carries a border, a background tint, AND a separate card/frame around it to signal the same grouping or boundary, cut down to one si…
- 1.7 — REMOVAL: when a lane renders on the board but never carries state that changes with play (no token ever occupies it, no counter tied to it ever updates), cut the lane ra…
