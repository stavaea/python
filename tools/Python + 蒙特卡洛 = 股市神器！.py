# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2024/2/5 9:40
# @Author : waxberry
# @File : Python + 蒙特卡洛 = 股市神器！.py
# @Software : PyCharm


# 定义了一个函数来获取调整后的收盘价数据。yfinanceget_yahoo_data
import yfinance as yf
def get_yahoo_data(ticker, start, end):
    data = yf.download(ticker, start=start, end=end)
    return data['Adj Close']




# 定义一个将执行模拟的函数。我们将使用历史每日回报来计算均值和标准差
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def monte_carlo_simulation(ticker, start, end, num_simulations):
    # Get historical data
    prices = get_yahoo_data(ticker, start, end)

    # Calculate daily returns
    daily_returns = prices.pct_change().dropna()

    # Calculate mean and standard deviation of daily returns
    mean_return = daily_returns.mean()
    std_dev = daily_returns.std()

    # Generate random numbers based on normal distribution
    simulations = np.random.normal(loc=mean_return, scale=std_dev, size=(num_simulations, len(prices)))

    # Calculate simulated prices
    simulated_prices = prices.iloc[-1] * (1 + simulations).cumprod(axis=1)

    # Visualize results
    plt.figure(figsize=(10, 6))
    plt.plot(simulated_prices.T, alpha=0.1)
    plt.title('Monte Carlo Simulation for {}'.format(ticker))
    plt.xlabel('Days')
    plt.ylabel('Price')
    plt.show()

# Define stock ticker and time period
ticker = '^MXX'
start_date = '2020-01-01'
end_date = '2024-01-25'

# Number of simulations
num_simulations = 10000

# Perform Monte Carlo simulation
monte_carlo_simulation(ticker, start_date, end_date, num_simulations)