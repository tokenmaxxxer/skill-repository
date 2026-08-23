# Rationalizations — implementation-performance-data-structure-choice

Real excuses agents used to skip or soften this gate, mined from
tokenmaxxxer/on-the-record patrol/defect/process records and tm-dicequest
implementation records. Each row: the excuse (verbatim-ish), the reality,
the rule it points back to, and the originating incident.

| Rationalization (excuse) | Reality | Rule | Citation |
|---|---|---|---|
| "No performance cliff here" — asserted without checking loop membership. | The NA verdict requires locating the loop and its bound, the same check the applied path does; the legitimate NA form states the bound explicitly. | rule 1 | tm-dicequest docs/issue-58/reports/implementation.md ('linear scan over ≤6 keyframes' — the bound-stating NA form); on-the-record#2062 (verdicts rendered without loading the rules) |
| "O(n log n) beats O(n²), done." | Asymptotic class alone ignores constants and n's actual range; measure at the real scale before swapping structures. | rule 3 | (pattern, from on-the-record#2103 — board reads optimized only after measuring the actual query/traffic shape, not the asymptotic story) |
| "Add a cache to be safe." | An unmeasured cache is a liability: staleness, memory, and invalidation cost with no demonstrated hit rate; measure first, then add. | rule 5 (REMOVAL) | (pattern, from on-the-record#1117/#1722 — 'safety' polling/heartbeat layers that produced noise until their actual value was measured and they were cut) |
