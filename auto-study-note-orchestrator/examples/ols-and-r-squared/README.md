# 样例：从讲义到合并稿的五份产物

这份样例演示的是**流程产物之间能不能接上**，不是版式参考。视觉样式看
`../../assets/通用笔记模板.tex`；本目录关心的是 `source_inventory.md`、`synthesis_plan.md`、
`continuity.md`、正文片段与交接 JSON 这条链。

素材是一份 12 页的一元回归讲义：一个课程单元内部有两个可独立讲解的问题，因此拆成两个写作批次。

## 文件

| 文件 | 由谁产出 | 说明 |
| --- | --- | --- |
| `source_inventory.md` | 编排器 | 6 个盘点项，附 `status` 终态 |
| `synthesis_plan.md` | 编排器 | 交付范围、execution_mode、两个批次的划分 |
| `continuity.md` | 编排器 | 可复用的定义、记号、结果键与正文标签 |
| `u01_body.tex` / `u01_handoff.json` | 写作批次 U01 | OLS 斜率的推导 |
| `u02_body.tex` / `u02_handoff.json` | 写作批次 U02 | $R^2$ 的解释，复用 U01 的记号 |
| `merged.tex` | 编排器 | 两份片段合并 + 唯一一处公式速查 |

## 这份样例特意演示的几件事

1. **正文片段不含文档级模块。** 两个 `_body.tex` 里都没有导言区、`\begin{document}`、
   `公式速查手册` 或 `FormulaSummaryTable`——这些只在 `merged.tex` 里出现，且只有一处。
2. **跨批次复用同一结果。** `ols_slope` 被 U01 定义、被 U02 的交接再次提名，且指向的
   `eq:ols-slope` 标签**位于 U01 的正文**。这正是 `check_handoffs.py` 必须把全部片段合起来
   解析标签、而不能只看单个片段的原因。
3. **提名不等于收录。** 两个批次共提名 3 条候选，去重后 `merged.tex` 里只有 2 行。
4. **一个盘点项可以只被间接覆盖。** `L1-04` 标为 `represented-indirectly`：两条代数性质由
   L1-03 的一阶条件直接落出，正文在推导尾部一段交代，不单独设小节。

## 怎么跑

```bash
# 交接契约与标签解析（本目录的样例应当 pass）
python ../../scripts/check_handoffs.py \
  --handoff u01_handoff.json --handoff u02_handoff.json \
  --body u01_body.tex --body u02_body.tex \
  --inventory source_inventory.md

# 公式候选去重
python ../../scripts/collect_formula_candidates.py u01_handoff.json u02_handoff.json

# 片段边界与文档结构
python ../../scripts/validate_study_note.py --tex merged.tex \
  --unit-fragment u01_body.tex --unit-fragment u02_body.tex
```

后一条命令要求 `study-note-style.sty` 与 `merged.tex` 同目录。工作流本来就要复制 `assets/`
（见 `orchestration-workflow.md` §3），本目录没有把 `.sty` 复制进来，以免样式文件出现第二份副本
而产生版本漂移。测试脚本会在临时目录里复制后运行。

## 已知未覆盖的部分

本样例能证明交接 JSON 与正文片段、合并稿、片段边界三者一致，以及公式候选能去重。
它**不能**证明 `source_inventory.md` 的每一项都真的在正文里有对应段落——覆盖质量仍是判断问题，
`check_handoffs.py` 只校验交接里引用的 coverage id 确实存在于清单，不校验覆盖是否充分。
