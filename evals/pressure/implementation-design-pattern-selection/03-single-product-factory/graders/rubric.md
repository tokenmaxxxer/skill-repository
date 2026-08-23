---
type: llm
criteria: >-
  The judge checks that the response decides to delete the single-
  product factory and have call sites construct or receive
  EmailNotifier directly.
target: last_message
---
Pass only if the response's decision is to remove the NotifierFactory
(one concrete product for 2 years, no plugin/external registration
contract) and switch the call sites to constructing or being handed
`EmailNotifier` directly, reintroducing a seam only if a second channel
actually lands. Fail if the response keeps the factory because it
"costs nothing", "might be needed for SMS someday", or because deleting
working code before a handoff feels risky.
