# 连续性记录

只记可复用的定义、记号、结果键和正文标签，不复制正文。

## 定义

| 名称 | 含义 | 正文标签 | 所属批次 |
| --- | --- | --- | --- |
| 总体回归函数 | $E(y\mid x)=\beta_0+\beta_1x$，描述条件均值 | sec:prf-srf | U01 |
| 样本回归函数 | $\hat y=\hat\beta_0+\hat\beta_1x$，PRF 的样本对应物 | sec:prf-srf | U01 |
| 拟合优度 $R^2$ | 被回归解释的平方和占总平方和的比例 | sec:sst-decomp | U02 |

## 记号

| 记号 | 含义 | 正文标签 | 所属批次 |
| --- | --- | --- | --- |
| $\hat S_{xy}$ | $\sum_i(x_i-\bar x)(y_i-\bar y)$ | sec:foc | U01 |
| $\hat S_{xx}$ | $\sum_i(x_i-\bar x)^2$ | sec:foc | U01 |
| $\hat\beta_1$ | OLS 斜率估计量 | eq:ols-slope | U01 |
| $SST,SSE,SSR$ | 总平方和、被解释平方和、残差平方和 | sec:sst-decomp | U02 |

## 结果键

| key | 结果 | 正文标签 | 所属批次 |
| --- | --- | --- | --- |
| ols_slope | $\hat\beta_1=\hat S_{xy}/\hat S_{xx}$，需 $\hat S_{xx}>0$ | eq:ols-slope | U01 |
| r_squared | $R^2=SSE/SST=1-SSR/SST$ | eq:r-squared | U02 |

U02 复用 `ols_slope`：按 `unit-writing.md`，复用同一结果时沿用同一 key 并指向 U01 的正文位置，
不新建一条速查行。合并后 `ols_slope` 在正文只有一处解释。
