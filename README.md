# 中文复习笔记 Skills

新版采用 study-note-style-v2：章节分组、逐知识点三级星标、推导和例题统一蓝框。正文直接讲知识，取消默认导读、章节过渡、批次小结和多层数字标题。

- auto-study-note-orchestrator：读取来源，确定知识点与星级，统稿、编译和验收。
- study-note-unit-writer：写作或精简指定范围的星标知识点与必要蓝框。
- coverage-audit-note-reviewer：检查星级入口与依据、来源覆盖、数学正确性、冗余和 PDF。

默认就地执行；多来源时用一份 review_notes.md 追踪来源、星级依据、正文位置和疑点。逐批交接 JSON 与复杂调度不再是新工程必需项。已有旧工程可以沿用其追踪工具。公式速查仍可按需在全书末尾集中添加一次。

三项 skill 共用总编排器 assets 下的模板和样式。保留当前已安装版本的 FandolKai 正文、FandolSong 粗体、Times New Roman 西文和 XITS Math 数学字体。所有独立知识点使用 \StudyPoint 或 \StudyTerm；必要推导用 proofbox，公式块用 formulabox，例题用 examplebox。

调用示例：

~~~text
使用 $auto-study-note-orchestrator，把这些课程资料整理成复习指南：逐知识点标注三级星级，必要推导和例题用蓝框，表达参照数字经济笔记，保留关键步骤并精简衔接。
~~~

三个文件夹可复制到个人 Skills 目录。改造前工作区与已安装版均已单独备份；对比用原始笔记保持不变。
