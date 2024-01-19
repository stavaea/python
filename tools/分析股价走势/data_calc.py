# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2024/1/19 10:07
# @Author : waxberry
# @File : data_calc.py
# @Software : PyCharm


import yfinance as yf
import matplotlib.pyplot as plt

# 定义股票符号
stocks = ['PDD', 'BABA', 'JD']

# 下载每支股票的历史数据
data = yf.download(stocks, start='2020-01-01', end='2023-12-31')

# 获取每只股票最大交易总额的日期
max_volume_dates = {stock: data['Voplume'][stock].idxmax() for }

# 计算每只股票的日收益率
daily_returns = data['Adj Close'].pct_change()

# 计算每只股票的累计收益率
cumulative_returns = (1 + daily_returns).cumprod()

# 绘制日收益率图表
plt.figure(figsize=(14, 7))
for stock in stocks:
    plt.plot(daily_returns[stock], label=f'{stock} Daily Ret ')
plt.title('Daily Returns of Stocks (2020-2023)')
plt.xlabel('Date')
plt.ylabel('Daily Returns')
plt.legend()
plt.show()
# 绘制累计收益率图表
plt.figure(figsize=(14, 7))
for stock in stocks:
    plt.plot(cumulative_returns[stock],label=f'{stock} Cum ')
plt.title('Cumulative Returns of Stocks (2020-2023)')
plt.xlabel('Date')
plt.ylabel('Cumulative Returns')
plt.legend()
plt.show()

# 输出最大交易总额的日期
print("Max Volume Dates :")
print(max_volume_dates)