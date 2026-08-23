---
type: llm
criteria: >-
  Checks whether the response answers no and requires re-checking contrast
  against the actual rendered composite (85% opacity over arbitrary photos,
  focus ring overlapping the photo edge, interaction states), not just the
  flat swatch pairs.
target: last_message
---
Pass only if the response says the verification is NOT sufficient and calls
for checking contrast as actually rendered — the semi-transparent panel
composited over variable user photos and the focus ring where it overlaps the
photo — rather than accepting the isolated swatch-pair ratios. Fail if it
closes the ticket on the passing swatch numbers, or only suggests unrelated
extra checks without identifying the compositing/rendered-layer gap.
