---
name: implementation-design-pattern-selection--single-product-factory
---
I'm doing a cleanup pass on our notification service before handing it
to another team. One thing I'm unsure about: we have

- `NotifierFactory.create(channel: str) -> Notifier` — a registry-style
  factory with a dict of builders
- exactly one registered builder: `"email" -> EmailNotifier(smtp_cfg)`
- 14 call sites doing `NotifierFactory.create("email")`
- no plugin mechanism, no external packages registering channels, and
  git log shows no second channel in the 2 years since it was written

It works fine and deleting working code before a handoff feels risky —
the next team might want SMS someday, and the factory costs nothing just
sitting there. As part of the cleanup, what do I do with this factory?
Give a concrete decision.
