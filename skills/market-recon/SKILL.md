---
name: market-recon
description: >-
  An execution harness that PERFORMS external market, demand, and competitive research —
  running the actual web searches and source sweeps, verifying its own coverage with objective
  stopping criteria (saturation), and delivering a confidence-graded evidence report. Use
  whenever the user asks to research, size, or judge a market or opportunity — "이 시장 조사해줘",
  "research this market", "how big is the market for X", "is there real demand for this",
  "who are the real competitors", "should we enter X — look into it", "size the TAM/SAM/SOM",
  "find the gap in this market", "market research for a new product/segment/region". Trigger
  it even when the user just describes a market bet and wants it investigated. It is the
  outward-looking companion to diagnose-first (which looks inward at causes). Do NOT use for
  a quick factual lookup (one market cap or pricing page — just answer), for internal
  root-cause/bottleneck problems (diagnose-first), or for creative/subjective work.
---

# Market Recon — a research execution harness

This skill is not advice about how the *user* should research a market. When it triggers, **you perform the research** — you run the searches, chase the sources, build the numbers, and check your own coverage — and what you hand back is a finished, confidence-graded evidence base. The methodology below is your quality control, applied to your own work.

## First: does this need the harness?

- **Single factual lookup** ("what's X's market cap?", "what does Y charge?") — just answer it. The harness builds evidence bases for decisions, not single numbers.
- **Internal problem** (cost/latency/failure root cause) — that's `diagnose-first`.
- **The user asks how to do research themselves** — answer from the criteria in `references/` without running a full scan.

Everything below applies when the user wants a market actually investigated.

## The one hard truth that shapes the whole run

You cannot verify a market estimate against ground truth until the future arrives. So the deliverable is not a confident number — it's a **defensible range with graded evidence and an honest coverage statement**. Concretely: every number traced to its primary source, independent triangulation, stated-preference data discounted, and an explicit record of what you did and didn't scan. Pretending to certainty the evidence doesn't support is the failure mode; a smaller, honest answer is the success mode.

## Evidence grade

- **The SSNIP test** (Small but Significant Non-transitory Increase in Price) for market definition: ●●○ — codified in the U.S. DOJ/FTC Horizontal Merger Guidelines (1982, revised 2010); the test is an analytical framework used by competition authorities, not an experimentally validated instrument.
- **Revealed-preference vs. stated-preference data**: ●●● — the gap is extensively measured. Stated willingness-to-pay systematically overstates actual payment behavior (~21% on average across multiple meta-analyses; List & Gallet 2001, Murphy et al. 2005). The mechanism (hypothetical bias) is well-documented in experimental economics.
- **Saturation as a stopping rule**: ●●○ — qualitative research methodology (Guest, Bunce & Johnson 2006 established ~12 interviews for code saturation in homogeneous samples; the concept traces to Glaser & Strauss 1967). The criterion is methodological, not experimentally validated.
- **Bottom-up vs. top-down sizing convergence**: ●○○ — a practitioner heuristic for internal consistency; no studied threshold exists for what constitutes "same order of magnitude."
- **Source-tiering** (government/audited > disclosed-methodology > blog > marketing): procedural design choice, not empirically validated. [설계]
- **Graveyard analysis** (searching for failed prior entrants): ●●○ — a well-established venture-capital and strategy-consulting practice; the logic is sound (survivorship bias correction) but no study quantifies its incremental predictive value.
- **The multi-modal sweep and saturation-ledger stopping rule**: procedural design choices adapted from production research systems. [설계]

Full evidence: `references/gate-criteria.md` (SSNIP, saturation formulas, hypothetical-bias magnitudes, HHI thresholds, reference-class forecasting).

