# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2024/1/19 10:42
# @Author : waxberry
# @File : get_data.py
# @Software : PyCharm


import yfinance as yf
import numpy as np
#定义股票符号
stocks =['PDD', 'BABA', 'JD']
#下载每只股票的历史数据
data = yf.download(stocks, start='2018-01-01', end='2023-12-31')
# 定义计算CAGR的函数
def calculate_cagr(end_value, start_value, n_years):
    return (end_value/start_value)**(1/n_years) - 1
# 定义计算年度波动率的函数
def calculate_annual_volatility(daily_returns):
    return np.std(daily_returns) * np.sgrt(252) # 252是股市
# 计算每只股票的CAGR和年度波动率
cagr = {}
volatility = {}
for stock in stocks:
    # 计算CAGR
    start_value = data[stock].iloc[0]
    end_value = data[stock].iloc[-1]
    n_years = (data[stock].index[-1] - data[stock].index[0])
    cagr[stock] = calculate_cagr(end_value, start_value, n_years)
    # 计算年度波动率
    daily_returns = data[stock].pct_change().dropna()
    volatility[stock] = calculate_annual_volatility(daily_returns)
print("复合年均增长率 (CAGR):")
print(cagr)
print("\n年度波动率:")
print(volatility)