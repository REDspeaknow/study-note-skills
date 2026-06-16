---
name: auto-study-note-orchestrator
description: Build complete Chinese LaTeX/PDF study and review guides from user-specified lecture PDF, slide deck, notes, or course ranges. Use when Codex needs to inventory all course materials, automatically split long course ranges into safe batches, classify concepts into textual knowledge, mathematical derivations, mixed sections, diagrams, mechanisms, tables, and cases, automatically delegate sections to specialist subagents by default when available, integrate a full LaTeX handout, compile it, and audit coverage so substantive knowledge points are not omitted.
---

# Auto Study Note Orchestrator

## Purpose

Turn a user-specified range of course materials into a complete Chinese LaTeX/PDF study guide. The default language is Chinese. Add English labels for concepts, keywords, or variable names only when the user explicitly asks for English annotation.

This skill coordinates specialist skills:

- `$math-derivation-note-writer` for derivations, proofs, formulas, and calculation procedures.
- `$concept-outline-note-writer` for definitions, textual knowledge, comparison tables, and exam-oriented summaries.
- `$diagram-mechanism-note-writer` for mechanism chains, TikZ diagrams, model movement, and diagram QA.
- `$coverage-audit-note-reviewer` for final source coverage, compile, and PDF audit.

Invoking `$auto-study-note-orchestrator` means the standard workflow should automatically use specialist subagents when the environment provides subagent tools, even if the user's prompt does not separately mention subagents. The user can opt out with phrases such as "不要派 subagent", "本地完成", or "不要并行代理".

The delegation architecture is content-type based, not course-specific. Classify work by what the knowledge point requires:

- `formal-reasoning`: mathematical derivations, proofs, algorithms, formal definitions, equations, optimization, statistics, and quantitative examples.
- `concept-synthesis`: definitions, assumptions, textual theory, institutional context, cases, empirical evidence, policy or managerial implications, and comparison tables.
- `visual-mechanism`: diagrams, mechanism chains, timelines, graphs, flows, tables that encode a process, and visual QA.
- `coverage-audit`: source coverage, gap closure, compile/PDF QA, and item-level completeness checks.
- `orchestrator`: inventory, batching, integration, style normalization, cross-references, and final assembly.

For the full orchestration protocol, read `references/orchestration-workflow.md` before starting any multi-file or chapter-range note task.

## Workflow

1. **Ground in the requested range.**
   - List all source PDFs, slide decks, `.tex` files, existing PDFs, outline images, and prior outputs in scope.
   - Use `pdfinfo` to confirm page counts and modification dates for PDFs.
   - Extract source text with `pdftotext -layout -enc UTF-8`, by whole file or page range.
   - Inspect existing `.tex` notes to reuse packages, colors, macros, box styles, section naming, and output conventions.

2. **Build the source inventory before drafting.**
   - Record chapter/session titles, slide/page titles, definitions, concepts, models, propositions, formulas, proofs, diagrams, tables, examples, cases, and comparison items.
   - Classify each substantive item as `concept`, `derivation`, `mixed`, `diagram`, `table`, `case`, or `review/admin/omit-candidate`.
   - Add a `required treatment` for every substantive item: `full model card`, `full derivation`, `comparison table`, `mechanism chain`, `case note`, `empirical-vs-theory note`, `policy note`, `formula sheet entry`, or `glossary entry`.
   - Treat this inventory as the coverage checklist for the whole task.
   - For any source range over 80 PDF pages or 3 lecture files, create an explicit inventory artifact named like `source_inventory.md` or `source_inventory.csv` before drafting. Do not replace this with a prose summary.
   - If the user provides a missing-topic screenshot or correction list, convert it into `gap_backlog.md` and map every gap to a source page, inventory id, target section, and required treatment before revising.

3. **Create the master outline and auto-batch plan.**
   - Use the user's requested unit order, outline image, or named course range as the organization.
   - Use the source inventory as the inclusion rule.
   - If a topic appears inside the requested source range, include it unless it is clearly review-only, administrative, duplicate, or outside scope.
   - If the requested range is large, automatically split it into batches before drafting. Prefer chapter, lecture, or model-family boundaries over raw page counts.
   - Keep tightly coupled derivations, diagrams, and examples in the same batch; do not split a proof, model, or mechanism chain across batches.
   - Produce a batch plan that lists batch id, source range, assigned outline sections, estimated density, specialist needs, and merge dependencies.
   - Add an `agent_owner` field for each batch or section: `formal-reasoning`, `concept-synthesis`, `visual-mechanism`, `coverage-audit`, or `orchestrator`. This owner determines automatic subagent dispatch.
   - For any source range over 120 PDF pages, 4 lecture files, or 60 inventory items, `batch_plan.md` is mandatory. Stop after producing the inventory and batch plan only if the user explicitly asked for planning only; otherwise continue drafting batch by batch.

