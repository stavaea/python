# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2024/1/19 10:55
# @Author : waxberry
# @File : save.py
# @Software : PyCharm


import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt

# 定义股票符号
# stocks = ['PDD'，BABA'，JD']
# 下载每只股票的历史数据
data = yf.download(stocks, start="2020-01-01", end="2023-12-31")

# 初始化模拟结果的字典
simulation_results = {stock: [] for stock in stocks}


#对每只股票进行1000次模拟
num_simulations = 1000
num_days = 252# 大约一年的交易日

for stock in stocks:
    # 计算历史日收益率
    daily_returns = data[stock].pct_change().dropna()
    mean_return = daily_returns.mean()
    std_deviation = daily_returns.std()
    # 进行1000次模拟
    for _ in range(num_simulations):
        #基于历史收益率的正态分布进行随机抽样
        future_returns = np.random.normal(mean_return, std_deviation)# 计算潜在的未来价格
        last_price = data[stock].iloc[-1]
        prices = [last_price * (1 + i) for i in np.cumprod(1)]
        simulation_results[stock].append(prices[-1])


# 绘制模拟结果的直方图
plt.figure(figsize=(14, 7))
for stock in stocks:
    plt.hist(simulation_results[stock], bins=50, alpha=0.5)
plt.title('Histogram of Simulated Stock Prices After 252 Day')
plt.xlabel('Simulated Price')
plt.ylabel('Frequency')
plt.legend()
plt.show()