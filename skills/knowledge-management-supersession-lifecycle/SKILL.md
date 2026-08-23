---
name: knowledge-management-supersession-lifecycle
description: >-
  Use when a knowledge-library entry is replaced, dropped, or edited — deciding whether to
  mark it superseded or deprecated, and how to record the change without deleting history.
  Trigger on requests like "supersede this ADR", "deprecated vs superseded", "이 결정 문서 대체됐는데
  어떻게 처리해", "two teams proposed competing replacements". Do NOT use for flagging stale
  entries for audit or merge (use knowledge-management-curation-pruning).
metadata:
  axis: supersession-lifecycle
  rule_count_floor: 10
---

# Supersession, deprecation, and removal lifecycle

Research trail: adr.github.io (Architectural Decision Records reference site), Martin Fowler's "Architecture Decision Record" bliki entry, TechTarget's ADR best-practices guide, Catio's 2026 ADR guide, and GitScrum's ADR documentation best practices, all fetched this session — the ADR status-lifecycle literature is this playbook's primary source because it is the most mature, citable public model of exactly this problem (superseding a prior decision without losing its history).

## Trigger

Apply this skill when a knowledge-library entry is replaced by a newer
one, when a practice is dropped with nothing replacing it, when two
proposed successors conflict, or when deciding whether a change to an
entry is a plain edit or a supersession.

## Procedure

1. Mark an entry `superseded` and add a forward link to its replacement
   rather than editing the old entry's content in place (rule 1).
2. Mark an entry `deprecated` (not `superseded`) when nothing replaces
   it (rule 2).
3. Write the reason for the change into the new, superseding entry, not
   only a status flip on the old one (rule 3).
4. Carry the status and forward link on the entry itself, not only in a
   separate index (rule 4).
5. Carry a decision's timestamp forward into any superseding entry's
   own record of when the old decision held (rule 5).
6. When two teams independently propose superseding the same entry with
   different replacements, file both as candidate successors and
   resolve the conflict explicitly rather than silently picking one
   (rule 6).
7. Assign status from a closed, small set (`proposed`/`accepted`/
   `deprecated`/`superseded`) rather than free-text status notes
   (rule 7).
8. Never delete a superseded entry (rule 8).
9. Move a `deprecated` entry with zero live citations and no forward
   link out of the actively-indexed set into an archive tier, rather
   than deleting it or leaving it live (rule 9).
10. When an entry is marked `superseded`, remove its tags from the
    active controlled-vocabulary term set if it was the sole entry
    keeping that term populated, per
    [[knowledge-management-taxonomy-tagging]] rule 8, while keeping the
    term itself resolvable from the entry's historical record (rule 10).
11. Treat a change as a supersession if the original reasoning no longer
    holds, and as a plain edit in place if only wording/typos/
    formatting changed and the reasoning still holds (rule 11).

## Output shape

A status-tagged entry (`proposed`/`accepted`/`deprecated`/`superseded`)
carrying its own forward link and reasoning, never deleted, with active
tags reconciled against the controlled vocabulary.

## Rules

1. When a knowledge-library entry (pattern, decision record, or index entry) is replaced by a newer one, mark the old entry's status as `superseded` and add a forward link to the replacement rather than editing the old entry's content in place — ADR practice is explicit that a decision record, once accepted, is not rewritten when the decision changes; it is superseded by a new record that references it. source: https://www.martinfowler.com/bliki/ArchitectureDecisionRecord.html

2. When an entry no longer applies but nothing has replaced it (the underlying practice was simply dropped, not swapped for an alternative), mark it `deprecated`, not `superseded` — the two statuses answer different questions for a reader (superseded = "use this other entry instead"; deprecated = "this no longer applies, nothing replaces it") and collapsing them into one status forces every reader to open the entry just to find out which case it is. source: https://docs.gitscrum.com/en/best-practices/documenting-architectural-decisions

3. When superseding an entry, write the reason for the change into the *new* entry (why the old decision stopped holding), not only a status flip on the old one — ADR best practice requires the superseding record to explain why the change was necessary, because a bare status flip with no reasoning forces a future reader to reconstruct the "why" from surrounding context that may no longer exist. source: https://www.techtarget.com/searchapparchitecture/tip/4-best-practices-for-creating-architecture-decision-records

4. When a reader lands on a superseded or deprecated entry via an old link or search hit, the entry itself (not just the index) must carry the status and the forward link — status recorded only in a separate index/tracker is invisible to anyone who reaches the entry directly, which is the majority path for search-driven and RAG-style retrieval (see [[structure-findability]]). source: https://adr.github.io/

5. When a decision is timestamped, carry that timestamp forward into any superseding entry's own record of "as of when did the old decision hold" — ADR practice ties each record to version/temporal context of the system it affected specifically so a reader can tell whether an old, superseded entry is still relevant to the version of the system they are currently working with. source: https://www.catio.tech/blog/architecture-decision-record

6. When two teams or roles independently propose superseding the same entry with different replacements, do not silently pick one — file both as candidate successors on the old entry and resolve the conflict explicitly (owner decision or a follow-up entry), because silently choosing one hides the disagreement a future reader might need to know existed.

7. When status is being assigned, use a closed, small status set (`proposed`/`accepted`/`deprecated`/`superseded`) rather than free-text status notes — a small closed vocabulary is what lets the [[taxonomy-tagging]] axis's tooling and any future gate script filter/count entries by lifecycle state mechanically; free text defeats that.

8. **REMOVAL**: When an entry has been superseded, never delete the superseded entry itself — ADR practice states superseded/deprecated records should never be deleted because they form a timeline of how understanding evolved, and a deleted entry breaks every historical link and citation that pointed at it (including any judgment record that cited it under [[pattern-extraction]] rule 10's provenance requirement). source: https://www.techtarget.com/searchapparchitecture/tip/4-best-practices-for-creating-architecture-decision-records

9. **REMOVAL**: When a `deprecated` entry's underlying practice has had zero live citations for a full review cycle and carries no forward link (nothing superseded it because nothing needed to), move it out of the actively-indexed/searched set into an archive tier rather than leaving it mixed into current search results — this is a retrieval-quality removal (per [[curation-pruning]]), distinct from and never combined with the content-deletion the previous rule forbids: the record stays; only its default visibility is cut.

10. When an entry is marked `superseded`, remove its tags from the *active* controlled-vocabulary term set it was indexed under if it was the sole entry keeping that term populated, per [[taxonomy-tagging]] rule 8 — but keep the term itself resolvable from the entry's own historical record, since the removal in rule 9 above is about active-index visibility, not about breaking the term's own lookup path for someone following a historical citation.

11. When deciding whether a change to an entry is an edit or a supersession, use this test: if the *reasoning* that justified the original choice no longer holds, it is a supersession (new entry, old one linked); if only wording/typos/formatting changed and the original reasoning still holds, it is a plain edit in place — conflating the two either buries real decision changes as silent edits (losing the history ADR practice exists to preserve) or creates noisy near-duplicate entries for every typo fix. source: https://www.martinfowler.com/bliki/ArchitectureDecisionRecord.html
