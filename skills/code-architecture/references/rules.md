# code-architecture — full rules and citations

Moved verbatim from SKILL.md by issue-100 progressive disclosure.
The SKILL.md body carries the rule index; read this file when a
matched rule's full text, citation, or counter-example is needed.

## [S1] Evidence grade

- **Information hiding / modularity** (Parnas 1972, Parnas 1978): ●●● — controlled experiments demonstrated that modular decomposition by design decisions produces measurably more change-tolerant code than decomposition by control flow.
- **Coupling and cohesion** (Yourdon & Constantine 1979): ●●● — the structured-design metrics have been measured, operationalized, and shown to correlate with defect density and change cost across multiple independent studies.
- **SOLID principles** (Martin, 2000s): ●●○ — industry standard with strong face validity; empirical support is mostly case-study (one large-scale study by Yamashita & Moonen 2012 found that SRP violations, specifically God Classes, correlate with higher defect rates — so the SRP part has quantitative backing; the rest of SOLID is practitioner consensus).
- **Design Patterns** (GoF 1994): ●●○ — cataloged recurring solutions with known tradeoffs; adoption is widespread and the pattern vocabulary aids communication, but pattern conformance vs. defect rate has not been quantitatively established.
- **Domain-Driven Design tactical patterns** (Evans 2003): ●●○ — widely adopted in domain-complex software (insurance, finance, logistics) with published case studies; no controlled experiment measures DDD-conformance vs. maintenance cost.
- **Clean / Hexagonal / Onion Architecture** (Cockburn 2005, Martin 2012): ●○○ — practitioner patterns with strong internal logic; the claimed benefits (testability, framework independence) are demonstrated anecdotally, not in controlled measurement.
- **YAGNI** (Beck 1999): ●●○ — the XP community's cumulative experience with speculative generality; the cost of removing dead abstraction is well-documented, but "how much abstraction to add now for known-future change" remains a judgment call.
- **Conway's Law** (Conway 1968): ●●○ — replicated across multiple large-scale empirical studies (Nagappan et al. 2008, and others at Microsoft Research found that organizational structure predicts module coupling better than technical dependencies do).
- **The archetype taxonomy itself**: procedural design choice, not an empirically validated instrument. The seven categories are constructed to be MECE by construction, not by experimental confirmation. The value is that they route the AI to the right body of rules, not that the classification itself has been measured. [설계]

## The archetype classification — pick one before you write anything

### The seven archetypes

| # | Archetype | Defining feature | Example |
|---|---|---|---|
| 1 | **Script** | Single execution path, no reuse, no callers | Data export, build script, migration one-off |
| 2 | **Library** | Called by external code; public API is the contract | Utility package, SDK, shared component library |
| 3 | **Data-Centric App** | CRUD with validation; business logic = data integrity rules | Admin panel, form-heavy SaaS, REST CRUD API |
| 4 | **Domain-Rich App** | Complex business rules independent of persistence | Insurance underwriting, trading engine, logistics routing |
| 5 | **Event-Driven System** | Asynchronous message passing; eventual consistency | Order processing pipeline, notification system, IoT ingestion |
| 6 | **Data Pipeline** | Extract-transform-load; streaming or batch | ETL job, log processor, ML feature pipeline |
| 7 | **Plugin System** | Extension points; core depends on interfaces, plugins implement | IDE extension, CMS plugin, payment gateway adapter |

### How to classify in 30 seconds

Ask three questions, in order:

1. **Is this called by external code (not just the same app)?** If yes → Library (2). If the external caller is a plugin/extension → Plugin System (7).
2. **Is the business logic non-trivial — rules that exist even without a database?** If yes → Domain-Rich App (4). If no (the app is mostly moving data in and out with validation) → Data-Centric App (3). If the data movement *is* the point (transform, not serve) → Data Pipeline (6).
3. **Does the system communicate across process boundaries with asynchronous messages?** If yes → Event-Driven System (5). If none of the above → Script (1).

**Gate A0:** the classification is written down with the reasoning (which question landed it). No code is written before this.

### Mixed archetypes