4. **Draft each batch with specialist delegation.**
   - Dispatch specialists automatically from the batch plan. Do not wait for the user to explicitly request subagents.
   - Send `formal-reasoning` items to the math derivation specialist.
   - Send `concept-synthesis` items to the concept outline specialist.
   - Send `visual-mechanism` items to the diagram/mechanism specialist.
   - Send `coverage-audit` items to the coverage audit specialist.
   - Split mixed items into concept explanation, derivation, and diagram/mechanism pieces before delegation.
   - Include a task packet with source excerpt, coverage item id, expected section title, language rule, LaTeX style constraints, and required formulas, tables, or figures.
   - For long sources and any batch with `agent_owner` other than `orchestrator`, specialist delegation is mandatory when subagent tools are available. If no subagent tool is available, record `subagent unavailable; local fallback used` in the batch log and delivery note.
   - For long tasks, complete one batch at a time, write a batch-level LaTeX fragment, then run a local mini-audit against that batch's inventory before starting the next batch.
   - Do not summarize away named models. Any model, theorem, mechanism, empirical conflict, or policy tool named in the inventory must receive its own subsection, paragraph cluster, table row, or explicit cross-reference.
   - For important models, use a full model card: setup, agents, timing/information, decision rule, equilibrium/result, comparative statics, intuition, and common mistakes.
   - If subagents are unavailable, do the same work locally and state the fallback in the delivery note.

5. **Integrate the LaTeX handout.**
   - Create a new `.tex` file; do not overwrite existing notes unless explicitly requested.
   - Default structure: title page, table of contents, learning map, main units, formula sheet, common mistakes checklist, and optional glossary when requested.
   - Prefer `ctexart`, `amsmath`, `amssymb`, `booktabs`, `tcolorbox`, `tikz`, and existing local macros.
   - Use only light boxes named `definitionbox`, `takeawaybox`, `mistakebox`, `keypointbox`, and `proofbox`.
   - Merge batch fragments only after all batch mini-audits pass. Maintain a global cross-reference list for symbols, formulas, diagrams, and glossary items.
   - Keep workflow artifacts outside the final study guide. Source inventories, batch plans, mini-audits, global audits, subagent handoff notes, and coverage tables should remain separate `.md`/`.csv` files unless the user explicitly asks to append them.

6. **Compile twice and audit coverage.**
   - Compile at least twice with `xelatex -interaction=nonstopmode -halt-on-error <file>.tex` or `latexmk -xelatex`.
   - Inspect logs for `Error`, `Warning`, `Overfull`, and `Underfull`.
   - Use `pdfinfo` to confirm a nonempty PDF and `pdftotext` to confirm extractable Chinese text.
   - Ask the coverage audit specialist to mark every source inventory item as represented, represented indirectly, intentionally omitted, or missing.
   - For long sources, audit at slide/title level. A coarse range such as `pages 1--30 covered` is not acceptable unless it is backed by item-level rows.
   - If source PDFs exceed 120 pages and the final PDF is very short, treat that as a coverage warning requiring deeper audit. A final PDF under `source_pages / 8` pages, or under 25 pages for a 200+ page source, must not be delivered as complete unless the user explicitly asked for a compressed summary.
   - Run a gap-backlog audit whenever the user supplied missing topics or the auditor finds weak coverage. The final deliverable cannot be marked complete while `gap_backlog.md` contains unresolved substantive items.
   - Fix missing substantive items before delivery, or record a concise omission reason when truly outside scope.

## Non-Negotiable Rules

- Do not let the user's outline replace source coverage; the outline controls order, the source inventory controls inclusion.
- Do not copy large slide text blocks. Synthesize, teach, and make the result exam-usable.
- For large ranges, auto-batch by coherent learning units before writing; do not attempt a whole-course final draft in one pass.
- Specialist subagents are part of the default architecture. Use them automatically by content type, not by course name, unless the user explicitly opts out or the environment does not provide subagent tools.
- Large-range deliverables must include visible artifacts or sections for source inventory, batch plan, batch mini-audits, and global audit.
- Process artifacts prove the workflow but do not belong in the final study guide unless explicitly requested.
- A topic is not covered merely because a broad section mentions its parent model; named subresults, parameter effects, variants, empirical conflicts, and policy tools need explicit treatment.
- Keep formulas LaTeX-native and diagrams editable whenever possible.
- Show intermediate algebra for derivations; do not jump from assumptions to final formulas.
- Use diagrams only when they clarify a model or mechanism; verify equilibrium points and movement arrows.
- Preserve source files and prior notes.
- Return absolute links to the final `.pdf` and `.tex`.

## Useful Commands

```powershell
Get-ChildItem -Recurse -File
pdfinfo '.\source.pdf'
pdftotext -layout -enc UTF-8 '.\source.pdf' '.\source.txt'
xelatex -interaction=nonstopmode -halt-on-error 'notes.tex'
latexmk -xelatex -interaction=nonstopmode -halt-on-error 'notes.tex'
pdftotext -layout -enc UTF-8 '.\notes.pdf' -
pdftoppm -png -r 120 -f 1 -l 3 '.\notes.pdf' '.\qa_page'
```
