# Unit writing and handoff

## Unit shape

Here, a unit is a bounded writing batch, not the course's own chapter/teaching-unit label. Several batches can build one chapter. The packet supplies the parent chapter and earlier definitions/results; continue that exposition without giving each batch a standalone introduction, recap or new heading by default.

When the exposition needs a heading, its title should answer one learning question. Start with the result or distinction that organizes the batch, then add only the setup, mechanism, derivation, example, or boundary needed to understand it. Several source slides may map to one paragraph or table. One source slide may require a worked derivation. Importance changes the depth of explanation; it does not create a mandatory list of subheadings.

For a model, establish notation once. A first substantive result may need actors, choices, assumptions, and equilibrium. Later results in the same model should inherit that setup and show only the changed step. Distinguish a source-derived result from an added explanation.

For a derivation, show the key transformation, the condition that licenses it, and the final result. Skip algebra that merely repeats an immediately visible substitution. A formula intended for memorization may be proposed in handoff metadata; do not build a local formula-summary table.

For a comparison, use one short synthesis sentence plus a compact table when the table replaces several parallel paragraphs. The table can be the main representation of comparison dimensions; the surrounding prose states the governing distinction.

## Handoff record

Save UTF-8 JSON beside the body fragment:

```json
{
  "unit_id": "U03",
  "coverage_ids": ["L1-13", "L1-14", "L1-15"],
  "coverage_map": {
    "L1-13": {"status": "represented", "body_labels": ["sec:two-sided-pricing"]},
    "L1-14": {"status": "represented-indirectly", "body_labels": ["sec:two-sided-pricing"]},
    "L1-15": {"status": "represented", "body_labels": ["sec:two-sided-pricing"]}
  },
  "unresolved": [],
  "continuity_updates": [
    {
      "kind": "notation",
      "name": "p_B",
      "meaning": "向买方收取的费用",
      "body_label": "sec:two-sided-pricing"
    }
  ],
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

### Coverage and issue records

`coverage_ids` lists the assigned items, including unfinished ones. `coverage_map` has exactly those IDs as keys. Each entry uses the inventory's `status` vocabulary: `pending`, `represented`, `represented-indirectly`, `intentionally-omitted`, `weak`, or `missing`. Represented/indirect/weak entries identify the actual teaching passage with `body_labels`; all other statuses, and `weak`, require a short `reason`. Several IDs may share an existing paragraph/table label; add anchors where useful, not headings per ID. A label proves location, not sufficient explanation.

Each `unresolved` entry is `{"issue_id":"U03-Q01","coverage_ids":["L1-15"],"description":"来源未说明内点解成立条件"}`. Use a stable batch-prefixed ID for a new issue; reuse the supplied ID and original description for an existing one. Report new or still-open issues relevant to this batch. The orchestrator owns closure after reading the correction.

The orchestrator initializes `issues.json` as `[]`, then retains every issue as the same object plus `status` (`open`, `resolved`, or `accepted`), `resolution`, and `body_labels`. Closing requires a concrete resolution explanation; `resolved` also points to the corrected body passage. `accepted` means an explicitly documented source limitation or authorized omission, not an unexplained waiver. Preserve original ID, description and coverage IDs; retain closed entries. An empty later handoff leaves the ledger unchanged. Give the next writer the open issues relevant to its packet.

After merging, the orchestrator reviews passages and updates handoff coverage locations/statuses and inventory statuses. Run `check_handoffs.py` with all handoffs in teaching/repair order; later entries for the same coverage ID supersede earlier ones. Its JSON report contains the consolidated `coverage_map`. For final accounting, supply only the final TeX and any fragments it actually includes as `--body`, with `--final --inventory <inventory> --issues <issues.json> --out <audit.json>`: every inventory ID needs a terminal coverage entry, all reported issues must still exist in the ledger, and open issues block completion. Accepted limitations remain visible in the report and delivery note. Keep unresolved work as a draft when it cannot be closed.

`key` identifies the result across units. If another unit reuses the result, use the same key and point to its earlier body explanation; do not create a new summary row. Formula candidates are optional nominations. The orchestrator decides which distinct retrieval targets enter one end-of-book formula section.

Use `continuity_updates` only for definitions, notation or results newly established or explicitly changed in this unit; use an empty list otherwise. Reuse prior canonical names and body labels from the packet. If prior context conflicts with source evidence, report the conflict in `unresolved` for the orchestrator to resolve before the next unit.

`kind` is one of exactly three values:

| `kind` | Use for | `name` holds |
| --- | --- | --- |
| `definition` | A term introduced or redefined here | The Chinese term |
| `notation` | A symbol introduced or changed here | The LaTeX symbol, e.g. `\hat S_{xy}` |
| `result` | A result worth retrieving later | The result key, matching any `formula_candidates[].key` for the same result |

Every `body_label` must be a label this unit actually emits with `\label{...}`, or one inherited from an earlier batch that this unit reuses. A label naming nothing is the most common silent handoff defect; `scripts/check_handoffs.py` resolves every `body_label` against the supplied bodies and fails the run when one does not resolve.

Keep process notes and source coverage metadata outside the `.tex` body. Never add a local `\section{公式速查手册}` or `FormulaSummaryTable` even when the unit contains many formulas.
