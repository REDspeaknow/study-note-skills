# 学习笔记 Skills

这套 skill 将课程资料整理为版式统一、内容精练的中文 LaTeX/PDF 复习指南。来源清单负责逐项追踪，综合单元负责组织正文；清单的一行不等于笔记的一节。

- `auto-study-note-orchestrator`：盘点来源、设计综合单元、统稿去重、统一编写可选的末尾公式速查、编译与验收。
- `study-note-unit-writer`：一个写作器同时处理单元内的概念、必要推导、案例和有依据的图表。只输出正文片段与独立交接记录。
- `coverage-audit-note-reviewer`：按需独立审查覆盖、推导、重复和 PDF 技术质量；不参与日常分批写作。

三项 skill 共用 `study-note-style-v1` 的视觉组件。总编排器的 `assets/` 包含模板和样式文件；`scripts/` 提供编译、候选公式汇集和结构/PDF 校验。全书至多在正文末尾有一个公式速查章节，可以按主题分表。概念型资料可省略它。

仓库中的旧概念、数学、图表三个专职写作 skill 已退休，可从 Git 历史取回。改动详情与尚未执行的校验见 [改动记录](CHANGELOG.md)。克隆或更新仓库不会自动覆盖个人 Skills 目录；需要启用新版时再安装这三个现行 skill。

调用示例：

```text
使用 $auto-study-note-orchestrator，把指定的课程资料整理成简洁、可溯源的中文 LaTeX/PDF 复习指南。
```
