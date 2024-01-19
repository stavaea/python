# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2024/1/19 10:48
# @Author : waxberry
# @File : sampled_data.py
# @Software : PyCharm


import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt

# 定义股票符号
# stocks = ['PDD'，BABA'，JD']
# 下载每只股票的历史数据
data = yf.download(stocks, start="2020-01-01", end="2023-12-31")

# 初始化模拟的结果
simulation_results = {}
simulated_daily_returns = {}

# 模拟未来252个交易日
for stock in stocks:
    # 计算历史日收益率
    daily_returns = data[stock].pct_change().dropna()
    mean_return = daily_returns.mean()
    std_deviation = daily_returns.std()
    # 基于历史收益率的正态分布进行随机抽样
    future_returns = np.random.normal(mean_return, std_deviation)
    simulated_daily_returns[stock] = future_returns
    #计算潜在的未来价格
    last_price = data[stock].iloc[-1]
    prices = [last_price * (1 + i) for i in np.cumprod(1 + future_returns)
    simulation_results[stock] = prices


# 绘制股票价格模拟图表
plt.figure(figsize=(14, 7))
for stock in stocks:
    plt.plot(simulation_results[stock], label=stock)
plt.title('Simulated Stock Prices for the Next 252 Trading')
plt.xlabel('Days')
plt.ylabel('Price')
plt.legend()
plt.show()


# 绘制模拟的每日收益直方图
plt.figure(figsize=(14, 7))
for stock in stocks:
    plt.hist(simulated_daily_returns[stock], bins=50, alpha= )
plt.title('Histogram of Simulated Daily Returns Over 252 Tr')
plt.xlabel('Daily Returns')
plt.ylabel('Frequency')
plt.legend()
plt.show()