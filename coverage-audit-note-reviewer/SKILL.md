---
name: coverage-audit-note-reviewer
description: Audit compiled LaTeX/PDF study guides against source course materials and source inventories. Use when Codex needs to verify no substantive knowledge points were omitted, inspect LaTeX compile logs, confirm PDF text extraction, review table of contents and glossary coverage, check formulas, diagrams, and boxes, and produce missing-item fixes or omission notes.
---

# Coverage Audit Note Reviewer

## Purpose

Review a generated study guide against the source inventory and compiled PDF. The goal is to catch omissions, skipped derivations, broken LaTeX, unreadable Chinese text, and diagram or coverage failures before delivery.

Read `references/audit-protocol.md` before auditing any full chapter or course-range guide.

## Audit Statuses

Mark every inventory item as:

- `represented`: directly covered in a section, formula, table, figure, glossary, or checklist.
- `represented indirectly`: covered under another title or integrated into a broader section.
- `intentionally omitted`: duplicate review, administrative, outside scope, or explicitly excluded.
- `missing`: substantive content absent from the output.

## Rules

- Missing substantive content must be fixed or clearly reported.
- Do not accept a table of contents as proof of coverage; search the extracted PDF text.
- Do not accept coarse page-range coverage claims for long sources; require item-level rows from the source inventory.
- For sources over 120 PDF pages, report source page count, final PDF page count, inventory row count, and batch count. Treat a very short final PDF as a coverage warning unless the user asked for a compressed summary.
- If the user supplies a missing-topic list or screenshot, require a `gap_backlog.md` or equivalent closure table and mark the audit `revise` until every source-supported gap is explicitly covered.
- Do not accept a parent section as coverage for a named subtopic. Named models, subresults, parameter effects, empirical conflicts, and policy tools require explicit body text, table rows, formulas, or cross-references.
- Process artifacts such as inventories, batch plans, mini-audits, and global audits should not appear as numbered final-PDF study-guide sections unless explicitly requested.
- Check derivation sections for skipped algebra.
- Check diagrams for point placement, arrows, labels, and convention consistency.
- Treat LaTeX errors as blockers. Treat warnings as review items unless harmless and content is verified.

## Output Contract

Return:

- Coverage audit table or compact status list.
- Compile/PDF QA summary.
- Missing or weak sections to fix.
- Intentional omission notes.
- Final pass/fail recommendation.
