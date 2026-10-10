# 样例：从讲义到合并稿的交接流程

这份样例演示的是**流程产物之间能不能接上**，不是版式参考。视觉样式看
`../../assets/通用笔记模板.tex`；本目录关心的是 `source_inventory.md`、`synthesis_plan.md`、
正文片段与交接 JSON 这条链；公共设定直接保存在综合计划中。

素材是一份 12 页的一元回归讲义：一个课程单元内部有两个可独立讲解的问题，因此拆成两个写作批次。

## 文件

| 文件 | 由谁产出 | 说明 |
| --- | --- | --- |
| `source_inventory.md` | 编排器 | 6 个来源要求，不另维护覆盖状态 |
| `synthesis_plan.md` | 编排器 | 批次分工与依赖、公共定义/记号/结果键 |
| `issues.json` | 编排器 | 保留问题原始编号、描述及解决依据 |
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
5. **覆盖与问题分别对账。** 每份交接的 `coverage_map` 对应实际段落；U02 提出的问题在
   `issues.json` 中保留原始记录及解决依据，关闭后不从交接中删除。
6. **知识解释优先。** 正文直接解释 OLS 一阶条件与 R² 的边界，去掉编纂自述和无关故事；必要推导步骤与成立条件保留。两批有依赖，因此本例顺序写；独立主题可使用多个实例并行。

## 怎么跑

```bash
# 最终对账：只读取合并后的实际正文
python ../../scripts/check_handoffs.py \
  --handoff u01_handoff.json --handoff u02_handoff.json \
  --body merged.tex \
  --inventory source_inventory.md --issues issues.json --final --out audit.json

# 公式候选去重
python ../../scripts/collect_formula_candidates.py u01_handoff.json u02_handoff.json

# 片段边界与文档结构
python ../../scripts/validate_study_note.py --tex merged.tex \
  --unit-fragment u01_body.tex --unit-fragment u02_body.tex
```

后一条命令要求 `study-note-style.sty` 与 `merged.tex` 同目录。工作流本来就要复制 `assets/`
（见 `orchestration-workflow.md` 的统稿步骤），本目录没有把 `.sty` 复制进来，以免样式文件出现第二份副本
而产生版本漂移。测试脚本会在临时目录里复制后运行。

## 检查边界

最终交接检查会逐项对账来源 ID、正文标签、覆盖状态和问题关闭记录，报告中汇总 `coverage_map`。
它能发现未认领的条目与丢失的问题记录，但标签存在不能证明解释充分，仍须主编阅读对应正文。
本轮更新了样例契约，未重新运行检查、测试或编译。