1. **Name the decision.** Research without a decision is boundless. Pin what this feeds: enter or not? price at what? which segment first? If the request is underspecified (no region, segment, or decision named), ask 2-3 sharp clarifying questions when the user is present; if they're away, state your assumptions at the top of the report and proceed.
2. **Define the market boundary — before searching.** Everything downstream depends on it. Use the substitution test (if a monopolist of the defined market raised prices ~5%, would buyers flee to something outside it? then that something is inside) or equivalently the job-to-be-done: count everything the customer would hire instead, including manual workarounds and doing nothing. Write the boundary down; you'll report against it.
3. **Write a research brief.** Decompose the decision into the specific sub-questions the report must answer (size? demand nature? competitive structure? unit economics? graveyard?) before running a single search. Every production deep-research system front-loads this decomposition — it's what turns searching into research. The brief is also your completeness checklist at the end.
4. **Scale the run to the bet.** Rough effort guide (borrowed from production research systems): a simple fact-bounded question ≈ one agent, 3-10 tool calls; a standard market scan ≈ one modality-per-subagent fan-out; a serious commitment decision ≈ 10+ subagents across modalities plus a verification pass. Say which depth you're running and why.

## The scan protocol

### Phase 1 — Plan a multi-modal sweep

One search angle is always blind. Before searching, list the source *modalities* you'll cover, then sweep them — in parallel with subagents when the environment provides them. Two rules that measurably improve fan-out quality: (a) **search broad-to-narrow** — open with short, wide queries to map the landscape, then progressively narrow to specifics; starting narrow anchors you on whatever the first specific source says. (b) **Subagents return compressed findings, not raw dumps** — each subagent's instruction is to distill what it found into the material facts *with source URLs and dates attached to each fact*, because uncompressed tool output wastes the synthesis context and citations get lost in the pile. Give each subagent an explicit goal, output format, and boundary (which modality is theirs, what to skip).

**Send these to the judgment tier, not the scout tier** (reasoner, not executor — see `model-routing`). A modality brief reads like retrieval, so it gets routed like retrieval, and that is the mistake: Phase 2 asks each subagent to chase footnote chains to the primary document, notice that three reports quoting one figure share a single origin, and reject an attribution a search summarizer invented. A scout-tier agent stops at the first plausible secondary source and hands it back as a fact — and because everything downstream is built on those facts, one cheap collection pass silently caps the quality of the whole report. Modality count is a separate dial: Setup's "scale the run to the bet" decides *how many* subagents, this decides *what tier* each one is.

The modalities:

- **Official / statistical**: government stats, census, regulator data, trade-association figures.
- **Industry & financial**: analyst/market reports, competitor filings and IR materials, funding rounds, M&A activity.
- **Competitive surface**: competitor pricing pages, product catalogs, job postings (hiring signals strategy), app-store presence.
- **Behavioral demand signals**: review volumes and content, search-volume trends, community discussions (what people actually pay for and complain about — this is your revealed-preference evidence).
- **Graveyard**: prior entrants who tried this space and failed or exited, and why. Search for them explicitly ("X 서비스 종료", "X shutdown", "failed startups in Y") — an empty space with a graveyard is a warning, not an opportunity.

### Phase 2 — Collect with discipline

- **Trace every number to its primary source.** When a market size appears, follow the citation chain. If three reports quote the same figure, find whether they share one origin — if so, log it as ONE source, not three. If the chain dead-ends ("industry sources say..."), mark the number ●○○.
- **Tier your sources as you collect.** Government/regulator statistics, peer-reviewed work, and audited filings are top-tier; methodology-disclosed industry reports and citable expert material are mid-tier; blogs and forum posts that cite upstream sources are low-tier; authorless marketing pages and SEO content are rejected, not down-weighted. A claim's evidence grade (Phase 6) can never exceed its best source's tier.
- **Date-stamp and conflict-check every fact.** Note the data year (not the publication year), and whether the source has skin in the game (a vendor-sponsored report gets flagged).
- **Keep a saturation ledger.** After each batch of sources, log how many genuinely *new* facts/insights/competitors it produced. This ledger is what lets you stop honestly (Phase 5).

### Phase 3 — Build the numbers yourself

Don't just quote a report's TAM — rebuild the size **bottom-up** from collected primitives: target customer count × plausible adoption × price. Then cross-check top-down (industry total × segment share) and check the two converge to the same order of magnitude; if they don't, one of your assumption chains is broken — find which before reporting either. Fermi-check against a ceiling (population, total category spend). Run sensitivity: swing key assumptions ±20-30% and report whether the conclusion survives. Benchmark any implied market share against what comparable companies actually achieved (usually 0.1-2%, not 10%). Report ranges, never points.

