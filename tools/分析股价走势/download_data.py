# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2024/1/19 9:58
# @Author : waxberry
# @File : download_data.py
# @Software : PyCharm

import yfinance as yf
import matplotlib.pyplot as plt

# 定义股票符号
stocks = ['PDD', 'BABA', 'JD']

# 下载每支股票的历史数据
data = yf.download(stocks, start='2020-01-01', end='2023-12-31')

# 绘制调整后的收盘价
plt.figure(figsize=(14, 7))
for stock in stocks:
    plt.plot(data[stock], label=stock)

plt.title('历史调整后收盘价（2020-2023）')
plt.xlabel('日期')
plt.ylabel('调整后收盘价（USD）')
plt.legend()
plt.show()

# 下载并绘制交易量数据
volume_data = yf.download(stocks, start='2020-01-01', end='2023-12-31')

plt.figure(figsize=(14, 7))
for stock in stocks:
    plt.plot(volume_data[stock], label=stock)

plt.title('历史交易量（2020-2023）')
plt.xlabel('日期')
plt.ylabel('交易量')
plt.legend()
plt.show()