# Rationalizations — implementation-complexity-coupling-management

Real excuses agents used to skip or soften this gate, mined from
tokenmaxxxer/on-the-record patrol/defect/process records and tm-dicequest
implementation records. Each row: the excuse (verbatim-ish), the reality,
the rule it points back to, and the originating incident.

| Rationalization (excuse) | Reality | Rule | Citation |
|---|---|---|---|
| "Not applicable — no threshold crossed" — asserted without measuring anything. | The NA verdict requires the same measurement the applied path does; keyword-matching the trigger sentence is not a coupling measurement. | rule 1 (CBO threshold) | tm-dicequest docs/issue-12/reports/implementation.md ('cross-family keyword match only' NA line); on-the-record#2062 (skills marked applied/NA without their rules ever being loaded) |
| "The monolith still works; we'll split it later." | Deferred decomposition compounds: the file that 'still worked' reached 9,351 lines and needed a strangler-fig program to touch safely. | rules 3, 6 (REMOVAL) | on-the-record#2105 (spawn.py 9,351-line monolith decomposition) |
| "Check ordering in the pipeline doesn't matter." | Ordering and batching determine how many round-trips a violation costs; one-violation-per-attempt reporting tripled spawn latency. | rules 8-9 | on-the-record#2085 (acceptance gate reported one missing element per spawn attempt — 3 round-trips for 3 requirements) |
