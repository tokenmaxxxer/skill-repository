# Rationalizations — conformance-review-verification-method-selection

Real excuses agents used to skip or soften this gate, mined from
tokenmaxxxer/on-the-record patrol/defect/process records and tm-dicequest
implementation records. Each row: the excuse (verbatim-ish), the reality,
the rule it points back to, and the originating incident.

| Rationalization (excuse) | Reality | Rule | Citation |
|---|---|---|---|
| "Reading the code is enough for this behavioral claim." | Inspection covers structural/static properties; behavioral claims need Test or Demonstration, or the verdict is a builder-style self-claim. | rules 1, 3 | on-the-record#1323 (verification was builder self-claim only; a deterministic check-runner had to be introduced) |
| "There's a test for this somewhere, count it verified." | Reusing a test as evidence requires actually executing it and citing the run, not gesturing at its existence. | rule 4 | on-the-record#1610 (typed pass-counts with no reproduced execution evidence, 6 confirmed instances) |
| "I'll just review it myself instead of running the machinery." | The method selection exists precisely so the reviewer's prose does not substitute for the named verification method. | rules 1-5 (method routing) | on-the-record#641 (consumer session planned 'I will review it myself and post the critique') |
