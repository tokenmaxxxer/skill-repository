---
type: llm
criteria: >-
  Checks whether the response deletes the single-child "Data Tools" parent and
  promotes CSV Export to a direct top-level item.
target: last_message
---
Pass only if the response removes the Data Tools parent level and places CSV
Export directly in the top nav (one click), rejecting the keep-for-consistency
argument given the empty roadmap. Fail if it keeps the single-child dropdown
for consistency or hypothetical future tools, or nests CSV Export under some
other parent instead of promoting it.
