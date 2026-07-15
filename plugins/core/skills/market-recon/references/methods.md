# Method Details — how to actually run each market-recon tool

The procedure names methods; this file is the how-to. Read the entry you need when you reach the stage that uses it. Grouped by stage.

## Stage 0 — Boundary

**SSNIP test (hypothetical monopolist).** Provisionally set a candidate market. Ask: if one firm monopolized it and raised price ~5% non-transitorily, would enough buyers switch to outside alternatives to make the rise unprofitable? If yes, add those alternatives to the market and repeat until the rise would hold. Uses critical-loss / recapture-rate logic. Needs cross-price elasticity data; approximate qualitatively if you lack it.

**Jobs-to-be-Done boundary.** Ask what job the customer hires the product to do, then list everything they'd hire instead — including doing nothing and manual workarounds. Those are your real competitors and market edge. (Milkshake case: competitors were bananas/bagels/boredom, not other shakes.)

## Stage 1 — Sizing

**TAM / SAM / SOM.** TAM = total category if you had 100% (a ceiling, never a target). SAM = the slice your business model can actually serve (geography, segment, regulation). SOM = what you can realistically win in 3-5 yr given competition and execution. State your definitions — even VCs don't agree on the exact boundaries.

**Bottom-up sizing (preferred).** Define the target segment precisely → count customers from census/industry/competitor-filings data → set price (value-based / competitive / cost-based) → multiply for per-customer revenue → sum across segments → project by year using realistic new-customer acquisition and retention. Every step is independently checkable — that's why it's defensible.

**Top-down sizing (cross-check only).** Industry total (gov stats / analyst reports) × target-segment % × assumed share %. The final share step is the weak link — never let it stand alone.

**Triangulation.** Estimate the same size ≥2 *independent* ways (e.g., bottom-up demand vs. supply-side revenue sum vs. expert interviews) and check order-of-magnitude convergence. Confirm the sources don't secretly share one origin (that's circular citation, not triangulation).

**Fermi estimation.** Decompose to sub-components, use round numbers (false precision adds error, not accuracy), multiply/sum, then sanity-check against a known ceiling (population, total spend) and present a range. Zero-check obsessively — a factor-of-ten slip is the most common sizing failure.

**Profit / value pool.** Map revenue AND profit separately across the value chain — profit concentration often differs from revenue concentration. The pool worth entering is where profit, not revenue, concentrates.

## Stage 2 — Demand

**The Mom Test.** Three rules: talk about their life, not your idea; ask about specific past actions, not hypothetical futures; talk less, listen more. Good question: "what did you do last time this problem came up, and did you pay for anything?" Void question: "would you use this if it existed?"

**Customer discovery.** Document falsifiable hypotheses with pass/fail criteria before interviewing; interview to saturation (new conversations stop surfacing new themes); look for early evangelists who already spend time/money hacking a solution — that's real demand.

**Van Westendorp PSM.** Four price questions (too cheap / cheap / getting expensive / too expensive); plot cumulative curves; intersections give the acceptable range and optimal price point. Downsides: direct-question underreporting, ignores competitors/other attributes, no volume/profit prediction — pair with the NMS extension for demand.

**Gabor-Granger.** Ask purchase intent at several set prices (adaptively bracketing up/down); build a demand curve and a revenue curve; the revenue-max price is computable. Prone to hypothetical bias and price anchoring.

**Conjoint / MaxDiff.** Present bundles of attributes-with-levels (or best/worst item choices); statistically decompose the relative utility of each attribute including price. Sample-size rule of thumb (CBC): n ≈ (levels × tasks × alternatives) / 500 for adequate exposure. Validate with hold-out tasks. Powerful but needs experimental-design expertise.

**Hypothetical-bias correction.** Discount stated WTP toward revealed WTP — average overstatement ~21%, more for specialty/high-price goods. Use cheap-talk scripts (warn respondents people overstate) and certainty-scale recoding (drop low-certainty "yes" to "no") to shrink it. Best of all: validate with an incentive-compatible test (real pre-sale/pilot).

## Stage 3 — Competition

**Porter's Five Forces.** Rate five forces — new entrants, supplier power, buyer power, substitutes, rivalry — each tied to observable data (entrant counts/survival, buyer concentration, real switching costs). Weak forces = attractive structure. Define the industry boundary first (via SSNIP), or the whole analysis warps.

