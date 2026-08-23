# Rationalizations — defect-verification-reproduction-evidence-quality

Real excuses agents used to skip or soften this gate, mined from
tokenmaxxxer/on-the-record patrol/defect/process records and tm-dicequest
implementation records. Each row: the excuse (verbatim-ish), the reality,
the rule it points back to, and the originating incident.

| Rationalization (excuse) | Reality | Rule | Citation |
|---|---|---|---|
| "It reproduced for me; the steps are in my head." | A finding with no reconstructable numbered path plus artifact is not independently re-checkable — the exact shape that failed a clean-checkout re-run. | rules 1, 5 | on-the-record#476 (core#163: recorded 'reproduced' claims failed when independently re-executed) |
| "It didn't repro on the first try, so: not-reproduced." | Confirm the starting state matches the candidate's description first; a mismatched-state failure is a false not-reproduced, not absence. | rule 8 | (pattern, from on-the-record#287 — a failed attempt reported indistinguishably from a clean result) |
| "I'll paste my whole exploration log as the repro." | The exploration trail is process, not evidence; record the reduced minimal path or the one load-bearing step is buried. | rules 2, 10 (REMOVAL) | (pattern, from on-the-record#1599 — narrated process text triggering record-lint misfires in place of evidence) |
