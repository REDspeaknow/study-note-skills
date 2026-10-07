# Audit protocol

## Inputs

Read the requested scope, available sources, inventory, plan, bodies/handoffs, `issues.json`, consolidated coverage report, final TeX/PDF and technical reports. If only a prior note exists, audit preservation relative to that note and the inventory, not the unavailable original course material.

## Coverage and correctness

1. For each substantive inventory ID, locate the actual teaching passage and record its section/label. Use the handoff contract's exact status values: `represented`, `represented-indirectly`, `intentionally-omitted`, `weak`, or `missing`. A keyword match is a search aid only.
2. For major models, compare setup, symbols, equilibrium/result, necessary algebra, and boundary conditions with available evidence. Later results may inherit a setup already established.
3. Check whether the reader can answer the unit's central question without reading repeated restatements.
4. Inspect visuals for valid source cues, meaningful placement, readable labels, and correct axes/arrows/intersections. Reject decorative or duplicate figures.
5. Check issue closures against the cited corrections and acceptance reasons, using `study-note-unit-writer/references/unit-writing.md`. Structural accounting cannot establish teaching quality; open gaps prevent completion, and accepted limitations must appear in the delivery note.

## Repetition and retrieval

Read neighboring sections and the end matter together. Highlight repeated definitions, reused setup, parallel case narratives, prose that merely reads back a table, long captions that restate the surrounding text, and boxes/exam tips that restate the same conclusion. Preserve any unique condition or exception when consolidating.

Inspect unit handoffs. A formula candidate is a nomination, not required output. Check duplicate keys and conflicting conditions. In the final TeX, unit fragments contain no FormulaSummaryTable or document-level summary sections; at most one formula-reference section follows the main chapters, with topic tables if useful. Reject intermediate algebra, worked substitutions, and numerical-example steps from that reference. Every retained row points to a body explanation.

## Technical QA

Run the compile helper and validator. Confirm A4, embedded configured fonts, extractable Chinese text, clickable borderless links, no unresolved references or missing glyphs, and sensible page breaks. Render representative concept, derivation, visual, formula-reference, and final pages. A low or high page count triggers editorial inspection, not an automatic verdict.

## Output

Return a compact table of actionable findings with source ID, body location, problem, and correction. State what evidence was unavailable. Finish with pass, pass with notes, or revise. Do not mark a guide complete merely because inventory titles appear in PDF text.
