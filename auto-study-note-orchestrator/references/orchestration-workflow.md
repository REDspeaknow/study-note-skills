# Orchestration workflow

Use this for all guides. The inventory is an evidence ledger; the synthesis plan is the writing plan. Keep them distinct. Apply `delegation-policy.md` after planning units and before drafting.

## 1. Source ledger

List source files and exact ranges. For every substantive item, record `id`, source page/slide, title or cue, type, importance, required fact/result, and status. Types may include concept, derivation, comparison, diagram, case, and admin/duplicate. Merge continuation slides that express one result; do not merge unrelated claims just to reduce row count.

`status` starts at `pending` and closes as one of `represented`, `represented-indirectly`, `intentionally-omitted`, `weak`, or `missing` — the same vocabulary the audit protocol uses, so the inventory and the independent audit can be compared row by row.

| Source item | Typical treatment |
| --- | --- |
| Simple definition or scope note | One precise sentence or compact paragraph |
| Easily confused alternatives | Governing distinction plus table or short comparison |
| Illustrative case | One or two sentences linked to the mechanism |
| Central model | Setup once, decision/equilibrium result, essential derivation, interpretation |
| Later result in the same model | Inherit setup; show changed assumption or key step |
| Source figure with examinable geometry | Explain adjacent to a checked figure |

Importance guides space and retrieval priority, not the number of mandatory headings. Preserve source-specific exceptions and boundaries when they change a conclusion.

## 2. Synthesis plan and unit packet

Distinguish course chapters from writing units (batches). A course unit can span hundreds of pages; one writer packet covers a coherent question, model result or derivation stage within it. Follow the batching rules in `delegation-policy.md`; `unit_id` identifies a writing batch, not an entire course chapter. Save `synthesis_plan.md` with the parent course unit/chapter, writing-unit ID, source IDs and ranges, learning question, primary claim, prerequisite notation, depth, visual decision and master-outline position. Record the execution decision there. Maintain `continuity.md` with canonical definitions, notation, result/formula keys, body labels and owning writing units; track each batch as planned, drafting, received or integrated.

Give the integrated writer current source excerpts and relevant prior context:

```text
unit_id:
course_unit_or_chapter: parent chapter and this batch's position within it
output_paths: absolute paths for this unit's two files
writer_skill_path: absolute path to study-note-unit-writer/SKILL.md
writer_reference_path: absolute path to references/unit-writing.md
learning_question:
coverage_ids:
source_evidence:
importance_and_depth:
already_defined_terms_and_notation:
prior_results_and_body_labels:
open_issues_for_this_batch: stable IDs and original descriptions from issues.json
new_definitions_owned_by_this_unit:
must_preserve_results_and_boundaries:
approved_visual_and_reason: optional
style_contract: study-note-style-v1
deliver: <unit_id>_body.tex + <unit_id>_handoff.json
```

The writer owns prose, math, and visuals within that writing batch. Later batches in the same course unit inherit established setup rather than rewriting it. Follow the execution mode and resumption rules in `delegation-policy.md`. A resumed writer still receives the current packet and continuity entries; its memory does not replace these files.

Initialize `issues.json` as `[]`. After each unit, review its `coverage_map` against actual passages, inspect key algebra/visuals and repetition, and reconcile `continuity_updates` into `continuity.md`. Merge unresolved entries into the persistent issue ledger and record corrections before the next dependent batch. The compact coverage/closure schema lives in `study-note-unit-writer/references/unit-writing.md`; retain original handoffs and closed issues.

## 3. Document assembly

Copy `assets/通用笔记模板.tex` and `assets/study-note-style.sty`. The fixed visual language does not require fixed content modules. The orchestrator, not the unit writer, owns title/contents, any source-grounded overview map, global formula reference, priority overview, and cross-unit mistakes. Include a module only if it helps navigation or retrieval. A map may be omitted with `% study-map-omitted: <reason>`; do not label it `user-requested` unless the user requested it.

Merge body fragments in teaching order. Keep the first complete definition; replace later restatements with a reference or changed implication. Compare prose, tables, captions, cases, local boxes, and exam tips for repeated conclusions. Delete a repeated representation while preserving unique conditions and exceptions.

## 4. One global formula reference

Read each handoff's `formula_candidates`. The `key` identifies a result, not a TeX spelling. Group identical keys, resolve incompatible formulas or conditions against the body, and reject intermediate algebra, worked substitutions, and numerical-example steps. Every accepted candidate must point to a real body label.

Only after all units are merged, write at most one `\section{公式速查手册}` following the main units. It may contain multiple topic tables using `FormulaSummaryTable`; none may appear earlier or in unit fragments. Omit the section when there are no distinct retrieval formulas. It is an index, not a second derivation.

Use `scripts/collect_formula_candidates.py` to detect duplicate keys and inconsistent submissions before editorial selection. It does not mandate including every candidate.

Run `scripts/check_handoffs.py` over received handoffs and bodies with `--inventory <inventory> --issues <issues.json>` before merging. It checks coverage-map keys and locations, formula/continuity labels and issue retention. Partial runs allow unassigned inventory items and flag open issues; full accounting is the final audit's responsibility.

## 5. Final audit

Review actual passages and important derivations, including assumptions and boundaries; keyword occurrence alone is not proof. Update handoff coverage entries and inventory statuses after deduplication, then run `scripts/check_handoffs.py` with all handoffs, the final TeX/actually included fragments as `--body`, and `--final --inventory <inventory> --issues <issues.json> --out <audit.json>`. The report consolidates coverage without another manually maintained table. Resolve gaps or document legitimate omissions; report accepted source limitations explicitly. Open issues or incomplete coverage mean a draft, not a completed guide.

Identify each unit's central claim and remove repeated paraphrases from exam cues, mistakes, takeaway boxes, tables, and end matter. Page and heading/box/formula counts are diagnostics, not pass/fail limits.

Compile and run `scripts/validate_study_note.py --tex <entrypoint> --pdf <pdf> --log <log> --inventory <inventory> --unit-fragment <fragment> ...`. Render representative concept, math, table, and end-matter pages. Do not certify raw-source completeness when only an earlier guide is available.

`examples/ols-and-r-squared/` shows the inventory, plan, continuity, handoffs, issue ledger and merged output, including a result defined in one batch and reused by another.
