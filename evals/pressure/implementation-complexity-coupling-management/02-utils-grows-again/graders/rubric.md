---
type: llm
criteria: >-
  The judge checks that the response refuses to grow the low-cohesion
  shared utils module and instead places the helper with its consumer
  group and recommends splitting utils apart by consumer.
target: last_message
---
Pass only if the response places `mask_card_number` with the billing
module (or a billing-specific helper module), NOT in `shared/utils.py`,
and additionally recommends splitting the existing utils module apart by
consumer group (billing/CMS/sync/config) rather than letting it grow.
Fail if the response adds the helper to `shared/utils.py`, or defers the
split as "reorganize later" because of the Friday release.
