# game-ui-board-and-lane-layout — full rules and citations

Moved verbatim from SKILL.md by issue-100 progressive disclosure.
The SKILL.md body carries the rule index; read this file when a
matched rule's full text, citation, or counter-example is needed.

## Decision rules

1. When a board interaction is implemented as a drag or merge
   gesture (e.g. dragging a token from one cell to another, or
   dragging one token onto another to merge them), ship a
   single-pointer tap-then-tap alternative that reaches the same
   result without requiring a sustained drag — select the source,
   then select the destination.
   why: users relying on switch access, eye-gaze, or a tremor-affected
   pointer cannot reliably complete a sustained drag path, and some
   input devices cannot express a drag gesture at all.
   source: W3C WAI, "Understanding SC 2.5.7 Dragging Movements"
   (https://www.w3.org/WAI/WCAG22/Understanding/dragging-movements.html):
   "For any action that involves dragging, provide a simple pointer
   alternative," unless dragging is essential to the function or the
   movement is controlled by the user agent, not the author.
   counter-example: a freehand drawing or path-tracing mechanic where
   the drag path itself is the essential input (the shape drawn is
   the state, not just a means to relocate an object) is exempt —
   there is no equivalent tap-then-tap action that preserves the
   mechanic.

2. When a board cell or token is interactive (tappable, draggable, or
   selectable), size its hit target to at least 24x24 CSS px on any
   pointer-input surface, and increase that floor toward the 40-48px
   range used by touch-optimized reference layouts on touch-primary
   surfaces where fingers, not a precise pointer, are the input.
   why: below the 24x24 floor, WCAG 2.2 treats a pointer target as
   inaccessible to users with limited fine motor control; on touch
   surfaces, NN/g's research shows targets sized only to a pixel
   minimum still miss the physical finger-contact area needed to
   avoid mis-taps.
   source: W3C WAI, "Understanding SC 2.5.8 Target Size (Minimum)"
   (https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html):
   a target meets the requirement when "it must be conceptually
   possible to draw a solid 24 by 24 CSS pixel square... completely
   within the target," independent of zoom level.
   source: Nielsen Norman Group, "Touch Targets on Touchscreens"
   (https://www.nngroup.com/articles/touch-target-size/): "Interactive
   elements must be at least 1cm x 1cm (0.4in x 0.4in) to support
   adequate selection time and prevent fat-finger errors," and larger
   still for primary actions or mobile use in motion.
   counter-example: a target whose exact on-screen position is itself
   game state the player must read precisely (e.g. a miniature map
   overview where the token's pixel position, not its tap area, is
   the information) can stay below the floor per WCAG's "essential"
   exception, provided an equivalent full-size control exists
   elsewhere for interaction.

3. When defining a board's grid, derive cell size, gutter width, and
   overall board aspect ratio from one base grid unit (e.g. all
   spacing and sizing are multiples of a single value) rather than
   hand-tuning each dimension independently, so the whole board scales
   coherently when the viewport or a token's assigned size changes.
   why: independently tuned dimensions drift out of alignment the
   first time any one of them must change for a new viewport or
   device class, silently breaking cell/token alignment.
   source: W3C WAI, "Understanding SC 2.5.8 Target Size (Minimum)"
   (https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html):
   the 24x24 CSS-px floor is defined in viewport-independent CSS
   pixels specifically so a layout keeps meeting the floor "regardless
   of the content scale," which only holds if the layout's own units
   scale together from one base rather than independently.
   counter-example: a fixed, non-scaling board that targets exactly
   one known device class (e.g. a kiosk with a locked physical screen)
   does not need a derived-unit system — a single hard-coded layout is
   sufficient and adding a unit system would be unused complexity.

4. When lanes sit next to a HUD (score, timer, hand, resource
   counters), give the boundary between them one explicit spatial
   signal — a gap, a frame, or a container edge — so a player scanning
   the board never mistakes live board state for static chrome or
   vice versa.
   why: a pip or token rendered without a clear board/HUD boundary can
   be read as decorative interface furniture rather than actionable
   state, causing a player to miss it entirely.
   source: W3C WAI, "Understanding SC 2.5.8 Target Size (Minimum)"
   (https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html)
   — the criterion's underlying rationale that a target must be
   unambiguously identifiable and separable from surrounding content
   before its size even matters, extended here from single targets to
   the board/HUD region boundary as a whole.
   counter-example: a HUD element deliberately overlaid on the board to
   show a live effect on a specific lane (e.g. a targeting reticle) is
   not a violation of this rule — it is the boundary rule applied
   correctly in reverse, where the overlay is meant to read as bound to
   that lane, not as separate chrome.

5. When a pip or token count on a cell exceeds the number a player can
   subitize or reliably count at speed at the shipped cell size
   (commonly beyond 4-6 individual marks at small board-cell scale),
   switch the display to a numeral instead of continuing to add
   individual pips.
   why: past the point where a cell's rendered pips overlap or shrink
   below a legible size, the pip count stops being readable at a
   glance, which is the property pips exist to provide in the first
   place — a numeral restores at-a-glance legibility once pips can no
   longer do so.
   source: Nielsen Norman Group, "Touch Targets on Touchscreens"
   (https://www.nngroup.com/articles/touch-target-size/): once
   individual elements shrink below a size that "effectively
   communicate[s]" at the surface's actual scale, the visual encoding
   fails regardless of how much data it is asked to carry — applied
   here to pip legibility rather than tap area.
   counter-example: a fixed, small-range counter (e.g. a value that
   never exceeds 3) does not need a numeral fallback — pips stay
   legible across its entire possible range, so switching to a
   numeral would only add a second encoding for no legibility gain.

6. REMOVAL: when a board region already carries a border, a
   background tint, AND a separate card/frame around it to signal the
   same grouping or boundary, cut down to one signal rather than
   stacking all three on the same edge.
   why: redundant boundary cues compete for attention on a surface
   where the actual game state (cell contents, token position) is what
   the player needs to scan quickly; extra chrome slows that scan
   without adding information.
   source: W3C WAI, "Understanding SC 2.5.8 Target Size (Minimum)"
   (https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html)
   — the criterion's spacing exception treats a target's boundary as
   defined by an imaginary minimal circle, not by how many visual
   layers surround it, implying extra boundary layers add no
   accessibility value once one clear boundary already exists.
   counter-example: do not remove a lane's last remaining boundary
   signal if doing so leaves it visually fused to an adjacent lane —
   the rule targets redundant stacking, not the one boundary a lane
   still needs to read as distinct.

7. REMOVAL: when a lane renders on the board but never carries state
   that changes with play (no token ever occupies it, no counter tied
   to it ever updates), cut the lane rather than leaving it as
   decoration.
   why: a lane that looks interactive or state-bearing but never
   changes trains players to ignore board regions that do matter,
   since they cannot tell decorative lanes from active ones without
   testing each one.
   source: W3C WAI, "Understanding SC 2.5.7 Dragging Movements"
   (https://www.w3.org/WAI/WCAG22/Understanding/dragging-movements.html)
   — the criterion's own scope note that it applies only where
   "functionality" is actually present, establishing the same
   distinction this rule draws between an element that carries real
   interaction/state and one that only visually resembles one.
   counter-example: a lane reserved for a not-yet-unlocked mechanic
   (e.g. a locked slot visibly different from active lanes) is not a
   removal target — it communicates real future state, unlike an
   inert lane with no state at any point.

