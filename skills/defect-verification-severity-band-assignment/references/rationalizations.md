# Rationalizations — defect-verification-severity-band-assignment

Real excuses agents used to skip or soften this gate, mined from
tokenmaxxxer/on-the-record patrol/defect/process records and tm-dicequest
implementation records. Each row: the excuse (verbatim-ish), the reality,
the rule it points back to, and the originating incident.

| Rationalization (excuse) | Reality | Rule | Citation |
|---|---|---|---|
| "The deadline makes this Critical." | Urgency is priority, a business axis; the band measures technical impact only and stays blind to scheduling. | rules 1, 10 (REMOVAL) | (pattern, from on-the-record#1610 — fix-policy language kept severity of confirmed violations separate from remediation urgency) |
| "It's rare, so band it down." | Band by impact IF it fires; likelihood is priority-side, and rare-path guard holes have turned out to be the common layout. | rule 7 | on-the-record#287 (S5: the 'rare' tests/ layout the guard never covered was the far more common one) |
| "Call it 'annoying, nice to fix'." | Locally-improvised vocabulary reintroduces the ambiguity the deterministic tiers remove; use only the defined bands, with the driving criterion stated. | rules 8, 9 (REMOVAL) | (pattern, from on-the-record#1599/#1620 — informal grading language that had to be replaced by a graded table before precision could be measured) |
