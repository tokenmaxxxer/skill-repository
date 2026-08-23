---
name: game-character-rendering-composition--facing-flip-rig
---
We're building a 2D browser RPG. The hero is rendered as inline SVG and will
be animated: idle breathing, a walk cycle, a sword swing, and a hurt flinch.
The hero walks both left and right on screen. The current draft SVG is one
<path> — the whole hero (body, arms, head, sword) drawn as a single merged
outline, which was quick to export from the design tool and renders fast. For
the left-facing version, the artist plans to export a second mirrored SVG so
"the light source stays consistent" and each direction can be tweaked
independently later.

Spec the SVG structure for this hero: what nodes/groups it should contain,
and how left/right facing should be implemented.
