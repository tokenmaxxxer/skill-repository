# Rationalizations — implementation-design-pattern-selection

Real excuses agents used to skip or soften this gate, mined from
tokenmaxxxer/on-the-record patrol/defect/process records and tm-dicequest
implementation records. Each row: the excuse (verbatim-ish), the reality,
the rule it points back to, and the originating incident.

| Rationalization (excuse) | Reality | Rule | Citation |
|---|---|---|---|
| "Strategy is the professional way, even with one case." | A pattern with one concrete case is indirection without a second reason to change; keep the direct form until the second case exists. | rules 1-3 | tm-dicequest docs/issue-8/reports/implementation.md (Strategy-vs-static-data-table decided for the direct table in phase-1 — the recorded counter-decision this excuse ignores) |
| "The pattern call was already made in phase-1" — claimed while a new pattern decision arose. | NA-by-prior-decision holds only when this phase truly adds no new decision point; a new divergence re-opens the question. | rules 1, 4 | tm-dicequest docs/issue-18/reports/implementation.md (the legitimate frozen-decision NA form; on-the-record#2039 made the per-skill verdict + reason obligatory because bare NA claims were unverifiable) |
| "Keep the factory, someone might need it." | A factory that only ever constructs one product is a removal candidate now; speculative generality is the excuse, YAGNI is the reality. | rule 5 (REMOVAL) | (pattern, from on-the-record#1044 — panel_cmd() shipped with no dispatch: capability built for a future caller that never came) |
