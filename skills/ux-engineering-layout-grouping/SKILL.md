---
axis: layout-grouping
rule_count_floor: 3
---

# Layout and grouping

Decision rules for proximity grouping, column layout, and label
placement, sourced from Gestalt grouping literature and form-layout
practitioner research actually fetched during issue #1174's
ux-engineering research pass (2026-08-13).

## Decision rules

1. When two or more fields are semantically related (e.g. city/state/
   zip, or start-date/end-date), place them with less vertical/
   horizontal whitespace between them than the whitespace separating
   them from the next unrelated field group — proximity alone should
   communicate the grouping before any border or label does.
   source: NN/g, "Gestalt Principle of Proximity" (fetched 2026-08-13,
   https://www.nngroup.com/articles/gestalt-proximity/): "Items close
   together are likely to be perceived as part of the same group" and
   "minimal spacing between a label and its corresponding input field
   establishes their relationship more clearly than larger margins."
   counter-example: do not tighten spacing between two fields that only
   look related by data type (two dropdowns) but are logically
   unconnected (a status filter and an unrelated language filter) — false
   proximity implies a relationship that doesn't exist and misleads scan
   order.

2. When a form has more than roughly 6-8 fields, split them into
   labeled sub-groups of 3-5 related fields each rather than presenting
   one long undifferentiated list — chunking keeps each group scannable
   as a unit.
   source: NN/g, "Gestalt Principle of Proximity" (fetched 2026-08-13,
   https://www.nngroup.com/articles/gestalt-proximity/): "a single
   12-field form appears overwhelming, whereas dividing those same
   fields into three meaningful groups (each containing 4 fields) feels
   manageable."
   counter-example: a short 8-field form that is already a single
   coherent concept (e.g. one address) should not be artificially
   split into sub-groups just to hit a "should chunk" heuristic —
   forcing group headers onto a form that has no natural seams adds
   noise, not clarity.

3. When a form's fields form one linear sequence with no independent
   sub-tasks, use a single-column layout, not a multi-column layout —
   default to single-column unless there is a specific, tested reason
   to break it.
   source: Luke Wroblewski, "Web Form Design: Filling in the Blanks"
   research, corroborated by CXL form-design study (fetched 2026-08-13
   via search results of
   https://www.lukew.com/resources/web_form_design.asp and
   https://cxl.com/blog/form-design-best-practices/): "users complete
   web forms from top to bottom, and forms with a simple vertical
   layout are always better than multi-column layouts... survey
   participants completed the linear, single-column form an average of
   15.4 seconds faster."
   counter-example: paired, tightly related short fields (e.g.
   month/year expiry, or city/state/zip on one physical line) can stay
   side-by-side on one row within an otherwise single-column form — this
   is a within-group exception Wroblewski's own research calls out, not
   a full multi-column layout.

4. When a form is short (roughly under 5 fields) or used repeatedly by
   an expert user who already knows the field order, place labels to
   the left of inputs to compress vertical space; when a form is longer
   or used by first-time/infrequent users, place labels above inputs so
   label and field can be read as one continuous top-to-bottom scan.
   source: Gestalt proximity guidance on label-to-field spacing
   (NN/g, fetched 2026-08-13,
   https://www.nngroup.com/articles/gestalt-proximity/) — "minimal
   spacing between a label and its corresponding input field
   establishes their relationship more clearly," which top-aligned
   labels satisfy more directly than left-aligned labels at a fixed
   column gap.
   counter-example: do not force top labels onto a dense repeated-entry
   table (e.g. a bulk line-item editor) just because it's "longer than
   5 fields" — a table's column headers already substitute for
   per-row labels, so top-label-per-row would duplicate information the
   table header already provides.

5. When grouped fields need a visible boundary because whitespace alone
   is not enough (e.g. dense enterprise UI with limited margin budget),
   use a subtle border or background-tint container rather than a hard
   rule/divider line — a soft container reads as one cohesive group
   without adding as much visual weight as boundary lines between every
   group.
   source: NN/g, "Gestalt Principle of Proximity" (fetched 2026-08-13,
   https://www.nngroup.com/articles/gestalt-proximity/), general
   grouping-signal guidance extended from the proximity-first case to
   the case where proximity alone is insufficient because space is
   tight.
   counter-example: in a very dense data-entry table where every row is
   already delimited by its own row lines, adding a further
   background-tint container per logical group can create competing
   visual boundaries — keep the table's existing row/column lines as
   the sole grouping signal instead.

6. REMOVAL: when a form's fields are already grouped by whitespace and
   a group also carries a redundant divider line, a background tint,
   AND a bordered card around it, cut down to just one grouping signal
   (usually whitespace, or whitespace plus one boundary treatment) —
   stacking three simultaneous grouping cues over the same set of
   fields adds visual noise without adding information.
   source: Adams, Converse, Hales & Klotz, "People systematically
   overlook subtractive changes," Nature 592 (2021) (fetched 2026-08-13
   via https://phys.org/news/2021-04-brains-opportunities.html summary)
   — the paper's core finding that people default to adding a fix
   (another boundary treatment) rather than checking whether removing a
   redundant one already solves the same problem, applied to
   over-boundaried grouping.
   counter-example: do not strip a group's only remaining boundary
   signal (e.g. its background tint) if removing it leaves the group
   indistinguishable from ungrouped surrounding fields — the removal
   rule targets redundant cues, not the last cue standing.

7. Prove a grouped layout's individual states — empty, loading, error,
   and populated — correct in isolation before assembling the group
   into a full screen; do not sign off on a group's layout using only
   its populated-with-sample-data state.
   rationale: a group's spacing, alignment, and grouping cues are often
   tuned against whatever sample data happened to be on hand, and only
   the populated state gets checked before handoff — the empty, loading,
   and error states then ship unreviewed and commonly break the same
   grouping logic (a group that looks correctly bounded with three rows
   collapses to an ambiguous sliver with zero).
   counter-example: a group with only one possible state (e.g. a static
   footer with no empty/loading/error variant) does not need the
   isolation pass — the rule applies where the state actually varies.

8. Before specifying a new component to fill a grouped layout's slot,
   check whether an existing component in the live library already
   covers the need, against the actual current library rather than
   assumed from memory of what it contained last time it was checked.
   rationale: a library drifts continuously as other work lands; a
   component believed absent may already exist under a different name,
   and a component believed reusable may have changed its contract
   since it was last used — specifying from a stale mental snapshot
   produces either a needless duplicate or a spec built against a
   contract the component no longer honors.
   counter-example: a slot with a requirement no existing component is
   even close to meeting (a genuinely novel interaction) does not need
   the lookup to conclude "build new" — the check is only wasted effort
   once the gap is already unambiguous.
