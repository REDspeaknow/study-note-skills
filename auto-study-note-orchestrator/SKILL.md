---
name: auto-study-note-orchestrator
description: Build complete Chinese LaTeX/PDF study guides from course materials with item-level source coverage, concept-first writing, a canonical Times New Roman study-note template, content-type specialist delegation, compilation, deterministic validation, and optional ChatGPT review.
---

# Auto Study Note Orchestrator

## Purpose

Turn a user-specified range of course materials into a complete Chinese LaTeX/PDF study guide. The default language is Chinese. Add English labels for concepts, keywords, or variable names only when the user explicitly asks for English annotation.

For every complete document, read `references/style-contract.md` and start from the canonical files in `assets/`. The required contract is `study-note-style-v1`: concept-first content, the supplied compact green/blue/cream design, borderless clickable links, Times New Roman for ordinary Latin text, and XITS Math for mathematics. Do not reconstruct the preamble from memory.

This skill coordinates specialist skills:

- `$math-derivation-note-writer` for derivations, proofs, formulas, and calculation procedures.
- `$concept-outline-note-writer` for definitions, textual knowledge, comparison content, and exam-oriented summaries.
- `$diagram-mechanism-note-writer` for mechanism chains, TikZ diagrams, model movement, and diagram QA.

There is no dedicated coverage-review subagent in this workflow. The orchestrator owns item-level coverage closure, compilation, validator execution, and PDF/layout gates. When the user explicitly combines this skill with `$codex-with-chatgpt`, ChatGPT provides the independent semantic review through the workspace connection; do not also dispatch a coverage-review specialist for the same checkpoint.

Invoking `$auto-study-note-orchestrator` means the standard workflow should automatically use specialist subagents when the environment provides subagent tools, even if the user's prompt does not separately mention subagents. The user can opt out with phrases such as "不要派 subagent", "本地完成", or "不要并行代理".

The delegation architecture is content-type based, not course-specific. Classify work by what the knowledge point requires:

- `formal-reasoning`: mathematical derivations, proofs, algorithms, formal definitions, equations, optimization, statistics, and quantitative examples.
- `concept-synthesis`: definitions, assumptions, textual theory, institutional context, cases, empirical evidence, policy or managerial implications, and comparison dimensions in prose.
- `visual-mechanism`: justified comparison or process tables, diagrams, mechanism chains, timelines, graphs, flows, and visual QA.
- `orchestrator`: inventory, batching, integration, style normalization, cross-references, source coverage closure, compile/PDF QA, item-level completeness checks, and final assembly.

Every substantive inventory row also carries:

- `importance`: `必背`, `重点`, or `了解`.
- `primary_treatment`: `concept body`, `derivation`, `comparison`, `case`, `mechanism`, or another explicit body treatment.
- `visual_needed`: `yes` or `no`.
- `visual_reason`: `source-essential`, `mechanism-essential`, `comparison-efficient`, `user-requested`, or blank when no visual is needed.

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
   - Add `importance`, `primary_treatment`, `required treatment`, `visual_needed`, and `visual_reason` for every substantive item.
   - A formula sheet, table, diagram, or glossary entry may supplement a concept but cannot be its only body treatment.
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
   - Add an `agent_owner` field for each batch or section: `formal-reasoning`, `concept-synthesis`, `visual-mechanism`, or `orchestrator`. This owner determines automatic subagent dispatch.
   - For any source range over 120 PDF pages, 4 lecture files, or 60 inventory items, `batch_plan.md` is mandatory. Stop after producing the inventory and batch plan only if the user explicitly asked for planning only; otherwise continue drafting batch by batch.

4. **Draft each batch concept first, then add formal or visual support.**
   - Dispatch specialists automatically from the batch plan. Do not wait for the user to explicitly request subagents.
   - Send `concept-synthesis` items to the concept outline specialist.
   - Complete and mini-audit the concept body before attaching derivations, formulas, tables, or diagrams.
   - Send `formal-reasoning` items to the math derivation specialist after their parent concept and notation are stable.
   - Send `visual-mechanism` items to the diagram/mechanism specialist only when `visual_needed: yes` and `visual_reason` passes the style-contract gate.
   - Split mixed items into concept explanation, derivation, and an optional visual piece before delegation; do not assume every mixed item needs a visual.
   - Include `style_contract: study-note-style-v1`, source excerpt, coverage item id, importance, primary treatment, parent concept section, language rule, and any justified formula or visual request in every task packet.
   - For long sources and any batch with `agent_owner` other than `orchestrator`, specialist delegation is mandatory when subagent tools are available. If no subagent tool is available, record `subagent unavailable; local fallback used` in the batch log and delivery note.
   - For long tasks, complete one batch at a time, write a batch-level LaTeX fragment, then run a local mini-audit against that batch's inventory before starting the next batch.
   - Do not summarize away named models. Any model, theorem, mechanism, empirical conflict, or policy tool named in the inventory must receive its own subsection, paragraph cluster, table row, or explicit cross-reference.
   - For important models, use a full model card: setup, agents, timing/information, decision rule, equilibrium/result, comparative statics, intuition, and common mistakes.
   - If subagents are unavailable, do the same work locally and state the fallback in the delivery note.

