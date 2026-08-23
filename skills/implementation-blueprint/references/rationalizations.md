# Rationalizations — implementation-blueprint

Real excuses agents used to skip or soften this gate, mined from
tokenmaxxxer/on-the-record patrol/defect/process records and tm-dicequest
implementation records. Each row: the excuse (verbatim-ish), the reality,
the rule it points back to, and the originating incident.

| Rationalization (excuse) | Reality | Rule | Citation |
|---|---|---|---|
| "The structure is obvious, skip classify." | The classify step is cheap and its veto is the tool's to give; 'obvious' pre-decisions are how predetermined answers enter the record. | section 'Workflow' step 1 | (pattern, from on-the-record#476 — predetermined answers performed through the procedure) |
| "Phase-1 already froze the architecture" — claimed while making a new structural decision. | Not-applicable is legitimate only when no new structural decision arises this phase; the verdict must name what was frozen and by which record. | section 'Workflow' (applicability check) | tm-dicequest docs/issue-58/reports/implementation.md and docs/issue-18/reports/implementation.md (the legitimate NA form these wrongly-claimed cases must match) |
| "Re-run classify until it gives the answer I wanted." | The recommendation is deterministic and emitted once; if the situation changed, the inputs changed — rerun with new inputs, never shop for output. | section 'Rules of engagement', determinism bullet | (pattern, from on-the-record#476 — gate-satisfying theater: procedure re-run to produce the pre-decided result) |
