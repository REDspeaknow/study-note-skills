# 中文复习笔记 Skills

架构：主编组织与统稿，写作器依据正文样例和写作要求生成内容，审核器按需核对。默认就地执行，用户要求时委派写作或独立审核。

- auto-study-note-orchestrator：来源、范围、记号、写作安排、统稿、编译和交付。
- study-note-unit-writer：先看实际正文样例，再按要求写作；知识点清楚、定义完整、逐点星标，保留必要解释与计算，减少衔接。
- coverage-audit-note-reviewer：内容审核先于技术检查，核对定义、星级、来源、冗余、推理和 PDF。

正文资源集中在写作器：

- [正文样例](study-note-unit-writer/references/body-example.tex)：概念、完整定义、推导和例题的实际 TeX。
- [写作要求](study-note-unit-writer/references/unit-writing.md)：内容取舍与完整性约束。
- [样例说明](study-note-unit-writer/references/reference-calibration.md)：来源范围、可打印入口和按需读取的 OLS 数学样例。

主编委派时显式传递上述正文样例、写作要求及 SKILL.md 的绝对路径。子代理交正文和必要疑点，主编用一份 review_notes.md 追踪来源并合并。旧交接检查、候选公式归并脚本及对应 JSON/流程样例已移除；有用的数学正文保留在写作器 examples。

模板和样式仍集中在总编排器 assets：FandolKai 正文、FandolSong Bold 粗体、Times New Roman 西文、XITS Math 数学字体。v3 蓝边框为细蓝边、暖白底、小号文字、框内题头。编排器 scripts 只保留编译和结构/PDF 校验。

~~~text
使用 $auto-study-note-orchestrator 整理复习指南。正文先参照 study-note-unit-writer 的 body-example.tex，再按 unit-writing.md 写作：知识点清楚、定义完整、逐点标星，推导和例题完整入框，少写铺垫与转场。
~~~

三个技能文件夹可一起复制到个人 Skills 目录。课程事实依据来源，样例只示范表达；自动 pass 不表示内容合格。
