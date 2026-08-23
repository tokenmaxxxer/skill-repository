---
type: llm
criteria: >-
  Checks whether the response prunes the stacked grouping signals down to one
  or two (e.g. whitespace plus a single boundary treatment) instead of adding
  the suggested icon and accent bar.
target: last_message
---
Pass only if the response removes redundant grouping cues — cutting the
divider/tint/bordered-card stack down to whitespace plus at most one boundary
treatment — and declines to add the icon and accent bar as more signals. Fail
if it adds the accent bar, icon, or any further boundary treatment on top of
the existing stack, or keeps all existing cues while merely restyling them.
