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

## Decision rules

1. When introducing a new progression milestone or tier, check that its
   effective power is never lower than the compounded value of the
   prior tier at the point where a player switches to it, before
   shipping the tier — a milestone that reduces effective power reads
   as a bug or a punishment, not progress, even if the designer's
   intent was a lateral trade-off.
   source: Ian Schreiber, "Level 3: Transitive Mechanics and Cost
   Curves" (https://gamebalanceconcepts.wordpress.com/2010/07/21/level-3-transitive-mechanics-and-cost-curves/):
   discusses how transitive-mechanic tiers must each represent a real
   step up in relative power, since a later, more expensive tier that
   fails to beat the effective value of the cheaper tier it replaces
   breaks the intended progression.
   counter-example: a tier that trades raw power for a genuinely new
   capability (e.g. a slower but area-effect item replacing a faster
   single-target one) is a lateral choice, not a monotonicity failure —
   the check applies to same-axis power, not to intentionally
   differentiated trade-offs.

2. When deciding a cost curve's shape, pick an increasing cost curve
   (cheap items give large early gains, expensive items give
   progressively smaller ones) to concentrate meaningful choice in the
   early game, and pick a decreasing cost curve (cheap items are weak,
   expensive items are strong) to concentrate it in the late game —
   choose the direction from where the design wants player attention,
   not by default.
   source: Ian Schreiber, "Level 3: Transitive Mechanics and Cost
   Curves" (https://gamebalanceconcepts.wordpress.com/2010/07/21/level-3-transitive-mechanics-and-cost-curves/):
   "If a game has an increasing cost curve where higher costs give
   progressively smaller gains, it puts a lot of focus on the early
   game... If instead you feature a decreasing cost curve where the
   cheap stuff is really weak and the expensive stuff is really
   powerful, this instead puts emphasis on the late game."
   counter-example: a short-session game with no meaningful "early" vs.
   "late" distinction (the whole run is a few minutes) gets little
   benefit from picking a curve direction for this reason — pick on
   other grounds (e.g. simplicity) instead.

3. Before a new currency's source ships, name at least one sink for
   that currency and size the sink's expected drain against the
   source's expected rate of production — do not ship a source and
   defer sink design to a later pass.
   source: Unity, "Designing a balanced in-game economy: How-to guide"
   part 3 (https://unity.com/how-to/design-balanced-in-game-economy-guide-part-3):
   frames a healthy economy as one where "the sum of sources" is
   balanced against "the sum of sinks," and treats sink design as a
   first-class, not incidental, part of shipping a currency.
   counter-example: a currency that exists purely as a scorekeeping or
   display number, with no player-facing use, does not need a
   spending sink — it needs to be reclassified as a stat, not a
   currency, rather than have an artificial sink bolted on.

4. When an item gates further progression (a key, a required upgrade,
   a story-critical resource), make its acquisition deterministic;
   reserve random-drop acquisition for content that a player can skip
   or substitute without being blocked, such as cosmetics or
   duplicate-tolerant boosts.
   source: Unity, "Designing a balanced in-game economy: How-to guide"
   part 3 (https://unity.com/how-to/design-balanced-in-game-economy-guide-part-3):
   ties sink/source pacing to keeping engaged players from finishing
   too quickly or too slowly, which random gating on required items
   undermines by producing unpredictable, sometimes unbounded, time
   to progress.
   counter-example: a randomized reward pool for a fully optional
   collection track is fine to leave random even though it is
   technically "progression" — the rule targets items that block the
   player's forward path, not every collectible.

5. Before tuning any constant inside a progression curve (cost per
   level, reward per tier, drop rate per rarity), first state the curve
   as an explicit function of its inputs (e.g. cost(n) = base *
   growth^n) rather than a table of hand-picked numbers — tune the
   function's parameters, not individual cells.
   source: Ian Schreiber, "Level 3: Transitive Mechanics and Cost
   Curves" (https://gamebalanceconcepts.wordpress.com/2010/07/21/level-3-transitive-mechanics-and-cost-curves/):
   the article's entire treatment of "cost curves" presumes the
   curve is a defined mathematical relationship (linear, exponential,
   or otherwise) that a designer can reason about and adjust as a
   whole, not a set of independently chosen values.
   counter-example: a one-off, hand-authored milestone (a single
   unique final-boss unlock) does not need a general function — the
   function requirement applies to a series of comparable
   tiers/levels, not a single bespoke point.

6. When a progression curve risks runaway inflation as play continues
   (currency accumulation, stat growth, prestige multipliers), apply a
   soft cap or diminishing-returns term past a threshold rather than a
   hard wall that simply stops the curve — a soft cap keeps the numbers
   still moving, which preserves the sense of progress, while curbing
   the rate the rest of the economy has to keep pace with.
   source: Unity, "Designing a balanced in-game economy: How-to guide"
   part 3 (https://unity.com/how-to/design-balanced-in-game-economy-guide-part-3):
   describes deliberately engineering "fluctuations" and pacing into
   sink/source balance so the economy self-corrects rather than being
   left to run unchecked, the same rationale a soft cap applies to an
   individual curve.
   counter-example: a curve that already terminates naturally at a
   fixed, low-count endgame (e.g. a five-tier upgrade with no further
   levels) does not need a soft cap — there is no unbounded growth to
   control.

7. When sizing a session-scoped sink (limited attempts, cooldown
   timers, energy costs), size it against how fast that session's
   sources let a player accumulate currency or progress, not against
   an arbitrary fixed number — a sink calibrated independently of its
   matching source either starves engaged players or fails to create
   the intended pacing.
   source: Unity, "Designing a balanced in-game economy: How-to guide"
   part 3 (https://unity.com/how-to/design-balanced-in-game-economy-guide-part-3):
   ties sink strength to limiting how quickly a heavily engaged player
   can progress through session count and session time, explicitly
   pacing the sink against the player's actual rate of play.
   counter-example: a sink meant purely as a one-time onboarding gate
   (a tutorial-only cooldown) does not need to be paced against
   steady-state source rate, since it only ever fires once.

8. REMOVAL: when a currency or progression track has accumulated over
   time but no longer has a distinct decision attached to it — every
   choice it offered has been folded into, or made redundant by,
   another track — cut the track rather than maintaining it in
   parallel.
   source: Ian Schreiber, "Level 3: Transitive Mechanics and Cost
   Curves" (https://gamebalanceconcepts.wordpress.com/2010/07/21/level-3-transitive-mechanics-and-cost-curves/):
   the article's framing of transitive mechanics as tools for
   producing meaningful choice implies that a mechanic offering no
   distinguishable choice no longer serves the purpose cost curves are
   built for, and should not be kept only for its own sake.
   counter-example: a track with no current decision but a named,
   scheduled future use (a currency banked ahead of a content drop
   that will add its sink) should be kept, since the missing decision
   is temporary, not structural.

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
