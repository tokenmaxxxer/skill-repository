---
name: implementation-performance-data-structure-choice
description: >-
  Use when choosing a data structure, algorithm, or communication scheme that could introduce a
  performance cliff — membership testing in a loop, comparing algorithms by asymptotic class,
  per-message connections, or a cache/index whose maintenance cost may now outweigh its benefit.
  Trigger on requests like "list vs set for lookup in this loop", "이 캐시 유지할 가치 있어?", "자료구조 뭐
  쓸까", "batch these small frequent messages?". Do NOT use for coupling/cohesion restructuring
  decisions (use implementation-complexity-coupling-management).
metadata:
  axis: performance-data-structure-choice
  rule_count_floor: 6
  tier: sparse
---

# Performance-degradation prevention: data structure, algorithm, and
# communication-scheme choice

Decision rules for picking the structure/algorithm/communication scheme
that avoids introducing an avoidable performance cliff, plus removal
rules for structures that are now pure overhead.

## Trigger

Apply this skill when writing or reviewing code that picks a data
structure, algorithm, or communication scheme: membership testing or
dedup inside a loop, a lookup structure choice under memory constraints,
comparing two algorithms by asymptotic class alone, a communication
scheme moving many small messages, or a cache layer or precomputed
index/denormalized field under review for whether its maintenance cost
still earns its keep.

## Procedure

1. If membership testing or dedup runs inside a loop, use a hash-based
   set/map instead of a linearly scanned list (rule 1).
2. If the target is memory-constrained and lookups are infrequent,
   accept a sorted-array + binary search over a hash map (rule 2).
3. If comparing two algorithms by asymptotic class, measure actual
   per-element cost before picking by class alone (rule 3).
4. If a communication scheme moves many small, frequent messages,
   prefer batching or a persistent connection over one connection per
   message (rule 4).
5. If a cache layer's measured hit rate is near zero, delete the cache
   rather than tuning it (rule 5).
6. If a precomputed index or denormalized field is read on less than
   the fraction of reads that justifies its write-side cost, drop it
   and compute on read instead (rule 6).

## Output shape

A structure/algorithm/scheme decision: the condition that triggered it,
the applicable rule number, and the concrete choice (structure,
algorithm, batching, removal) selected.

## Rules

1. When membership testing or dedup runs inside a loop over a
   collection, use a hash-based set/map (O(1) average lookup) instead of
   a list scanned with `in`/linear search (O(n) per check, O(n^2) total)
   — this is the standard time-vs-space tradeoff: hashing spends memory
   to avoid the quadratic blowup.
   source: https://codecake.ai/blog/data-structures-and-algorithm-complexity/

2. When the target runs in a memory-constrained environment (embedded,
   high-fanout server processes) and lookups are infrequent, accept a
   sorted-array + binary search (O(log n) lookup, O(1) extra space) over
   a hash map (O(1) lookup, higher constant memory overhead) — space
   constraint outweighs the asymptotic lookup win when lookups are rare.
   source: time/space tradeoff guidance, https://thegeekplanets.medium.com/the-ultimate-guide-to-complexity-analysis-in-data-structures-and-algorithms-c4f9be147a54

3. When comparing two candidate algorithms by asymptotic class alone
   (e.g. O(n log n) vs O(n)), do not pick by class alone if the O(n)
   candidate carries a large per-element constant (heavy allocation,
   locking, or I/O per iteration) — measure actual per-element cost,
   because Big-O hides constants and an O(n log n) algorithm with light
   per-op cost can outperform an O(n) algorithm with heavy per-op cost
   at realistic input sizes.
   source: https://dev.to/easewithtuts/big-o-notation-a-comprehensive-guide-253j

4. When a communication scheme must move many small, frequent messages
   between components, prefer batching or a persistent connection over
   one request/connection per message — per-message connection setup
   (TCP handshake, TLS negotiation) is a fixed per-call constant that
   linear-scales into a dominant cost at high call volume even though
   each individual call is O(1).
   source: constant-factor cost model per https://flexiple.com/algorithms/big-o-notation-cheat-sheet

5. REMOVAL — when a cache layer's hit rate is measured and found to be
   near zero (cold data, unique-key-per-call access pattern), delete the
   cache rather than tuning it; a cache that never hits still pays
   insertion/eviction cost on every call and is a pure performance
   regression relative to no cache. Measure hit rate before assuming a
   cache is default-beneficial — the additive instinct is to keep
   tuning it, the correct move is often to remove it.
   source: Adams, Converse, Hales & Klotz, Nature 592 (2021) 258-261,
   https://www.nature.com/articles/s41586-021-03380-y

6. REMOVAL — when a precomputed index or denormalized field is
   maintained on every write but read on less than a fraction of reads
   that would justify the write-side cost, drop the index/denormalized
   field and compute the value on read instead; sustained write-side
   overhead for a rarely-read value is a net-negative trade, not a
   neutral optimization to leave in place.
   source: time/space tradeoff framing per https://codecake.ai/blog/data-structures-and-algorithm-complexity/

## Counter-example tests

- Rule 1 counter-example: a membership check performed exactly once
  against a collection of 5 known-small constant items (e.g. a fixed
  enum of 4 states) does not justify a hash-set conversion — the O(n)
  linear scan is already O(1) in practice at that fixed small n, and the
  hash-set adds construction overhead with no measurable win.
- Rule 5 counter-example: a cache with low aggregate hit rate but whose
  hits fall on the small number of extremely expensive-to-recompute
  keys (e.g. a multi-second report query hit 2% of the time) is NOT a
  removal candidate — total cost saved by the rare hits can still exceed
  total cache-maintenance cost; rule 5's condition is "near-zero hit
  rate," not "low hit rate," and requires checking cost-per-hit, not
  just hit-rate percentage, before removal.

## Rationalizations

Documented excuses agents used to skip this gate, each rebutted and tied
back to a rule and its originating incident: see
[references/rationalizations.md](references/rationalizations.md).
