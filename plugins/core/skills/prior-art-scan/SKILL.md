---
name: prior-art-scan
description: >-
  An execution harness for prior-art and patent scanning that runs the actual triple search
  (keyword + classification + citation) across free patent databases, reads claims correctly,
  tracks recall/coverage, and delivers a graded findings report — while staying strictly on the
  research side of the research-vs-legal-opinion line. Use whenever the user wants to check what
  already exists before building or filing — "이거 특허 있나 찾아봐", "prior art search for this",
  "is this idea already patented", "freedom to operate check", "has someone done this before",
  "patent landscape for X", "will this infringe existing patents". Trigger it when someone is
  about to build or file assuming the space is clear. It produces a research base and flags what
  needs a patent attorney; it does NOT give a legal clearance opinion. Do NOT use for trademark
  questions, general market/competitor research (market-recon), or when the user explicitly needs
  a formal legal FTO opinion (that requires a qualified attorney — say so).
---

# Prior-Art Scan — a search harness that stays on the research side of the legal line

When this triggers, **you run the search** — the real triple search across free databases, reading claims the way examiners do — and hand back a graded findings report. The hard boundary: this produces *research*, never a legal clearance opinion. The failure mode it prevents two ways: building/filing on the false belief that a space is empty (because a keyword-only search missed it), and overstepping into legal conclusions that only a qualified attorney (patent attorney/변리사) can give.

## First, fix the search type — it changes everything

The type determines what you search, which documents count, and which part you read. Get this wrong and the whole scan is misaimed:

- **Patentability / novelty** — is the idea new enough to patent? Search ALL disclosures, any date, any language, patent *and* non-patent; read the full disclosure.
- **Freedom to operate (FTO) / clearance** — will building this infringe someone's *live* rights? Only **in-force** patents (unexpired, fees paid) count; read the **claims only**; jurisdiction-by-jurisdiction (patents are territorial). Expired patents are irrelevant here (but are still prior art for patentability).
- **Invalidity** — kill a specific patent's claims? Deep dive on one patent's claims, hunt disclosures before its priority date.
- **Landscape** — map a field? Broad and shallow, for R&D/entry strategy.

State the type up front and run the scan accordingly.

## The one rule that carries the most weight

**No single search method is a complete search.** Keyword-only recall is badly incomplete — synonyms, coined terms, and translations slip through; measured recall for single methods runs anywhere from 0% to ~50%. Real coverage needs the **triple search**: keyword + classification (CPC/IPC) + citation chasing (forward/backward from seed patents). Each finds documents the others miss; only together do they close the gaps. Examiners are explicit that text search alone is rarely a thorough search.

## The protocol

### 1 — Terms and classes

Brainstorm the concept's terms *and* their variants — synonyms, spelling variants (catalyse/catalyze), hyphenation (nanotube/nano tube), and non-English equivalents, because missing a variant silently drops whole families. Find the relevant CPC/IPC classification codes and read the class definitions to confirm scope. The classes, not the keywords, are the backbone (USPTO's 7-step strategy treats keywords as a supplement to classification).

### 2 — Search the databases (run it, multi-source)

No single database is complete; sweep several because their national full-text coverage differs — Google Patents (broadest, 100+ offices, machine translation, includes non-patent literature), Espacenet (EPO, strong bibliographic/family data), USPTO Patent Public Search (US + examination history), WIPO PATENTSCOPE (PCT + many countries, but OCR full-text varies wildly by country), KIPRIS (Korea). Run keyword + classification + citation on each relevant one. Include **non-patent prior art** — papers, standards, open-source code, product catalogs, dated web pages — because any public disclosure counts, and it has no classification codes so it's easy to miss.

### 3 — Read the documents correctly

- **Claims define the right.** The claims — not the abstract, not the description — set the legal scope. For FTO this is everything: read the independent claims and check whether your product falls within them. Reading the abstract instead of the claims is the classic error.
- **Dates matter.** Priority date is the novelty cutoff (anything public before it can be prior art); filing and publication dates differ from it. For FTO, check the patent is actually in force (not expired/lapsed/abandoned) — "dead patent" status flips relevance.

### 4 — Coverage and honesty

Track a saturation signal: are new searches surfacing only documents you've already found? That approximate saturation, plus "every probable classification field covered and documented," is the practical completeness bar — there is no quantitative recall threshold, and 100% recall is theoretically impossible (someone's unpublished earlier-priority filing can always exist). So the report states coverage honestly: databases and classes searched, languages/sources not reached, and residual uncertainty.

### 5 — Deliver, and stop at the legal line

Report each relevant reference with: patent/publication number, the specific claim(s) or passage that matters, priority date, legal status (for FTO), and a plain-language note on *why* it's relevant. Grade confidence. Then hold the line: an FTO *opinion* — "you are/aren't clear to launch" — is a legal conclusion reserved for a qualified attorney, and getting it matters because a documented attorney opinion is the defense against willful-infringement treble damages. Your job ends at "here's what exists and what looks close; here's what a patent attorney should opine on." Say when the stakes (crowded field, litigation history, big investment) mean a professional searcher/attorney should take over.

## Standing disciplines

1. **Search type first** — it dictates documents, dates, and what you read.
2. **Triple search or it's incomplete** — keyword alone is a known failure.
3. **Claims, not abstracts** — the abstract is a lure; the claims are the right.
4. **Variants and non-patent literature** — synonyms, translations, papers, code.
5. **Research, not legal opinion** — flag the attorney's territory, don't enter it.

## References

Read `references/criteria.md` for a high-stakes scan needing the precise mechanics and sources — search-type comparison table, database coverage specifics, recall studies, claim-reading and date rules, the FTO legal boundary, common-mistake checklist. Light "has anyone done X" questions never need it.