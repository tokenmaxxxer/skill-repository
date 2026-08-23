---
name: knowledge-management-curation-pruning
description: >-
  Use when an entry has gone uncited past a review cycle, when auditing a flagged entry, or
  when deciding whether to update, merge, supersede, or remove a knowledge-library entry.
  Trigger on requests like "prune stale knowledge entries", "audit the pattern library", "안
  쓰는 문서 정리해줘", "merge these duplicate entries". Do NOT use for how to mark a replaced
  entry's status and forward link (use knowledge-management-supersession-lifecycle).
metadata:
  axis: curation-pruning
  rule_count_floor: 10
---

# Curation quality gate and pruning

Research trail: G2's "What Is Content Pruning?", Conductor's content-pruning step-by-step guide, The Influence Agency's content-pruning guide, Backlink Manager's "Content Curation vs. Content Pruning", and Wikipedia's community-moderation model as referenced in the same sweep, all fetched this session — the literature here is SEO/content-ops in origin, applied to an internal knowledge library rather than a public site; the underlying mechanism (stale content erodes trust and buries good content) transfers, and is flagged as such rather than presented as knowledge-management-native research.

## Trigger

Apply this skill when an entry has gone uncited or unreused past a
review cycle, when auditing a flagged entry, when entries overlap or
duplicate each other, when prioritizing what to audit first, or when
deciding whether to update, merge, supersede, or remove a
knowledge-library entry.

## Procedure

1. Flag an entry for audit when it has not been cited, reused, or
   confirmed for a full review cycle, rather than waiting to notice it
   by accident (rule 1).
2. During an audit, aim to curate (fix, merge, or explicitly retire)
   rather than delete-by-default (rule 2).
3. If an entry's factual detail has changed but the underlying decision
   still holds, update it in place; if the decision itself no longer
   holds, supersede it per [[knowledge-management-supersession-lifecycle]]
   (rule 3).
4. Merge overlapping entries during the audit rather than leaving
   near-duplicates live (rule 4).
5. Prioritize auditing entries under high-traffic/high-reuse tags first
   (rule 5).
6. Rely on distributed review across all contributors in addition to
   scheduled audits, not a single-owner bottleneck (rule 6).
7. Record the audit date on an entry that passes with no changes, so
   the next cycle can tell "reviewed" from "never reviewed" (rule 7).
8. Remove an entry from the actively-searched index once an audit
   confirms it obsolete (rule 8).
9. When curating near-duplicates, keep the single best-written version
   and fold others' unique content into it, moving attribution to the
   provenance field rather than keeping redundant entries (rule 9).
10. Do not prune an entry solely for low use — target inaccurate,
    outdated, or redundant content, not merely unpopular content
    (rule 10).
11. Tie audit cadence to the underlying system's rate of change rather
    than a fixed calendar interval applied uniformly (rule 11).

## Output shape

An audit decision per flagged entry — update in place, merge, supersede,
or remove — dated on the entry, prioritized by tag traffic and system
change rate.

## Rules

1. When an entry has not been cited, reused, or confirmed (per [[pattern-extraction]] rule 11) for a full review cycle, flag it for audit rather than leaving it silently in the active index — content-pruning practice treats a scheduled audit, not ad hoc discovery, as the mechanism that catches staleness, because nobody reliably notices an unused entry by accident. source: https://www.g2.com/articles/content-pruning

2. When auditing a flagged entry, the goal is curation (fix, merge, or explicitly retire it), not deletion-by-default — content-pruning guidance is explicit that the aim is "mass curation, not mass deletion": most flagged entries should be updated or merged, and only genuinely obsolete ones removed from the active set. source: https://backlinkmanager.io/blog/content-curation-vs-content-pruning-understanding-difference/

3. When an entry references facts, tools, or system state that has since changed, update it in place if the underlying decision still holds, or supersede it per [[supersession-lifecycle]] if the decision itself no longer holds — do not leave outdated factual detail live just because the entry is still "mostly" correct, since a reader trusts every line of an entry equally and cannot tell which parts have rotted. source: https://theinfluenceagency.com/blog/guide-to-content-pruning-and-its-benefits

4. When multiple entries cover overlapping ground with none clearly superseding another, merge them during the audit rather than leaving near-duplicates live — content-pruning practice treats near-duplicate content as a retrieval-quality cost even when each individual entry is accurate, because a searcher/RAG system now has to choose between competing near-identical hits with no signal for which is authoritative. source: https://www.conductor.com/academy/content-pruning/

5. When curating, prioritize auditing entries that sit under high-traffic/high-reuse tags (per [[taxonomy-tagging]]) first — pruning guidance frames prioritization by impact (traffic/crawl-budget in the SEO analogy) because audit effort is finite and a stale entry under a heavily-searched tag corrupts far more retrievals than a stale entry under a rarely-used one. source: https://www.compose.ly/content-strategy/content-pruning

6. When a community/multiple contributors maintain the same library, rely on distributed review (any contributor can flag/fix an entry they encounter as stale) in addition to scheduled audits, rather than making curation a single-owner bottleneck — Wikipedia's community-moderation model demonstrates sustained accuracy at scale specifically because review is distributed across everyone who touches an article, not gated on one curator.

7. When an entry passes an audit with no changes needed, record the audit date on the entry itself — this is what lets the *next* audit cycle (rule 1) distinguish "reviewed recently and still correct" from "never reviewed," so the same entry doesn't get needlessly re-flagged every cycle while genuinely stale neighbors get missed.

8. **REMOVAL**: When an entry is confirmed obsolete during an audit (the practice it describes is gone and nothing supersedes it, per [[supersession-lifecycle]] rule 2's `deprecated` case), remove it from the actively-searched index, not just leave it live with a mental note — pruning guidance is explicit that leaving known-stale content live measurably degrades trust in the *whole* library once a reader hits even one obviously wrong entry, not just that one entry. source: https://theinfluenceagency.com/blog/guide-to-content-pruning-and-its-benefits

9. **REMOVAL**: When curating a set of near-duplicate entries (rule 4), do not keep "one from each contributor" for attribution reasons — keep the single best-written, most complete version and fold the others' unique content into it; attribution belongs in the entry's provenance/source-issue field (per [[pattern-extraction]] rule 10), not in a proliferation of otherwise-redundant entries.

10. When an audit finds an entry that is accurate but has never been retrieved/cited since filing, do not prune it solely for lack of use — pruning guidance targets content that is *inaccurate, outdated, or redundant*, not content that is merely unpopular; a correct, unique, low-traffic entry is exactly the kind of tail knowledge a curated library exists to preserve that a popularity-only heuristic would wrongly cut. source: https://www.g2.com/articles/content-pruning

11. When deciding the audit cadence itself, tie it to the rate of change in the underlying system the library documents (a fast-moving codebase/process needs shorter cycles than a stable one), rather than a fixed calendar interval applied uniformly across every tag — a uniform cadence under-audits fast-changing areas and wastes review effort on stable ones, the same impact-weighting logic as rule 5 applied to time instead of traffic.
