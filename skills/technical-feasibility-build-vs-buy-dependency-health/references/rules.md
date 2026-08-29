# technical-feasibility-build-vs-buy-dependency-health — full rules and citations

Moved verbatim from SKILL.md by issue-100 progressive disclosure.
The SKILL.md body carries the rule index; read this file when a
matched rule's full text, citation, or counter-example is needed.

## Rules

1. **when** grading a candidate dependency's ongoing maintenance
   **choose** run the OpenSSF Scorecard `Maintained` check (activity
   and maintenance status of the project) rather than eyeballing the
   commit graph — it is the automated, comparable signal this skill's
   evidence bar requires (`check-name score` citation format).
   source: "The Maintained check checks the activity and maintenance
   status of the project" — OpenSSF Scorecard checks documentation
   (https://github.com/ossf/scorecard/blob/main/docs/checks.md).

2. **when** grading a candidate dependency's contribution-quality
   controls **choose** the `Code-Review` check (does the project
   require human review before merge) as a distinct evidence line from
   `Maintained` — review-gating catches a different failure class
   (unintentional bugs/vulnerabilities merged unreviewed) than raw
   activity does, so the two must be scored and cited separately, not
   folded into one "looks healthy" verdict.
   source: "This check determines whether the project requires human
   code review before pull requests ... Reviews detect various
   unintentional problems, including vulnerabilities" — OpenSSF
   Scorecard checks documentation
   (https://github.com/ossf/scorecard/blob/main/docs/checks.md).

3. **when** a candidate dependency scores well on Scorecard but the
   record cites only the aggregate score **choose** reject the
   citation and require per-check breakdown (which named checks,
   which scores) — the skill's own evidence-citation rule requires
   `check-name score`, singular check named, not an aggregate number
   that hides which specific control passed or failed.
   source: docs/specs evidence-citation directive, this skill spec's
   `evidence-citation` module — evidence-citation/hooks/directive.sh
   (this repo).

4. **when** comparing build vs. buy for a capability the spec needs
   **choose** treat "buy" (adopt an existing dependency/vendor) as the
   default candidate to evaluate first, and require the record to
   state per-dependency health evidence before "build" can be chosen —
   the skill's own probe requirement is a build-vs-buy comparison WITH
   per-dependency health evidence, not a build-first assumption.
   source: feasibility skill directive (this repo,
   feasibility/hooks/directive.sh): "prior_art: a build-vs-buy
   comparison with per-dependency health evidence, OpenSSF-Scorecard-
   or-equivalent (skill: build-vs-buy)".

5. **when** no OpenSSF Scorecard run exists for a candidate dependency
   **choose** run one before citing it, rather than substituting a
   GitHub star count or a blog post's opinion — stars and popularity
   are not maintenance-health signals and do not satisfy the
   `check-name score` evidence shape this skill requires.
   source: OpenSSF Scorecard project description, "OpenSSF Scorecard
   assesses open source projects for security risks through a series
   of automated checks" — OpenSSF Scorecard homepage
   (https://scorecard.dev/); evidence-citation directive, this repo.

6. **when** two candidate dependencies are close on Scorecard but one
   has a known unpatched vulnerability in its `Vulnerabilities` check
   **choose** the one without the open vulnerability even if its other
   checks score marginally lower — an unpatched-vulnerability signal
   is a direct, present risk and outweighs a marginal aggregate-quality
   difference.
   source: OpenSSF Scorecard checks documentation lists
   `Vulnerabilities` as a distinct check alongside `Maintained` and
   `Code-Review`
   (https://github.com/ossf/scorecard/blob/main/docs/checks.md).

7. **when** a "build" option is chosen over "buy" **choose** require
   the record to name the specific health gap in the rejected buy
   candidate (which check failed, what score) as the one-line
   rejection reason — a bare "not chosen" note does not satisfy the
   plural-candidates-with-cited-reason discipline this skill's proposal
   phase already applies to architectural options.
   source: MADR options-considered discipline (this session's
   SessionStart hook, rule 2: "One-line rejection reason per
   candidate ... 'Not chosen' or similar content-free filler does not
   satisfy this") — MADR options-considered discipline directive.

8. **when** the candidate is a SaaS vendor rather than an open-source
   dependency and Scorecard does not apply **choose** substitute the
   closest equivalent evidence: the vendor's published SLA/uptime
   history and incident-disclosure record, cited by URL, not a bare
   "reputable vendor" assertion — the evidence bar (`<claim> — <source>`)
   applies regardless of whether the candidate is a repo or a service.
   source: evidence-citation directive, this repo
   (evidence-citation/hooks/directive.sh): "no bare assertions."

9. **when** a dependency's Scorecard `Maintained` check is currently
   passing but the record only checked it once **choose** note the
   check date in the citation (the score is a point-in-time read, not
   a durable property) — a stale Scorecard citation misrepresents an
   automated check's output as more current than it is.
   source: check-name-score citation-shape requirement, evidence-
   citation directive, this repo.

10. **REMOVAL — when** a dependency candidate has been superseded by
    the vendor's own successor project (deprecated upstream, migration
    guide published) **choose** drop it from the comparison table
    entirely rather than carrying it forward as a scored-but-rejected
    row — a deprecated candidate is not a live tradeoff, and keeping
    it in the table dilutes the comparison with a foregone-conclusion
    row.
    source: MADR carry-forward rule permits dropping a candidate only
    with an explicit `dropped: <reason>` — deprecation-by-vendor is
    the canonical case for that explicit drop, not silent
    disappearance (this session's SessionStart hook, MADR discipline).

11. **when** scoring a candidate dependency's health **choose**
    calibrate the bar to the consuming project's own maturity/stage
    (a pre-launch prototype vs. a production system under compliance
    obligations) rather than applying one fixed pass/fail bar to every
    project — the same Scorecard evidence can be an acceptable risk
    for an internal prototype and a disqualifying one for a
    regulated production system, and a single fixed bar either
    over-blocks the prototype or under-protects the production case.
    source: survey of maturity-adaptive scoring tools — adaptive
    scoring adjusts its pass bar to the project's detected maturity
    level rather than scoring every project against one fixed
    template, and requires every finding to carry a source link
    rather than a bare severity label.

