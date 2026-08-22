---
name: market-analysis-evidence-rigor
description: Use when deciding whether a market/competitor claim needs a primary source, tracing a secondary citation to its primary source, labeling an unsourced claim as an assumption, hedging a forecast or count claim, or checking a citation list for padding or staleness. Applies to the evidence-rigor axis.
axis: evidence-rigor
rule_count_floor: 10
---

# Evidence-rigor rules

Decision rules for whether a methodological/factual claim carries a
source or must be labeled an assumption (this rulebook's `Sources:`
list / evidence-appendix requirement). Research trail: layer 1
(practitioner sourcing standards) plus layer 3 (overconfidence/
forecasting-bias literature bearing on how unlabeled certainty should
be treated).

## Trigger

Apply this skill when a market or competitor claim is being written
down, when only a secondary source is available for a claim, when no
source can be found at all, when a forecast or count claim is being
stated, or when reviewing a citation list for redundancy or staleness.

## Procedure

1. When stating a factual market/competitor claim, attach a primary
   source; if only a secondary source is available, trace its citation
   chain to the primary source rather than citing the secondary
   summary (rules 1-2, 4).
2. When no source can be found after a genuine search, label the claim
   explicitly as an assumption rather than stating it as fact (rule 3).
3. When presenting a market-sizing or forecast number, hedge it as a
   range or with an explicit confidence qualifier rather than a single
   precise figure (rule 5).
4. When citing a competitor's own marketing claim, flag it as
   self-interested testimony and pair it with an independent source
   before it counts as evidence (rule 6).
5. When a count or ratio claim appears in the record, require it to be
   reproducible from a named, checkable source rather than stated as a
   bare number (rule 8).
6. When reviewing a citation list, drop redundant secondary citations
   that restate the same primary fact, keep the primary-vs-secondary
   type visibly distinguishable, and note the source date for any
   time-sensitive claim (rules 7, 9-10).

## Output shape

Every factual, count, or forecast claim in the record either carries a
traceable primary source or is explicitly labeled an assumption, with
secondary sources reserved for context, redundant citations removed,
and time-sensitive claims dated.

## Rules

1. When a claim states a fact about the market or a competitor
   (a number, a price, a share, a date), attach a primary source
   (the original filing, pricing page, dataset, or interview) — a
   primary source is original material created at the time of the
   fact, and is what a rigorous claim requires as its base evidence.
   source: https://researcher.life/blog/article/primary-vs-secondary-sources-differences-and-examples/
2. When only a secondary source (an analyst summary, a news article) is
   available for a claim, and that secondary source itself cites a
   primary one, trace the chain and cite the primary source directly —
   citing the secondary source alone when a traceable primary exists is
   the specific anti-pattern rigorous sourcing practice warns against.
   source: https://nickwolny.com/secondary-sources-primary-sources-how-to-cite/
3. When no source can be found for a claim after a genuine search,
   label it explicitly as an assumption (e.g. "Assumption:") rather than
   stating it as fact with no citation — an unlabeled, uncited claim is
   indistinguishable from a sourced one to a downstream reader, which is
   the exact failure this axis exists to prevent.
   source: docs/issue-1174/proposals/operational-playbook-program.md
   (this rulebook's own governing role-directive, `PRODUCES` field)
4. When a secondary source is being used, restrict its role to
   establishing context, showing a debate exists, or summarizing
   consensus — never as the sole direct evidence for a specific factual
   claim the record depends on. source:
   https://researcher.life/blog/article/primary-vs-secondary-sources-differences-and-examples/
5. When an analyst's own confidence in a market-sizing or forecast claim
   has not been checked against an external data point, present the
   number as a range or with an explicit confidence qualifier rather
   than a single precise figure — self-assessed forecasts are
   systematically overconfident absent an external check, so an
   unhedged point estimate overstates the evidence. source:
   https://www.researchgate.net/publication/363213009_From_Noise_to_Bias_Overconfidence_in_New_Product_Forecasting
6. When citing a competitor's own marketing claim or press release as
   evidence for a competitive-positioning fact, flag it as
   self-interested testimony, not neutral evidence, and pair it with an
   independent source before it counts toward a verdict — a
   self-reported claim from an interested party fails the "original,
   firsthand, neutral" bar primary evidence otherwise meets.
   source: https://researcher.life/blog/article/primary-vs-secondary-sources-differences-and-examples/
7. **REMOVAL**: when a citation list has grown to include multiple
   secondary sources that all restate the same underlying primary fact,
   drop the redundant secondary citations and keep only the primary
   source plus at most one secondary source for context — a padded
   citation list creates an illusion of independently-corroborated
   evidence where only one underlying fact actually exists.
   source: https://www.nature.com/articles/s41586-021-03380-y
8. When a count or ratio claim appears in the record (e.g. "N of M
   competitors do X"), require the claim to be reproducible from a
   named, checkable source (a dataset, a fenced command output, or an
   enumerated citation list) rather than stated as a bare number — an
   unreproducible count is not distinguishable from a guess.
   source: docs/issue-1174/proposals/operational-playbook-program.md
9. When citation-style differs across primary and secondary sources
   used in the same record (e.g. APA-style journal citation next to a
   bare URL for a pricing page), keep the underlying source type visibly
   distinguishable (primary vs. secondary) even if exact citation
   formatting is not standardized — the type distinction is what lets a
   reviewer judge evidentiary weight, not the formatting itself.
   source: https://www.clearvoice.com/resources/primary-vs-secondary-sources/
10. When a claim is time-sensitive (pricing, headcount, market share)
    and the cited source is more than one reporting cycle old, note the
    source's date next to the claim rather than presenting it as
    current — an undated time-sensitive claim silently overstates its
    own freshness to a reader relying on the record today.
    source: https://researcher.life/blog/article/primary-vs-secondary-sources-differences-and-examples/

## Related skills

- [market-analysis-competitor-mapping](../market-analysis-competitor-mapping/SKILL.md) — the competitor claims this skill vets typically originate from a competitor-mapping pass.
