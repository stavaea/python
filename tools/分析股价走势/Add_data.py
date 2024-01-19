# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2024/1/19 11:08
# @Author : waxberry
# @File : Add_data.py
# @Software : PyCharm


import numpy as np
import matplotlib.pyplot as plt

# 假设 simulation_results 是我们之前模拟得到的字典
#  simulation_results = [PDD': [...]，BABA': [...]，JD!

# 绘制直方图并计算统计数据
plt.figure(figsize=(14, 7))
for stock in ['PDD', 'BABA', 'JD']:
    #计算平均值、5%分位数和95%分位数
    mean_value = np.mean(simulation_results[stock])
    percentile_5 = np.percentile(simulation_results[stock]
    percentile_95 = np.percentile(simulation_results[stock]
    #绘制直方图
    plt.hist(simulation_results[stock], bins=50, alpha=0.5)
    #在直方图上标记统计数据
    plt.axvline(mean_value, color='k',linestyle='dashed')
    plt.axvline(percentile_5, color='r', linestyle='dashed')
    plt.axvline(percentile_95, color = 'g',linestyle='dashed')
    # 添加注释
    plt.text(mean_value, 50, f'Mean: [mean_value:.2f]', rot)
    plt.text(percentile_5,50, f'5th percentile: {percentile}')
    plt.text(percentile_95,50,f'95th percentile:{percentile}'）
plt.title('Simulated Stock Prices Distribution with Mean and')
plt.xlabel('Simulated Price')
plt.ylabel('Frequency')
plt.legend()
plt.show()