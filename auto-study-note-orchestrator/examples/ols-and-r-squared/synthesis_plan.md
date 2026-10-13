# 综合计划

交付范围：一元回归讲义 handout-01（12 页）的完整复习指南。execution_mode：`delegated`，按 `orchestration-workflow.md` 执行；本文件是静态样例，不虚构 agent ID。

## 写作批次

| 批次/正文顺序 | 来源 ID | 必须讲清的问题 | depends_on | 输出路径（相对此目录） | 状态 |
| --- | --- | --- | --- | --- | --- |
| U01 / 第 1 节 | L1-01, L1-02, L1-03, L1-04 | OLS 斜率如何从两个一阶条件得到？ | [] | u01_body.tex + u01_handoff.json | integrated |
| U02 / 第 2 节 | L1-05, L1-06 | 平方和为何可分解，R² 的含义与边界是什么？ | [U01] | u02_body.tex + u02_handoff.json | integrated |

两批同属“一元回归”章节。U02 依赖 U01 的结果，因而顺序推进；存在其他独立且就绪的主题时可并行。实际派发时提供输出绝对路径。续写保留示例已有标签。

## 公共设定

只记跨批复用内容，新增信息由主编从交接中合并。

| 定义/记号/结果键 | 含义 | 正文标签 | 归属 |
| --- | --- | --- | --- |
| 总体回归函数 | $E(y\mid x)=\beta_0+\beta_1x$，描述条件均值 | sec:prf-srf | U01 |
| 样本回归函数 | $\hat y=\hat\beta_0+\hat\beta_1x$，由样本估计 | sec:prf-srf | U01 |
| $\hat S_{xy}$ | $\sum_i(x_i-\bar x)(y_i-\bar y)$ | sec:foc | U01 |
| $\hat S_{xx}$ | $\sum_i(x_i-\bar x)^2$ | sec:foc | U01 |
| ols_slope | $\hat\beta_1=\hat S_{xy}/\hat S_{xx}$，需 $\hat S_{xx}>0$ | eq:ols-slope | U01 |
| $SST,SSE,SSR$ | 总平方和、被解释平方和、残差平方和 | sec:sst-decomp | U02 |
| r_squared | $R^2=SSE/SST=1-SSR/SST$，含截距 OLS 且 $SST>0$ | eq:r-squared | U02 |

U02 复用 `ols_slope` 的结果键与标签，主编最终只保留一条对应速查项。
