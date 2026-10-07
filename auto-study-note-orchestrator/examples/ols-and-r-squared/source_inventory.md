# 来源清单 — 一元回归讲义 handout-01（12 页）

`status` 在盘点时为 `pending`，本文件展示的是合并去重后的终态。
取值：`pending` / `represented` / `represented-indirectly` / `intentionally-omitted` / `weak` / `missing`。

| id | 来源 | 标题 | type | importance | 必留结果 | status |
| --- | --- | --- | --- | --- | --- | --- |
| L1-01 | p.3 | 总体回归函数与样本回归函数 | concept | 必背 | PRF 与 SRF 的对象不同，不可混用 | represented |
| L1-02 | p.4 | 最小二乘准则 | concept | 重点 | 最小化残差平方和 | represented |
| L1-03 | p.5 | 斜率的一阶条件 | derivation | 必背 | $\hat\beta_1=\hat S_{xy}/\hat S_{xx}$ 及 $\hat S_{xx}>0$ | represented |
| L1-04 | p.6 | 回归线的代数性质 | concept | 了解 | 残差和为零、回归线过均值点 | represented-indirectly |
| L1-05 | p.8 | 拟合优度 $R^2$ | concept | 重点 | $R^2$ 的平方和分解与定义 | represented |
| L1-06 | p.9 | $R^2$ 的常见误读 | case | 重点 | 高 $R^2$ 不等于因果或设定正确 | represented |

L1-04 标为 `represented-indirectly`：两条代数性质直接由 L1-03 的一阶条件落出，正文在推导尾部一段交代，
不单独设小节。
