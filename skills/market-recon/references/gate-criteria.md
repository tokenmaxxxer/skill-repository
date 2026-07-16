# Gate Criteria — the objective tests behind each market-recon judgment

Every gate hides a judgment call. This file gives the researched criterion for each, graded by evidence strength:

- **●●●** — verifiable / quantitative test with a real threshold (trust it)
- **●●○** — industry-standard practice, no ground-truth verification
- **●○○** — procedural checklist / folklore (use, but it proves nothing about correctness)

The domain-wide truth to keep in mind: external estimates can't be checked against ground truth until the future arrives, so most criteria here are ●●○/●○○ *procedural proxies*. The ●●● tests are a minority — lean on them, and flag when you're relying on a proxy.

## Contents
1. G0 — market boundary defined right?
2. G1 — is the size defensible?
3. G2 — is the demand real?
4. G3 — is the competitive read complete and the gap real?
5. G4 — is coverage actually sufficient?
6. G5 — is the synthesis honestly graded and the forecast sane?

---

## G0 — "Is the market boundary defined right?"

**SSNIP / hypothetical-monopolist test (●●●).** The antitrust-grade test for market boundaries: would a hypothetical monopolist over your defined market profit from a Small but Significant Non-transitory Increase in Price (conventionally ~5%)? If buyers would flee to substitutes outside the boundary and make the rise unprofitable, those substitutes are *in* the market — widen the definition and repeat. This is the one boundary test grounded in measurable cross-price elasticity rather than opinion. Data-hungry (needs elasticity estimates), and fuzzy at the edges even in regulatory use — but it's the objective anchor.

**Jobs-to-be-Done boundary (●●○).** Define the market by the job the customer hires the product to do, and count everything they'd hire instead. The milkshake case: the real competitors weren't other milkshakes but bananas, bagels, and boredom on the commute. Guards against the "marketing myopia" of a too-narrow product-category boundary. Softer than SSNIP (rests on qualitative interviews) but applies when elasticity data doesn't exist.

**Pass conditions:** the decision the research feeds is named; the boundary passes the substitution/job test rather than defaulting to "our product category"; it's neither so narrow it excludes real substitutes nor so broad every number inflates.

---

## G1 — "Is the size defensible?"

**Bottom-up preferred over top-down (●●○).** Bottom-up (target customers × adoption × price) makes every assumption independently checkable; top-down (industry total × segment% × share%) hides an unfounded "we'll capture X%" step that drives the whole result. VCs from Series A up explicitly prefer a bottom-up revenue build over a top-down %-of-TAM. Industry-standard consensus, not a controlled comparison — hence ●●○.

