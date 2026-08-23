---
name: game-growth-system-design
description: Use when setting a cost/pacing curve across sessions, adding or auditing a currency's sources and sinks, scheduling upgrade choices, choosing deterministic vs chance-based progression, or setting a return cadence. Applies to the growth-system-design axis.
metadata:
  axis: growth-system-design
  rule_count_floor: 5
---

# Game Growth System Design

The rules below are sourced from published game-design practice, gathered for issue #93's game-development research pass, 2026-08-23. They cover pacing, currency economy, choice cadence, deterministic-vs-chance gating, and return cadence for a growth system.

## Trigger

Use this skill when setting a cost/pacing curve across sessions, adding or auditing a currency's sources and sinks, scheduling upgrade choices, choosing deterministic vs chance-based progression, or setting a return cadence.

## Procedure

1. Define the target purchase interval across sessions and derive the cost curve from it, not the reverse (rule 1).
2. Audit every currency touched by the change: list its sources, its sinks, and check aggregate source rate against sink rate (rule 2).
3. Check whether the change introduces or modifies an acquisition point; if it is auto-buy, restructure it into a meaningful choice at a stated cadence (rule 3).
4. Classify each reward as gating or non-gating; assign deterministic progression to gating rewards and reserve chance for non-gating variety (rule 4).
5. Decide whether the system needs a return-cadence timer; if yes, state its target session spacing, else omit it explicitly (rule 5).

## Output shape

A growth-system spec should state: the pacing curve with target purchase intervals across sessions (not raw costs alone); a per-currency ledger of named sources and sinks with an inflation check; the upgrade-choice cadence (interval and what options are offered); an explicit deterministic-vs-chance assignment per reward type; and a return-cadence target session spacing, or an explicit note that no return-cadence timer is used.

## Decision rules

### 1. When tuning cost curves, tune the purchase interval, not just the raw numbers

When setting a pacing curve across sessions, do not tune a single-session cost table in isolation; instead treat the time between meaningful acquisitions (the purchase interval) as the tuned quantity, because an exponential cost curve only reads as fair pacing when it lands players on that target interval session after session, not when the raw numbers merely look reasonable in a spreadsheet.

source: Creating a Casual Game Progression Curve (https://www.gamedeveloper.com/design/creating-a-casual-game-progression-curve) shows exponential cost curves derived from a target acquisition interval rather than from raw cost values.
counter-example: Does not apply to one-shot unlocks with no repeat purchase cadence (e.g. a single tutorial-gated feature) — there is no interval to tune.

### 2. Before shipping a new currency source, run a full source/sink lifecycle audit

When adding or modifying a currency source, list every named source and every named sink for that currency and check the aggregate source rate against the aggregate sink rate over a typical session, because a source added without a matching new sink increases inflation and flattens the intended progression curve.

source: Idle Game Economy Design: What Your Currency Sinks Actually Eat (https://dev.to/sam_novak_574b07811e18495/idle-game-economy-design-what-your-currency-sinks-actually-eat-1non) shows sink design as the counterweight that must be audited alongside any new source, and Game Economy Balancing (https://dev.to/hiroshi_takamura_c851fe71/game-economy-balancing-how-to-tune-rewards-costs-and-progression-2ale) shows the source-vs-sink rate check as the balancing method.
counter-example: Does not apply to a cosmetic-only currency with no economic feedback into gameplay progression — there is no curve to flatten.

### 3. Schedule upgrade acquisitions as meaningful choices at a stated interval, not as auto-buys

When scheduling upgrade choices, design a decision point where the player picks between distinct options at a defined cadence, because a choice between mutually exclusive upgrade paths sustains engagement, while an acquisition that is simply "afford it, buy it" with no alternative is not a choice and should be restructured into one.

source: Game Progression (https://gamedesignskills.com/game-design/game-progression/) shows upgrade cadence framed as scheduled decision points, not automatic purchases.
counter-example: Does not apply to strictly linear tutorial-phase unlocks where a single guaranteed next step is intentional to avoid early-game decision fatigue.

### 4. Gate advancement with deterministic rewards; reserve chance for non-gating variety

When choosing between deterministic and chance-based progression for a reward, use deterministic delivery for anything that gates advancement (the next milestone, level, or required resource) and reserve randomness for optional variety rewards that do not block progress, because retention evidence favors players who can see a guaranteed path to their next milestone over players facing chance-gated advancement.

source: Understanding Games That Retain Players (https://medium.com/googleplaydev/understanding-games-that-retain-1847b16c86a7) shows retained players correlating with visible, guaranteed progression paths rather than chance-gated ones.
counter-example: Does not apply to purely cosmetic loot or collection variety systems with no bearing on advancement — chance there does not create the retention risk this rule addresses.

### 5. Set a stated target session spacing for any return-cadence timer, or omit the timer

When a system includes an energy/regen/daily-style return-cadence timer, state the target session spacing it is designed to produce, or remove the timer entirely if no such target exists, because a timer left in as a leftover default produces friction rather than the retention effect it was meant to create.

source: Understanding Games That Retain Players (https://medium.com/googleplaydev/understanding-games-that-retain-1847b16c86a7) shows return-cadence mechanics tied to a deliberate target return interval as a driver of retention.
counter-example: Does not apply to single-session or session-length-capped games with no cross-session return loop — there is no cadence to design.

## Related skills

- game-design-core-loop-and-progression: hop there when checking loop monotonicity or sink-before-source ordering at the core-loop level rather than the growth-system economy level.
- game-feel-juice-and-feedback: hop there when making a purchase, level-up, or upgrade moment feel rewarding through feedback and juice, not just structurally correct.
- product-discovery-guardrail-metrics: hop there when defining the retention metrics used to measure whether a growth-system change actually worked.
- finance-unit-economics-ltv-churn-assumption: hop there when the economy design touches revenue modeling or churn assumptions beyond retention pacing.
