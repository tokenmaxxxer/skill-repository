---
type: llm
criteria: >-
  The judge checks that the response recommends deleting the near-zero-
  hit-rate cache rather than tuning keys, TTL, or instance size.
target: last_message
---
Pass only if the response's primary recommendation is to remove the
cache layer entirely — a 0.4% hit rate on effectively-unique keys means
every request pays ~3ms of cache overhead to occasionally save 8ms, a
net regression — rather than tuning it. (Noting that a redesigned cache
could be reintroduced later only if measurements justify it is
acceptable.) Fail if the response's main proposal is tuning: key
normalization, longer TTL, bigger instance, or other cache improvements
that keep the near-zero-hit cache in place.
