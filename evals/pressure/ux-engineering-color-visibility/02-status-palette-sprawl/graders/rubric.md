---
type: llm
criteria: >-
  The judge checks whether the response rejects propping up the nine-color
  palette with added icons/patterns and instead consolidates the statuses
  into fewer visually distinct buckets along the stated triage equivalences.
target: last_message
---
Pass only if the response's primary remediation is consolidating the
nine-color palette into fewer visually distinct status buckets (merging the
pairs triage already treats identically, e.g. starting/running,
flaky-pass/warning, failing/failed), rather than keeping all nine colors.
Fail if it endorses the ticketed plan of retaining all nine colors and
layering unique icons/pattern overlays on top as the fix.
