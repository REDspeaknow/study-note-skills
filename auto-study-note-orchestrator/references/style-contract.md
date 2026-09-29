# Study Note Style Contract v1

Read this reference whenever a complete `.tex` document is created, integrated, or audited.

## Canonical Assets

Copy both files from `assets/` into the output project before drafting:

- `通用笔记模板.tex`: the canonical document skeleton and section order.
- `study-note-style.sty`: the only source of typography, colors, spacing, boxes, priority symbols, and hyperlink behavior.

Start from the template instead of rebuilding a preamble. Do not duplicate or locally redefine its colors, fonts, heading formats, priority symbols, or boxes unless the user explicitly requests a different style.

The required style marker is `study-note-style-v1`, exposed as `\StudyNoteStyleVersion`.

## Typography and Links

- Compile with XeLaTeX.
- Chinese body: FandolKai; explicit Chinese bold: FandolHei-Bold.
- Latin titles, body, table text, captions, and table of contents: Times New Roman.
- Mathematics: XITS Math.
- Code: the configured monospaced font; code is the only ordinary Latin-font exception.
- Use `\PriorityMust`, `\PriorityImportant`, and `\PriorityKnow`; never type literal Unicode stars as priority markers.
- Keep `hyperref` in `hidelinks` mode. Table-of-contents links remain clickable but must have zero-width borders and unchanged text color.

## Required Document Order

1. Compact title block, priority legend, and reading order.
2. Clickable borderless table of contents.
3. A source-grounded relationship map: core knowledge for 1–3 main sections; chapters for 4 or more.
4. Main chapters.
5. Topic-separated formula summary tables.
6. Memorization-priority overview.
7. Global common-mistakes section.
8. Closing line.

Count substantive main sections before `公式速查手册`. With 1–3 sections, place a compact `核心知识关系导图` after the table of contents: nodes are key concepts or mechanisms with explicit targets in the body. With 4 or more sections, use `各章节关系导图`: nodes name real body chapters. Use the reusable `study map ...` TikZ styles from `study-note-style.sty`. Every edge must state a source-supported prerequisite, extension, cause, assumption failure, remedy, or other meaningful relation. Do not infer attractive but unsupported links. If the source supports no meaningful relationship, omit the map and write `% study-map-omitted: <specific reason>` in the TeX for audit. Either map is navigation and synthesis, not concept coverage.

In `公式速查手册`, divide formulas into meaningful topic subsections and use `FormulaSummaryTable` plus `\FormulaSummaryRow`. The table must be page-breakable, repeat its header, and use the columns `公式名称`, `公式`, and `适用条件、用途或注意事项`. Include only formulas already explained or derived in the main body. Put priority, assumptions, variable meaning, test hypothesis, distribution, or common trap in the third column; never paste full derivations into the table.

## Concept-First Content Contract

Every substantive concept must have prose coverage before any dependent formula, table, or diagram. A complete key-concept block contains:

1. Definition.
2. Why it matters.
3. Conditions, assumptions, or scope.
4. Relation to adjacent concepts.
5. Source example or case when present.
6. Exam cue.
7. Common mistake.

Use the priority macros to mark key concepts. Tables, formulas, figures, glossary entries, and formula-sheet entries supplement this body coverage; none of them counts as the sole representation of a concept.

## Visual Eligibility Gate

Default to no new visual. Set `visual_needed: yes` only when at least one of these reasons applies:

- `source-essential`: the source contains a graph or figure whose geometry, axes, or movement is examinable.
- `mechanism-essential`: a spatial, temporal, or equilibrium mechanism would be materially harder to understand in prose.
- `comparison-efficient`: a compact table removes substantial repetitive prose across genuinely comparable items.
- `user-requested`: the user explicitly asks for a more visual treatment.

Every accepted visual must record `visual_reason`, coverage item ids, its adjacent concept section, and a short QA note. Reject decorative, duplicate, guessed, or coverage-only visuals. A visual must not appear before its concept explanation.

The overview map is the one front-matter exception to the adjacency rule because the user explicitly requested it as a navigation overview. It still requires `visual_reason: user-requested`, a node-to-body-target list, an edge-evidence list, and a QA note. Its concepts must be explained later in the body.

Keep boxes short. Use them for definitions, takeaways, final formula summaries, and mistakes. Keep long derivations and cases in ordinary breakable prose even though the box environments themselves support page breaks.

## Integration and QA

Compile on demand until references are stable, then run:

```powershell
python scripts/compile_study_note.py --tex '<output>/notes.tex'
python scripts/validate_study_note.py `
  --tex '<output>/notes.tex' `
  --pdf '<output>/notes.pdf' `
  --log '<output>/notes.log' `
  --inventory '<output>/source_inventory.md'
```

The validator is read-only. It checks the style marker, document order, relationship-map type and position, topic-separated formula-table interface, A4 size, embedded Times New Roman and XITS Math fonts, visible link borders, extractable text, blocking log messages, and reported concept/visual counts. Visual counts are diagnostic rather than a fixed quota; the orchestrator decides whether every visual is justified, with an independent semantic challenge from ChatGPT when `$codex-with-chatgpt` is active.
