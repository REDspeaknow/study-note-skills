# 中文复习笔记 Skills

新版采用 study-note-style-v3：知识点边界清楚、定义准确、逐点三级星标；各点直接展开，删除导读、铺垫、转场和重复总结。模型参数与运算步骤归入所属知识点，不逐项加星。

- auto-study-note-orchestrator：读取来源，确定知识点与星级，统稿、编译和验收。
- study-note-unit-writer：写作或精简指定范围的星标知识点与必要蓝框。
- coverage-audit-note-reviewer：检查星级入口与依据、来源覆盖、数学正确性、冗余和 PDF。

默认就地执行；多来源时用一份 review_notes.md 追踪来源、星级依据、正文位置和疑点。逐批交接 JSON 与复杂调度不再是新工程必需项。已有旧工程可以沿用其追踪工具。公式速查仍可按需在全书末尾集中添加一次。

三项 skill 共用总编排器 assets 下的模板和样式。沿用 FandolKai 正文、FandolSong 粗体、Times New Roman 西文和 XITS Math 数学字体。短定义使用同段的 \StudyTerm，模型等用 \StudyPoint；推导与例题各自完整放一个框。蓝边框向数字经济参考稿校准为细蓝边、暖白底、小号文字、框内题头，无独立标题栏；普通辅助公式可无框。

起草前读取[实际段落校准](study-note-unit-writer/references/reference-calibration.md)，可编译样例见[复习密度校准.tex](auto-study-note-orchestrator/examples/review-calibration/复习密度校准.tex)，其来源与局部范围见同目录 review_notes.md。先核对定义、冗余、必要解释和计算，再做技术检查；自动 pass 不表示内容合格。

调用示例：

~~~text
使用 $auto-study-note-orchestrator，把这些课程资料整理成复习指南：知识点清楚、定义准确、逐点三级星标；各点直接展开，少写铺垫和转场。推导与例题各放一个完整蓝边框，保留必要解释和计算，先参照实际段落校准后写作。
~~~

三个文件夹可复制到个人 Skills 目录。改造前工作区与已安装版均已单独备份；对比用原始笔记保持不变。
