---
type: llm
criteria: >-
  Checks whether the response gates the designs on a solid-black silhouette
  test at the shipped 48px size and fixes distinguishability at the shape/
  silhouette level, rather than approving a detail/glow/aura pass.
target: last_message
---
Pass only if the response requires testing each enemy's shape filled solid
black at the actual 48x48 shipped size (or equivalent silhouette-at-size
gate) before any detail sign-off, and directs the fix toward distinct
silhouettes/shape language for the confused roles rather than more detail.
Fail if it approves the detail pass, or accepts the contractor's rune-glow
and colored-aura fix as the primary remedy for the confusion.
