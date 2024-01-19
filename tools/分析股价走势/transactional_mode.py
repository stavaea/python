# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2024/1/19 10:33
# @Author : waxberry
# @File : transactional_mode.py
# @Software : PyCharm


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf

# 定义股票符号
# stocks = ['PDD'，BABA'，JD']
# 下载每只股票的历史数据
data = yf.download(stocks, start="2020-01-01", end="2023-12-31")
#计算移动平均线
short_window = 20
long_window = 50

for stock in stocks:
    data[f'{stock}_SMA20'] = data[stock].rolling(window=short )
    data[f'[stock]_SMA50'] = data[stock].rolling(window=long )
# 计算相对强弱指数(RS工)
def compute_rsi(data, window=14):
    delta = data.diff()
    up = delta.clip(lower=0)
    down = -1 * delta.clip(upper=0)
    ma_up = up.rolling(window).mean()
    ma_down = down.rolling(window).mean()
    rsi = 100(100(1 + ma_up / ma_down))
    return rsi

for stock in stocks:
    data[f'{stock}_RSI'] = compute_rsi(data[stock])
# 绘制带有SMA和RSI的数据
plt.figure(figsize=(14,10))
for i, stock in enumerate(stocks):
    plt.subplot(len(stocks), 1, i+1)
    plt.plot(data[stock],label=f'[stock] Price')
    plt.plot(data[f'[stock]_SMA20'], label='SMA 20 Days')
    plt.plot(data[f'[stock]_SMA50'], label='SMA 50 Days')
    plt.title(f'[stock] Stock Price with SMA and RSI')
    plt.legend()
plt.tight_layout()
plt.show()


# 绘制每只股票的RSI
plt.figure(figsize=(14, 10))
for i,stock in enumerate(stocks):
    plt.subplot(len(stocks), 1, i+1)
    plt.plot(data[f'[stock]_RSI'], label=f'[stock] RSI')
    plt.axhline(70, color='red',  linestyle='--')
    plt.axhline(30,  color='green', linestyle='--!')
    plt.title(f'{stock} RSI')
    plt.legend()
plt.tight_layout()
plt.show()