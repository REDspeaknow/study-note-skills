# 旧工程交接兼容性样例

本目录维护已有 JSON 交接格式的兼容性，用于 check_handoffs.py 的回归检查。新版默认使用一份 review_notes.md，不要求这些流程产物；正文示例已改为 v2 的星标入口和蓝框。

u01_body.tex 演示 OLS 斜率推导，u02_body.tex 演示拟合优度并复用前一结果。merged.tex 是合并稿，末尾仅一处公式速查。交接 JSON 保留原覆盖位置与问题历史，供旧工程续写时参考。

需要编译时，把 ../../assets/study-note-style.sty 复制到临时输出目录，再复制 merged.tex 编译。版式基准是 assets/通用笔记模板.tex，星级示例不是实际考试证据。
