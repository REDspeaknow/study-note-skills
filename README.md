# 学习笔记 Skills

这是一套用于把课程资料整理成中文 LaTeX/PDF 学习笔记的 Codex Skills。默认先写完整概念正文，再补充必要的推导与图表，并逐项核对来源覆盖情况。

全套笔记使用 `study-note-style-v1`，以 `通用笔记模板.tex` 为版式基准：紧凑的绿、蓝、米白配色；可点击且无红框的目录；西文使用 Times New Roman，数学使用 XITS Math；1–3 个正文主章节绘制核心知识关系导图，4 章及以上绘制章节关系导图；末尾使用按主题分组、可跨页的公式速查表。

## 组成

- `auto-study-note-orchestrator`：盘点资料、规划长资料批次、统筹写作、整合模板并完成最终检查。
- `concept-outline-note-writer`：编写定义、适用条件、相邻概念关系、案例、考试提示和易错点。
- `math-derivation-note-writer`：在概念正文之后补充推导，并整理简短的公式速查内容。
- `diagram-mechanism-note-writer`：判断图表是否必要，只绘制有资料依据的机制图或比较表。
- `coverage-audit-note-reviewer`：可在后期需要独立复核时检查覆盖情况、版式、字体、链接及 PDF 质量；不会在任务开始时自动创建。

权威模板与样式文件位于 `auto-study-note-orchestrator/assets/`。生成笔记时应复制这两个文件，不要重新拼写导言区。

## 安装与调用

将五个 Skill 文件夹复制到 Codex 的个人 Skills 目录：

```powershell
Copy-Item -Recurse .\auto-study-note-orchestrator,.\math-derivation-note-writer,.\concept-outline-note-writer,.\diagram-mechanism-note-writer,.\coverage-audit-note-reviewer "$env:USERPROFILE\.codex\skills"
```

调用总编排器时可以说：

```text
使用 $auto-study-note-orchestrator，把我指定的课程资料整理成采用 study-note-style-v1 的中文 LaTeX/PDF 学习笔记。
```

默认按内容类型安排概念、数学和图表写作器；用户可以明确要求不使用子代理。总编排器负责常规覆盖审计，独立覆盖审计器只在后期确有需要时使用。

## 编译与校验

先运行一次 XeLaTeX；仅当目录、书签或交叉引用尚未稳定时继续编译：

```powershell
python .\auto-study-note-orchestrator\scripts\compile_study_note.py `
  --tex '<输出目录>\notes.tex'
python .\auto-study-note-orchestrator\scripts\validate_study_note.py `
  --tex '<输出目录>\notes.tex' `
  --pdf '<输出目录>\notes.pdf' `
  --log '<输出目录>\notes.log' `
  --inventory '<输出目录>\source_inventory.md'
```

只读校验器检查样式版本、章节顺序、导图类型或省略原因、公式速查表接口、A4 页面、PDF 字体资源、链接边框、文字可提取性及编译错误，并报告概念与视觉内容数量。

笔记没有固定的最大页数。来源资料达到 80、120、200 页等阈值时，会加强逐项清单、分批和覆盖检查；`来源页数 / 8`、以及 200 页以上资料对应的 25 页，是“成品可能过短”的审计警示，不是输出页数上限。

`auto-study-note-orchestrator/tests/` 中的样例用于回归检查导图类型、多页目录、公式表跨页、字体和无边框链接。
