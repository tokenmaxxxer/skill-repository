---
type: llm
criteria: >-
  Checks whether the response prunes the stacked contrast treatments to a
  minimal combination that still passes 3:1 (e.g. elevation plus scrim, or
  elevation plus border) instead of enlarging/animating more signals.
target: last_message
---
Pass only if the response removes some of the four stacked signals (shadow,
scrim, border, label) down to a minimal combination that still passes the 3:1
non-text contrast check, and rejects adding emphasis (bigger label, pulsing
border). Fail if it keeps all four signals, adds the proposed
label-enlargement or border animation, or otherwise resolves the "busy"
feedback by strengthening signals rather than pruning them.
