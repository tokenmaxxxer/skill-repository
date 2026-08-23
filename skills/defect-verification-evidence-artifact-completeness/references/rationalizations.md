# Rationalizations — defect-verification-evidence-artifact-completeness

Real excuses agents used to skip or soften this gate, mined from
tokenmaxxxer/on-the-record patrol/defect/process records and tm-dicequest
implementation records. Each row: the excuse (verbatim-ish), the reality,
the rule it points back to, and the originating incident.

| Rationalization (excuse) | Reality | Rule | Citation |
|---|---|---|---|
| "The test passed when I ran it" — nothing captured. | Capture the artifact once, at attempt time; an uncaptured run is a typed claim that later re-verification may contradict. | rules 1, 4 | on-the-record#1610 (fix policy forced dated re-runs because attempt-time output was never captured) |
| "See the linked recording" — no pointer that resolves. | A reference that cannot be opened at the cited sha is not an artifact; the removal rule exists because these links rot. | rule 9 (REMOVAL) | (pattern, from on-the-record#1624 — 4 evidence citations that no longer resolved) |
| "Environment details are optional metadata." | Without sha/run context the attempt cannot be re-checked against a moved-forward branch; the same steps pass on one sha and fail on another. | rules 3, 10 (REMOVAL) | on-the-record#1610 (claims were unre-checkable precisely because no environment was recorded with them) |
