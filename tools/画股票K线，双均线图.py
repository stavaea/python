# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2023/12/20 9:59
# @Author : waxberry
# @File : 画股票K线，双均线图.py
# @Software : PyCharm


from pyecharts import options as opts
from pyecharts.charts import Kline
import pandas as pd

# 2.画出五粮液股票的K线图
# 画出五粮液股票的K线图
# 读取数据
file_path = 'xxxx.csv'
data = pd.read_csv(file_path)

# 将交易日期转换为列表
data_list = data['交易日期'].tolist()
# 将开盘价、收盘价、最低价和最高价组合成K线所需的格式
ohlc = data[['开盘价', '收盘价', '最低价', '最高价']].values.tolist()
# 创建K线图
kline = Kline()
kline.add_xaxis(data_list)
kline.add_yaxis('title', ohlc)
# 设置全局配置项
kline.set_global_opts(
    xaxis_opts=opts.AxisOpts(is_scale=True),
    yaxis_opts=opts.AxisOpts(is_scale=True, splitarea_opts=opts.SplitAreaOpts(is_show=True, areastyle_opts=True)),#areastyle_opts定义了区域的样式（如透明度）
    title_opts=opts.TitleOpts(title='xxx-xx天K线图')
)
# 渲染图表到HTML文件
kline.render('xxx_kline.html')

# 3.在图上标出最高价和最低价
# 创建k线图
kline = Kline()
kline.add_xaxis((data_list))
kline.add_yaxis(
    'xxx',
    ohlc,
    markpoint_opts=opts.MarkPointOpts(
        data=[
            opts.MarkPointItem(type_='max', name='最高价'),
            opts.MarkPointItem(type_='min', name='最低价')
        ]
    )
)

# 4.在图上画出10日MA均线
# 计算10日均线
ma10 = data['收盘价'].rolling(window=10).mean().dropna()
print(ma10)
start_date = ma10.index[0]

# 创建折线图以显示10日均线
line_ma10 = Kline()
line_ma10.add_xaxis(data_list[start_date:])
line_ma10.add_yaxis(
    'MA10',
    ma10.tolist(),
    is_smooth=True,
    is_symbol_show=False,#不显示均线的数据点符号
    lable_opts=opts.LabelOpts(is_show=False)#不显示均线的数据点标签
)
line_ma10.set_global_opts(legend_opts=opts.LegendOpts(pos_left='right'))
# 重叠k线图和均线图
kline.overlap(line_ma10)
# 创建grid
grid = Grid(init_opts=opts.InitOpts(width='1400px', height='800px'))
grid.add(
    Kline,
    grid_opts=opts.GridOpts(pos_left='10%', pos_right='10%', height='60%')
)
# 渲染图表到HTML文件
grid.render('kline_with_ma10_tooltip1.html')


# 5.在图上画出10日，20 日 双MA均线
# 计算20日均线
data['MA20'] = data['收盘价'].rolling(window=20, min_periods=1).mean().dropna()
# 创建折线图以显示20日均线
line_ma20 = Kline()
line_ma20.add_xaxis(data_list)
line_ma20.add_yaxis(
    'MA20',
    data['MA20'].tolist(),
    is_smooth=True,
    is_symbol_show=False,#不显示均线的数据点符号
    lable_opts=opts.LabelOpts(is_show=False)#不显示均线的数据点标签
)
# 重叠k线图和均线图
kline.overlap(line_ma10)
kline.overlap(line_ma20)
