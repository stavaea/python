# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2023/4/20 9:28
# @Author : waxberry
# @File : test.py
# @Software : PyCharm


from matplotlib import pyplot as plt
import pandas as pd
import pynimate as nim
import matplotlib
matplotlib.use('qt5agg')

df = pd.DataFrame(
    {
        'time': ['1960-01-01', '1961-01-01', '1962-01-01'],
        'Afghanistan': [1, 2, 3],
        'Angola': [2, 3, 4],
        'Albania': [1, 2, 5],
        'USA': [5, 3, 4],
        'Argentina': [1, 4, 5]
    }
).set_index('time')

cnv = nim.Canvas()
bar = nim.Barplot(df, '%Y-%m-%d', '2d')
bar.set_time(callback=lambda i, datafier: datafier.data.index[i].year)
cnv.add_plot(bar)
cnv.animate()
plt.show()