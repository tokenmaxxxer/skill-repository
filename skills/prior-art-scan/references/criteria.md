# Prior-Art Scan — objective criteria and their sources

Grades: ●●● official/quantitative · ●●○ industry standard · ●○○ folklore.

## Search types (●●○)

| Type | Question | Documents | Read | Dates |
|---|---|---|---|---|
| Patentability/novelty | Is it new enough to patent? | all disclosures, any date/language, patent + non-patent | full disclosure | anything before priority date |
| FTO/clearance | Will building it infringe live rights? | only in-force patents, per jurisdiction | **claims only** | current legal status |
| Invalidity | Can this patent's claims be killed? | disclosures before the target's priority date | target's claims | before target priority |
| Landscape | What's the field? | broad patent + NPL | overview | current |

Expired patents: irrelevant to FTO, still prior art for patentability. (Spruson & Ferguson; GreyB; USPTO.)

## Triple search — why single methods fail (●●●)

Keyword recall is fundamentally limited by synonym/translation mismatch. Measured single-method recall ranges 0-50% (FullRecall, arXiv 2507.14946); combining IPC classification + semantic similarity + citation reached 100% recall in that study. USPTO MPEP §904: "it is rare that a text search alone will constitute a thorough search." USPTO 7-step strategy leads with classification, treats keywords as a supplement. Citation chasing (forward = who cited this seed; backward = what it cited) extends from known-relevant seeds but is blind to brand-new fields — hence all three.

## Databases (●●●/●●○)

- **Google Patents** — 100+ offices, 120M+ docs, 22+ countries full-text, machine translation, integrates non-patent literature; explicitly "does not guarantee complete coverage." Free.
- **Espacenet (EPO)** — 80+ countries bibliographic, strong INPADOC family data. Free.
- **USPTO Patent Public Search** — US patents + applications + file wrapper (examination history). Free.
- **WIPO PATENTSCOPE** — 122+ countries + PCT, ~128M docs, but OCR full-text indexing varies hugely by country (China 45.5M, US 11.6M, JP 11.8M full-text; many others abstract-only). Free.
- **KIPRIS** — Korea patents/utility/design/trademark + linked foreign data. Free.
- **Derwent (Clarivate)** — paid; value is *rewritten standardized abstracts* that absorb terminology mismatch, not more patents.

Free databases have different national strengths — cross-search several; one is never enough.

## Reading (●●●)

Claims define the legal scope (Wikipedia/EPO/USPTO MPEP §2111); the specification supports and interprets claims but doesn't set the right. For FTO only the claims matter — reading the abstract instead is the classic error. Priority date = novelty cutoff; filing date and publication date (~18 months after filing) differ. For FTO, verify the patent is in force (unexpired, maintenance fees paid).

## Completeness (●●○ / ●○○)

MPEP §904.02 defines a thorough search as covering "all probable fields" where relevant art is most likely — a coverage judgment, not a percentage. No quantitative stopping rule exists (●○○); practical bars are (1) every probable classification covered and documented, (2) saturation — new searches return only already-found documents, (3) budget/time (state it if that's why you stopped). 100% recall is theoretically impossible: an unpublished earlier-priority application can always exist. EPO showed higher detection than USPTO/JPO; detection falls with geographic distance, technical complexity, and family size (Scientometrics 2016).

## Non-patent literature (●●●)

Any public disclosure is prior art regardless of type — papers, conference proceedings, standards, theses, open-source code, product catalogs, dated websites. USPTO examiners search 102k+ e-journals and 487k+ e-books via STIC. NPL usually lacks classification codes, so it's keyword-dependent and easy to miss; open-source code needs commit-timestamp/repository evidence to establish a public date.

## The legal boundary (●●○)

FTO is a *legal opinion from a qualified IP attorney*, not a search result. The driver: US willful infringement can trigger treble (3×) damages, and a documented attorney opinion evidences reasonable investigation. Research (this skill) = "this art exists, this claim looks close, a regulator/examiner interpreted it thus." Legal advice (attorney only) = "your product is/isn't clear." Escalate to a professional searcher/attorney for crowded fields, litigation history, large investment, or injunction exposure. Attorney-client privilege and 변호사/변리사 scope vary by jurisdiction — out of this skill's scope.

## Common mistakes checklist (●●○, PatSeer)

Missing synonyms/spelling/hyphenation variants; poor translation coverage of CJK filings; skipping classification codes or sub-classes; searching title/abstract instead of full claims; not defining search type first; ignoring working examples in the specification; assuming a "dead" patent is safe without checking status. AI/semantic search tools improve *finding* but not *interpreting* — claim-to-claim novelty/infringement judgment stays with a human; embedding-only recall is still unproven (FullRecall).