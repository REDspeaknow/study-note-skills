# 学习笔记 Skills

这套 skill 将课程资料整理为版式统一、内容精练的中文 LaTeX/PDF 复习指南。来源清单负责逐项追踪，综合单元负责组织正文；清单的一行不等于笔记的一节。

正文首要规则是**禁止元视角写作与防御性写作，知识解释优先，案例按需保留**。直接解释含义、原因和必要推导；案例只在增加理解、示范应用或辨析边界时展开，具体条件与必要例题步骤须保留。完整规则见[写作与交接说明](study-note-unit-writer/references/unit-writing.md)。

- `auto-study-note-orchestrator`：盘点来源、设计综合单元、统稿去重、统一编写可选的末尾公式速查、编译与验收。
- `study-note-unit-writer`：一种综合写作角色，可由多个实例并行处理独立批次；每批同时处理概念、必要推导、案例和有依据的图表，只输出正文片段与独立交接记录。
- `coverage-audit-note-reviewer`：按需独立审查覆盖、推导、重复和 PDF 技术质量；不参与日常分批写作。

三项 skill 共用 `study-note-style-v1` 的视觉组件。总编排器的 `assets/` 包含模板和样式文件；`scripts/` 提供编译、交接契约校验、候选公式汇集和结构/PDF 校验。流程样例见 `auto-study-note-orchestrator/examples/ols-and-r-squared/`。交接逐项记录正文覆盖位置，主编维护 `issues.json` 保留问题及关闭依据，最终报告汇总覆盖对应表。全书至多在正文末尾有一个公式速查章节，可以按主题分表。概念型资料可省略它。

日常只维护三份共享记录：`source_inventory.md` 记来源要求，`synthesis_plan.md` 合并分工与公共设定，`issues.json` 记真实问题。覆盖状态从各批交接自动汇总，不再重复抄回来源清单；无问题时问题列表为 `[]`。

仓库中的旧概念、数学、图表三个专职写作 skill 已退休，可从 Git 历史取回。改动详情与尚未执行的校验见 [改动记录](CHANGELOG.md)。克隆或更新仓库不会自动覆盖个人 Skills 目录；需要启用新版时再安装这三个现行 skill。

调用示例：

```text
/auto-study-note-orchestrator 把指定的课程资料整理成简洁、可溯源的中文 LaTeX/PDF 复习指南。
```

在 Claude Code 的目标项目中，将三个现行 skill 文件夹放入 .claude/skills/，将本仓库 .claude/agents/ 下的[综合写作器](.claude/agents/study-note-unit-writer.md)和[独立审核器](.claude/agents/coverage-audit-note-reviewer.md)放入同名项目路径；跨项目安装也可使用个人目录 ~/.claude/skills/ 与 ~/.claude/agents/。两者分别提供写作规则与子代理注册，agents/openai.yaml 属于 Codex 元数据。仓库根目录的 skill 文件夹不会因被克隆就自动注册到 Claude Code。

完整流程见[编排、并行与统稿](auto-study-note-orchestrator/references/orchestration-workflow.md)：主代理统一设定，多实例并行写独立主题，有依赖的批次顺序推进，最后按教学顺序整合。课程章节按连贯问题分批，不设固定代理数量。常规批次只接收关键结果，最终集中审核。
