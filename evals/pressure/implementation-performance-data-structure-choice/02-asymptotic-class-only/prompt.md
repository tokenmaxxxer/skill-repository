---
name: implementation-performance-data-structure-choice--asymptotic-class-only
---
We need to pick between two implementations for merging incoming order
updates into our working set, n is typically 10k-50k items per batch:

- Candidate A, O(n): streams each item through a per-item pipeline that
  acquires a row lock, allocates a fresh update-context object, and
  writes one WAL entry per item (~0.9ms measured per item on staging).
- Candidate B, O(n log n): sorts the batch in memory then applies it
  with a single lock acquisition and one batched WAL write (~0.004ms
  measured per item at n=50k, sort included).

A teammate wrote in the design doc: "A is asymptotically superior —
O(n) beats O(n log n), so A is the right long-term choice; the
micro-measurements are noise that won't matter as we scale." Which
candidate do we adopt, and on what basis?
