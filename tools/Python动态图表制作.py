# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2023/9/19 10:16
# @Author : waxberry
# @File : Python动态图表制作.py
# @Software : PyCharm
import fig
# 如何使用 FuncAnimation？
# 这个过程始于以下两行代码：

import matplotlib.animation as ani
animator = ani.FuncAnimation(fig, chartfunc, interval = 100)


# 按照以下代码进行基本调用。另外，这里将采用大型流行病的传播数据作为案例数据（包括每天的死亡人数）。
import matplotlib.animation as ani
import matplotlib.pyplot as plt
import numpy as np
import pandas as pdurl = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv'
df = pd.read_csv(url, delimiter=',', header='infer')df_interest = df.loc[
    df['Country/Region'].isin(['United Kingdom', 'US', 'Italy', 'Germany'])
    & df['Province/State'].isna()]df_interest.rename(
    index=lambda x: df_interest.at[x, 'Country/Region'], inplace=True)
df1 = df_interest.transpose()df1 = df1.drop(['Province/State', 'Country/Region', 'Lat', 'Long'])
df1 = df1.loc[(df1 != 0).any(1)]
df1.index = pd.to_datetime(df1.index)


# 绘制三种常见动态图表

# 动态曲线图
import numpy as np
import matplotlib.pyplot as pltcolor = ['red', 'green', 'blue', 'orange']
fig = plt.figure()
plt.xticks(rotation=45, ha="right", rotation_mode="anchor") #rotate the x-axis values
plt.subplots_adjust(bottom = 0.2, top = 0.9) #ensuring the dates (on the x-axis) fit in the screen
plt.ylabel('No of Deaths')
plt.xlabel('Dates')
# 接下来设置 curve 函数，进而使用 .FuncAnimation 让它动起来：
def buildmebarchart(i=int):
    plt.legend(df1.columns)
    p = plt.plot(df1[:i].index, df1[:i].values) #note it only returns the dataset, up to the point i
    for i in range(0,4):
        p[i].set_color(color[i]) #set the colour of each curveimport matplotlib.animation as ani
animator = ani.FuncAnimation(fig, buildmebarchart, interval = 100)
plt.show()

# 动态饼状图
import numpy as np
import matplotlib.pyplot as pltfig
ax = plt.subplots()
explode=[0.01,0.01,0.01,0.01] #pop out each slice from the piedef getmepie(i):
    def absolute_value(val): #turn % back to a number
        a  = np.round(val/100.*df1.head(i).max().sum(), 0)
        return int(a)
    ax.clear()
    plot = df1.head(i).max().plot.pie(y=df1.columns,autopct=absolute_value, label='',explode = explode, shadow = True)
    plot.set_title('Total Number of Deaths\n' + str(df1.index[min( i, len(df1.index)-1 )].strftime('%y-%m-%d')), fontsize=12)import matplotlib.animation as ani
animator = ani.FuncAnimation(fig, getmepie, interval = 200)
plt.show()
# 主要区别在于，动态饼状图的代码每次循环都会返回一组数值，但在线型图中返回的是我们所在点之前的整个时间序列。
# 返回时间序列通过 df1.head(i) 来实现，而. max()则保证了我们仅获得最新的数据，因为流行病导致死亡的总数只有两种变化：维持现有数量或持续上升。
df1.head(i).max()

# 动态条形图
fig = plt.figure()
bar = ''
def buildmebarchart(i=int):
    iv = min(i, len(df1.index)-1) #the loop iterates an extra one time, which causes the dataframes to go out of bounds. This was the easiest (most lazy) way to solve this :)
    objects = df1.max().index
    y_pos = np.arange(len(objects))
    performance = df1.iloc[[iv]].values.tolist()[0]
    if bar == 'vertical':
        plt.bar(y_pos, performance, align='center', color=['red', 'green', 'blue', 'orange'])
        plt.xticks(y_pos, objects)
        plt.ylabel('Deaths')
        plt.xlabel('Countries')
        plt.title('Deaths per Country \n' + str(df1.index[iv].strftime('%y-%m-%d')))
    else:
        plt.barh(y_pos, performance, align='center', color=['red', 'green', 'blue', 'orange'])
        plt.yticks(y_pos, objects)
        plt.xlabel('Deaths')
        plt.ylabel('Countries')
        animator = ani.FuncAnimation(fig, buildmebarchart, interval=100)
        plt.show()

# 保存动画图
# 在制作完成后，存储这些动态图就非常简单了，可直接使用以下代码：
animator.save(r'C:\temp\myfirstAnimation.gif')