5. **Integrate with the canonical template.**
   - Copy `assets/通用笔记模板.tex` and `assets/study-note-style.sty` into a new output project. Do not overwrite existing notes unless explicitly requested.
   - Keep the required order: compact title block and reading order, borderless clickable table of contents, one source-grounded overview map, main units, topic-separated formula summary tables, memorization-priority overview, global common mistakes, closing line.
   - Count substantive main sections before the formula summary. For 1–3 sections, draw `核心知识关系导图` from the main concepts or mechanisms and link every node to its body explanation. For 4 or more sections, draw `各章节关系导图` from the actual chapters. Put the map after the table of contents. Build a `map_contract` with node targets and evidence for every relationship. If no genuine relationship is supported, omit the map and record a specific reason as `% study-map-omitted: ...` in the TeX; do not invent connections.
   - Use `FormulaSummaryTable` and `\FormulaSummaryRow` for the final formula section. Split rows into topic subsections, repeat the three-column header across pages, and include only formulas already explained or derived in the body. The third column must state applicability, assumptions, use, or a concrete warning.
   - Keep long derivations and cases in ordinary prose. Use the supplied light boxes only for short definitions, takeaways, final formula summaries, and mistakes.
   - Do not redefine fonts, colors, priority symbols, hyperlink behavior, heading spacing, or boxes outside `study-note-style.sty`.
   - Merge batch fragments only after all batch mini-audits pass. Maintain a global cross-reference list for symbols, formulas, diagrams, and glossary items.
   - Keep workflow artifacts outside the final study guide. Source inventories, batch plans, mini-audits, global audits, subagent handoff notes, and coverage tables should remain separate `.md`/`.csv` files unless the user explicitly asks to append them.

6. **Compile until references stabilize, then audit coverage.**
   - Run `scripts/compile_study_note.py --tex <file>.tex` to start with one XeLaTeX pass and rerun only when the table of contents, bookmarks, or cross-references are stale. A clean existing build may finish in one pass; a new table of contents normally needs another. If they remain unstable after the bounded retries, report the failure instead of delivering a PDF with wrong references.
   - Inspect logs for `Error`, `Warning`, `Overfull`, and `Underfull`.
   - Use `pdfinfo` to confirm a nonempty PDF and `pdftotext` to confirm extractable Chinese text.
   - Run `scripts/validate_study_note.py` with the TeX entrypoint, PDF, compile log, and source inventory. Visible link borders, missing Times New Roman or XITS Math resources, font substitution, incorrect section order, a missing or wrong map type without a documented source-grounded omission, a noncanonical formula summary, or a missing style marker block delivery.
   - The orchestrator must mark every source inventory item as represented, represented indirectly, intentionally omitted, or missing, using source evidence and extracted PDF text rather than delegation.
   - When `$codex-with-chatgpt` is active, send one review checkpoint after local validation and ask ChatGPT to inspect the inventory, generated sources, and current outputs through the workspace connection. Treat its findings as an independent semantic challenge, then resolve them locally. Do not run a second coverage-review subagent for the same checkpoint.
   - Require prose body coverage for every substantive concept. A table, figure, formula sheet, or glossary entry alone does not qualify as represented.
   - Audit every visual against its recorded `visual_reason`, source cue, coverage ids, and adjacent concept section. Remove decorative, duplicate, guessed, or coverage-only visuals.
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
- Use diagrams only after concept coverage and only when the visual eligibility gate passes; verify equilibrium points and movement arrows.
- Treat the front-matter overview map as navigation, never as body coverage. Verify every node resolves to a real body concept or chapter and every edge has an evidence note.
- Keep the final formula summary grouped by topic and limited to body-backed retrieval cues; never duplicate long derivations there.
- Use `\PriorityMust`, `\PriorityImportant`, and `\PriorityKnow` instead of literal Unicode stars.
- Preserve the canonical style contract unless the user explicitly requests a different design.
- Preserve source files and prior notes.
- Return absolute links to the final `.pdf` and `.tex`.

## Useful Commands

```powershell
Get-ChildItem -Recurse -File
pdfinfo '.\source.pdf'
pdftotext -layout -enc UTF-8 '.\source.pdf' '.\source.txt'
python .\scripts\compile_study_note.py --tex 'notes.tex'
pdftotext -layout -enc UTF-8 '.\notes.pdf' -
pdftoppm -png -r 120 -f 1 -l 3 '.\notes.pdf' '.\qa_page'
```
