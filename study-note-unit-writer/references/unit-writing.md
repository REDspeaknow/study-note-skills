# Unit writing and handoff

## Unit shape

The title should answer one learning question. Start with the result or distinction that organizes the unit, then add only the setup, mechanism, derivation, example, or boundary needed to understand it. Several source slides may map to one paragraph or table. One source slide may require a worked derivation. Importance changes the depth of explanation; it does not create a mandatory list of subheadings.

For a model, establish notation once. A first substantive result may need actors, choices, assumptions, and equilibrium. Later results in the same model should inherit that setup and show only the changed step. Distinguish a source-derived result from an added explanation.

For a derivation, show the key transformation, the condition that licenses it, and the final result. Skip algebra that merely repeats an immediately visible substitution. A formula intended for memorization may be proposed in handoff metadata; do not build a local formula-summary table.

For a comparison, use one short synthesis sentence plus a compact table when the table replaces several parallel paragraphs. The table can be the main representation of comparison dimensions; the surrounding prose states the governing distinction.

## Handoff record

Save UTF-8 JSON beside the body fragment:

```json
{
  "unit_id": "U03",
  "coverage_ids": ["L1-13", "L1-14", "L1-15"],
  "unresolved": [],
  "formula_candidates": [
    {
      "key": "two_sided_price_structure_foc",
      "name": "固定总价的内点条件",
      "formula": "(D_B)'/D_B=(D_S)'/D_S",
      "conditions": "两侧需求为正且可微，解在可行区间内部",
      "body_label": "sec:two-sided-pricing"
    }
  ]
}
```

`key` identifies the result across units. If another unit reuses the result, use the same key and point to its earlier body explanation; do not create a new summary row. Formula candidates are optional nominations. The orchestrator decides which distinct retrieval targets enter one end-of-book formula section.

Keep process notes and source coverage metadata outside the `.tex` body. Never add a local `\section{公式速查手册}` or `FormulaSummaryTable` even when the unit contains many formulas.
