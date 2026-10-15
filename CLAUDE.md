# Study Note Skills — Claude Code 入口

默认使用中文，用户要求优先。整本整理使用 auto-study-note-orchestrator；指定范围写作使用 study-note-unit-writer；审核使用 coverage-audit-note-reviewer。

正文写作先读 study-note-unit-writer/references/body-example.tex，再读 references/unit-writing.md。样例示范表达，课程资料决定知识内容。知识点与定义直接展开，逐点三级星标，必要解释和步骤写足；删除铺垫、转场与重复，不设定义句数或字数目标，也不把定义展开成讲解段。

按内容选择表达：完整定义用文字，数理推导用数学链，课件文字推理用带前提和条件的逻辑链/分支图，分类比较用条目/表格。非定义性内容不铺成长解释段，逻辑链前后不重复讲解。保留 ★★★/★★/★。数学推导用 proofbox、例题用 examplebox；stepbox 仅用于独立可复用方法，formulabox 按需使用，不套固定流程。

主编负责来源范围、记号、分工、合并与交付；写作器交正文和必要疑点。委派时把写作器 SKILL.md、正文样例、写作要求的绝对路径一同交给子代理。默认就地完成，仅在用户要求时委派或独立审核。

整本笔记在标题区后、可选目录和正文之前放一张全局思维导图，参照数字经济的课程—模块—核心知识布局，由主编统一绘制。正文保留课件中的必要交点图、均衡图和比较表，重复与装饰图可省略；图表要求见写作器 unit-writing.md。

模板与样式在 auto-study-note-orchestrator/assets，使用 study-note-style-v3，四种蓝框（proofbox / examplebox / stepbox / formulabox）共用同一视觉。不要求逐批交接 JSON：多来源时主编用一份 review_notes.md 维护来源、星级依据、正文位置和疑点；公式速查按需在全部正文后集中一次。

先检查内容，再做编译与技术校验；脚本通过不表示内容合格。保留原资料；用户暂缓验证时说明未验证项。
