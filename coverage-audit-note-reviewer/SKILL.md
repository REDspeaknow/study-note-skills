---
name: coverage-audit-note-reviewer
description: Audit study-guide LaTeX/PDF outputs for item-level source coverage, concept-first balance, canonical study-note-style-v1 layout, embedded fonts, borderless links, compilation quality, justified visuals, and final completeness.
---

# Coverage Audit Note Reviewer

## Purpose

Review a generated study guide against the source inventory and compiled PDF. Catch omissions, skipped derivations, broken LaTeX, unreadable text, workflow-artifact leakage, style drift, font/link regressions, and unjustified visual expansion before delivery.

Read `references/audit-protocol.md` before auditing any full chapter or course-range guide.

This skill is item-level and gate-driven. For canonical notes, also read the orchestrator's `references/style-contract.md` and inspect the output of `scripts/validate_study_note.py`.

## Audit Statuses

Mark every inventory item as:

- `represented`: directly covered with the row's required body treatment; an inherently formula- or visual-specific row may use its artifact only when adjacent explanatory prose is present.
- `represented indirectly`: covered under another title or integrated into a broader section.
- `intentionally omitted`: duplicate review, administrative, outside scope, or explicitly excluded.
- `missing`: substantive content absent from the output.
- `resolved after revision`: previously missing or weak content that has been added and verified.

## Pass/Fail Gates

For long sources, require separate item-level inventory, batch plan, mini-audits, global audit, and count summaries. Reject broad page-range coverage claims.

For `study-note-style-v1`, require all three gates:

- **Layout:** canonical style marker and required section order; a core-knowledge map for 1–3 main sections or chapter map for 4 or more, after the table of contents, unless a specific source-grounded omission reason is recorded; topic-separated page-breakable formula tables; no unrequested workflow artifacts in the final PDF.
- **Technical:** A4 PDF, extractable text, embedded Times New Roman and XITS Math, zero-width link borders, no missing-font substitution or unresolved references.
- **Content balance:** every substantive concept has prose body coverage; every visual has a valid reason, source cue, coverage ids, and adjacent concept section; no visual is decorative, duplicate, guessed, or sole coverage.

## Rules

- Missing substantive content must be fixed or clearly reported.
- Do not accept a table of contents as proof of coverage; search the extracted PDF text.
- Do not accept coarse page-range coverage claims for long sources; require item-level rows from the source inventory.
- For sources over 120 PDF pages, report source page count, final PDF page count, inventory row count, and batch count. Treat a very short final PDF as a coverage failure unless the user asked for a compressed summary.
- If the user supplies a missing-topic list or screenshot, require a `gap_backlog.md` or equivalent closure table and mark the audit `revise` until every source-supported gap is explicitly covered.
- Do not accept a parent section as coverage for a named subtopic. Named models, subresults, parameter effects, empirical conflicts, and policy tools require explicit body text, table rows, formulas, or cross-references.
- Do not accept a table, diagram, formula sheet, glossary entry, or box as the sole coverage for a substantive concept.
- Process artifacts such as inventories, batch plans, mini-audits, and global audits should not appear as numbered final-PDF study-guide sections unless explicitly requested.
- Check derivations for setup, notation, intermediate algebra, final result, and intuition; long derivations must not be trapped in boxes.
- Check diagrams for eligibility, point placement, arrows, labels, source cues, adjacent concept references, redundancy, and convention consistency.
- For the overview map, verify that its type matches the main-section count, every node resolves to body prose, every edge has an evidence-backed relation label, the map remains legible, and it is not counted as sole concept coverage. If omitted, verify the recorded reason against the source.
- For the final formula summary, verify topic grouping, repeated three-column headers, body provenance for every row, and a specific applicability/use/warning cell. Reject long derivations or new formulas introduced only in the summary.
- Treat visible link borders, absent required fonts, missing style marker, wrong end-matter order, and font-substitution warnings as blockers for canonical notes.
- Treat LaTeX errors as blockers. Treat warnings as review items unless harmless and content is verified.

## Output Contract

Return:

- Coverage audit table or compact status list with item-level statuses.
- Compile/PDF QA summary.
- Layout, technical, and content-balance gate results.
- Long-source gate and final-PDF cleanliness status when applicable.
- Missing or weak sections to fix.
- Intentional omission notes.
- Final pass/fail recommendation.
