---
name: knowledge-management-taxonomy-tagging
description: >-
  Use when adding, merging, or scoping a term in the controlled vocabulary, or when tagging
  an entry with an ambiguous, cross-cutting, or synonym-prone concept. Trigger on requests
  like "which tag should this get", "merge these synonym tags", "태그 체계 정리해줘", "SKOS
  broader/narrower mapping". Do NOT use for choosing an entry's Diátaxis type, title, or
  file path (use knowledge-management-structure-findability).
metadata:
  axis: taxonomy-tagging
  rule_count_floor: 10
---

# Taxonomy, tagging, and controlled vocabulary

Research trail: ISO 25964 (Thesauri and interoperability with other vocabularies, parts 1-2), ANSI/NISO Z39.19, SKOS (W3C Simple Knowledge Organization System) as summarized by NISO and Hedden Information Management, and Wikipedia's "Controlled vocabulary" entry, all fetched this session.

## Trigger

Apply this skill when two entries could be described by different
words for the same concept, when adding a new tag/term to the index,
when a term's meaning could be ambiguous, when choosing between
folksonomy and controlled vocabulary, or when tagging a cross-cutting
or source-specific entry.

## Procedure

1. When two entries could be described by different words for the same
   concept, pick one preferred term and register the other as a
   non-preferred synonym pointing to it (rule 1).
2. Place a new term inside the existing hierarchy via broader/narrower
   relationships rather than adding it as an unconnected flat label
   (rule 2).
3. Attach a scope note fixing a term's intended sense when its meaning
   could be ambiguous to a future tagger (rule 3).
4. Use a controlled vocabulary once the library exceeds a size where
   synonym/near-duplicate tags start fragmenting retrieval, rather than
   free tagging (rule 4).
5. Represent the vocabulary for machine consumption with SKOS's
   `broader`/`narrower`/`related`/`prefLabel`/`altLabel` primitives
   rather than an ad hoc nested-bullet list (rule 5).
6. Record a related-but-distinct concept as an associative relationship
   rather than forcing it into a false hierarchy (rule 6).
7. Tag a cross-issue index entry by concept, not by source-issue number
   (rule 7).
8. Remove a tag from the controlled vocabulary once it has had zero
   entries filed under it for a full review cycle and no scope note
   justifies keeping it (rule 8).
9. Merge two terms found to always co-occur on the same entries with no
   entry tagged with only one of them (rule 9).
10. Use ISO 25964 Part 2's interoperability mapping types
    (exact/close/broad/narrow match) rather than silently aliasing terms
    1:1 when aligning against another system's taxonomy (rule 10).
11. Tag a single entry with both terms when it genuinely spans two
    unrelated concepts, rather than forcing a single-tag choice
    (rule 11).

## Output shape

A term placed in the broader/narrower hierarchy with a scope note where
ambiguous, encoded in SKOS primitives, with synonyms and associative
relationships recorded explicitly rather than aliased or flattened.

## Rules

1. When two entries in the pattern library could plausibly be described by different words for the same concept (e.g. "stale record" vs. "outdated record"), pick one preferred term and register the other as a non-preferred synonym pointing to it — ISO 25964's equivalence relationship (preferred/non-preferred terms) exists specifically so indexers and searchers converge on one retrievable term instead of splitting the same concept across two tags. source: https://www.niso.org/standards-committees/iso-25964

2. When adding a new tag/term to the index, place it inside the existing hierarchy via broader-term/narrower-term relationships rather than adding it as an unconnected flat label — ISO 25964's hierarchical relationship is what lets a search on a broad term (e.g. "record lifecycle") also surface entries tagged with a narrower term (e.g. "supersession") without the tagger having to double-tag every entry. source: https://www.niso.org/schemas/iso25964

3. When a term's meaning could be ambiguous to a future tagger (e.g. "review" meaning code review vs. record review), attach a scope note fixing the intended sense for this vocabulary — ISO 25964 and thesaurus practice use scope notes precisely to stop indexing drift when the same word is tagged inconsistently over time by different people. source: https://www.niso.org/standards-committees/iso-25964

4. When choosing between a free-tagging (folksonomy) scheme and a controlled vocabulary for the pattern library, use the controlled vocabulary once the library exceeds a size where synonym/near-duplicate tags start fragmenting retrieval — folksonomy tagging research documents that uncontrolled tagging degrades precision as vocabulary grows, which is exactly the failure this playbook's own [[pattern-extraction]] axis warns against (near-duplicate entries). source: https://arxiv.org/pdf/cs/0701072

5. When representing the vocabulary for machine consumption (so tooling can render cross-references, not just a human reading the file), use SKOS's `broader`/`narrower`/`related`/`prefLabel`/`altLabel` primitives rather than an ad hoc nested-bullet list — SKOS is the W3C-standard, interoperable encoding of exactly the ISO 25964 relationship types, so adopting it avoids inventing a bespoke schema that only this repo's tooling can parse. source: https://moderndata101.substack.com/p/demystifying-skos-for-practitioners

6. When a related-but-distinct concept exists elsewhere in the taxonomy (not broader, not narrower, just associated — e.g. "supersession" is related to but not a parent/child of "pattern-extraction"), record it as an associative relationship rather than forcing it into a false hierarchy — ISO 25964 keeps associative relationships as their own category precisely because forcing association into hierarchy misleads a searcher who narrows by broader/narrower terms. source: https://www.niso.org/standards-committees/iso-25964

7. When tagging a cross-issue index entry, tag by concept, not by source-issue number — issue numbers are not retrievable knowledge units for someone who doesn't already know which issue to look in; the controlled-vocabulary term is the retrieval key, and the issue number belongs in the entry's body as provenance, not as the index key.

8. **REMOVAL**: When a tag has had zero entries filed under it for a full review cycle (see [[curation-pruning]]) and no scope note justifies keeping it as a placeholder for known future content, remove the tag from the controlled vocabulary rather than leaving it live — an empty term with no scope note is dead weight a future tagger might misuse, and Z39.19-style vocabulary maintenance treats vocabulary size itself as a precision cost, not a free asset. source: https://www.hedden-information.com/category/taxonomy-standards/

9. **REMOVAL**: When two terms are found, after use, to always co-occur on the same entries with no entry ever tagged with only one of them, merge them into a single term rather than keeping both — a synonym pair that survived initial registration (rule 1) but was missed should be collapsed the first time usage data reveals it, not left as two tags a searcher must remember to check both of.

10. When importing or aligning this vocabulary against another system's taxonomy (e.g. a skill spec's own spec tags, or another skill's index), use ISO 25964 Part 2's interoperability mapping types (exact/close/broad/narrow match) rather than silently aliasing terms 1:1 — a naive 1:1 alias breaks the first time the two vocabularies' term granularity diverges, while an explicit match-type records the fact of the divergence for future maintainers. source: https://www.niso.org/standards-committees/iso-25964

11. When a single entry genuinely spans two unrelated concepts (not near-duplicate, not hierarchical — e.g. a pattern that is both a taxonomy fix and a supersession precedent), tag it with both terms rather than forcing a single-tag choice — controlled vocabulary constrains which terms exist, not how many terms may apply to one entry; multi-tagging a genuinely cross-cutting entry is correct use of the scheme, not vocabulary sprawl.