**SWOT (use with caution).** Widely used, heavily criticized as subjective and unfalsifiable (the same fact can be "strength" or "weakness"). If used: attach evidence to every item (drop unsupported ones), state facts as specific events not vague conditions, keep desires out of "strengths," and convert to a TOWS matrix (SO/WO/ST/WT) so items map to actions.

**Strategic-group / perceptual map.** Pick two axes that are material, variable, and independent; operationalize each as an observable metric; plot firms with bubble size = share; label clusters; identify mobility barriers and empty space. Re-draw with different axes to confirm clusters aren't an artifact. Perceptual maps via MDS carry a stress fit-statistic.

**White-space analysis.** Scan customer pain points and unmet needs → benchmark competitor offerings to find saturated vs. empty areas → for each gap, verify demand (real WTP) and check for prior failed entrants and structural barriers → size the opportunity → validate with prospects before treating it as real.

**HHI / CR4.** CR4 = sum of top-4 shares. HHI = Σ(share%)². Thresholds: HHI <1,000 unconcentrated, 1,000-1,800 moderate, >1,800 concentrated. Requires a correctly-defined market; ignores demand elasticity and entry barriers.

**Blue Ocean strategy canvas / ERRC.** Plot value curves (competing factors × offering level) for you vs. rivals; use the Six Paths framework to source factors systematically; build an Eliminate-Reduce-Raise-Create grid — and check all four quadrants are populated (raise/create only = overengineering). Good strategy shows focus, divergence, and a one-line tagline.

## Stage 4 — Coverage

**Saturation tracking.** Pre-set a base-set size and a run length; compute (new themes/competitors/risks in run ÷ base-set count); stop when it falls below your threshold (≤5% ≈ light coverage, 0% ≈ thorough) across consecutive runs. The one coverage rule with real numbers.

**PRISMA reproducibility.** Document search sources and exact queries so a third party could re-run and reach the same landscape; search multiple source types (single source ≠ complete); include grey literature and citation-chasing. The test is reproducibility, not a source count.

**PESTEL / horizon scanning.** Fill Political/Economic/Social/Technological/Environmental/Legal with evidenced items; scan fringe areas for weak signals on a regular cadence. Procedural coverage only — a filled grid isn't proof; report it as "no obvious blind spots," never "complete."

**Delphi.** Anonymous expert panel, multiple rounds; round 1 open-ended (surfaces unknown-unknowns), later rounds converge with group feedback. Pre-declare the stopping rule (consensus % — commonly ~75% — item-drop rule, max rounds) since most studies otherwise just stop on round count.

## Stage 5 — Synthesis & forecast

**Reference-class forecasting.** (1) Identify comparable past launches/projects; (2) build the distribution of their actual outcomes (overrun %, adoption, share); (3) place your case on that distribution (usually adjust toward the base rate + add contingency). Outside view before inside view. ~90% of megaprojects overrun — expect it.

**Bass diffusion model.** Cumulative adoption from innovation coefficient p (≈0.01-0.03) and imitation coefficient q (≈0.3-0.5) over market potential m. Borrow p, q from genuinely similar categories; re-fit from early real sales. Highly sensitive to p, q, m — pair with a TAM check on m.

**Structured analogies.** Use ≥2 analogs (never one), rate them on explicit comparability attributes (size, price, distribution, tech-lifecycle stage), weight by similarity, and prefer forecasters who lived the analog. Beware hidden decisive differences (regulation, psychology).

**Pre-sale / pilot / test market validation.** Before full launch: landing page + real payment/deposit (not email signup) for conversion; limited-region test market for real sell-through; pilot cohort for repeat/churn. Compare the actuals to your bottom-up assumptions, Bass p, and analog forecast, and recalibrate. Distinguish real payment from mere "interest" — the latter massively overstates demand.

**Forecast accuracy (MAPE etc.).** After outcomes arrive, measure error to build a track record: MAPE (%-standardized, but distorted for low-volume items — use WAPE there), plus a separate bias check (over/under-forecast direction). Realistic targets vary by item — don't hold every forecast to one threshold. Can't be applied to a true first-of-kind forecast (that's what reference-class/analogs are for).