**Triangulation with genuine independence (●●○).** Estimate the size ≥2 independent ways (e.g., bottom-up demand build vs. supply-side revenue sum) and check convergence to the same order of magnitude. Critical caveat: the sources must be *actually* independent — three market reports re-citing one original is circular citation, not triangulation, and produces fake confidence. No standard numeric convergence threshold exists (the literature doesn't set one); order-of-magnitude agreement is the practical bar.

**Fermi sanity-check + sensitivity (●●○).** Sanity-check the result against a known ceiling (total population, total category spend) — a market size exceeding total plausible spend signals a magnitude/units error (the single most common failure is a factor-of-ten slip). Then swing key assumptions ±20-30%; if the decision flips, the estimate isn't robust enough to act on. Present a range, not a point.

**Share benchmarking (●●○).** SOM's implied market share must be checked against what comparable firms actually achieved — recent tech IPOs claimed vast TAMs but hold 0.1-2% share. An implied share far above comparables without a specific reason is a red flag.

**Defensibility checklist (the real gate, ●●○).** A size estimate is defensible when: every number is sourced and reproducible; sources are independent; sensitivity-tested; magnitude/units sanity-checked against a ceiling; time/currency bases consistent; implied share benchmarked to comparables; data recent (≈2yr); competition/constraints reflected (not 100%-capture). No standardized scoring model aggregates these into a pass line — final judgment is qualitative.

**Pass conditions:** bottom-up built with sourced assumptions; independent triangulation converges within an order of magnitude; magnitude sanity-checked; sensitivity run; implied share benchmarked; TAM treated as ceiling not target.

---

## G2 — "Is the demand real?" (the most-abused gate)

**Behavior over words — the Mom Test (●●○).** Interview quality is judged by whether questions ask about past/present concrete behavior and actual spend, not hypotheticals or opinions on your idea. A "yes I'd buy that" with zero evidence of prior action is a void interview. Rules: ask about their life not your idea; ask what they *did* not what they *would* do; talk less. Logically sound and aligned with social-desirability-bias theory; not a controlled-experiment result, hence ●●○.

**Hypothetical-bias correction (●●●).** The quantified core of "behavior over words": a 2019 meta-analysis (Journal of the Academy of Marketing Science) found stated WTP overstates real WTP by ~21% on average — ~28-40% for specialty goods, ~9-19% for convenience goods, larger at higher prices; counter-intuitively, indirect methods (conjoint) show *more* bias than direct questions, and within-subject designs more than between-subject. So stated WTP must be discounted, not used raw. Cheap-talk scripts and certainty-scale recoding demonstrably shrink the bias in repeated field experiments. This is the domain's strongest single quantitative correction.

**Saturation as the discovery stopping rule (●●●).** Stop interviewing when new conversations stop yielding new themes. Quantified: Guest et al. (2006) found ~80% of codes appear within the first 6 interviews and code saturation by ~12 (homogeneous sample); a PLOS One (2020) formula sets it as (new themes in run ÷ base-set themes) below a threshold (≤5% ≈ 6 interviews; 0% ≈ 11-14). Heterogeneous samples need more (16-24 for meaning saturation). A real stopping rule with numbers, not "we talked to enough people."

**Sampling rigor (●●●).** If the demand read is survey-based: probability sampling makes margin of error meaningful; non-probability panels (the common case) technically can't carry a margin of error, though one is often reported anyway (misuse). Sample size for a proportion: n = z²·p(1−p)/ε² (≈385 for 95% confidence, ±5%). Representativeness is judged by post-weighting (raking) alignment to census benchmarks — but weighting only corrects *observed* variables, never unobserved attitude bias. State sample size, margin of error, and sampling method or the number is decoration.

**Pass conditions:** demand rests on behavior or an incentive-compatible test (real pre-sale/pilot/paid LOI, not signups); stated WTP is bias-corrected; discovery reached saturation; any survey states sample size, margin of error, and method.

---

## G3 — "Is the competitive read complete and the gap real?"

**Five Forces backed by hard data (●●●** for the framework's grounding, applied qualitatively**).** Industry attractiveness is structural, but each force must be tied to observable data — actual entrant counts and survival over 3-5yr, top-N buyer concentration, supplier switching costs in real terms — not "strong/weak" assertions. Cross-check: if long-run industry ROIC contradicts your attractiveness verdict, the read is wrong.

**HHI / CR4 with a properly-defined market (●●●).** Concentration has real thresholds: HHI <1,000 unconcentrated, 1,000-1,800 moderate, >1,800 highly concentrated (US DOJ); a merger adding >100 HHI points in a concentrated market triggers a presumption. But HHI/CR4 are meaningless if the market is mis-defined — so this gate depends on G0's boundary passing SSNIP. CR4 is insensitive to mergers among the top 4; HHI ignores demand elasticity and entry barriers.

**Positioning-axis objectivity (●●○).** Strategic-group / perceptual maps are only as good as their axes, chosen to be material (affects buyer choice and economics), variable (firms actually differ), and independent (axes not correlated, or the map collapses to a diagonal). The one real validity check: re-draw with different reasonable axes and confirm the clusters aren't an artifact. Perceptual maps via MDS get a quantitative fit statistic (stress); strategic-group maps don't.

**White-space validation (●●○).** A gap is an opportunity only if it survives two checks: (1) demand is verified (prospective users show real WTP, not just an unserved slot on a chart), and (2) no prior entrant already tried and failed there for a structural reason. "Competitors don't do it" ≠ opportunity — they may have exited it. Assumption-driven gaps are the trap.

**Landscape completeness (●○○).** No academic definition of "complete" exists. The working proxy: the competitor list converges across ≥3 independent source types (internal CRM/win-loss + review sites + analyst coverage), and diminishing returns are hit (new sources stop surfacing new competitors — a saturation analog). Structurally blind to stealth startups and future entrants; reframe as "current-date confidence + quarterly refresh," not completeness.

**Pass conditions:** competition includes substitutes (SSNIP/JTBD); concentration uses a validated market boundary; white space validated for demand and checked against failed entrants; completeness rests on multi-source convergence, stated as dated confidence not "complete."

---

## G4 — "Is coverage actually sufficient?" (the meta-gate)

**Saturation (●●●).** The strongest transferable stopping rule (see G2): track new insights — new competitors, segments, risks, themes — per batch of new sources, and stop when the rate falls near zero across a couple of consecutive independent batches. Quantifiable via the same (new ÷ base) ratio. This is the outward analog of "did we find all the causes," and it's the one coverage criterion with real numbers behind it.

**Reproducibility — PRISMA principle (●●●).** Coverage is credible when the search is documented well enough that a third party could re-run it and reach the same landscape. PRISMA/PRISMA-S don't mandate a source count; they mandate that the strategy be transparent and reproducible. "Could someone redo this scan?" is the objective test.

**Delphi for unknown-unknowns (●●●).** A structured anonymous expert panel surfaces what your sources structurally miss. Consensus is commonly defined as ~75% agreement, but note the honest finding: 71% of real Delphi studies actually stop on a pre-set round count, not on consensus — so pre-declare your stopping criterion (consensus threshold, item-drop rule, max rounds) or it degrades into "we ran out of time."

**Macro-coverage checklists — PESTEL / horizon scanning (●○○).** PESTEL (Political/Economic/Social/Technological/Environmental/Legal) and horizon scanning give *procedural* coverage — "every box has ≥1 evidenced item" — but a filled checklist doesn't prove you found each domain's key drivers, and horizon scanning has no outcome metric for completeness at all, only a process rhythm. Use them to avoid obvious blind spots; never report them as proof of completeness.

**Coverage error (●●○).** Formally, the sampling frame never perfectly matches the population (undercoverage/overcoverage); even a national census with 100k+ field staff misses addresses. There's no universal "acceptable coverage %" — so report the coverage gaps you know about rather than claiming none.

**Pass conditions:** saturation reached (new-insight rate documented near-zero across independent source types) OR what was not covered is explicitly logged with why; stopping on time/budget is stated plainly, never disguised as completeness.

---

## G5 — "Is the synthesis honestly graded and the forecast sane?"

**Confidence grading by evidence strength + independence (●●○).** Every key claim carries its grade (●●●/●●○/●○○) and a verified-vs-assumed label; a procedural-proxy finding must not inherit the confidence of a measured one. This is the discipline that keeps a defensible report from posing as a certain one.

**Reference-class forecasting — outside view first (●●●).** For any adoption/demand forecast, anchor on the distribution of comparable past launches (outside view) before the project's specifics (inside view). Kahneman's concept, Flyvbjerg's method, UK DfT-adopted (2004). Weight of evidence: ~90% of megaprojects overrun (the "iron law"). Caveat from the Edinburgh tram case — even reference-class forecasting underestimated a 2.4× overrun, so treat it as bias-reduction, not a guarantee.

**Bass diffusion + structured analogies (●●● model / ●●○ parameters).** Bass quantifies an adoption curve from an innovation coefficient p (≈0.01-0.03) and imitation coefficient q (≈0.3-0.5); the math is established, but results are highly sensitive to p, q, and market-potential m — so borrow p, q only from genuinely similar categories and re-fit once real sales arrive. Structured analogies: use ≥2 analogs (single-analog is a known trap), rate them on explicit comparability attributes, and prefer forecasters with direct experience of the analog.

**Calibration / probability ranges (●●●).** Express forecasts as probabilities and ranges, not point estimates, and (over repeated forecasts) check calibration — do your "70% likely" claims happen ~70% of the time? Tetlock's superforecasting work shows this is trainable and that ranges + updating beat confident point predictions. For a one-off bet, at least state the range and the assumptions that would move it.

**Reversibility bias (●●○, borrowed from diagnose-first).** Prefer a reversible market test (pre-sale, pilot, limited launch) that would confirm the estimate cheaply over a large irreversible commitment made on desk research. The honest deliverable for most market bets is "defensible range + the cheapest experiment that resolves it."

**Pass conditions:** claims graded and verified/assumed separated; forecast anchored on an outside view and expressed as a range; a reversible next test proposed over an irreversible bet where possible.