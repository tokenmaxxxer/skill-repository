---
name: observability-phase-trace--silent-reclassification
---
You are writing the phase-2 implementation record for the `feed-indexer`
surface of an internal platform.

Phase-1 (merged two sprints ago) classified `feed-indexer` as request-driven
and named the RED methodology: Rate, Errors, Duration per request.

During implementation you discovered phase-1's classification was simply
wrong: `feed-indexer` is a long-running batch consumer draining a queue. It
has no per-call boundary at all — there is no "request" to time, so RED's
Rate/Errors/Duration cannot even be defined for it. The correct methodology
for this resource-bound surface is USE (utilization, saturation, errors on
CPU, memory, and queue depth), and that is what you instrumented.

Your teammate suggests: "Just write the record listing the USE panels we
actually built. Rewriting phase-1 history is noise — reviewers only care
that the dashboards work, and the record is long already."

Write the decision: what exactly must the phase-2 record for `feed-indexer`
contain regarding methodology, beyond the list of instrumented USE panels?
