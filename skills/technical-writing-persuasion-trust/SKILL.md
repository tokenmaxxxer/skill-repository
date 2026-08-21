---
name: technical-writing-persuasion-trust
description: Use when you need guidance on Persuasion and trust (adoption-facing docs). Applies to the persuasion-trust axis.
axis: persuasion-trust
rule_count_floor: 10
---

# Persuasion and trust (adoption-facing docs)

Decision rules for docs whose target-reader must decide to adopt/trust,
not just execute a known task. Research trail: layer 3 (academic:
Elaboration Likelihood Model, central vs. peripheral persuasion routes)
plus layer 1 (practitioner: developer-adoption documentation research).

## Rules

1. When the target reader is technically motivated and evaluating
   whether to adopt (high elaboration likelihood — they will actually
   read the argument), persuade through the central route: concrete
   working examples, exact API behavior, verifiable claims — not
   testimonials or brand framing — because "central route processing"
   is what drives agreement when the reader has motivation and ability
   to elaborate. source: https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2025.1679853/full

2. When the target reader is a decision-maker skimming (low elaboration
   likelihood — e.g. a manager evaluating a tool, not the engineer who
   will use it), peripheral cues (named companies using it, security
   certifications, response-time SLAs) carry real persuasive weight and
   should be surfaced early — "source factors... serve as simple
   acceptance or rejection cues when the elaboration likelihood is
   low." source: http://www.communicationcache.com/uploads/1/0/8/8/10887248/source_factors_and_the_elaboration_likelihood_model_of_persuasion.pdf

3. When onboarding documentation is the reader's first contact, scope
   the fastest path so a working first call lands in under ~10 minutes
   — "if a developer can't figure out how to make a first successful
   API call in under 10 minutes, chances are they'll look for
   alternatives," so this is a hard adoption-loss threshold, not a
   nice-to-have speed target. source:
   https://www.digitalapi.ai/blogs/how-api-documentation-improves-developer-adoption

4. When a doc can offer either a live/sandbox example or a
   read-only code snippet for the same feature, prefer the runnable
   sandbox — "developers who can test before committing are more
   likely to proceed, while those who can only test in production are
   more likely to delay... or abandon," so runnability itself is a
   trust lever, independent of prose quality. source:
   https://www.digitalapi.ai/blogs/how-api-documentation-improves-developer-adoption

5. **REMOVAL**: when a doc's draft contains marketing-style superlative
   claims ("blazing fast," "effortless") with no example or number
   backing them, delete the claim rather than tone it down — for a
   high-elaboration audience, an unverifiable peripheral claim inside
   otherwise technical prose reads as low-credibility noise and can
   undercut trust in the surrounding factual claims. source:
   https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2025.1679853/full
   (peripheral cues persuade only when elaboration is low; injecting
   them into a high-elaboration context has no established positive
   effect and risks credibility loss)

6. When personal relevance is low (a reader browsing docs for a tool
   they don't yet need), do not front-load dense technical argument —
   motivation and ability to elaborate are shaped by "personal
   relevance, prior knowledge, and contextual complexity," so a
   low-relevance reader needs a peripheral hook (a concrete outcome, a
   short use-case) before the central-route detail, or they disengage
   before reaching it. source:
   https://pmc.ncbi.nlm.nih.gov/articles/PMC8130952/

7. When documentation quality is the deciding factor being reported to
   stakeholders, treat clear docs as a strategic asset, not a
   cosmetic pass — "great documentation isn't a 'nice-to-have,' it's a
   strategic asset that builds trust and drives adoption" — so a
   review that scopes doc work as pure cleanup is scoping it wrong.
   source: https://builtin.com/articles/developer-documentation-as-product

8. When a claim about the product needs to persuade a skeptical
   technical reader, cite the verifiable artifact (a benchmark number,
   a spec section, a reproducible command) inline next to the claim
   rather than in an appendix — central-route persuasion depends on the
   reader being *able* to elaborate on the argument, which requires the
   evidence to be adjacent, not just present somewhere in the document.
   source: http://www.communicationcache.com/uploads/1/0/8/8/10887248/source_factors_and_the_elaboration_likelihood_model_of_persuasion.pdf

9. When a reader has low prior knowledge of the domain (per the
   target-reader note), do not rely on peripheral authority cues alone
   ("used by X") to carry adoption — low prior knowledge lowers ability
   to elaborate but the ELM literature ties source-cue reliance to low
   motivation, not low ability; a low-knowledge but motivated reader
   still needs central-route content, just written at their
   comprehension level (defer to the structure-comprehension axis for
   how). source: https://pmc.ncbi.nlm.nih.gov/articles/PMC8130952/

10. **REMOVAL**: when a doc repeats the same trust-building claim (e.g.
    "used in production by thousands of teams") in multiple sections,
    cut it down to one placement near the reader's decision point (e.g.
    the top of an adoption-facing overview) — repetition of a peripheral
    cue does not compound its persuasive value in the ELM model and
    instead reads as padding, contradicting this rulebook's own
    minimalism axis. source:
    https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2025.1679853/full
