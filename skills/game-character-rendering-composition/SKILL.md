---
name: game-character-rendering-composition
description: Use when drawing or assembling a character from parts, judging silhouette readability, splitting an SVG/DOM rig into layers, handling facing/flip, or setting character-vs-field z-order. Applies to the character-rendering-composition axis.
metadata:
  axis: character-rendering-composition
  rule_count_floor: 4
---

# Game Character Rendering Composition

These rules were sourced from published animation and game-art-direction references and gathered for issue #93's game-development research pass, 2026-08-23. They cover how to build a character's on-screen form — from silhouette to part layering to z-order — so the result reads correctly at shipped size before detail work begins.

## Trigger

Use this skill when drawing or assembling a character from parts, judging whether a character's silhouette reads at its shipped size, splitting an SVG/DOM character rig into layers or groups, handling left/right facing or flip behavior, or deciding how a character z-orders against field/background elements.

## Procedure

1. Block the character's overall silhouette solid black at target on-screen size and confirm it reads before adding any detail (rule 1).
2. Build outward in order — trunk, then limbs, then head, then fine details — checking readability at distance after each layer before advancing (rule 2).
3. Assign base shapes (rounded, angular, etc.) to roles so player, threat, and pickup types are distinguishable in grayscale, independent of color (rule 3).
4. Split the rig into SVG/DOM nodes by animation need: independent-moving parts get their own group, always-together parts stay merged; implement facing as a root-level transform flip (rule 4).
5. Declare a single named z-order contract across background, field, characters, effects, and UI layers rather than adjusting z-index per frame (rule 5).

## Output shape

A character build spec: the silhouette gate result (pass/fail at target size), the part/layer split (which nodes are independent groups vs. merged), the shape-language assignment per role, and the z-order contract naming each layer band the character interacts with. For an animated gameplay entity, the part split must explicitly name head/torso/limbs/weapon-or-tool (cross-ref `game-character-animation-and-motion`'s layered rig floor) and record the rig decision — including a single-primitive build, which is only valid as a stated exception. **Fail condition: a build spec for an animated gameplay entity that ships a single-primitive node without a recorded rig-decision exception fails this output shape.**

## Decision rules

### 1. When judging first-pass readability, gate on silhouette before detail

When a character design is new or being revised, test its shape filled solid black at the actual shipped on-screen size before refining any internal detail, and weight effort roughly 70/30 toward silhouette over detail, because a design that fails to read as a shape will not be fixed by detail added on top of it.
source: Silhouette in Animation (https://anim.works/silhouette-in-animation/) — describes silhouette testing as the first readability check in character design; also Stylized 3D Characters Art Direction Principles (https://nastyrodent.com/stylized-3d-characters-art-direction-principles/) — frames silhouette-first as core to art direction.
counter-example: For a character that is always shown large, close-up, or with unlimited screen real estate (e.g. a portrait/dialogue bust), silhouette-at-distance testing does not apply since read distance is not a constraint.

### 2. When building a character, order construction trunk to limbs to head to details with a gate at each step

When constructing a new character, build in the order trunk, then limbs, then head, then fine details, and do not proceed to the next layer until the current layer reads correctly at intended viewing distance, because errors compound outward and are cheaper to catch before the next layer is added on top.
source: Stylized 3D Characters Art Direction Principles (https://nastyrodent.com/stylized-3d-characters-art-direction-principles/) — lays out staged build order with readability checkpoints.
counter-example: For a character assembled entirely from a fixed pre-approved part library (no new base forms being drawn), the staged build-order gate is unnecessary since each part already passed its own readability check.

### 3. When multiple character roles must be told apart at a glance, assign shape language before color

When a scene contains multiple character roles (player, enemy, pickup, etc.), assign each role a distinct base shape family — e.g. rounded forms for friendly/player, angular forms for threat — before relying on color to distinguish them, because shape reads correctly even in grayscale or under color-vision limitations, while color alone does not.
source: Shape Language Technique (https://pixune.com/blog/shape-language-technique/) — explains assigning shape families to communicate role and intent; also Shape Language in Game Character Design (https://rocketbrush.com/blog/shape-language-in-game-character-design-how-to-make-characters-readable-and-consistent) — ties shape choice directly to gameplay-role readability.
counter-example: For characters within the same role/faction that only need cosmetic variety (e.g. palette-swapped skins of the same unit), shape-language differentiation does not apply since the role is already identical and only decoration should vary.

### 4. When splitting a character into an SVG/DOM rig, group parts by animation need and flip via transform

When building a character as an SVG or DOM rig, give each part that must move independently its own node or group, keep parts that always move together merged into one node, and implement left/right facing as a single `scaleX(-1)` transform on the rig root rather than duplicating mirrored art, because this keeps the rig's node count matched to its actual animation degrees of freedom and avoids maintaining two copies of the same art. For a gameplay entity that is animated (not a static icon), the part split must name at minimum head, torso, limbs, and weapon-or-tool as independent nodes — this is the same layered rig floor `game-character-animation-and-motion` sets for its rules; record which of those named parts exist as a rig decision in the build spec. A single-primitive node stands only as a recorded exception (e.g. an explicitly noted static/iconic case), never as an unstated default.
source: Joshwcomeau — sprite/character animation in CSS and DOM (https://www.joshwcomeau.com/animation/sprites/) — covers DOM/CSS mechanics for animating and flipping character parts.
counter-example: For a fully static character with no animation and no facing change (e.g. a single-orientation icon), splitting into independently animatable groups adds unnecessary complexity since nothing will ever move independently — but this exemption must itself be written down as the recorded rig decision, not left implicit.

### 5. When a character shares the screen with field/background elements, declare a named z-order contract once

When a character must render correctly against background, field, effects, and UI elements, declare a single named layer order (e.g. background, field, characters, effects, UI) once at the rig/scene level rather than adjusting z-index per frame or per interaction, because an ad hoc per-frame z-index fix creates silent regressions the next time an element's stacking order changes.
source: Shape Language Technique (https://pixune.com/blog/shape-language-technique/) — discusses readability of a character against its background, extended here to a stated character-vs-background/field layering contract.
counter-example: For a one-off cutscene or transient effect where layering is visually adjusted by hand for a single shot, a persistent named z-order contract is unnecessary overhead since the layering will not recur.

## Related skills

- game-character-animation-and-motion: hop there when the rig's parts exist to be animated and you need timing/motion rules, not just the part split.
- game-hit-reaction-and-impact: hop there when rendering hit flicker, flash, or impact feedback on top of the already-built rig.
- game-ui-board-and-lane-layout: hop there when deciding the field/board layout the character sits in, beyond the character's own z-order contract.
- brand-design-color-visibility: hop there when checking contrast of the chosen character palette against backgrounds.
- ux-engineering-color-visibility: hop there when a distinction between character states or roles is being made by color alone and needs a non-color-only fallback.
