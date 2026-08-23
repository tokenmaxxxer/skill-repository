# Rationalizations — conformance-review-finding-record

Real excuses agents used to skip or soften this gate, mined from
tokenmaxxxer/on-the-record patrol/defect/process records and tm-dicequest
implementation records. Each row: the excuse (verbatim-ish), the reality,
the rule it points back to, and the originating incident.

| Rationalization (excuse) | Reality | Rule | Citation |
|---|---|---|---|
| "The what/why fields are boilerplate anyway, fill them to pass the gate." | Fields filled to satisfy the record gate carry zero information; the rationale must connect this evidence to this verdict. | rule 3.5 | on-the-record#476 (records routinely satisfied required fields as boilerplate to pass record-fields-gate) |
| "Paraphrasing what the diff does is faster than pointing at it." | Evidence is the reproduction path (file, line, hunk) — a paraphrase cannot be independently re-checked and fails record lint. | rule 3.4 | on-the-record#1596 and #1609 (patrol record-lint-violation on docs/issue-831/reports/architecture.md) |
| "The verdict is obvious, no rationale needed." | Unattributed verdicts are exactly the tallies later found unevidenced; every verdict line carries its one-line why. | rules 3.3, 3.5 | on-the-record#1628 (unevidenced tallies surfaced in the final sweep-queue drain) |
