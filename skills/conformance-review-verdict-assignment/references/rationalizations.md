# Rationalizations — conformance-review-verdict-assignment

Real excuses agents used to skip or soften this gate, mined from
tokenmaxxxer/on-the-record patrol/defect/process records and tm-dicequest
implementation records. Each row: the excuse (verbatim-ish), the reality,
the rule it points back to, and the originating incident.

| Rationalization (excuse) | Reality | Rule | Citation |
|---|---|---|---|
| "I couldn't reach that environment, so I marked it Present." | Cannot-check is its own verdict; converting unavailability into a pass makes a negative result unfalsifiable. | rule 3 | on-the-record#287 (closure_sweep printed 'no violations' and exited 0 whenever gh failed) |
| "A prior review already marked it Present." | Re-derive at the current sha; inherited Present verdicts have covered fabricated verification before. | rule 4 | on-the-record#476 (core#163: a record claimed two findings 'reproduced' whose own repro tests failed in a clean checkout) |
| "The code landed, so the requirement is met." | Code-landed is not verified-in-use; the verdict names the observed behavior against the clause, not the merge event. | rules 1, 5 | on-the-record#1037 (northpole gap audit: 'requirement closed' claims refuted as code-landed-only) |
