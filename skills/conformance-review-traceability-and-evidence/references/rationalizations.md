# Rationalizations — conformance-review-traceability-and-evidence

Real excuses agents used to skip or soften this gate, mined from
tokenmaxxxer/on-the-record patrol/defect/process records and tm-dicequest
implementation records. Each row: the excuse (verbatim-ish), the reality,
the rule it points back to, and the originating incident.

| Rationalization (excuse) | Reality | Rule | Citation |
|---|---|---|---|
| "test_spawn.py passes (56/56)" — typed as evidence, no output. | A typed count is a claim, not evidence; cite file:line plus the reproduced output or the executable path a third party can re-run. | rule 1 | on-the-record#1610 (docs/issue-83/reports/coding.md '56/56' and 3 sibling #333-class unsupported test-count claims) |
| "See the linked record for the evidence." | Bare pointers rot; the citation must be exact (path + line range) and must still resolve at the cited sha. | rules 1-2 | on-the-record#1624 (4 broken test-path citations — test/ vs tests/, renamed files — in issue-711/476/1461 records) |
| "The earlier record already tallied this, I'll reuse the number." | Backward-trace to the primary evidence; inherited tallies were found unevidenced when finally traced. | rule 3 | on-the-record#1628 and #1630 (unevidenced 0/3 tallies in issue-645 and issue-476 records) |
