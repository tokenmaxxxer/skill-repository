# parallel-decomposition — full rules and citations

Moved verbatim from SKILL.md by issue-100 progressive disclosure.
The SKILL.md body carries the rule index; read this file when a
matched rule's full text, citation, or counter-example is needed.

## [S1] Evidence grade

Full evidence grades with source-by-source detail in `references/evidence.md`. Summary: all studies are pre-2013 observational human-organization data; none measured agents and none was an experiment. The premise that the discipline pays off on agent fleets is untested.

## [S2] The reading that drives the procedure

Conway's constraint, pointed at a fleet, says something specific. Agents working in parallel
exchange nothing directly while they work — they share a repo and a common brief, but no channel
carries a decision from one to another mid-flight. An organization shaped like that can apply a
decomposition; it cannot discover one.

That gives the failure mode its shape. Fan out a change whose pieces must *agree* on something — a
type, a signature, a schema, an invariant — and each agent makes a locally plausible decision about
it. Every piece passes its own check. The disagreement is only visible in the union. The fix is not
more agents or better briefs: freeze the thing they would have had to agree on **before** any of
them starts, which turns a cross-cutting change into a module-shaped one.

Whether defects actually concentrate there is, per the evidence grade, an untested implication.
What is not in doubt is the mechanism: two agents that never exchange a message cannot converge on
an unstated convention except by luck.

## [S3] When the procedure says no

"Do not parallelize this" is an honest output, not a failure. A change whose contract can only be
discovered by doing the work, or whose write sets cannot be made disjoint, is serial work. Reporting
that costs one paragraph. The alternative costs N confident agents and a union nobody can untangle.

