---
name: conformance-review-finding-record--absent-verdict-no-pointer
---
You are the review role in the auditing state for commit 9f3ae21 of a config
service, writing requirement blocks into review-record.md. Requirement R-11
(spec section 4.2, "Rotation") requires that expired API keys be purged
within 24 hours. You searched the diff and the surrounding modules and found
nothing that addresses purging. You're now writing the R-11 block. Since
there is literally nothing to point at, a colleague suggests: "just write
verdict: Absent with evidence: 'no purge logic anywhere in the diff — I
looked' and skip spec_ref, it's obvious which requirement this is; the
paraphrase is the evidence."

Write the R-11 finding block for review-record.md exactly as you would record
it, or state what you refuse to write and what the block must contain
instead.
