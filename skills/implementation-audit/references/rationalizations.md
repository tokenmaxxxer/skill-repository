# Rationalizations — implementation-audit

Real excuses agents used to skip or soften this gate, mined from
tokenmaxxxer/on-the-record patrol/defect/process records and tm-dicequest
implementation records. Each row: the excuse (verbatim-ish), the reality,
the rule it points back to, and the originating incident.

| Rationalization (excuse) | Reality | Rule | Citation |
|---|---|---|---|
| "I wrote it, I can check it myself." | Self-review defends the work instead of testing it; evaluation belongs to an independent Session B that never sees the builder's intent. | section 'The two-session protocol' | on-the-record#641 (session defaulted to 'I will review it myself' until corrected live) |
| "The claims are obviously true, skip the extraction step." | Unextracted claims are unfalsifiable; the audit exists because 'obviously true' records have carried fabricated verification. | Step A1 (falsifiable, atomic claims) | on-the-record#476 (fabricated-verification shape caught only by an independent re-run) |
| "Tests pass N/N" — offered as audit evidence with no run output. | A typed count is grade-F evidence; the evaluator needs the reproduced execution, or the claim is annotated unverifiable. | section 'Evidence grade' | on-the-record#1610 (6 confirmed unsupported test-count claims across 3 records) |
