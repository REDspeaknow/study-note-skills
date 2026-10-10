# Study Note Skills — Claude Code 协作说明

默认使用中文，用户要求优先。按当前角色读取对应 skill：主代理使用 auto-study-note-orchestrator，写作实例使用 study-note-unit-writer，按需独立审核使用 coverage-audit-note-reviewer。

起草、统稿和审核均遵守 study-note-unit-writer/references/unit-writing.md 中的正文最高规则：**禁止元视角写作与防御性写作，知识解释优先，案例按需保留。** 完整定义和取舍标准只在该文件维护。

主代理按 auto-study-note-orchestrator/references/orchestration-workflow.md 盘点、分工、调度和统稿。同一种综合写作器可有多个实例并行处理独立批次，有依赖的批次在前置结果确认后推进；主代理统一记号、讲解归属和共享记录，最后按教学顺序整合。

每个写作实例只交分配的正文片段及交接 JSON。整本文档结构与可选的末尾一次性公式速查由主代理编写，版式沿用 study-note-style-v1。来源清单负责追踪，不规定正文栏目或案例篇幅。

保留原资料与旧产物。用户暂缓测试或编译时交付未验证草稿，并在交付说明中记录暂缓项。
