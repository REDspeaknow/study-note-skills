# Orchestration workflow

Use this for multi-file or chapter-range guides. The inventory is an evidence ledger; the synthesis plan is the writing plan. Keep them distinct.

## 1. Source ledger

List source files and exact ranges. For every substantive item, record `id`, source page/slide, title or cue, type, importance, required fact/result, and status. Types may include concept, derivation, comparison, diagram, case, and admin/duplicate. Merge continuation slides that express one result; do not merge unrelated claims just to reduce row count.

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

Group inventory IDs into learning units around one central question or model. Save `synthesis_plan.md` with unit ID, source IDs, learning question, primary claim, prerequisite notation, depth, visual decision, and master-outline position. Keep a model's setup and application together; do not create one batch per slide.

Give the integrated writer current source excerpts and relevant prior context:

```text
unit_id:
learning_question:
coverage_ids:
source_evidence:
importance_and_depth:
already_defined_terms_and_notation:
must_preserve_results_and_boundaries:
approved_visual_and_reason: optional
style_contract: study-note-style-v1
deliver: <unit_id>_body.tex + <unit_id>_handoff.json
```

The writer owns prose, math, and visuals within that unit. Keep related units sequential and reuse writer context if possible. If delegation is unavailable or declined, write locally under the same boundaries.

After each unit, locate each assigned ID in the body or an unresolved note, inspect key algebra and visuals, and identify claims already explained elsewhere. Record findings and fixes compactly.

## 3. Document assembly

Copy `assets/通用笔记模板.tex` and `assets/study-note-style.sty`. The fixed visual language does not require fixed content modules. The orchestrator, not the unit writer, owns title/contents, any source-grounded overview map, global formula reference, priority overview, and cross-unit mistakes. Include a module only if it helps navigation or retrieval. A map may be omitted with `% study-map-omitted: <reason>`; do not label it `user-requested` unless the user requested it.

Merge body fragments in teaching order. Keep the first complete definition; replace later restatements with a reference or changed implication. Compare prose, tables, captions, cases, local boxes, and exam tips for repeated conclusions. Delete a repeated representation while preserving unique conditions and exceptions.

## 4. One global formula reference

Read each handoff's `formula_candidates`. The `key` identifies a result, not a TeX spelling. Group identical keys, resolve incompatible formulas or conditions against the body, and reject intermediate algebra, worked substitutions, and numerical-example steps. Every accepted candidate must point to a real body label.

Only after all units are merged, write at most one `\section{公式速查手册}` following the main units. It may contain multiple topic tables using `FormulaSummaryTable`; none may appear earlier or in unit fragments. Omit the section when there are no distinct retrieval formulas. It is an index, not a second derivation.

Use `scripts/collect_formula_candidates.py` to detect duplicate keys and inconsistent submissions before editorial selection. It does not mandate including every candidate.

## 5. Final audit

Create a compact coverage map: each inventory ID -> body section/label, intentional omission reason, or unresolved. Review actual passages; keyword occurrence alone is not proof. Check important derivations against available source or inherited notes, including assumptions and boundaries.

Identify each unit's central claim and remove repeated paraphrases from exam cues, mistakes, takeaway boxes, tables, and end matter. Page and heading/box/formula counts are diagnostics, not pass/fail limits.

Compile and run `scripts/validate_study_note.py --tex <entrypoint> --pdf <pdf> --log <log> --inventory <inventory> --unit-fragment <fragment> ...`. Render representative concept, math, table, and end-matter pages. Do not certify raw-source completeness when only an earlier guide is available.
