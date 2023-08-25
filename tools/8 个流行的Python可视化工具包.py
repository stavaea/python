# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2023/8/9 11:05
# @Author : waxberry
# @File : 8 个流行的Python可视化工具包.py
# @Software : PyCharm

'''用 Matplotlib 及相关工具所做的示例图：
在处理篮球队薪资数据时，我想找出薪资中位数最高的团队。为了展示结果，我将每个球队的工资用颜色标成条形图，来说明球员加入哪一支球队才能获得更好的待遇。'''
import seaborn as sns
import matplotlib.pyplot as plt

color_order = ['xkcd:cerulean', 'xkcd:ocean',
                'xkcd:black','xkcd:royal purple',
                'xkcd:royal purple', 'xkcd:navy blue',
                'xkcd:powder blue', 'xkcd:light maroon',
                'xkcd:lightish blue','xkcd:navy']

sns.barplot(x=top10.Team,
            y=top10.Salary,
            palette=color_order).set_title('Teams with Highest Median Salary')

plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))

# 第二个图是回归实验残差的 Q-Q 图。这张图的主要目的是展示如何用尽量少的线条做出一张有用的图，当然也许它可能不那么美观。
import matplotlib.pyplot as plt
import scipy.stats as stats

#model2 is a regression model
log_resid = model2.predict(X_test)-y_test
stats.probplot(log_resid, dist="norm", plot=plt)
plt.title("Normal Q-Q plot")
plt.show()



# ggplot 代码的简单示例。我们先用 ggplot 实例化图，设置美化属性和数据，然后添加点、主题以及坐标轴和标题标签。
#All Salaries
ggplot(data=df, aes(x=season_start, y=salary, colour=team)) + geom_point() + theme(legend.position="none") + labs(title = 'Salary Over Time', x='Year', y='Salary ($)')



# Bokeh 具备可以做出专业图形和商业报表且便于使用的界面。根据 538 Masculinity Survey 数据集写了制作直方图的代码：
import pandas as pd
from bokeh.plotting import figure
from bokeh.io import show

# is_masc is a one-hot encoded dataframe of responses to the question:
# "Do you identify as masculine?"

#Dataframe Prep
counts = is_masc.sum()
resps = is_masc.columns

#Bokeh
p2 = figure(title='Do You View Yourself As Masculine?',
          x_axis_label='Response',
          y_axis_label='Count',
          x_range=list(resps))
p2.vbar(x=resps, top=counts, width=0.6, fill_color='red', line_color='black')
show(p2)

#Pandas
counts.plot(kind='bar')




'''Ploty 入门时有一些要注意的点：

安装时要有 API 秘钥，还要注册，不是只用 pip 安装就可以；

Plotly 所绘制的数据和布局对象是独一无二的，但并不直观；

图片布局对我来说没有用（40 行代码毫无意义！）'''

'''你可以在 Plotly 网站和 Python 环境中编辑图片；
支持交互式图片和商业报表；
Plotly 与 Mapbox 合作，可以自定义地图；
很有潜力绘制优秀图形。
以下是我针对这个包编写的代码：'''
#plot 1 - barplot
# **note** - the layout lines do nothing and trip no errors
data = [go.Bar(x=team_ave_df.team,
              y=team_ave_df.turnovers_per_mp)]

layout = go.Layout(

    title=go.layout.Title(
        text='Turnovers per Minute by Team',
        xref='paper',
        x=0
    ),

    xaxis=go.layout.XAxis(
        title = go.layout.xaxis.Title(
            text='Team',
            font=dict(
                    family='Courier New, monospace',
                    size=18,
                    color='#7f7f7f'
                )
        )
    ),

    yaxis=go.layout.YAxis(
        title = go.layout.yaxis.Title(
            text='Average Turnovers/Minute',
            font=dict(
                    family='Courier New, monospace',
                    size=18,
                    color='#7f7f7f'
                )
        )
    ),

    autosize=True,
    hovermode='closest')

py.iplot(figure_or_data=data, layout=layout, filename='jupyter-plot', sharing='public', fileopt='overwrite')



#plot 2 - attempt at a scatterplot
data = [go.Scatter(x=player_year.minutes_played,
                  y=player_year.salary,
                  marker=go.scatter.Marker(color='red',
                                          size=3))]

layout = go.Layout(title="test",
                xaxis=dict(title='why'),
                yaxis=dict(title='plotly'))

py.iplot(figure_or_data=data, layout=layout, filename='jupyter-plot2', sharing='public')

[Image: image.png]



'''使用 Pygal 非常简单：
实例化图片；
用图片目标属性格式化；
用 figure.add() 将数据添加到图片中。
'''






''' Networkx 是基于 matplotlib 的，但它仍是图形分析和可视化的绝佳解决方案。图形和网络不是我的专业领域，
但 Networkx 可以快速简便地用图形表示网络之间的连接。以下是我针对一个简单图形构建的不同的表示，
以及一些从斯坦福 SNAP 下载的代码（关于绘制小型 Facebook 网络）。
我按编号（1~10）用颜色编码了每个节点，代码如下：'''
options = {
    'node_color' : range(len(G)),
    'node_size' : 300,
    'width' : 1,
    'with_labels' : False,
    'cmap' : plt.cm.coolwarm
}
nx.draw(G, **options)
# 用于可视化上面提到的稀疏 Facebook 图形的代码如下：
import itertools
import networkx as nx
import matplotlib.pyplot as plt

f = open('data/facebook/1684.circles', 'r')
circles = [line.split() for line in f]
f.close()

network = []
for circ in circles:
    cleaned = [int(val) for val in circ[1:]]
    network.append(cleaned)

G = nx.Graph()
for v in network:
    G.add_nodes_from(v)

edges = [itertools.combinations(net,2) for net in network]

for edge_group in edges:
    G.add_edges_from(edge_group)

options = {
    'node_color' : 'lime',
    'node_size' : 3,
    'width' : 1,
    'with_labels' : False,
}
nx.draw(G, **options)