Real systems often span archetypes. A data-centric app that exposes a client library (3 + 2). A domain-rich app with an async event bus (4 + 5). The rule: **classify each component separately.** The CRUD endpoints get archetype-3 treatment; the domain model gets archetype-4 treatment; the event handler gets archetype-5 treatment. Do not force one archetype onto the whole system. Do name the boundary between them explicitly.

## [S2] Archetype-specific structural rules

### Archetype 1 — Script

**The one rule:** the code should be readable top-to-bottom in a single pass. Structure follows execution order. Functions exist to name steps, not to hide decisions — if the function is called exactly once and its name is just a restatement of its content, it's noise.

**Minimal structure:**
- Entry point at the top or clearly marked
- Named functions for non-trivial transforms (purely for readability)
- No classes, no inheritance, no dependency injection
- No abstracted configuration — read it at point of use
- Error handling: fail loudly with a message, exit nonzero. No retry, no graceful degradation — the operator needs to know it failed.

**Gate A1:** no abstractions that serve exactly one concrete implementation. No code whose removal would leave the script equally functional. The entry point is findable within 5 seconds.

**Common anti-pattern:** wrapping a 50-line script in a class with `__init__`, `run()`, and `main()` — Python's `if __name__ == "__main__": main()` is the conventional entry point; a class around a linear flow adds indirection with zero benefit.

### Archetype 2 — Library

**The one rule:** design from the call site outward. Write the calling code first — the ideal API shape — then implement to satisfy it. Every public name is a maintenance commitment; keep the surface area minimal. A library's quality is measured by how much you can change the internals without the callers noticing.

