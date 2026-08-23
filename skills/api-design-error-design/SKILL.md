---
name: api-design-error-design
description: Use when designing or reviewing an HTTP API's error response shape — envelope, machine-readable codes, field-level validation errors, retryability signaling, or error-message text — before or during implementation.
metadata:
  axis: error-design
  rule_count_floor: 10
---

# Error response design

Research trail: RFC 9457 (Problem Details for HTTP APIs, primary source, obsoletes RFC 7807), Stripe API error/idempotency docs, Microsoft REST API Guidelines, Zalando RESTful API Guidelines, Google AIP-193 (Errors), and HCI literature on programming error-message readability. The academic layer is thin — usability/HCI research on error messages exists but is sparse and mostly qualitative, as noted below.

## Trigger

Apply this skill when designing or reviewing a JSON HTTP API's error
response shape: the base envelope, machine-readable error identifiers,
multi-field validation errors, error-code namespacing, human-readable
message text, retryability signaling, or an automated design-review
check over error responses.

## Procedure

1. Adopt the RFC 9457 `application/problem+json` envelope (`type`,
   `title`, `status`, `detail`, `instance`) as the base shape (rule 1).
2. Add a stable machine-readable identifier for client branching
   (`type` URI, or `code`/`reason` pair) rather than relying on HTTP
   status alone (rule 2).
3. For multi-field validation failures, return a structured per-field
   errors array rather than one flat message (rule 3).
4. Namespace error codes (domain+reason or nested hierarchy) rather
   than a flat global enum (rule 4).
5. Keep `detail`/`message` as human prose only; put anything a client
   parses into a typed extension field (rule 5).
6. Keep `title` a fixed string per error type, with per-instance data
   only in `detail` (rule 6).
7. Before returning any response to an external client, strip stack
   traces, internal paths, and SQL fragments from the payload
   (rule 7).
8. For retryable errors, expose retryability as a structured field
   rather than prose, and require/support idempotency keys on requests
   safe to retry, documenting which status/error-type combinations are
   retryable (rules 8-9).
9. Use a typed, extensible details mechanism (`innererror`,
   `google.rpc.Status` details) when more error context than
   code+message is needed (rule 10).
10. Write message text for the actual audience (end user vs.
    integrating developer), concrete and actionable (rule 11).
11. Keep `status` (or equivalent) consistent with the actual HTTP
    response status code (rule 12).
12. If encoding these rules into an automated check, tag each check as
    blocking or advisory rather than one pass/fail signal (rule 13).

## Output shape

An error-response contract (or a review verdict on one) stating: the
envelope shape used, the machine-readable identifier scheme, whether
multi-field validation errors are structured, the code-namespacing
scheme, confirmation that `detail`/`title` follow the stability rules,
confirmation implementation details are stripped, the retryability
signal and idempotency-key policy, and — if a CI check was authored —
each rule's blocking/advisory tag.

## Rules

1. When designing the base error envelope for a JSON HTTP API, use the RFC 9457 `application/problem+json` shape (`type`, `title`, `status`, `detail`, `instance`) rather than inventing a bespoke `{success: false, ...}` wrapper — all fields are optional but each has defined semantics, so adopting the standard gets you interoperable tooling and documented client behavior for free. source: https://www.rfc-editor.org/rfc/rfc9457.html

2. When a client needs to branch program logic on error type, include a stable machine-readable identifier (RFC 9457 `type` URI, or a `code`/`reason` string as in Stripe's `error.type`/`error.code` or Google AIP-193's `(domain, reason)` pair) rather than requiring clients to switch on HTTP status codes or parse the human-readable message — HTTP status alone is too coarse-grained (e.g., 400 covers many distinct causes) and AIP-193 explicitly makes `ErrorInfo` the "canonical machine-readable identity for an API error" for this reason. source: https://google.aip.dev/193

