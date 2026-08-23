---
name: code-architecture
description: >-
  Use whenever you are about to write non-trivial code spanning multiple modules or files
  and need to decide on structure — proactively when building a new module, feature, or
  service whose structural decisions will outlive the initial implementation. A decision
  framework for selecting the appropriate code structure and architecture pattern,
  synthesizing five decades of software-engineering methodology (Parnas 1972 through DDD
  2003) into a situational classification system. Trigger on "이 코드 어떻게 구조화할까", "어떤 패턴 써야 돼",
  "아키텍처 설계해줘", "how should I structure this code", "what pattern should I use here". Do NOT
  use for a single-file script, a one-line fix, a config change, or purely algorithmic work
  with no structural choice; for the CLI-backed, database-queried variant of the same
  selection use implementation-blueprint. It does not audit existing code
  (implementation-audit) or select external technology (tech-feasibility).
---
# Code Architecture — situational structure selection for AI-generated code

## First: does this even need the procedure?

Two checks before engaging, because the most expensive mistake in code structure is ceremony applied where it doesn't earn its keep:

- **Single file, single concern, no callers beyond the immediate task?** A script, a one-off data transform, a config generator, a single UI component with no child hierarchy — just write it correctly. The procedure is overhead. At most, keep a one-sentence note: "this is a script; flat is fine."
- **Trivial structural decision?** A one-line fix, a config value, a single validation rule, a formatting change — no procedure needed.

Everything below applies when the code will span multiple modules or files, will be extended or maintained, or has callers with expectations about the interface.

## What this skill is actually for

The failure mode this skill prevents is the AI's most common structural error: selecting a pattern by familiarity rather than fit, producing either over-engineered code (layers that don't earn their keep — the Repository-Service-Controller stack for a script with two database calls) or under-structured code (a 3000-line file because "it started simple"). The right structure is a function of what the code *is* and what *changes about it* — a very small number of archetypes captures the structural variation that matters, and picking the wrong one costs more than picking none.

Parnas (1972) stated the principle that drives everything below: **"One begins with a list of difficult design decisions or design decisions which are likely to change. Each module is then designed to hide such a decision from the others."** Structure exists to contain change. If nothing changes, no structure is needed. If everything changes in lockstep, no separation is needed. Structure earns its keep only when things change at different rates and for different reasons.

## Rule index

Full rule text, citations, and counter-examples:
`references/rules.md` in this skill's directory — read it when a
matched rule's detail is needed.

- 2.1 — **Is this called by external code (not just the same app)?** If yes → Library (2). If the external caller is a plugin/extension → Plugin System (7)
- 2.2 — **Is the business logic non-trivial — rules that exist even without a database?** If yes → Domain-Rich App (4). If no (the app is mostly moving data in and out with vali…
- 2.3 — **Does the system communicate across process boundaries with asynchronous messages?** If yes → Event-Driven System (5). If none of the above → Script (1)
- 1 — Coupling — what must change together?
- 2 — Cohesion — does everything in this module belong together?
- 3 — Abstraction level — is every function at a consistent level?
- 5.1 — **Structure follows change, not convention.** Don't add a layer because "this is how we always do it." Add it because you can name a thing that will change independently…
- 5.2 — **Abstraction earns its keep in maintenance, not in writing.** The test is not "does this abstraction make the code shorter now?" — abstractions usually make code longer…
- 5.3 — **Conway's Law is a design constraint.** If one person will maintain all of this code, elaborate module boundaries are ceremony — they protect nothing. If two teams will…
- 5.4 — **Start one archetype simpler than you think.** If you're torn between archetype 3 and 4, start at 3 — upgrading is cheaper than downgrading. The archetype-3 service tha…
- 5.5 — **The rule of three for patterns.** Apply a structural pattern (Repository, Strategy, Factory, Observer) only when: (a) you have three concrete cases today, or (b) you h…
- S1 — Evidence grade → references/rules.md
- S2 — Archetype-specific structural rules → references/rules.md
- S3 — References → references/rules.md
