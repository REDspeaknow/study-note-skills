# Study Note Skills — Claude Code 使用说明

默认使用中文，用户要求优先。按角色读取 auto-study-note-orchestrator、study-note-unit-writer 或 coverage-audit-note-reviewer 的 SKILL.md。

正文表达先读 study-note-unit-writer/references/unit-writing.md 及其链接的 reference-calibration.md：知识点边界清楚、定义准确、各点直接展开，删除铺垫与转场，保留必要解释。模型参数和运算步骤不各自加星；一个完整推导/例题一个蓝边框，辅助公式可无框。旧稿需重组内容，不能只换标题与框外壳。

主代理按 auto-study-note-orchestrator/references/orchestration-workflow.md 核实来源、归组知识点、统稿和验收，版式使用 study-note-style-v3（细蓝边、暖白底、小号字、框内题头）。先完成代表稿自审，再展开全书；先核对内容，再做技术检查。脚本通过不表示内容合格。默认就地完成；用户要求委派或独立审核时，使用对应代理。分批只是执行范围，不自动生成正文标题。

新任务默认不要求逐批交接 JSON。写作实例交指定正文和必要疑点，主代理维护统一来源记录；已有工程明确需要时可沿用原交接工具。公式速查按需在全部正文后集中添加一次。

定义不设句数或字数上限：与课程定义相比，关键特征和条件必须完整；必要解释写足。精简只针对衔接与重复，不以“一点一句”压缩知识，也不因星级低而删掉定义条件。

保留原资料与旧产物。用户暂缓测试或编译时，交付说明标明未验证项。
