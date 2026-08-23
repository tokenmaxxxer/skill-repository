---
type: llm
criteria: >-
  Checks whether the response rejects the proposed 2-column grid and specifies
  a single-column layout for this linear-sequence form (allowing at most
  tightly paired fields like start/end date on one row).
target: last_message
---
Pass only if the response chooses a single-column layout for the form (it may
place tightly related pairs such as start-date/end-date side by side within
one row) and rejects the PM's 2-column left/right grid. Fail if it adopts the
proposed 2-column layout, splits the linear sequence across two independent
columns, or accepts multi-column mainly to fit above the fold.