### Phase 4 — Weigh demand and competition evidence

- **Grade demand evidence by its nature.** Actual purchases, paid subscriptions, revenue figures, sustained review activity = behavioral (strong). Survey "would buy" percentages and interview enthusiasm = stated (systematically inflated — stated willingness-to-pay overstates real WTP by ~21% on average, more for premium/specialty categories). When your only demand evidence is stated, discount it and say so; recommend an incentive-compatible test (pre-sale, pilot) as the confirmation step.
- **Count competitors by the job, not the category.** Include indirect substitutes and the customer's current workaround. For any white space you find, apply the two-part test: is demand verified there, and did someone already try and fail (Phase 1 graveyard)? Only then call it an opportunity.
- If concentration matters, compute HHI/CR4 from the shares you collected — valid only against the boundary defined in Setup.

### Phase 5 — The coverage gate: stop honestly

This is the harness's distinctive discipline. You stop scanning when ONE of these holds, and you **state which**:

- **Saturation** (the objective criterion): your ledger shows a batch of new sources across *different* modalities produced ~zero new material facts. That's the researched stopping rule — new-information rate near zero across consecutive independent batches.
- **Budget/time cap**: you hit the effort ceiling appropriate to the bet's weight. Legitimate — but then the report must say "stopped on budget, not saturation" and list what a deeper pass would cover.

Either way, the report carries a **coverage statement**: modalities scanned, notable sources not reached (paywalled reports, non-public data, languages not searched), saturation status, and the date — because this landscape has a shelf life. Silent truncation that reads as "we covered everything" is the violation.

### Phase 6 — Synthesize single-pass, then verify citations

Two rules from production systems before you write:

- **Research in parallel, write alone.** Never assemble the report from sections written by different subagents — that reliably produces disjoint, contradictory prose (the lesson every multi-agent research team learned the hard way). Subagents feed you compressed findings; *you* write the whole report in one pass against the research brief from Setup.
- **Run a citation-verification pass after writing.** Walk the finished draft claim by claim and check each citation is (a) real and (b) actually supports *that specific claim* — benchmark audits found even frontier research agents attach real-but-irrelevant URLs to claims, which no "does the link work" check catches. Fix or downgrade anything that fails.

The deliverable is a report with four mandatory parts:

1. **The answer as a range**, tied to the decision from Setup ("defensible size: X–Y; demand evidence: moderate-behavioral; entry verdict hinges on assumption Z").
2. **An evidence table**: each key claim with its source, date, evidence grade (●●● verified/quantitative · ●●○ industry-standard/consistent secondary · ●○○ untraced/single-source/stated-only), and verified-vs-assumed label. Never let a ●○○ claim wear ●●● confidence.
3. **The coverage statement** from Phase 5.
4. **The cheapest reversible next test** that would confirm or kill the key assumption (pre-sale with real payment, limited pilot, one-region launch) — because desk research has a ceiling, and the honest end of most market questions is "here's the defensible range, and here's the cheap experiment that resolves it."

## Standing disciplines (apply at every phase)

1. **Behavior over words** — revealed-preference evidence outranks stated; discount the stated.
2. **Independence before convergence** — triangulation only counts when sources don't share an origin.
3. **Primary sources or it's ●○○** — chase every number's footnote chain.
4. **Defensibility over false precision** — sourced round ranges beat unsourced precise points.
5. **Know and state your coverage** — what you didn't scan, dated.

## References — when to read them

Read `references/` only for a high-stakes run where you need the precise test or method mechanics: `references/gate-criteria.md` (the objective criteria with evidence grades — SSNIP, saturation formulas, hypothetical-bias magnitudes, HHI thresholds, reference-class forecasting), `references/methods.md` (how-tos: bottom-up sizing, Van Westendorp, Five Forces, Bass, saturation tracking). A light scan never needs them — everything required is on this page.