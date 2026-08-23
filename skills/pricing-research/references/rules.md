# pricing-research — full rules and citations

Moved verbatim from SKILL.md by issue-100 progressive disclosure.
The SKILL.md body carries the rule index; read this file when a
matched rule's full text, citation, or counter-example is needed.

## [S1] First: does this even need the procedure?

Run this gate before touching any method — the whole point of this skill is matching the method
to what the pricing decision needs, and skipping straight to a favorite technique (usually
conjoint, because it sounds rigorous, or PSM, because it's cheap) is exactly the failure mode this
skill exists to block.

- **Is the question actually about willingness to pay / price setting** — as opposed to "what do
  competitors charge for something similar"? The latter is competitor/market research. Route it to
  `market-recon` instead; this skill does not re-derive competitor pricing.
- **Is there a defined product or feature bundle whose attributes can be enumerated?** If nothing
  about the offer is fixed enough to list attributes and levels (or, for PSM, to describe the
  single concept respondents will price), it is too early for pricing research. Say so and stop —
  route back to product definition first.
- **Does the decision actually need primary research at all?** An existing number is adequate — and
  new fieldwork is not warranted — only if there is a prior study **on the same offer, covering the
  same price range, whose method passes Steps 2-5 of this skill**. Cost-plus figures and existing
  tiers are not WTP evidence and do not clear this check; they are internal constraints. If an
  adequate prior study exists, exit and say which study and why it qualifies.

Everything below applies only once a genuine WTP/pricing question is on the table, the offer is
enumerable, and no adequate number already exists.

## [S2] Evidence grade — read before citing this to anyone

This skill's spine is an asymmetry between two method families. State it precisely; do not
overstate it.

**The asymmetry, stated correctly**: conjoint's advantage is NOT "conjoint is validated and PSM is
not." It is that conjoint has a predictive-validity literature including a 2025 meta-analysis,
plus machine-checkable design gates (in CVA's case), while PSM has a fixed, cheap procedure whose
*interpretation layer* is not defended on theory even in the documentation of a vendor that sells
PSM tooling. For PSM, the honest
statement is: no validity study was found in this research, and the criticisms circulating in
vendor blogs failed independent verification — that is a coverage gap plus weak sourcing, not a
demonstrated absence of validity. None of what follows is RCT evidence that using either method
improves actual pricing outcomes.

**Conjoint lineage — CONFIRMED, three-part (NOT single-origin)**:
- Luce & Tukey (1964, *Journal of Mathematical Psychology* 1(1):1-27) — axiomatic conjoint
  measurement; the theory.
- Green & Rao (1971, *JMR* 8(3):355-363) — the marketing operationalization. Their own abstract
  calls conjoint measurement "a new development in mathematical psychology" and limits their
  contribution to applying "these techniques to illustrative problems in marketing." Their real
  contributions: the two-factor trade-off matrix collection method and non-metric part-worth
  estimation (MONANOVA). "Full-profile" is a later label (formalized in Green & Srinivasan 1978);
  Johnson (1974) is named as a parallel introducer. **REFUTED**: attributing conjoint's origin
  solely to Green & Rao 1971 — do not write that.
- Louviere & Woodworth (1983, *JMR* 20(4):350-367) — integration with discrete choice theory; the
  starting point of choice-based conjoint (CBC). Their own 1983 remark about limited external
  validity evidence is a self-assessment of that origin paper — cite it only as such, never as a
  grade of today's CBC.

**Taxonomy dispute — CONFIRMED, must be named whenever a conjoint-family method is chosen**:
Louviere, Flynn & Carson (2010, *Journal of Choice Modelling* 3(3):57-72, "Discrete Choice
Experiments Are Not Conjoint Analysis") argue that treating discrete choice experiments as a
special case of conjoint analysis is "a mistake" and that the CBC name is "potentially very
misleading" — the theoretical bases differ (random utility theory vs. conjoint measurement
theory); health economics journals dropped the conjoint label in the late 1990s. **Consequence for
this skill**: never grade CBC and rating-based conjoint on one shared "conjoint" evidence scale —
name which one is meant, every time.

**Conjoint predictive-validity evidence — CONFIRMED, with three mandatory qualifications (the most
misquotable finding here)**:
- *Marketing Letters* (2025) 36:533-546 meta-analysis: 134 effect sizes from 34 papers (working
  papers deliberately included as a publication-bias defense — never call it "34 published
  articles"), N=12,980 respondents (4,165 incentive-aligned / 8,815 hypothetical), scope limited to
  work from 2000 onward.
- Result: incentive alignment significantly increases predictive validity (β = 0.11, SE = 0.02,
  p < .001), reported by the authors as a ~12% **relative** increase in hit rate.
- **Qualification 1** (state whenever the 12% is cited): raw hit rates run the other way —
  incentive-aligned 48.26% vs. hypothetical 50.25%. The advantage appears only after controlling
  for chance level (14.60% vs. 22.76%); as improvement-over-chance it is 33.66% vs. 27.49% = 6.16
  percentage points. Citing "12% better" as an observable gap is a misreading.
- **Qualification 2**: the authors detected publication bias themselves (funnel-plot asymmetry
  test) and controlled for it with standard error as a moderator — the estimate is
  bias-corrected, not raw.
- **Qualification 3**: the authors qualify their own metric — hit rate is "sometimes criticized as
  an assessment of predictive validity."
- Cost datum: incentive alignment adds about $7.81 per participant (≈$2,343 at n=300).
- **REFUTED**: "individual-level estimation has significantly higher predictive validity than
  aggregate" — do not write that.

**Design gates — CONFIRMED, with a scoping caveat that must be honored**:
- Sawtooth's CVA software recommends 3× as many choice tasks as parameters (parameters = total
  levels − number of attributes + 1), but the manual itself says this ideal "often is not used in
  practice" and "some experienced conjoint analysts are willing to ask as few as 1.5x." The
  software's actual enforced gates are a **warning below 1.5×** and a **hard block below 1×** — 3×
  is an unenforced ideal, not a gate.
- Practical ceiling: "asking more than about 30 conjoint questions may result in poor quality
  data."
- Orthogonality: "Attributes must vary independently of each other to allow efficient estimation
  of utilities," while the same manual concedes "it might not be possible to create a perfectly
  balanced, orthogonal design"; Kuhfeld argues orthogonality is a pre-computational-era requirement
  and "a design does not have to be orthogonal to be efficient" — efficiency and unbiasedness are
  different properties. **REFUTED**: defining orthogonal design as the two-property combination of
  balance + orthogonality — do not write that.
- **SCOPING CAVEAT (must appear whenever these gates are cited)**: CVA is a legacy minority method
  (~2% of projects, ≤6 attributes) — its manual cannot stand as the standardization basis for
  conjoint in general. Present these as CVA's software gates specifically, and state that the
  general-case (CBC) gate argument would have to rest on CBC documentation, which this research did
  not establish. **REFUTED**: "full-profile is recommended only for ≤6 attributes and typical
  commercial practice violates design requirements" — do not write that.

**Van Westendorp PSM — CONFIRMED**:
- Origin: Peter H. van Westendorp, "NSS Price Sensitivity Meter (PSM)," 29th ESOMAR Congress,
  Venice, September 5-9 1976, pp.139-167. Do not call him an economist — unverified in independent
  primary sources.
- Operationalization (the whole of it): four price questions (too expensive / too cheap / getting
  expensive / bargain) → cumulative curves → four crossing points (PMC, PME, IPP, OPP).
- **The arithmetic fact that drives this skill's hardest gate**: basic PSM does not merely fail to
  optimize revenue or profit — it does not collect the inputs. No quantity, no purchase intent, no
  cost data, so revenue (price × quantity) is arithmetically incomputable from PSM data alone.
  OPP's "optimal" means minimal extreme-rejection, **not** an economic optimum.
- Crossing-point criticism, verified only in this narrow form: Sawtooth — a vendor that sells PSM
  tooling — states in its own documentation that the "line-crossing approach has largely been
  criticized and discredited as lacking good theory" (medium grade). It is one vendor's
  documentation, not an admission by PSM's proprietor; do not upgrade it.
- **REFUTED THIS ROUND — must NOT appear**: "PSM has no theoretical foundation," "no published
  explanation of its theory exists," "PSM has no track record of predictive validity," "PSM
  produces guidance that resists empirical validation," "PSM assumes linear price perception and
  ignores brand/quality/market trends." All of these failed verification; they were vendor-blog
  assertions. The correct statement is: no PSM validity study was **found** in this research, and
  even the vendor does not defend the crossing-point interpretation layer — but absence of found
  evidence is not proof of absence. Never write "PSM has no validity evidence."

## [S3] Report format

Report, per pricing study:

- Step 1: scope gate result (proceed / routed to `market-recon` / exited as too early / exited —
  adequate number already exists, with the qualifying study named).
- Step 2: which input the decision needs (quantity / purchase intent / cost / none of these), and
  the method chosen because it collects that input.
- Step 3 (conjoint-family only): the named family (CBC vs. rating-based conjoint) and the taxonomy
  dispute noted.
- Step 4: attributes and levels, computed parameters, task count, and the ratio. For CVA-style
  designs, which gate band it falls in (blocked / warned / ideal-not-met / clear). For CBC, the
  ratio as a reference figure only, with the statement that no CBC-general gate was established —
  never a band verdict.
- Step 5: the incentive-alignment decision, its cost, and — if the meta-analytic benefit is
  cited — all three qualifications alongside it.
- Step 6: the numbers with their labels (PSM crossings labeled as perception thresholds; conjoint
  utilities/shares labeled per the model that produced them) and the residual list of what the
  method cannot answer.
- The evidence-grade asymmetry restated briefly: conjoint has a predictive-validity literature
  (2025 meta-analysis) plus machine-checkable design gates (CVA-specific); PSM has a fixed, cheap
  procedure whose interpretation layer even its vendor won't defend on theory, and no validity
  study was found (a coverage gap, not a demonstrated absence). Neither is RCT evidence that the
  method improves actual pricing outcomes.

Match the report's weight to the decision's weight:

- **High-stakes** (revenue-critical launch, multi-year contract, method-family debate materially changes the number): full per-step report format below.
- **Directional / early-stage**: the six numbered elements from Step 6's gate plus the evidence-grade asymmetry note are sufficient — the per-step walkthrough is not required.

In all cases the number must be traceable to a named method and family, a stated set of inputs it actually collected, and gates that were checked before the number was trusted. State explicitly which format you used and why, so the reader knows whether a compressed report reflects low stakes or omitted procedure.

## [S4] Related skills

- [pricing-method-family](../pricing-method-family/SKILL.md) — route back to method-family first if the family choice (PSM vs. conjoint) itself is still open.

