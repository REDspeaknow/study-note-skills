---
name: study-note-unit-writer
description: Write one coherent Chinese study-guide unit from grouped course evidence, combining concepts, necessary derivations, cases, and justified visuals without repeating a full-document template.
---

# Study Note Unit Writer

完成主编分配的一批正文。先读取 `references/unit-writing.md`：其中**禁止元视角与防御性写作、知识解释优先和案例取舍**是正文首要规则，交接格式也仅在该文件维护。

其他实例可并行写独立批次。沿用任务包提供的公共设定和讲解归属，仅编辑分配的正文与交接路径；新标签默认使用小写 `unit_id` 前缀，继承标签保持原名。公共设定冲突交给主编处理。

## Deliverables

1. `<unit_id>_body.tex`：只写知识正文，重要结论的条件和必要推导在对应位置讲清楚。不含导言区、`\begin{document}`、全书关系图、`公式速查手册`、`FormulaSummaryTable` 或全局复盘模块。
2. `<unit_id>_handoff.json`：按契约记录覆盖对应、真实问题、候选公式及新增公共设定。没有问题、候选或变动时相应列表为 `[]`。

完成后返回两份文件路径与确有必要的疑点，不另写通过项清单。主编负责后续调度、共享记录和整本统稿。
