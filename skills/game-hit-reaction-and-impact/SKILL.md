---
name: game-hit-reaction-and-impact
description: Use when tuning a hit's stop/knockback, adding damage numbers, assigning invulnerability frames, deciding screen-level hit feedback. Applies to the hit-reaction-and-impact axis.
axis: hit-reaction-and-impact
rule_count_floor: 5
---

# Game Hit Reaction and Impact

Landing a hit needs to feel like it landed: a freeze, a shove, a number, a window of safety. These rules are sourced from fighting-game design analysis and reference wikis, gathered for issue #93's game-development research pass, 2026-08-23.

## Trigger

Use when tuning a hit's stop/knockback duration or curve, adding floating damage numbers, assigning invulnerability frames to a recovery state, or deciding whether a hit warrants screen-level feedback.

## Procedure

1. Classify the attack by weight (light/medium/heavy) and set the hit-stop duration band accordingly (rule 1).
2. Shape the knockback as a decaying curve scaled to the same weight class as hit-stop (rule 2).
3. Attach invulnerability frames to a named recovery state with a visible flicker cue (rule 3).
4. Spawn damage numbers at the impact point with bounded lifetime and batching for rapid hits (rule 4).
5. Reserve screen-level shake/flash for the heavy-impact tier only, deferring the restraint contract elsewhere (rule 5).
6. Compile the per-attack-class values into the impact contract artifact.

## Output shape

The artifact is an impact contract per attack class: a table or config listing hit-stop frames, knockback curve parameters, invulnerability-frame state names and durations, damage-number spawn/lifetime rules, and whether the class qualifies for screen-level feedback. The contract must also name which rig layer(s) flash or recoil on hit (e.g. torso, limb) — the hurt pose comes from posing the named rig layers recorded in `game-character-rendering-composition`'s build spec (per `game-character-animation-and-motion`'s layered rig floor), not from a whole-token tint or flash applied to an un-decomposed entity. **The contract is explicitly unfillable for an entity with no recorded rig decision: if the build spec carries no named part split, there is no rig layer to name as flashing/recoiling, and this output shape cannot be completed until that decision is recorded.**

## Decision rules

### 1. Hit-stop duration scales with attack weight

When an attack lands, freeze both attacker and victim briefly before knockback begins, and set the freeze duration by attack weight class — light attacks shorter, heavy attacks longer — because a uniform stop duration makes light jabs feel mushy and heavy attacks feel weightless. Fighting-game canon anchors light ≈ 9, medium ≈ 11, heavy ≈ 13 frames at 60fps; scale proportionally to your own tick rate.
source: SSBWiki, Hitlag (https://www.ssbwiki.com/Hitlag) shows per-weight-class hitlag frame values used as a canonical anchor.
counter-example: For continuous damage-over-time or environmental hazards with no discrete "hit" moment, hit-stop does not apply — there is no single contact frame to freeze on.

### 2. Knockback uses a decaying curve, not a linear shove

When applying knockback after a hit, use a strong initial impulse that eases out over time rather than a constant-velocity push, and scale the magnitude to the same weight class used for hit-stop, because knockback is a flow/combo-control signal and a linear or mismatched curve breaks combo readability and desyncs the visual impact from the mechanical effect.
source: Shane Sicienski, Capcom-style hitstop and impact analysis (https://shane-sicienski.com/blog/blog-post-title-one-55pmn) shows decaying-impulse knockback curves paired with hitstop weight tiers.
counter-example: For a pure knockdown/stagger attack that fully interrupts and repositions the target to a fixed point (not a physics shove), a decaying velocity curve is unnecessary — use a positional transition instead.

### 3. Invulnerability frames attach to named recovery states, not untracked timers

When a character needs post-hit or knockdown-getup safety, attach the invulnerability window to a named state (e.g. "post-hit-recovery", "getup") rather than a bare countdown timer, and render a visible flicker or blink for the duration, because an untracked timer decouples invulnerability from animation and produces edge cases where the window outlives or under-runs the visible cue, misleading players about their safety.
source: Super Smash Bros Fandom Wiki, Invincibility frame (https://supersmashbros.fandom.com/wiki/Invincibility_frame) shows invincibility tied to specific named states (spawn, roll, getup) with visible flicker feedback.
counter-example: For a permanent god-mode/debug toggle, a raw timer or boolean flag is appropriate since there is no associated recovery animation to bind to.

### 4. Damage numbers spawn at impact point and batch on rapid hits

When a hit lands, spawn the damage number at the impact point, float it upward, and fade it out within a bounded lifetime, never letting it obstruct the character or an incoming threat; when multiple hits land in quick succession, batch them into a single combined number rather than stacking unreadable columns, because unbatched rapid-hit numbers overwhelm screen space and reduce the readability the numbers exist to provide.
source: Sonic Hurricane, impact-freeze readability discussion (https://sonichurricane.com/?p=1043) frames impact readability as a design constraint alongside hit-freeze timing.
counter-example: For a single big finishing-blow number meant to be a deliberate spectacle (e.g. a critical/finisher display), the fade-fast/batch rule does not apply — let it linger and read clearly on its own.

### 5. Screen-level feedback is reserved for the heavy-impact tier and capped

When a hit occurs, keep per-hit feedback (hit-stop, knockback, numbers) as the default signal, and only add screen-level effects like camera shake or flash for attacks in the design's heavy-impact tier, capping intensity rather than scaling it per-hit, because hitlag is already a distinct, cheaper per-hit signal and uncapped screen-level effects compound into nausea and readability loss — defer the restraint/reduced-motion contract to game-feel-juice-and-feedback rather than restating it here.
source: SSBWiki, Hitlag (https://www.ssbwiki.com/Hitlag) shows hitlag functioning as the per-hit signal distinct from screen-level camera/flash effects.
counter-example: For a boss's telegraphed ultimate attack or a scripted cutscene beat, screen-level effects may be justified outside the heavy-impact-tier cap since the moment is a one-off spectacle rather than routine combat feedback.

## Related skills

- game-feel-juice-and-feedback: hop there when deciding screen-level effect restraint or the reduced-motion contract for shake/flash.
- game-character-animation-and-motion: hop there when defining the hit/death animation states the reaction plays against, and for the layered rig floor (named parts) the hurt pose is built from.
- game-character-rendering-composition: hop there when the rig's part split/layer decision has not yet been recorded — the impact contract's rig-layer flash/recoil naming depends on that recorded decision.
- game-design-core-loop-and-progression: hop there when checking whether damage/knockback numbers fit the core loop's pacing.
- html5-game-rendering-loop: hop there when implementing hit-stop as a freeze against the actual frame timer.
