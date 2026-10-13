# Study Note Skills — Claude Code 使用说明

默认使用中文，用户要求优先。按角色读取 auto-study-note-orchestrator、study-note-unit-writer 或 coverage-audit-note-reviewer 的 SKILL.md。

正文表达统一读取 study-note-unit-writer/references/unit-writing.md：每个独立知识点有三级星标入口，必要推导与例题用蓝框，保留关键步骤并精简衔接和重复。

主代理按 auto-study-note-orchestrator/references/orchestration-workflow.md 核实来源、归组知识点、统稿和验收，版式使用 study-note-style-v2。默认就地完成；用户要求委派或独立审核时，使用对应代理。分批只是执行范围，不自动生成正文标题。

新任务默认不要求逐批交接 JSON。写作实例交指定正文和必要疑点，主代理维护统一来源记录；已有工程明确需要时可沿用原交接工具。公式速查按需在全部正文后集中添加一次。

保留原资料与旧产物。用户暂缓测试或编译时，交付说明标明未验证项。
