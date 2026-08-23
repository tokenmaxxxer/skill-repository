---
name: game-character-animation-and-motion
description: Use when defining a character's animation state machine, choosing keyframes vs tween vs steps() for a state, setting anticipation/follow-through timing, or animating a DOM/SVG character. Applies to the character-animation-and-motion axis.
axis: character-animation-and-motion
rule_count_floor: 5
---

# Game Character Animation and Motion

These rules are sourced from published animation and web-performance guidance, gathered for issue #93's game-development research pass, 2026-08-23. They cover state-machine structure, timing principles, animation mechanism choice, and sprite-sheet fundamentals for character motion.

## Trigger

Use this skill when defining a character's animation state machine, choosing between keyframes, CSS transitions, steps(), or JS-driven tweens for a given state, setting anticipation/follow-through timing on an action, or animating a DOM/SVG character.

## Procedure

1. Enumerate the character's states (idle/run/jump/attack/hit/death) and their transitions and interruptibility before tuning any per-state art or timing (rule 1).
2. For attack and jump states, add an anticipation frame band; for landing/stop states, add 1-3 follow-through frames scaled to weight (rule 2).
3. Pick the animation mechanism per state's shape: CSS transition, steps() keyframes, or JS-driven transform updates (rule 3).
4. Constrain all motion to transform/opacity properties only (rule 4).
5. Assign each state a duration and interruptibility value in a single declared table (rule 5).
6. For sprite-sheet-based states, fix frame size/pivot and mark each state as loop or one-shot (rule 6).

## Output shape

A per-character animation spec: a state machine diagram or table (states, transitions, interruptibility), a duration/interruptibility table, per-state anticipation/follow-through frame counts, the chosen animation mechanism per state, and sprite-sheet frame/pivot/loop metadata where applicable.

## Decision rules

### 1. Character has multiple behavioral states → declare the state machine before tuning any single state
When a character can idle, run, jump, attack, take a hit, or die, declare the full state machine (states, transitions, interruptibility) before tuning any single state's art or timing, because per-state tuning done before the transition graph exists gets redone once interruption rules surface conflicts.
source: sprite-ai.art animation principles guide (https://www.sprite-ai.art/guides/animation-principles) shows state-machine-first workflows for sprite characters
counter-example: a single-state, non-interactive decorative sprite (e.g. an ambient background creature with no gameplay input) does not need a declared transition graph.

### 2. Action carries weight → add anticipation and follow-through frames scaled to that weight
When a state represents an attack, jump, or other weighted action, add an anticipation frame band before the main motion and 1-3 follow-through frames after landing/stopping, scaling frame counts to the action's perceived weight, because even a single anticipation frame measurably changes how impactful a jump or swing reads.
source: Game Developer's 12 principles of animation in video games (https://www.gamedeveloper.com/production/the-12-principles-of-animation-in-video-games) documents anticipation/follow-through's effect on perceived weight
counter-example: instantaneous, non-physical state changes (e.g. a UI cursor swap or an idle-to-idle blend) don't carry weight and don't need anticipation/follow-through.

### 3. Mechanism choice depends on state shape → transition, steps(), or JS-driven transform
When a state is a simple two-value change, use a CSS transition; when it is a frame-by-frame sprite-sheet sequence, use CSS keyframes with steps(); when it is continuous physics-coupled motion, drive transform updates from JS, because each mechanism matches a different update cadence and none of the three substitutes cleanly for another.
source: Josh Comeau's sprite animation guide (https://www.joshwcomeau.com/animation/sprites/) contrasts steps()-based sprite playback against transition-based state changes; LogRocket's sprite-sheet CSS animation guide (https://blog.logrocket.com/making-css-animations-using-a-sprite-sheet/) shows the steps() keyframe pattern in practice
counter-example: a state driven entirely by an external physics engine that already emits per-frame transforms doesn't need a separate CSS mechanism.

### 4. Motion must stay on the compositor → animate transform/opacity, never layout properties
When animating character position or visibility, animate transform and opacity only, never top/left/width/height, because layout-property animation forces synchronous layout recalculation and drops frames under load.
source: web.dev's animations guide (https://web.dev/articles/animations-guide) documents compositor-only properties for jank-free animation
counter-example: a one-time, non-animated layout change (e.g. repositioning a character on level load, with no transition) is not subject to this constraint since no animation is running.

### 5. Multiple states need consistent timing → declare per-state duration and interruptibility in one table
When a character has several animated states, declare duration and interruptibility for each state together in a single table rather than setting each tween's timing independently, because locomotion/idle should read as snappy and interruptible, attacks should commit through recovery, and hit/death should interrupt everything — and that pattern only stays consistent when authored as one policy, not scattered per-tween values.
source: sprite-ai.art animation principles guide (https://www.sprite-ai.art/guides/animation-principles) frames per-state timing as a systemic authoring decision
counter-example: a character with only one animated state (e.g. a static idle-only prop) has no cross-state consistency to maintain.

### 6. State uses a sprite sheet → fix frame size/pivot and mark loop vs one-shot
When a state is built from a sprite sheet, keep frame size and pivot point consistent across all frames, build locomotion states (idle/run) as looping cycles, and mark one-shot states (attack/hit/death) to never loop, because inconsistent pivots cause visible jitter and looping a one-shot state causes it to visibly repeat mid-action.
source: pixel-editor.com's sprite animation fundamentals article (https://www.pixel-editor.com/articles/sprite-animation-fundamentals) covers frame consistency and loop-vs-one-shot classification
counter-example: vector/SVG-rigged characters that don't use sprite sheets have no frame-size or pivot consistency requirement.

## Related skills

- game-feel-juice-and-feedback: hop there when juice (squash/stretch, screen shake, particles) needs to layer on top of an already-working animation state machine.
- game-hit-reaction-and-impact: hop there when the hit/death state's specific reaction behavior (knockback, flash, hitstop) needs its own rules beyond generic timing.
- game-character-rendering-composition: hop there when deciding how the rig or sprite layers are assembled before any animation is applied.
- html5-game-rendering-loop: hop there when frame timing or draw-loop mechanics underlying the animation need to be established first.
- accessibility-aria-and-contrast-rules: hop there when a reduced-motion contract needs to be defined for players who disable animation.
