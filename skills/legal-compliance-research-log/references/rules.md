# legal-compliance-research-log — full rules and citations

Moved verbatim from SKILL.md by issue-100 progressive disclosure.
The SKILL.md body carries the rule index; read this file when a
matched rule's full text, citation, or counter-example is needed.

## [S1] Axis: lawful-basis-selection -> `playbook/lawful-basis-selection.md`

- Layer 1/2 (named legal standard, primary text): query "GDPR Article 6
  lawful basis selection criteria", fetched
  https://gdpr-info.eu/art-6-gdpr/ directly for Art 6(1) full text ->
  rules 1-3 (contract-vs-consent, legitimate-interest balancing,
  consent-as-fallback).
- Layer 1 (practitioner synthesis): search-summarized
  https://gdprlocal.com/gdpr-legitimate-interest/ and
  https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/lawful-basis/a-guide-to-lawful-basis/
  -> rule 4 (removal: one basis per purpose, drop duplicate stacking).

## [S2] Axis: retention-and-minimization -> `playbook/retention-minimization.md`

- Layer 1/2 (named legal standard, primary text): fetched
  https://gdpr-info.eu/art-5-gdpr/ directly for Art 5(1)(c)/(e) full
  text -> rules 1, 4 (drop unnecessary fields; new purpose = new
  necessity check).
- Layer 1 (practitioner): search-summarized
  https://support.secureprivacy.ai/article/data-retention-policies-dpo-guidance/
  -> rule 2 (shortest-period-per-category, not a flat org-wide period).
- Layer 1 (practitioner): search-summarized
  https://gdprlocal.com/gdpr-storage-limitation/ -> rule 3 (removal:
  delete/anonymize on lapse, no "might be useful later" archive).

## [S3] Axis: cross-border-transfer-mechanism -> `playbook/cross-border-transfer.md`

- Layer 1/2 (named legal mechanisms): search-summarized
  https://www.legiscope.com/blog/cross-border-data-transfers.html and
  https://www.termsfeed.com/blog/dpf-scc-bcr/ -> rules 1, 2
  (adequacy-skip-SCCs, SCC-over-BCR for external vendors).
- Layer 1 (practitioner): search-summarized
  https://inplp.com/latest-news/article/sccs-and-cocs-and-bcr-untangling-the-web-and-spotting-the-difference/
  and https://trustarc.com/resource/selecting-the-best-eu-us-data-transfer-mechanism/
  -> rule 3 (BCR-over-SCC amortization for growing multinational
  groups).
- Layer 1/2: search-summarized
  https://www.recordinglaw.com/world-laws/world-data-privacy-laws/eu-data-privacy-laws/gdpr-international-data-transfers/
  -> rule 4 (removal: cut a transfer plan or exposure finding that
  skips the mandatory Transfer Impact Assessment).

## [S4] Axis: consent-mechanism-ux -> `playbook/consent-ux.md`

- Layer 1/2 (named legal standard + practitioner UX guidance):
  search-summarized https://www.cookieyes.com/blog/dark-patterns-in-cookie-consent/
  (quoting Art 7(4) and Recital 32) -> rules 1, 2 (equal-prominence
  reject, unticked-by-default non-essential consent).
- Layer 1 (practitioner): search-summarized
  https://www.truevault.com/learn/keeping-your-cookie-banner-gdpr-compliant/
  -> rule 3 (name the specific purpose and rejection means in plain
  language).
- Layer 1/2 (enforcement precedent): search-summarized
  https://www.cnil.fr/en/dark-patterns-cookie-banners-cnil-issues-formal-notice-website-publishers
  -> rule 4 (removal: remove purpose-bundling and reject-path friction
  rather than adding disclosure copy).

## [S5] Axis: vendor-dpa-requirements -> `playbook/vendor-dpa.md`

- Layer 1/2 (named legal standard, Art 28): search-summarized
  https://www.recordinglaw.com/world-laws/world-data-privacy-laws/eu-data-privacy-laws/gdpr-data-processing-agreement/
  -> rules 1, 3 (DPA required before data flows; sub-processor
  obligations flow down).
- Layer 1/2: search-summarized
  https://watchdogsecurity.io/gdpr/processor-safeguards-and-management
  -> rule 2 (prior authorization before sub-processor engagement).
- Layer 1 (practitioner): search-summarized
  https://kirkpatrickprice.com/blog/requirements-for-gdpr-data-processing-agreement/
  -> rule 4 (removal: prune stale sub-processor list entries).

## [S6] Axis: oss-license-compatibility -> `playbook/license-compatibility.md`

- Layer 1 (practitioner explainer): search-summarized
  https://milvus.io/ai-quick-reference/what-are-license-compatibility-issues-in-open-source
  and https://www.credativ.de/en/blog/credativ-inside/understanding-open-source-licenses-gpl-mit-apache-compared/
  -> rules 1, 2, 4 (permissive-is-safe default; GPL propagation; GPLv2/
  GPLv3 mutual incompatibility, removal choice on conflict).
- Layer 2 (named standard/FAQ): search-summarized
  https://www.mend.io/blog/top-10-apache-license-questions-answered/
  -> rule 3 (Apache-2.0-vs-GPLv2 patent-clause conflict).

## [S7] Sources fetched but not used as a rule citation

- https://gdpr-text.com/read/article-6/ and
  https://watchdogsecurity.io/gdpr/lawfulness-of-processing — appeared
  in the lawful-basis search results as duplicate/alternate renderings
  of Art 6; the direct gdpr-info.eu fetch was used as the primary-text
  citation instead to avoid citing a secondary mirror for the same
  clause.
- https://usercentrics.com/knowledge-hub/gdpr-data-retention/ — used
  only as corroboration inline in retention-minimization.md rule 4, not
  as a standalone rule's sole citation.

## [S8] Removal-rule coverage check (amendment 4)

Every axis file carries at least one rule whose choice is subtractive
(drop/remove/delete/cut/prune), grounded where the removal itself needed
independent justification (rather than restating the same primary-source
prohibition already cited) in Adams, Converse, Hales & Klotz, "People
systematically overlook subtractive changes," Nature 592 (2021), summary
fetched this session via
https://phys.org/news/2021-04-brains-opportunities.html: "people
systematically default to additive solutions... even when subtraction
would be more effective... because subtractive ideas require more
cognitive effort" — the general cognitive-bias backdrop for why an
all-additive playbook undercounts real practitioner judgment, per the
amendment-1 academic-layer requirement.

- lawful-basis-selection.md rule 4 — drop duplicate stacked basis.
- retention-minimization.md rule 1 — drop unnecessary field collection;
  rule 3 — delete/anonymize on retention lapse.
- cross-border-transfer.md rule 4 — cut a transfer plan/finding that
  skips the Transfer Impact Assessment.
- consent-ux.md rule 4 — remove purpose-bundling and reject friction.
- vendor-dpa.md rule 4 — prune stale sub-processor entries.
- license-compatibility.md rule 4 — remove one of two incompatible GPL
  components.