3. When a single request fails validation on multiple fields, return a structured list of per-field errors (RFC 9457's `errors` extension array with `detail`+`pointer`, or the equivalent `invalid_params` array with `name`+`reason`) rather than a single flat error message, so clients can render all field-level failures in one round trip instead of fixing and resubmitting one field at a time. source: https://www.rfc-editor.org/rfc/rfc9457.html

4. When defining error codes across services, namespace them (Google AIP-193's `domain` + `reason`, or Microsoft's nested `innererror` hierarchy) rather than a single flat global enum — this lets new, more specific codes be introduced anywhere in the hierarchy over time "without breaking backwards compatibility, so long as old error codes still appear." source: https://github.com/microsoft/api-guidelines/blob/vNext/graph/articles/errorResponses.md

5. When writing the human-readable `detail`/`message` field, keep it a developer-facing explanation of the specific occurrence and not a source of machine-parsed information — RFC 9457 states "consumers should not parse the detail member for information; extensions are more suitable and less error-prone ways to obtain such information" — so treat `detail` as prose for humans, and put anything a client needs to branch on into a typed extension field instead. source: https://www.rfc-editor.org/rfc/rfc9457.html

6. When populating `title`, keep it a fixed string per error type that "should not change from occurrence to occurrence... except for localization," and put anything instance-specific in `detail` — mixing per-instance data into `title` breaks client-side error grouping/deduplication that assumes `title` is stable. source: https://www.rfc-editor.org/rfc/rfc9457.html

7. **REMOVAL**: When generating any error response destined for an external client, strip stack traces, internal file paths, SQL fragments, and other implementation details from the payload — RFC 9457 explicitly warns generators to "avoid making implementation details such as a stack dump available through the HTTP interface, since this can expose sensitive details of the server implementation, its data, and so on," and AIP-193 similarly requires messages to "not assume that the user will know anything about its underlying implementation." source: https://www.rfc-editor.org/rfc/rfc9457.html

8. **REMOVAL**: When an error can be retried by the client, do not bury retryability inside prose in the message field — instead drop free-text retry guidance and expose it as a structured, service-defined signal (e.g., Stripe distinguishes `rate_limit_error`/`api_error` as retryable from `invalid_request_error`/most 400s as non-retryable, and recommends idempotency keys plus exponential backoff for the retryable class) so client SDKs can automate retry decisions instead of pattern-matching on human text. source: https://docs.stripe.com/error-handling?lang=node

9. When a request is safe to retry (network failure, timeout, 5xx, or 429), require or support an idempotency key on the request and document which status/error-type combinations are safe to retry versus which must not be retried (Stripe: "400 (user) errors and 429... are not retried, nor are 500 errors which result from POST requests" without idempotency support) — this prevents duplicate side effects from naive client retry loops. source: https://docs.stripe.com/api/idempotent_requests

10. When a service needs to expose more error context than a flat code+message (e.g., which fields are wrong, quota details, or a help link), use a typed, extensible details mechanism rather than free-form nested objects — Microsoft's `innererror` for progressively more specific codes, or google.rpc.Status's repeated `details` (`google.protobuf.Any`) with a well-known `BadRequest` type for validation — so that new detail types can be added without breaking existing clients that don't recognize them. source: https://google.aip.dev/193

11. When designing error message text, write for the actual audience of the message (end user vs. integrating developer) and keep it concrete and actionable rather than terse or jargon-heavy — AIP-193 requires messages to "help a reasonably technical user understand and resolve the issue" and be "brief but actionable," and HCI research on programming error messages independently finds that cryptic, jargon-laden messages measurably slow debugging, though the research base here is thin (one CHI-era study plus a handful of later readability studies, not a mature literature). source: https://google.aip.dev/193

12. When an error object could carry both a stable status/code and a description, always keep `status` (or the HTTP status equivalent) consistent with the actual response status code the client received — RFC 9457 requires that "generators must align this with the actual response code" specifically to avoid confusing HTTP-aware intermediaries (proxies, caches, gateways) that read the response line but not the body. source: https://www.rfc-editor.org/rfc/rfc9457.html

13. When encoding this playbook's rules into an automated design-review check (a CI linter over a spec or an error-response contract test), do not give every rule the same enforcement weight — tag each check as blocking (fails the build: e.g. rule 1's envelope shape, rule 12's status/code mismatch) or advisory (flags for human judgment: e.g. rule 11's message-quality guidance, which cannot be verified mechanically) — collapsing both into one pass/fail signal either blocks merges on subjective calls or lets objectively wrong shapes through with the rest. source: https://meta.stoplight.io/docs/spectral/e5b9616d6d50c-severity-and-disabling-rules
