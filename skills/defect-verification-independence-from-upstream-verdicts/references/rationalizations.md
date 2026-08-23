# Rationalizations — defect-verification-independence-from-upstream-verdicts

Real excuses agents used to skip or soften this gate, mined from
tokenmaxxxer/on-the-record patrol/defect/process records and tm-dicequest
implementation records. Each row: the excuse (verbatim-ish), the reality,
the rule it points back to, and the originating incident.

| Rationalization (excuse) | Reality | Rule | Citation |
|---|---|---|---|
| "Review already marked it Present, no need to re-test." | Present is a claim to independently test; deferring to it is how fabricated 'reproduced' findings survived until an operator re-run. | rule 1 | on-the-record#476 (core#163: 'reproduced' findings whose repro tests failed in a clean checkout) |
| "The upstream record is clean, so fewer attempts are fine." | A clean upstream record is not evidence of absence and must not shrink the attempt list at planning time. | rule 9 (REMOVAL) | on-the-record#476 (gate-satisfying theater: verification shaped to match the expected outcome) |
| "The sha probably still matches, cite-and-skip." | Cite-and-skip is legitimate only on a genuinely matching sha; under time pressure the incentive is to declare a match without checking. | rules 3, 8 | on-the-record#1037 (closed_checks-style claims found stale when re-derived from primary evidence) |
