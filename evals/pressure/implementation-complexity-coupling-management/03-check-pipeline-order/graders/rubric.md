---
type: llm
criteria: >-
  The judge checks that the response orders cheap touched-files checks
  before the expensive full-repo ones and consolidates the overlapping
  format/import tools instead of keeping all five.
target: last_message
---
Pass only if the response (a) orders cheapest-and-narrowest checks first
and the expensive full-repo mypy/tests last, and (b) consolidates the
overlapping formatting/import tools (e.g. drops black/isort in favor of
ruff, or an equivalent single tool covering the union) instead of
keeping all five. Fail if it keeps the teammate's expensive-first order,
or keeps all overlapping tools on the "more checks = more coverage"
reasoning.
