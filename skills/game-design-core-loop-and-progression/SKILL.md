---
name: game-design-core-loop-and-progression
description: >-
  Use when defining a progression tier or level, a stage difficulty curve, a cost curve, a
  currency's sources and sinks, or the acquisition method for a gating item — including
  balance derivation for per-stage monster and enemy HP/damage scaling so hits-to-kill lands
  in a target band. Trigger on requests like "stage difficulty curve", "monster HP and damage
  scaling per stage", "hits-to-kill balance derivation", "몬스터 밸런스 잡아줘". Do NOT use for
  cross-session pacing, upgrade cadence, or comeback-visit scheduling (use
  game-growth-system-design).
metadata:
  axis: core-loop-and-progression
  rule_count_floor: 5
---

# Core loop and progression

Decision rules for progression-tier design, cost curves, and currency
economies, sourced from game-balance and game-economy practitioner
literature gathered for issue #90's game-development research pass
(2026-08-23).

## Trigger

Apply this skill when defining a progression milestone or tier, setting
the direction of a cost curve, adding or sizing a currency's sinks and
sources, choosing deterministic vs. random acquisition for an item, or
tuning a progression curve's constants. Distinguish it from
`game-feel-juice-and-feedback` (the moment-to-moment feel of an action,
not the long-run reward structure) and `game-ui-board-and-lane-layout`
(spatial presentation, not the underlying progression math).

## Procedure

1. Before shipping a new progression tier, check its value against the
   compounded value of the prior tier at the switch threshold (rule 1).
2. Decide the cost curve's direction — increasing or decreasing — from
   where the design wants player attention concentrated, early or late
   (rule 2).
3. Before a currency source ships, name the currency's sink and size it
   against the source (rule 3).
4. For an item that gates progression, use deterministic acquisition;
   reserve randomized acquisition for non-gating content (rule 4).
5. State each progression curve as an explicit function of its inputs
   before tuning any constant inside it (rule 5).
6. Where a curve risks runaway inflation, apply a soft cap or
   diminishing-returns term rather than a hard wall (rule 6).
7. Size session-scoped sinks (limited attempts, cooldowns) against how
   fast the loop's sources let a player accumulate (rule 7).
8. REMOVAL: cut a currency or a progression track once it has no
   distinct decision attached to it (rule 8).

## Output shape

A progression/economy spec: per-tier value table with a monotonicity
check result, the cost curve's direction and explicit function, each
currency's named sources and sinks with a balance check, and the
acquisition method (deterministic/random) per gating vs. non-gating
item — plus any track flagged for removal under rule 8.

## Related skills

- `game-feel-juice-and-feedback`: hop there for the moment-to-moment
  feedback on gaining or spending currency/progress, not the
  underlying rate or curve math.
- `html5-game-rendering-loop`: hop there when the question is how the
  loop is driven frame-to-frame, not what the loop's reward structure
  should be.
- `game-ui-board-and-lane-layout`: hop there for how progression state
  is laid out and displayed on screen, once the underlying economy is
  decided here.
- `implementation-performance-data-structure-choice`: hop there once a
  progression curve's evaluation itself becomes a per-frame or
  per-tick performance concern.

## Rule index

Full rule text, citations, and counter-examples:
`references/rules.md` in this skill's directory — read it when a
matched rule's detail is needed.

- 1.1 — When introducing a new progression milestone or tier, check that its effective power is never lower than the compounded value of the prior tier at the point where a play…
- 1.2 — When deciding a cost curve's shape, pick an increasing cost curve (cheap items give large early gains, expensive items give progressively smaller ones) to concentrate me…
- 1.3 — Before a new currency's source ships, name at least one sink for that currency and size the sink's expected drain against the source's expected rate of production — do n…
- 1.4 — When an item gates further progression (a key, a required upgrade, a story-critical resource), make its acquisition deterministic; reserve random-drop acquisition for co…
- 1.5 — Before tuning any constant inside a progression curve (cost per level, reward per tier, drop rate per rarity), first state the curve as an explicit function of its input…
- 1.6 — When a progression curve risks runaway inflation as play continues (currency accumulation, stat growth, prestige multipliers), apply a soft cap or diminishing-returns te…
- 1.7 — When sizing a session-scoped sink (limited attempts, cooldown timers, energy costs), size it against how fast that session's sources let a player accumulate currency or…
- 1.8 — REMOVAL: when a currency or progression track has accumulated over time but no longer has a distinct decision attached to it — every choice it offered has been folded in…
