---
name: game-character-animation-and-motion
description: Use when defining a character's animation state machine, choosing keyframes vs tween vs steps() for a state, setting anticipation/follow-through timing, or animating a DOM/SVG character. Applies to the character-animation-and-motion axis.
axis: character-animation-and-motion
rule_count_floor: 9
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
7. Before animating anything, decompose the entity into named rig parts (head/torso/limbs/weapon-or-tool minimum) with parent→child hierarchy and joint overlap, or record a single-primitive exception explicitly; a state machine over an undecomposed entity is not a valid starting point (rule 7).
8. For each of the six canonical cycles the entity uses (idle/walk/jump/attack/hurt/death), author key poses first — walk as contact/down/pass/up on a fixed frame grid, other cycles as anticipation→contact→recover triads — before adding in-between frames, respecting the per-cycle frame budget (idle ~2, walk 4-12, attack 3+) (rule 8).
9. For each cycle's key poses, run the silhouette test at the entity's target render scale and record pass/fail per pose before treating the cycle as done (rule 9).

## Output shape

A per-character animation spec: a state machine diagram or table (states, transitions, interruptibility), a duration/interruptibility table, per-state anticipation/follow-through frame counts, the chosen animation mechanism per state, sprite-sheet frame/pivot/loop metadata where applicable, the rig part list (named parts, hierarchy, or the recorded single-primitive exception), and a per-cycle key-pose sheet (key poses per canonical cycle with a silhouette pass/fail per pose). An animation spec with no recorded rig decision — neither a rig part list nor an explicit single-primitive exception — FAILS this output shape, regardless of how complete the rest of the spec is.

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

### 7. Entity is animated → decompose into a named rig before authoring any state, not a single primitive by default
When an entity has a state machine (idle/run/jump/attack/hit/death or a subset), decompose it into named rig parts — head, torso, limbs, and weapon-or-tool at minimum — with parent→child hierarchy and drawn joint overlap, because a single merged shape cannot carry per-part motion (a swung weapon, a stepping leg) without every other part moving with it; treat a single-primitive entity as a recorded exception, never the default starting shape.
source: drawphics.com's 2D character rigging guide (https://drawphics.com/how-to-rig-a-2d-character/) documents the named part-cut and joint-overlap floor; Toon Boom's cut-out character-building docs (http://docs.toonboom.com/help/game-studio-24/game-asset-editor/getting-started/character-building.html) show the parent→child cut-out hierarchy; game-ace's rigging-for-video-games overview (https://game-ace.com/blog/character-rigging-for-video-games/) confirms the hierarchy pattern for 2D game rigs
counter-example: a decorative, non-interactive, single-pose prop with no state machine at all has nothing to decompose and is exempt — the exception applies once an entity gains states, not before.

### 8. Cycle is one of the six canonical types → author key poses first on a fixed frame budget, not in-betweens first
When authoring idle, walk, jump, attack, hurt, or death, block the key poses before any in-between frame: walk as contact/down/pass/up on a fixed frame grid; jump/attack/hurt/death as one-shot anticipation→contact→recover triads. Hold each cycle to its frame budget (idle ~2, walk 4-12, attack 3+) because MapleStory-grade sprite depth comes from distinct poses, not frame count, and in-betweens authored before the key poses exist get redone once the poses change.
source: Wikipedia's Walk cycle article (https://en.wikipedia.org/wiki/Walk_cycle) documents the contact/down/pass/up canon; stevenschubert.com's walking-animation guide (https://stevenschubert.com/how-to-make-a-walking-animation) and garagefarm.net's walk-cycle guide (https://garagefarm.net/blog/walk-cycle-easy-steps-to-animate-walking-animation-for-beginners) show the frame-grid placement; mapleanime.com's frame-sequence thread (https://www.mapleanime.com/forum/viewtopic.php?t=927) and sprite-ai.art's sprite-animation-frames guide (https://www.sprite-ai.art/blog/sprite-animation-frames) anchor the per-cycle frame budgets
counter-example: a cycle whose entity has no discrete action beats at all (e.g. a purely tinted color-cycle effect with no pose change) has no key poses to block and is exempt from this breakdown.

### 9. Key pose exists → run the silhouette test at target render scale before calling the pose done
When a key pose is authored for any of the six canonical cycles, fill it solid black at the entity's shipped on-screen size and confirm the action reads from the outline alone, recording pass/fail per pose, because a pose that only reads with interior detail will not read at gameplay distance and the failure is cheaper to catch per-pose than after the whole cycle is assembled.
source: animotionx.com's readable-silhouette-in-gameplay-animation guide (https://www.animotionx.com/en/post/how-to-create-a-readable-silhouette-in-gameplay-animation) and anim.works's silhouette-in-animation article (https://anim.works/silhouette-in-animation/) apply the silhouette test to gameplay poses specifically; parkland.edu's silhouettes-and-poses lecture (https://csit.parkland.edu/~ddallas/csc189/Lecture/silhouettes/silhouettesAndPoses.html) ties silhouette distinctness to individual key poses, not just overall design
counter-example: a pose that is never rendered at gameplay scale (e.g. a cutscene close-up bust with no read-distance constraint) is exempt from the render-scale silhouette pass/fail.

## Related skills

- game-feel-juice-and-feedback: hop there when juice (squash/stretch, screen shake, particles) needs to layer on top of an already-working animation state machine.
- game-hit-reaction-and-impact: hop there when the hit/death state's specific reaction behavior (knockback, flash, hitstop) needs its own rules beyond generic timing — the hurt/death cycle's reaction must name which rig layer plays it, using this skill's rig part list (rule 7) as the source of layer names.
- game-character-rendering-composition: hop there when deciding how the rig or sprite layers are assembled before any animation is applied — its part/layer split (rule 4) must match this skill's rig part list (rule 7).
- html5-game-rendering-loop: hop there when frame timing or draw-loop mechanics underlying the animation need to be established first.
- accessibility-aria-and-contrast-rules: hop there when a reduced-motion contract needs to be defined for players who disable animation.
