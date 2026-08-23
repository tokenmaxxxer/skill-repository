---
type: llm
criteria: >-
  The judge checks whether the response splits the bundled acceptance
  paragraph into one line item per obligation (roughly six: CSV validation,
  rejected-row logging with line number, 207 on partial failure, per-row
  status array, import.partial metric, admin UI outcome+link) instead of one
  or two lumped items.
target: last_message
---
Pass only if the response extracts a list with one obligation per line item,
separately covering at least: schema validation, logging rejected rows with
line numbers, HTTP 207 on partial failure, the per-row status array, the
import.partial metric, and the admin UI outcome display/link (five or more
distinct items). Fail if it keeps the paragraph as one or two bundled
checklist lines such as "import flow works as described".
