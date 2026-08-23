# Rationalizations — conformance-review-severity-classification

Real excuses agents used to skip or soften this gate, mined from
tokenmaxxxer/on-the-record patrol/defect/process records and tm-dicequest
implementation records. Each row: the excuse (verbatim-ish), the reality,
the rule it points back to, and the originating incident.

| Rationalization (excuse) | Reality | Rule | Citation |
|---|---|---|---|
| "It felt Medium to me." | Severity is a deterministic table lookup over observable characteristics, not a vibe; freehand scoring is the DREAD failure the field already abandoned. | section 'The shape of the classification' | (pattern, from on-the-record#1599 — 15% measured precision when findings were rendered without deterministic criteria) |
| "The author pushed back, so I dropped the finding." | A disputed finding is re-rated, never dropped; the finding survives with an adjusted band. | section 'What it asks the user for' | (pattern, from on-the-record#641 — deliverable critique softened when the reviewing session deferred instead of recording findings) |
| "It only fires in a rare corner, so it's Low." | Rarity is priority-side; the band measures impact if it fires. Downgrading by likelihood smuggles scheduling into a technical measure. | section 'The shape of the classification' (band criteria) | (pattern, from on-the-record#287 — S4/S5 fail-open guard holes were 'rare paths' that turned out to be the common layout) |