**Minimal structure:**
- Public API surface explicitly declared (module-level `__all__`, `exports`, `pub` — the language's mechanism)
- Internal implementation hidden behind the public API; no internal detail leaked through return types or thrown exceptions
- One module = one responsibility; module boundaries aligned with what changes together
- Versioned if distributed independently (SemVer)
- Documented at the call-site level: for each public function, what it accepts, what it returns, what it throws, and one example call

**Gate A2:** every public symbol is justified — removing any of them would genuinely break a legitimate caller. No internal type appears in a public signature. The public surface is smaller than the internal implementation.

**Common anti-pattern:** exposing internal utilities "just in case someone needs them." In a library, every exposed thing is a forever commitment. Also: a `utils` or `helpers` module — name things by what they do, not by where they belong.

### Archetype 3 — Data-Centric App

**The one rule:** the business logic is thin enough that it fits in validation rules and simple transformations. The structure separates concerns by technical role (request handling, business rules, data access), not by domain concept — because the domain concepts are simple enough that a domain model would cost more than it saves.

**Minimal structure (layered):**
- **Controller / Handler layer** — parse input, call service, format output. No business logic. No direct database access.
- **Service / Use-Case layer** — orchestrate operations, enforce business rules, call repositories. This is where validation and authorization live. A service method should read like a checklist: validate input, check permissions, perform operation, return result.
- **Repository / Data-Access layer** — encapsulate data store access. Returns domain-appropriate data structures, not raw query results. The repository interface hides whether the store is SQL, a document store, or an in-memory cache.
- **Model / Entity** — data structures with fields and simple validation. May have computed properties but no complex domain logic (that's archetype 4 territory).

**Gate A3:** every function can be classified as exactly one of the three layers. The service layer contains no SQL strings or ORM calls. The controller layer contains no business rules. Cross-layer calls go in one direction: controller → service → repository. No upward or sideways calls.

**When to upgrade to archetype 4:** the moment a service method contains branching business logic that depends on the state of the entity (not just field validation), or when the same business rule appears in more than one service, it's time for a domain model. Don't fight it — extract the logic into the entity and reclassify.

### Archetype 4 — Domain-Rich App

**The one rule:** the code's structure mirrors the domain's own concepts, not technical layers. A new team member should be able to find the relevant code by knowing the business domain, without knowing the technical stack. The domain layer has zero framework dependencies. This is Evans (2003) operationalized as a structural check.

**Minimal structure:**

- **Domain layer** (innermost, no dependencies on frameworks or infrastructure):
  - *Entities* — objects with identity that runs through time (a Customer, an Order). Mutable state with behavior.
  - *Value Objects* — immutable, identified by their values (Money, Address, DateRange). Behavior-rich; no setters.
  - *Aggregates* — clusters of entities and value objects with a single root that enforces invariants. References between aggregates are by ID only, never by object reference.
  - *Domain Services* — stateless operations that don't naturally belong to any entity or value object.
  - *Domain Events* — facts that happened, named in past tense (OrderPlaced, PaymentReceived).
  - *Repository interfaces* — defined in the domain layer, implemented in infrastructure.

- **Application layer** (depends on domain, not on infrastructure):
  - Use cases / application services that orchestrate domain objects. Thin — delegates to the domain. The application layer's job is transaction management, authorization, and wiring.

- **Infrastructure layer** (depends on domain and application):
  - Repository implementations, external API clients, message bus adapters, persistence mappings.

- **Interface layer** (outermost):
  - HTTP controllers, CLI commands, event handlers — adapt external input to application-layer calls.

**Gate A4:** the domain layer imports nothing from infrastructure or interface layers. No ORM annotations on domain objects. No framework code in the domain. Business rules are callable without a database, a web server, or a DI container. Every aggregate root enforces its invariants on every state change — no "the service checks the invariant before calling the entity" escape hatch.

**No-getter discipline (optional but strong signal):** domain objects expose behavior, not internal state. `order.total()` not `order.getTotal()`. A domain object that is mostly getters and setters is a data structure, not a domain model — reclassify as archetype 3.

### Archetype 5 — Event-Driven System

**The one rule:** every handler must be safe to call zero, one, or more than one time with the same input. Idempotency is not optional — it is the price of admission.

**Minimal structure:**
- **Events** — immutable, named in past tense, contain the ID of the aggregate they describe and a correlation/causation ID for tracing
- **Commands** — named in imperative mood, directed at a specific handler. A command can be rejected; an event is a fact that happened.
- **Handlers** — one handler per message type. Stateless. Idempotent: receiving the same message twice produces the same outcome, not a double charge.
- **State machines / Sagas** — long-running processes modeled as explicit states and transitions. The current state is stored; the next state is determined by current state + incoming event. No implicit state in local variables or in-flight promises.
- **Dead-letter handling** — messages that fail processing go to a dead-letter queue with the original payload, the error, and the retry count. No silent drops.

**Gate A5:** every handler has a documented idempotency strategy (idempotency key, deduplication by event ID, at-least-once with idempotent downstream). Every event has a schema version. The system can survive any single component being restarted mid-operation — no in-memory state that isn't reconstructable from the event log.

**Common anti-pattern:** distributed transactions pretending to be event-driven — a handler that calls three services synchronously and rolls back on failure. That's RPC with extra steps. Event-driven means: emit the event, let other handlers react. The compensation is eventual.

### Archetype 6 — Data Pipeline

**The one rule:** each stage is independently testable with a known input schema and output schema. The pipeline is the composition of stages. If you can't test a stage in isolation with canned input and verify its output, the boundary is wrong.

**Minimal structure:**
- **Source / Extractor** — reads from the origin, emits a stream of records with a known schema. Handles connection errors, pagination, and backpressure.
- **Transform stages** — each does exactly one transformation. A stage that filters AND enriches AND aggregates is three stages composed. Named by what they do, not how.
- **Sink / Loader** — writes to the destination. Idempotent (upsert, not insert-or-die). Handles partial failure: a batch of 1000 where record 573 fails should not lose records 1-572.
- **Error channel** — an explicit path for records that fail processing. Dead-letter with the offending record, the stage that failed, and the error. The pipeline continues processing valid records.

**Gate A6:** every stage can be tested independently. The schema at each stage boundary is explicit (typed, not "a dict with some keys"). Error records are preserved, not dropped. The pipeline can be replayed from any stage.

### Archetype 7 — Plugin System

**The one rule:** the core knows only the interface. Plugins know the core. Never the reverse. This is the Dependency Inversion Principle applied at the module level — the core defines the contract (interface/abstract class/protocol), and plugins satisfy it.

**Minimal structure:**
- **Core** — defines the extension point interface, the plugin discovery/registration mechanism, and the orchestration logic that calls plugins. Has zero imports from plugin packages.
- **Extension Point Interface** — the contract. Minimal surface area: what the plugin must provide, what the core will pass to it, what the plugin may return, and what errors the plugin may raise.
- **Plugin** — implements the interface. Self-registers (declarative entry in config or package metadata, or programmatic registration at startup). A plugin that fails to load must not crash the core — log, skip, continue.
- **Plugin lifecycle** — init (validate configuration, acquire resources), execute (the actual work), dispose (release resources). The core calls these in order.

**Gate A7:** the core package has no import of any plugin package. A new plugin can be added by creating a package in the plugins directory and registering it — no core code changes. The core handles a plugin that throws on init without crashing.

## Verification — the three fundamentals

After applying the archetype-specific rules, verify against these three. They apply across all archetypes but manifest differently in each.

### 1. Coupling — what must change together?

**The test:** pick a likely change (a new database, a new payment provider, a new output format). Count how many files must change. For a database switch in a data-centric app, the answer should be exactly the repository implementations — not the services, not the controllers. If the answer is "most of the codebase," the modules are coupled along the wrong axis.

**Parnas's test, operationalized:** "For every module, name the design decision it hides. If you can't name it, the module doesn't earn its existence. If two modules hide the same decision, they should be one."

**Gate V1:** for each module, the design decision it hides is written down in one sentence. No two modules hide the same decision. No module hides zero decisions.

### 2. Cohesion — does everything in this module belong together?

**The test:** can you describe what the module does without using the word "and"? "Handles user authentication" — cohesive. "Handles user authentication and sends email notifications and formats dates" — not cohesive. The "and" test is crude but effective: every "and" in the module description is a candidate split point.

**Gate V2:** every module description passes the "no and" test. Functions that appear together in the module are called together by their clients — if `foo()` and `bar()` always appear in the same calling file, co-locating them is justified; if they never appear together, they belong in different modules.

### 3. Abstraction level — is every function at a consistent level?

**The test:** read the function names and calls within a module top-to-bottom. If you see `processOrder()` calling `validateEmail()`, `checkInventory()`, and `UPDATE orders SET status = …` (inline SQL), the SQL string is at the wrong abstraction level — it's an implementation detail of persistence leaking into business logic.

**Gate V3:** within a single function, every call is at the same level of abstraction. No raw infrastructure operations (SQL strings, file handles, HTTP client calls) live alongside domain logic. The infrastructure is behind a named function whose name describes what it does, not how.

## Standing disciplines

1. **Structure follows change, not convention.** Don't add a layer because "this is how we always do it." Add it because you can name a thing that will change independently. A layer that never paid for itself in a future change was a mistake.

2. **Abstraction earns its keep in maintenance, not in writing.** The test is not "does this abstraction make the code shorter now?" — abstractions usually make code longer. The test is "when X changes next month, will this abstraction repay its cost?"

3. **Conway's Law is a design constraint.** If one person will maintain all of this code, elaborate module boundaries are ceremony — they protect nothing. If two teams will own different parts, the module boundary must match the team boundary exactly, or the code will drift to match it anyway.

4. **Start one archetype simpler than you think.** If you're torn between archetype 3 and 4, start at 3 — upgrading is cheaper than downgrading. The archetype-3 service that grows a domain model is a straightforward extraction. The archetype-4 domain model with thin business logic is dead weight that must be dismantled.

5. **The rule of three for patterns.** Apply a structural pattern (Repository, Strategy, Factory, Observer) only when: (a) you have three concrete cases today, or (b) you have one case today and a confirmed need for a second within the visible planning horizon. Never for "we might need this someday." Beck's YAGNI, not a suggestion — the industry has forty years of "someday" abstractions that never paid their rent.

## [S3] References

Read `references/methodology-lineage.md` for the full evidence chain: primary sources, empirical studies, and the precise evidence grade for each methodological influence. Light classification tasks never need it.

