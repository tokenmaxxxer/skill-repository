# Scout brief — issue #96 motion-design depth

Mode: PARALLEL fan-out (4 concurrent WebSearch calls, one sweep round).
Stages used: 1 of 5 — stopped at saturation (every survey gap got a
usable source in the sweep; a deepening round would not change a build
decision).

## Category must-bes (what strong sources assume)

- A rigged 2D game character is cut into named parts — head, torso,
  upper/lower arm, hand, upper/lower leg, foot (weapon as a hand
  attachment) — with hierarchy (child follows parent) and overlap drawn
  at joints; a single merged shape is not a rig.
- A walk cycle is authored as 4 canonical key poses per leg — contact,
  down, pass, up — placed on a fixed frame grid (contact at 0/12/24 at
  24fps), minimum 8 frames, seamless loop.
- Action animations (attack) are pose-first: anticipation → contact →
  recovery key poses, with attack blending back into idle.
- Pose quality is gated by the silhouette test: fill the key pose solid
  black at read distance; if the action doesn't read from the outline
  alone, the pose fails — applied per key pose, not just per design.
- MapleStory-grade sprites use a small fixed frame budget per cycle
  (idle ~2, walk 4-12, attack 3+ frames) with a nested/layered part
  structure — depth comes from distinct poses, not frame count.

## Performance axes

1. Pose readability (silhouette-distinct keys) vs. frame count — the
   field competes on poses, not smoothness.
2. Rig granularity (degrees of freedom) vs. authoring cost.

## Adopt / skip

- Adopt: named-part rig floor; contact/down/pass/up walk canon;
  anticipation-contact-recover pose triads per action cycle; per-key-pose
  silhouette test at target render scale; recorded rig decision as a
  checklist artifact.
- Skip: bone/mesh-deformation tooling specifics (Spine/Live2D/Unity IK)
  — this repo's targets are SVG/DOM rigs; cite the part-set canon, not
  the tool.

## Gap line

Current skills already meet: state-machine-first, anticipation/
follow-through frames, design-time silhouette gate, group-by-animation-
need. Missing: minimum named part set, per-cycle key-pose breakdowns,
silhouette test applied to poses at render scale, and any checklist item
that fails a single-primitive entity with no recorded rig decision.

## Segment fit

Same segment as wave-2 skills: browser DOM/SVG game characters at small
render scale; MapleStory anchor confirms layered-part + few-distinct-
poses is the grade demanded in tm-dicequest#58.

Sources:
- https://drawphics.com/how-to-rig-a-2d-character/ (part cut list, joint overlap)
- http://docs.toonboom.com/help/game-studio-24/game-asset-editor/getting-started/character-building.html (cut-out rig hierarchy)
- https://game-ace.com/blog/character-rigging-for-video-games/ (2D rig tools/hierarchy)
- https://en.wikipedia.org/wiki/Walk_cycle (contact/down/pass/up canon)
- https://stevenschubert.com/how-to-make-a-walking-animation (9-pose walk breakdown, frame grid)
- https://garagefarm.net/blog/walk-cycle-easy-steps-to-animate-walking-animation-for-beginners (frame placement)
- https://www.animotionx.com/en/post/how-to-create-a-readable-silhouette-in-gameplay-animation (silhouette in gameplay animation)
- https://anim.works/silhouette-in-animation/ (silhouette pose test)
- https://csit.parkland.edu/~ddallas/csc189/Lecture/silhouettes/silhouettesAndPoses.html (key-pose silhouette distinctness)
- https://www.mapleanime.com/forum/viewtopic.php?t=927 (MapleStory frame sequence: stand/walk/hit/die/attack1-3)
- https://www.sprite-ai.art/blog/sprite-animation-frames (per-cycle frame budgets)
- https://www.sprite-ai.art/guides/how-to-animate-pixel-art (idle/walk/attack authoring)
