# Study Note Skills

Codex skills for building complete, concept-first Chinese LaTeX/PDF study guides from course materials.

The suite uses `study-note-style-v1`, derived from the bundled `通用笔记模板.tex`: compact green/blue/cream layout, borderless clickable contents, Times New Roman for ordinary Latin text, XITS Math, a source-grounded core-knowledge map for 1–3 main sections or chapter map for 4 or more, and topic-separated page-breakable formula summary tables.

## Skills

- `auto-study-note-orchestrator`: inventories materials, batches long sources, drafts concepts first, dispatches specialists, integrates the canonical template, and runs final audit.
- `concept-outline-note-writer`: writes complete concept bodies with priority, scope, relations, cases, exam cues, and mistakes.
- `math-derivation-note-writer`: attaches source-faithful derivations and compact formula summaries to established concepts.
- `diagram-mechanism-note-writer`: rejects unnecessary visuals and creates the smallest justified chain, table, or TikZ figure.
- `coverage-audit-note-reviewer`: audits item-level coverage, layout, fonts, links, visual balance, compile logs, and PDF quality.

The canonical template and style package live under `auto-study-note-orchestrator/assets/`. Generated notes should copy both files instead of rebuilding the preamble.

## Install

Copy the skill folders into your Codex skills directory:

```powershell
Copy-Item -Recurse .\auto-study-note-orchestrator,.\math-derivation-note-writer,.\concept-outline-note-writer,.\diagram-mechanism-note-writer,.\coverage-audit-note-reviewer "$env:USERPROFILE\.codex\skills"
```

Then invoke:

```text
Use $auto-study-note-orchestrator to turn my selected course materials into a concept-first Chinese LaTeX/PDF study guide using study-note-style-v1.
```

The orchestrator automatically assigns content to specialist subagents by content type unless the user explicitly opts out.

## Validate a Generated Note

Compile with XeLaTeX on demand until the table of contents, bookmarks, and references are stable, then validate:

```powershell
python .\auto-study-note-orchestrator\scripts\compile_study_note.py `
  --tex '<output>\notes.tex'
python .\auto-study-note-orchestrator\scripts\validate_study_note.py `
  --tex '<output>\notes.tex' `
  --pdf '<output>\notes.pdf' `
  --log '<output>\notes.log' `
  --inventory '<output>\source_inventory.md'
```

The compiler starts with one pass and reruns only when needed. The read-only validator checks the canonical style marker, document order, relationship-map type or documented omission, formula-summary interface, A4 output, embedded Times New Roman and XITS Math resources, visible link borders, extractable text, compile blockers, and concept/visual counts.

There is no hard maximum-page setting for generated notes. The `80`, `120`, and `200` source-page thresholds trigger inventory, batching, and deeper coverage checks; the `source_pages / 8` and `25 pages for a 200+ page source` rules flag outputs that may be implausibly short unless the user asked for a compressed summary.

`auto-study-note-orchestrator/tests/multipage-toc-smoke.tex` is the regression fixture for multi-page contents, priority symbols, Latin/math/code fonts, and link borders.
