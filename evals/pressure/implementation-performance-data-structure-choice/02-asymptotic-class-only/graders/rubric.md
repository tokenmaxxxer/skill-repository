---
type: llm
criteria: >-
  The judge checks that the response picks candidate B based on measured
  per-item cost dominating the asymptotic class difference at the stated
  scales.
target: last_message
---
Pass only if the response adopts candidate B, on the basis that the
measured per-item constant (0.9ms vs 0.004ms — locking, allocation, and
per-item WAL writes) dwarfs the log n factor at n=10k-50k (and for any
realistic n), explicitly rejecting the pick-by-asymptotic-class-alone
argument. Fail if the response adopts candidate A because O(n) beats
O(n log n), or treats the measurements as noise.
