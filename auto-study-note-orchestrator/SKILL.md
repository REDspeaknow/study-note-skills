---
name: auto-study-note-orchestrator
description: 组织课程资料并统稿为中文 LaTeX/PDF 复习指南，按写作器的正文样例与要求完成知识点、定义、星标、推导和例题，编译并验收。
---

# 复习笔记编排

负责来源、范围、记号、写作安排、统稿及交付。正文表达使用 study-note-unit-writer 中的[正文样例](../study-note-unit-writer/references/body-example.tex)和[写作要求](../study-note-unit-writer/references/unit-writing.md)，先看样例再读要求；实际知识内容依据课程资料。

1. 递归读取课程资料及 TeX 的 input/include，包括 build 子目录，确认范围与真实正文。
2. 按课程知识点组织内容，核定星级，统一记号。来源较多时维护一份 review_notes.md，记录来源、依据、正文位置和真实疑点。
3. 按写作器的样例与要求起草。生成整本时读取[版式契约](references/style-contract.md)，使用 assets 中的模板和样式。
4. 合并并核对知识点、定义、必要解释、计算和课件中的必要图表，处理重复与冲突。保持各点直接展开，避免合并时添加铺垫转场。
   整本笔记在标题区后、可选目录及正文之前放一张全局思维导图，参照数字经济的“课程 → 主题模块 → 核心知识”布局；由主编依据实际内容统一绘制，写作器不逐批生成。
5. 按需在全部正文后集中添加一次公式速查；编译、技术校验并查看 PDF，内容自审与技术结果分别判断。

默认就地完成。用户要求委派时，给写作器课程来源/范围、知识点与星级依据、已确认的记号、正文样例及写作要求的绝对路径、独占输出路径。只接收正文片段和必要疑点，由主编统稿。用户要求独立审核时调用 coverage-audit-note-reviewer。

多来源、分批或续写时读取[工作流](references/orchestration-workflow.md)。交付 PDF、TeX 与必要样式，说明真实缺项及未验证项；保留原资料。
