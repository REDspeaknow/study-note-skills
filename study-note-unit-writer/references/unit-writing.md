# Unit writing and handoff

## 正文最高写作规则

**禁止元视角写作与防御性写作。** 正文直接讲述知识、论证及其适用条件。删除从作者、编纂者或生成过程出发的安排介绍、讲解自评和取舍说明，例如“本节将介绍”“为了帮助读者”“这里合并了三条”。删除空泛保留、重复免责声明和预防性辩解；需要限定结论时，直接写具体条件、边界、反例或有依据的不确定性。按句子作用判断，不按词语黑名单删句。

这条规则适用于所有写作实例和主编统稿，优先于模板、示例和栏目建议。模型假设、方法局限、必要引用与有依据的风险说明属于知识内容，必须准确保留。来源缺失、编纂取舍、覆盖情况与未验证状态放在交接或交付说明中；影响结论成立的限制同时写在对应正文位置。

**知识解释优先，案例按需保留。** 重要知识点应让读者理解含义、成立原因与使用条件；推导须保留设定、关键变换、条件和结果。若去掉故事性叙述后只剩术语和结论，应补足机制或推导。简单定义可以一句话讲清，不给每个概念套同一组栏目，不设统一字数或案例占比。

案例仅在解释抽象关系、展示必要计算或推理、辨析边界，或原材料明确要求掌握其事实/分析方法时展开。同一机制的重复故事优先保留最有解释力的一个；删减无关背景、人物、时间线与重复结果，保留独特知识和必要例题步骤。案例清单项可落到一句话、一个步骤或已有解释，不自动获得小节；有意省略仍按覆盖契约登记。用多个故事或“这个案例说明了”重复结论，不能替代原因和过程。

例如讲需求弹性，先解释为何比较变动比例，再推导弹性与总收入的关系；降价故事只在新增理解时保留。写“在含截距的样本内 OLS 中……”可明确条件；“实际情况复杂，不能一概而论”应改成具体边界。

## 成文方式

`unit_id` 是一次连贯写作批次，可以只占课程章节的一部分。多个来源 ID 可共同落在一个段落或表格，批次边界不强制产生标题、导言或结尾总结。先解释核心问题，再按需要加入设定、推导、比较或例题；只在实际需要时增加小标题。

沿用已确认的定义和记号，后续结果只补变化的条件与关键步骤。首次出现的方法和非显然变换须写出依据及必要中间式，使读者能接续推导；已讲清的同类运算可以压缩，不省略理解结论所需的中间关系。图表须增加信息或替代重复叙述，比较表前用一句话明确判据；框、图注和易错提示也不重复正文。来源不足或公共设定冲突写入 `unresolved`，不以泛化教材内容补齐。

## Handoff record

Save UTF-8 JSON beside the body fragment:

```json
{
  "unit_id": "U03",
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

`coverage_map` contains every assigned ID as a key, including unfinished items; omit the redundant top-level `coverage_ids`. The checker derives IDs from the map; if a legacy `coverage_ids` list is present, it must match the keys. Its `status` is `pending`, `represented`, `represented-indirectly`, `intentionally-omitted`, `weak`, or `missing`. Represented/indirect/weak entries identify the actual teaching passage with `body_labels`; all other statuses, and `weak`, require a short `reason`. Several IDs may share a paragraph/table label without individual explanations or headings. Coverage status is maintained here and consolidated by the checker; the source inventory only records requirements. A label proves location, not sufficient explanation.

Each `unresolved` entry is `{"issue_id":"U03-Q01","coverage_ids":["L1-15"],"description":"来源未说明内点解成立条件"}`. Use a stable batch-prefixed ID for a new issue; reuse the supplied ID and original description for an existing one. Report new or still-open issues relevant to this batch. The orchestrator owns closure after reading the correction.

The orchestrator initializes `issues.json` as `[]`, then retains every issue as the same object plus `status` (`open`, `resolved`, or `accepted`), `resolution`, and `body_labels`. Closing requires a concrete resolution explanation; `resolved` also points to the corrected body passage. `accepted` means an explicitly documented source limitation or authorized omission, not an unexplained waiver. Preserve original ID, description and coverage IDs; retain closed entries. An empty later handoff leaves the ledger unchanged. Give the next writer the open issues relevant to its packet.

After merging, the orchestrator updates handoff locations/statuses against actual passages. Final accounting follows the [orchestration workflow](../../auto-study-note-orchestrator/references/orchestration-workflow.md). Later repair entries supersede earlier coverage entries; retain issue history. Optional content in `unresolved`, `formula_candidates` and `continuity_updates` uses `[]` when absent, with no extra “nothing to report” prose.

`key` identifies the result across units. If another unit reuses the result, use the same key and point to its earlier body explanation; do not create a new summary row. Formula candidates are optional nominations. The orchestrator decides which distinct retrieval targets enter one end-of-book formula section.

Use `continuity_updates` only for definitions, notation or results newly established or explicitly changed in this unit. The orchestrator merges reusable entries into the shared-context section of `synthesis_plan.md`. Reuse canonical names and labels; report conflicts in `unresolved` before dependent batches proceed.

`kind` is one of exactly three values:

| `kind` | Use for | `name` holds |
| --- | --- | --- |
| `definition` | A term introduced or redefined here | The Chinese term |
| `notation` | A symbol introduced or changed here | The LaTeX symbol, e.g. `\hat S_{xy}` |
| `result` | A result worth retrieving later | The result key, matching any `formula_candidates[].key` for the same result |

Every `body_label` must be a label this unit actually emits with `\label{...}`, or one inherited from an earlier batch that this unit reuses. A label naming nothing is the most common silent handoff defect; `scripts/check_handoffs.py` resolves every `body_label` against the supplied bodies and fails the run when one does not resolve.

Keep process notes and source coverage metadata outside the `.tex` body. Never add a local `\section{公式速查手册}` or `FormulaSummaryTable` even when the unit contains many formulas.
