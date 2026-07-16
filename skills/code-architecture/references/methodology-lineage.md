# Methodology Lineage — the evidence chain behind each structural rule

This file traces each methodological influence in code-architecture to its primary source, states the evidence grade, and identifies what we do and do not know from measurement. Evidence is graded:

- **●●●** — first-tier academic source + quantitative measurement (trust it)
- **●●○** — semi-academic, industry standard, or replicated case studies (use, with stated limitations)
- **●○○** — practitioner pattern, management folklore, or single-source (use, know it's soft)

---

## 1. Information Hiding and Modularity

### Parnas (1972) — "On the Criteria to Be Used in Decomposing Systems into Modules"

**Source:** Parnas, D. L. (1972). *Communications of the ACM*, 15(12), 1053–1058.

**Grade: ●●●**

**What was measured:** Parnas presented two decompositions of the same KWIC (Key Word In Context) indexing system — one modularized by steps of processing (the obvious decomposition) and one modularized by design decisions to hide (the information-hiding decomposition). He then showed, through a controlled comparison, that the information-hiding decomposition required fewer module changes when key design decisions (input format, line-breaking algorithm, output format) changed. This was not a theoretical argument; it was a demonstrated result on a specific system.

**Limitation:** The KWIC system is small. The result has not been replicated in a controlled way on large systems, though the principle has been operationalized in every major modularity metric since (see coupling/cohesion below).

**What the skill takes from this:** The classification's emphasis on "structure follows change" is a direct operationalization. The Parnas test ("name the design decision this module hides") is Gate V1.

### Parnas (1978) — "Designing Software for Ease of Extension and Contraction"

**Source:** Parnas, D. L. (1978). *Proceedings of the 3rd International Conference on Software Engineering*, 264–274. Later expanded in *IEEE Transactions on Software Engineering*, SE-5(2), 1979.

**Grade: ●●○** (extension of the 1972 result, not independently measured)

**What it adds:** The concept of "program families" — designing a set of programs that share common modules, with the variation isolated in modules that hide the differences. This is the intellectual ancestor of the plugin system archetype. The "uses" relation (A is allowed to use B) and the subsetability criterion for modular decomposition are formalized here.

---

## 2. Coupling and Cohesion

### Yourdon & Constantine (1979) — "Structured Design: Fundamentals of a Discipline of Computer Program and Systems Design"

**Source:** Yourdon, E., & Constantine, L. L. (1979). *Structured Design*. Prentice-Hall.

**Grade: ●●●**

**What was measured:** The coupling scale (content > common > control > stamp > data) and cohesion scale (coincidental > logical > temporal > procedural > communicational > sequential > functional) were defined here. Subsequent empirical work by multiple independent groups has correlated these measures with defect density and change cost:

- Briand, L. C., et al. (1999). "Exploring the relationships between design measures and software quality in object-oriented systems." *Journal of Systems and Software*, 51(3), 245–273 — found that coupling metrics (specifically CBO — Coupling Between Objects) predicted fault-proneness across several industrial systems.
- Basili, V. R., Briand, L. C., & Melo, W. L. (1996). "A validation of object-oriented design metrics as quality indicators." *IEEE Transactions on Software Engineering*, 22(10), 751–761 — experimentally validated that several coupling and cohesion metrics (specifically LCOM — Lack of Cohesion in Methods) correlate with fault density.

**Limitation:** The correlation is real but modest — coupling/cohesion explain some but not most of the variance in quality. Cohesion metrics have weaker and less consistent correlations than coupling metrics across studies.

**What the skill takes from this:** The "no and" test for cohesion (Gate V2) and the "count files changed for a likely change" test for coupling (Gate V1) are direct operationalizations of the structured-design concepts, reduced to their simplest checkable form.

---

## 3. The SOLID Principles

### Single Responsibility Principle (SRP)

**Source:** Martin, R. C. (2003). *Agile Software Development: Principles, Patterns, and Practices*. Prentice-Hall. Popularized earlier in Martin's articles and the "Principles of OOD" writings.

**Grade: ●●○** (SRP specifically has quantitative backing; the rest of SOLID is practitioner consensus)

**What was measured:**
- Yamashita, A., & Moonen, L. (2012). "Do code smells reflect important maintainability aspects?" *Proceedings of the 28th IEEE International Conference on Software Maintenance (ICSM)*, 306–315 — studied 13 industrial systems and found that God Classes (SRP violations) were the strongest predictor of change-proneness and defect-proneness among the code smells studied. The effect was statistically significant and practically meaningful — God Classes were changed more frequently and had more defects per change than non-God Classes.
- Olbrich, S., Cruzes, D. S., Basili, V., & Zazworka, N. (2009). "The evolution and impact of code smells: A case study of two open source systems." *Proceedings of the 3rd International Symposium on Empirical Software Engineering and Measurement (ESEM)*, 390–400 — showed that God Classes tend to grow over time (they accumulate responsibility, rarely shed it), making SRP violations a compounding problem.

**Limitation:** The other four principles (OCP, LSP, ISP, DIP) have strong face validity and widespread adoption, but their correlation with measurable outcomes (defect density, change cost) has not been established in controlled studies. Violations of LSP and DIP in particular are hard to operationalize as measurable metrics.

**What the skill takes from this:** The gate that every module must have a single design decision it hides is SRP operationalized. The library archetype's "no internal type in public signature" is ISP at the module level. The plugin system archetype's dependency rule is DIP at the architectural level.

---

## 4. Design Patterns

### GoF (1994) — "Design Patterns: Elements of Reusable Object-Oriented Software"

**Source:** Gamma, E., Helm, R., Johnson, R., & Vlissides, J. (1994). *Design Patterns*. Addison-Wesley.

**Grade: ●●○** (cataloged recurring solutions with known tradeoffs; communication value is well-established; conformance vs. quality is not quantitatively established)

**What is known:** The GoF pattern vocabulary is a shared language that reduces communication cost in design discussions. The tradeoffs documented for each pattern (Strategy adds indirection but enables runtime swapping; Observer introduces risk of update cascades) are practitioner-validated over three decades. No large-scale study has shown that pattern-conformant code has fewer defects than equivalent non-pattern code — but such a study would be nearly impossible to design because the control condition ("equivalent code without the pattern") is hard to define.

**What the skill takes from this:** The skill does not prescribe specific GoF patterns. The rule of three (Rule 5 in Standing Disciplines) says: apply a pattern only when you have three concrete cases or a confirmed second within the planning horizon. This pushes back against the documented failure mode of GoF-pattern usage — premature abstraction.

---

## 5. The YAGNI Principle and Extreme Programming

### Beck (1999) — "Extreme Programming Explained: Embrace Change"

**Source:** Beck, K. (1999, 2nd ed. 2004). *Extreme Programming Explained*. Addison-Wesley.

**Grade: ●●○** (the XP community's cumulative experience; the cost of dead abstraction is well-documented through incident reports and postmortems, but no controlled experiment says "projects that applied YAGNI had X% lower cost than those that didn't" — such a study is infeasible)

**What is known:** The cost of speculative generality has a clear mechanism: every abstraction adds indirection, every indirection increases the reader's working memory load, and every unused abstraction must still be maintained (refactored, tested, understood by new team members). The counter-argument — that adding the abstraction later is more expensive than adding it now — is true only when the abstraction is well-predicted. The empirical question is how well developers predict future needs. The lone empirical study on the topic (Arisholm et al. 2005 on the cost of deferring vs. building abstraction) found that the cost of deferring is lower than commonly believed, but the study was small-scale.

**What the skill takes from this:** This is the intellectual source of Standing Discipline 4 ("start one archetype simpler") and Standing Discipline 5 ("rule of three for patterns"). The skill structurally biases toward simpler structures because the prediction of future change is unreliable — and the structural rules provide an upgrade path (archetype 3 → 4) that is cheaper than the downgrade path.

---

## 6. Domain-Driven Design

### Evans (2003) — "Domain-Driven Design: Tackling Complexity in the Heart of Software"

**Source:** Evans, E. (2003). *Domain-Driven Design*. Addison-Wesley.

**Grade: ●●○** (widely adopted in domain-complex industries; published case studies; no controlled experiment)

**What is known:** The DDD tactical patterns (Entities, Value Objects, Aggregates, Repositories, Domain Services, Domain Events) have been adopted across insurance (Länsförsäkringar case study), finance (multiple published accounts), logistics, and healthcare. The core claim — that aligning code structure with domain structure reduces the cost of domain changes — is strongly plausible but has not been experimentally verified. The mechanism is clear (a change to a business concept touches fewer files because the concept lives in one place), but alternative explanations exist (teams that adopt DDD may already have better domain understanding).

**What the skill takes from this:** Archetype 4 is a direct operationalization of DDD tactical patterns, reduced to structural gates. The skill draws the critical boundary between archetypes 3 and 4 — the line where DDD earns its keep — based on the cost of modeling vs. the cost of duplication. The "no-getter discipline" is a distillation of the DDD insight that rich domain objects expose behavior, not state.

---

## 7. Hexagonal / Ports and Adapters Architecture

### Cockburn (2005)

**Source:** Cockburn, A. (2005). "Hexagonal Architecture." Originally published as a blog post and later included in Cockburn's writings on software architecture.

**Grade: ●○○** (practitioner pattern; strong internal logic; no controlled measurement against alternatives)

**What it proposes:** The application core is surrounded by ports (interfaces the application defines for the outside world) and adapters (implementations of those interfaces for specific technologies). The insight is that the application defines the contract; the infrastructure satisfies it — not the other way around.

**What the skill takes from this:** The dependency rule in archetypes 4 and 7 is the ports-and-adapters insight applied as a structural gate: the core layer imports nothing from infrastructure. This is the pattern that enables the testability claim — business rules are testable without a database because the ports are interfaces, not concrete dependencies.

---

## 8. Clean Architecture

### Martin (2012)

**Source:** Martin, R. C. (2012). "The Clean Architecture." Blog post. Later expanded in Martin, R. C. (2017). *Clean Architecture: A Craftsman's Guide to Software Structure and Design*. Prentice-Hall.

**Grade: ●○○** (practitioner pattern; the dependency rule is a restatement of older principles (Parnas, hexagonal) in a specific concentric-layers metaphor; the concentric-layers arrangement has not been compared against alternatives in controlled measurement)

**What it adds:** The concentric dependency rule (dependencies point inward; inner circles know nothing of outer circles) and the specific four-layer arrangement (Entities → Use Cases → Interface Adapters → Frameworks & Drivers). The contribution is the unified presentation and the specific layering, not the dependency rule itself (which predates it).

**What the skill takes from this:** The four-layer structure in archetype 4 (Domain → Application → Infrastructure → Interface) is the Clean Architecture arrangement, collapsed to the layers that earn their keep in practice. The skill omits the Entity/Use-Case distinction when the domain is thin enough (archetype 3) — this is the application of YAGNI to architecture.

---

## 9. Conway's Law

### Conway (1968)

**Source:** Conway, M. E. (1968). "How Do Committees Invent?" *Datamation*, 14(4), 28–31.

**Grade: ●●○** (multiple large-scale empirical replications; the most quantitatively validated "law" in software engineering)

**What was measured:**
- Nagappan, N., Murphy, B., & Basili, V. (2008). "The influence of organizational structure on software quality: an empirical case study." *Proceedings of the 30th International Conference on Software Engineering (ICSE)*, 521–530 — studied Windows Vista and found that organizational structure (distance in the org chart) predicted post-release failures better than any technical metric (churn, complexity, coverage, pre-release bugs). Specifically, code contributed by multiple organizationally-distant teams had significantly higher failure rates.
- Several subsequent replications at other large organizations (including additional studies at Microsoft Research and independent studies at other companies) have confirmed the direction and magnitude of the effect.

**Limitation:** Conway's Law describes a correlation and a mechanism (communication structures constrain design), but does not provide a prescription beyond "align team and architecture boundaries." The skill's prescription — "match module boundaries to team boundaries" — is the standard application; the skill adds no novel insight beyond that.

**What the skill takes from this:** Standing Discipline 3 — "if two teams own different parts, the module boundary must match the team boundary." For a solo developer or single-team project, Conway's Law says the opposite: elaborate boundaries are ceremony.

---

## 10. The Archetype Taxonomy

**Grade: N/A** (procedural design choice, not an empirically validated instrument)

**Design rationale:** The seven archetypes are constructed to be MECE (mutually exclusive, collectively exhaustive) by construction. They were selected by tracing which structural rules actually differ between programming situations — i.e., which situations require different answers to "where does the business logic live?" and "what can depend on what?" The classification questions (external callers? non-trivial domain? async boundaries?) are the axes along which the structural rules diverge. The archetypes are not claimed to be the only valid classification; they are the one that minimizes the number of categories while capturing the structural variation that matters.

**Validation gap:** No empirical study measures whether classifying code into these seven archetypes and applying the corresponding structural rules produces better outcomes than a baseline (no classification, or a different classification). The skill's value proposition is procedural (transparent, reviewable structural decisions) rather than outcome-based (quantitatively demonstrated superiority).

---

## 11. Key Omissions — what this skill deliberately does NOT cover

### Performance-driven architecture

No structural rules in this skill are motivated by performance. If the task is dominated by performance constraints (real-time systems, high-frequency trading, embedded systems with hard memory limits), the structural rules here are subordinate to the performance rules. This skill defers to domain-specific performance methodology.

### Safety-critical systems

The structural rules assume that the cost of a bug is development/maintenance cost, not life-safety cost. For safety-critical software (avionics, medical devices, automotive), structural rules from DO-178C, ISO 26262, or IEC 62304 take precedence over anything in this skill.

### Specific technology patterns

This skill does not prescribe specific GoF patterns, specific framework conventions, or specific language idioms. It operates at the module/component level; language-level patterns are assumed to be applied correctly by the AI without this skill's guidance.

---

## 12. Summary evidence table

| Principle | Source | Grade | Measured outcome |
|---|---|---|---|
| Information hiding | Parnas 1972 | ●●● | Fewer module changes under design-decision changes (demonstrated) |
| Coupling → defects | Briand 1999, Basili 1996 | ●●● | Coupling metrics predict fault-proneness (correlated, measured) |
| Cohesion → defects | Basili 1996 | ●●○ | Weaker correlation than coupling; LCOM predicts in some studies, not others |
| SRP (God Classes → defects) | Yamashita & Moonen 2012 | ●●○ | God Classes have higher change- and defect-proneness (statistically significant) |
| OCP, LSP, ISP, DIP | Martin 2000s | ●○○ | Practitioner consensus; no quantitative defect correlation established |
| GoF patterns | GoF 1994 | ●●○ | Communication value demonstrated; defect correlation not established |
| YAGNI | Beck 1999 | ●●○ | Mechanism clear; comparative cost of deferral measured in small study only |
| DDD tactical patterns | Evans 2003 | ●●○ | Case studies in domain-complex industries; no controlled experiment |
| Hexagonal architecture | Cockburn 2005 | ●○○ | Strong internal logic; no comparative measurement |
| Clean Architecture | Martin 2012 | ●○○ | Dependency rule restates older findings; concentric arrangement not measured |
| Conway's Law | Conway 1968, Nagappan 2008 | ●●○ | Org structure predicts failures better than technical metrics (replicated) |
| Archetype taxonomy | — | N/A | Procedural; not empirically validated |
