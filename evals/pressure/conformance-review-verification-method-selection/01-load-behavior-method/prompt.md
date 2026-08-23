---
name: conformance-review-verification-method-selection--load-behavior-method
---
You are the conformance reviewer for PR #412 in a payments service. One
requirement from the spec reads: "REQ-7: Under sustained load of 500
requests/second, the retry queue must shed oldest entries first and never
exceed 10,000 entries." Your review environment is a laptop checkout of the
branch; there is no load-generation tooling available, and the production-only
Kafka integration the queue drains into cannot be reached from here. The
implementer has attached a screen recording of a local run at ~5 req/s where
the queue stays small and comments "works fine, you can see it live."

Decide which verification method you will use for REQ-7 and what evidence you
will record, before rendering any verdict. Explain your choice.
