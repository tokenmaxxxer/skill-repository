# Rationalizations — conformance-review-requirement-extraction

Real excuses agents used to skip or soften this gate, mined from
tokenmaxxxer/on-the-record patrol/defect/process records and tm-dicequest
implementation records. Each row: the excuse (verbatim-ish), the reality,
the rule it points back to, and the originating incident.

| Rationalization (excuse) | Reality | Rule | Citation |
|---|---|---|---|
| "The acceptance section is one paragraph, so it is one requirement." | Bundled obligations get one verdict for many promises; each 'and'/'or' clause is checked (or missed) separately. | rule 1 | on-the-record#2085 (acceptance gate surfaced one missing element per attempt — bundled requirements cost three round-trips to even enumerate) |
| "This requirement can't really be tested, so I'll drop it from the list." | Unverifiable-as-written items are flagged and kept, never silently dropped — a dropped item reads later as 'checked clean'. | rule 2 | on-the-record#287 ("can't check" reported as "checked clean" across closure_sweep/flows/deliverable-guard) |
| "The task text already implies the answer, so extraction is a formality." | When the task string pre-shapes the expected verdict, extraction is exactly where independence is recovered; skipping it reduces review to transcription. | rule 5 | on-the-record#476 (orchestrator task strings containing the solution, reducing the role to transcription) |
