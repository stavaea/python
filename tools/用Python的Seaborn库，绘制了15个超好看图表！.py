# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2023/8/25 9:29
# @Author : waxberry
# @File : 用Python的Seaborn库，绘制了15个超好看图表！.py
# @Software : PyCharm

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

print('\n')
data = pd.read_csv('iris.csv')
print(data[10:15])

# 查看不同种类数量情况.
print(data['species'].value_counts())


# 01. 柱状图
sns.barplot(x='species', y='petal_length', hue='species', data=data)
plt.show()

# 02. 散点图
sns.scatterplot(x='petal_length', y='sepal_length', hue='species', style='species', s=90, data=data)
plt.show()

# 03. 直方图
sns.histplot(x='sepal_length', kde=True, data=data)
plt.show()
# 两个变量的直方图.
sns.histplot(x='sepal_length', kde=True, hue='species', data=data)
plt.show()

# 04. 折线图
sns.lineplot(x='petal_length', y='petal_width', data=data)
plt.show()

# 05. 小提琴图
sns.violinplot(x='species', y='petal_length', data=data, hue='species')
plt.show()

# 06. 箱线图
sns.boxplot(x='species', y='sepal_length', data=data, hue='species')
plt.show()

# 07. 热力图
heat_corr = data.corr()
sns.heatmap(heat_corr, annot=True)
plt.show()

# 08. 点线图
sns.pointplot(x='species', y='petal_length', data=data, markers='^', color='g')
plt.show()

# 09. 密度图
sns.kdeplot(x='petal_length', data=data, hue='species', multiple='stack')
plt.show()
# 还可以修改密度图的显示方式，和等高线有点像.
sns.kdeplot(x='petal_length', y='sepal_length', data=data, hue='species')
plt.show()

# 10. 计数图
sns.countplot(x='species', data=data)
plt.show()

# 11. 分簇散点图
sns.swarmplot(x='sepal_length', y='species', data=data, hue='species', dodge=True, orient='h', size=8)
plt.show()

# 12. 特征图
sns.set(rc={'figure.figsize': (6, 3)})
sns.pairplot(data=data, hue='species')
plt.show()

# 13. FacetGrid
g = sns.FacetGrid(data, col='species', height=4, hue='species')
g.map(sns.histplot, 'petal_length')
plt.show()

# 14. 联合分布图
sns.jointplot(x='sepal_length', y='sepal_width', data=data, palette='Set2', hue='species')
plt.show()

# 15. 分类图
sns.catplot(data=data, x='petal_length', y='species', kind='violin', color='.9', inner=None)
sns.swarmplot(data=data, x='petal_length', y='species', size=3)
plt.show()