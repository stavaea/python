# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2023/4/17 11:00
# @Author : waxberry
# @File : 情人节.py
# @Software : PyCharm

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

'''
# 先送一朵玫瑰花
fig = plt.figure(figsize=(12, 10))
ax = fig.gca(projection="3d")
[x, t] = np.meshgrid(np.array(range(25))/24.0,
                     np.arange(0, 575.5, 0.5)/575*30*np.pi-4*np.pi
                     )
p = (np.pi/2) * np.exp(-t / (8*np.pi))

change = np.sin(20*t)/50
u = 1 - (1 - np.mod(3.3*t, 2*np.pi)/np.pi)**4/2+change
y = 2 * (x**2-x)**2*np.sin(p)
r = u * (x*np.sin(p)+y*np.cos(p))*1.5
h = u * (x*np.cos(p)-y*np.sin(p))

c = plt.get_cmap('magma')
surf = ax.plot_surface(r*np.cos(t), r*np.sin(t), h, rstride=1, cstride=1, cmap=c, linewidth=0, antialiased=True)

plt.show()

# 什么! 颜色太单一? 那来个五颜六色的
fig = plt.figure(figsize=(12, 10))
ax = fig.gca(projection='3d')

[x, t] = np.meshgrid(np.array(range(25)) / 24.0,
                     np.arange(0, 575.5, 0.5) / 575 * 17 * np.pi - 2 * np.pi)
p = (np.pi / 2) * np.exp(-t / (8 * np.pi))

u = 1 - (1 - np.mod(3.6 * t, 2 * np.pi) / np.pi) ** 4 / 2
y = 2 * (x ** 2 - x) ** 2 * np.sin(p)
r = u * (x * np.sin(p) + y * np.cos(p))
h = u * (x * np.cos(p) - y * np.sin(p))

c = cm.gist_rainbow_r
surf = ax.plot_surface(r * np.cos(t), r * np.sin(t), h, rstride=1, cstride=1, cmap=c, linewidth=0, antialiased=True)
plt.show()

# 把绿色去掉, 保留玫瑰花的红色
fig = plt.figure(figsize=(12, 10))
ax = fig.gca(projection='3d')

[x, t] = np.meshgrid(np.array(range(25)) / 24.0,
                     np.arange(0, 575.5, 0.5) / 575 * 17 * np.pi - 2 * np.pi)

p = (np.pi / 2) * np.exp(-t / (8 * np.pi))
u = 1 - (1 - np.mod(3.6 * t, 2 * np.pi) / np.pi) ** 4 / 2
y = 2 * (x ** 2 - x) ** 2 * np.sin(p)
r = u * (x * np.sin(p) + y * np.cos(p))
h = u * (x * np.cos(p) - y * np.sin(p))
c = cm.get_cmap('spring_r')

surf = ax.plot_surface(r * np.cos(t), r * np.sin(t), h, rstride=1, cstride=1, cmap=c, linewidth=0, antialiased=True)
plt.show()
'''
# 玫瑰花盛开! 祝你表白成功!
# ax = plt.subplots(subplot_kw={'projection': '3d'})
fig = plt.figure(figsize=(12, 10))
ax = fig.gca(projection='3d')

[x, t] = np.meshgrid(np.array(range(25)) / 24.0,
                     np.arange(0, 575.5, 0.5) / 575 * 6 * np.pi - 4*np.pi)
p = (np.pi / 2) * np.exp(-t / (8 * np.pi))

change = np.sin(10*t)/20
u = 1 - (1 - np.mod(5.2 * t, 2 * np.pi) / np.pi) ** 4 / 2 + change
y = 2 * (x ** 2 - x) ** 2 * np.sin(p)
r = u * (x * np.sin(p) + y * np.cos(p)) * 1.5
h = u * (x * np.cos(p) - y * np.sin(p))
c = plt.get_cmap('spring_r')

surf = ax.plot_surface(r * np.cos(t), r * np.sin(t), h, rstride=1, cstride=1, cmap=c, linewidth=0, antialiased=True)

plt.show()