# coding: utf-8

import numpy as np


def sep(title):
    print("\n")
    print(title)
    print("-" * 10)


sep("题目1：多维数组索引")
arr = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
print("第二行第三列：", arr[1, 2])
print("前两行后两列：")
print(arr[:2, 1:])


sep("题目2：统计函数应用")
prices = np.array([100, 102, 101, 105, 107])
print("平均价格：", prices.mean())
print("价格波动率：", prices.std())
print("价格极差：", prices.max() - prices.min())


sep("题目3：条件筛选与where函数")
returns = np.array([0.05, -0.03, 0.12, -0.08, 0.02])
print(np.where(returns < 0, 0, returns))


sep("题目4：数组合并与拆分")
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
merged = np.vstack((arr1, arr2))
print("合并后：")
print(merged)
a, b = np.vsplit(merged, 2)
print("拆分1：")
print(a)
print("拆分2：")
print(b)


sep("题目5：线性代数求解")
A = np.array([[3, 2, 1], [1, 4, 2], [2, 1, 5]])
b = np.array([15, 20, 25])
x = np.linalg.solve(A, b)
print("x, y, z：", x)


sep("题目6：随机数生成与概率分布")
np.random.seed(0)
samples = np.random.normal(0.1, 0.2, 100)
print("下四分位数：", np.percentile(samples, 25))
print("上四分位数：", np.percentile(samples, 75))


sep("题目7：排序与索引")
returns = np.array([0.03, -0.02, 0.15, -0.05, 0.10])
idx = np.argsort(returns)[::-1]
print("降序索引：", idx)
print("对应收益率：", returns[idx])


sep("题目8：蒙特卡罗模拟")
np.random.seed(1)
n_sim = 10000
n_days = 252
S0 = 50
mu = 0.08
sigma = 0.25
dt = 1 / 252
shocks = np.random.normal((mu - 0.5 * sigma ** 2) * dt, sigma * np.sqrt(dt), (n_sim, n_days))
paths = S0 * np.exp(np.cumsum(shocks, axis=1))
final_prices = paths[:, -1]
ci = np.percentile(final_prices, [2.5, 97.5])
print("最终价格95%置信区间：", ci)


sep("题目9：投资组合优化")
returns = np.array([[0.02, 0.01, -0.005], [0.03, 0.02, -0.002], [-0.01, 0.005, 0.003]])
weights = np.array([0.4, 0.3, 0.3])
daily_return = returns @ weights
print("组合日收益率：", daily_return)


sep("题目10：布尔索引与数据筛选")
prices = np.array([[50, 52, 48], [55, 53, 49], [60, 58, 54]])
rows, cols = np.where(prices >= 55)
print("满足条件的元素：", prices[rows, cols])
print("行索引：", rows)
print("列索引：", cols)
