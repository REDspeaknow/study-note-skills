---
name: auto-study-note-orchestrator
description: Turn course materials into a concise, source-traceable Chinese LaTeX/PDF study guide with coherent learning units, necessary derivations, one document-level formula reference, and PDF quality checks.
---

# Auto Study Note Orchestrator

生成知识点可追踪、关键解释与推导清楚的中文复习资料。正文首要规则是**禁止元视角写作与防御性写作，知识解释优先、案例按需保留**；起草和统稿前读取[正文规则](../study-note-unit-writer/references/unit-writing.md)。模板或示例的表达与它冲突时，以该规则为准。

## 工作流

读取 `references/orchestration-workflow.md`，按以下流程执行：

1. **盘点。** 按来源列出必须保留的知识、推导和独特案例信息；一条清单不自动生成一个正文小节。
2. **分工。** 在综合计划中统一讲解归属、记号与依赖；同一种综合写作器可启动多个实例，并行处理前置条件齐备的独立批次。
3. **写作。** 每批交正文片段与交接 JSON；主编接收关键结果，维护公共设定和真实未决问题，再派发依赖批次。
4. **统稿。** 主编按教学顺序合并、补足解释、删去重复和无关案例细节，统一筛选至多一个位于全部正文之后的公式速查章节。
5. **验收。** 集中核对知识覆盖、解释充分性、推导和版式，编译并检查 PDF。独立审核器只在用户要求或存在具体疑点时调用。

## 交付

整本笔记使用 `references/style-contract.md` 与 `assets/` 中的统一样式。保留原资料和旧产物，交付 PDF、TeX、来源清单、综合计划与最终审核结果；流程记录留在正文之外。来源缺失、未完成项和用户暂缓的检查在交付说明中如实记录。
