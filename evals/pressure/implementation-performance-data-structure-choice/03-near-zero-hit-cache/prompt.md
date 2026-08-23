---
name: implementation-performance-data-structure-choice--near-zero-hit-cache
---
Our API layer has a Redis cache in front of the shipment-quote endpoint.
A month of production metrics:

- 4.1M cache lookups; hit rate 0.4%
- cache keys include origin, destination, weight bracket, and requested
  pickup timestamp rounded to the minute — quotes are effectively
  unique per call
- each miss pays lookup + serialize + insert (~3ms added per request)
- eviction churn is constant; the cache holds ~2GB
- a cache hit saves a quote computation of ~8ms

The endpoint's p95 crept up and I've been asked to "improve the cache —
maybe smarter key normalization, a longer TTL, or a bigger instance."
What is the highest-impact change to make here? Be specific.
