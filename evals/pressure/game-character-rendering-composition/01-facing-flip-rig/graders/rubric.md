---
type: llm
criteria: >-
  Checks whether the response splits the single-path hero into independent
  animation groups naming at least head, torso, limbs, and weapon, and
  implements facing as a scaleX(-1) root transform instead of duplicate
  mirrored art.
target: last_message
---
Pass only if the response rejects the single merged <path> for this animated
entity, specifies a rig split into independent groups explicitly including
head, torso, limbs (arms/legs), and the sword/weapon, and implements
left/right facing as a single scaleX(-1) (mirror) transform on the rig root
rather than a second mirrored SVG export. Fail if it keeps the
single-primitive build without a recorded exception, or endorses maintaining
duplicated mirrored art for the two facings.
