---
type: llm
criteria: >-
  Whether the response selects Analysis (tracing the shedding/bounding code path or reasoning from a model) for REQ-7 and explicitly rejects treating the 5 req/s happy-path recording as establishing the 500 req/s requirement.
target: last_message
---
Pass only if the response chooses Analysis as the verification method —
tracing the code path / reasoning about the bounding and eviction logic —
because the named condition (sustained 500 req/s with the production Kafka
integration) cannot be realistically reproduced in the review session, and
explicitly declines to count the implementer's ~5 req/s recording as
evidence for the load requirement. Fail if the response accepts the
recording (Demonstration under artificial conditions) as sufficient,
proposes to mark the requirement satisfied based on the local run, or
picks Inspection/Demonstration/Test without addressing the unreproducible
load condition.
