# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2023/12/7 14:32
# @Author : waxberry
# @File : 分析瑞幸和星巴克全国门店分布关系.py
# @Software : PyCharm


# 导入相关库
import pandas as pd
import requests
import time
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon

# 抽取星巴克和瑞幸门店数据，通过下秒机器人API调用
# 抽取星巴克门店数据
headers = { "x-token": "tk7a2980431688455e8976e4bad4d13d6a" }#token鉴权
starbucks_list = []
for i in range(1,10):
    response_1 = requests.get("http://app.chafer.nexadata.cn/openapi/v1/sheet/sht22nId5uouP2/records?size=500&page={0}".format(i), headers = headers)
    starbucks = response_1.json()['data']['list']
    starbucks = pd.DataFrame(starbucks)
    time.sleep(1)
    starbucks_list.append(starbucks)
starbucks = pd.concat(starbucks_list)
# 抽取瑞幸门店数据
luckin_list =[]
for j in range(1,9):
    response_2 = requests.get("http://app.chafer.nexadata.cn/openapi/v1/sheet/sht22nIeomVmYy/records?size=500&page={0}".format(j), headers = headers)
    luckin = response_2.json()['data']['list']
    luckin = pd.DataFrame(luckin )
    luckin_list.append(luckin)
    time.sleep(1)
luckin = pd.concat(luckin_list)

# 第三步：判断星巴克门店方圆500米范围内的瑞幸门店数

# 根据星巴克咖啡店坐标绘制半径为XX米的地理区域
def circle(data,radius):
    # radius 表示区域半径
    # 给定地理坐标
    center_latitude = float(data['维度'])
    center_longitude = float(data['经度'])
    # 创建圆形区域
    center_point = Point(center_longitude, center_latitude)
    circle = center_point.buffer(radius/111300)
    # 创建多边形区域
    polygon = Polygon(circle.exterior)
    return polygon

# 根据经纬度构建坐标点
def point(data):
    # 给定地理坐标
    center_latitude = float(data['维度'])
    center_longitude = float(data['经度'])
    # 创建坐标点
    center_point = Point(center_longitude, center_latitude)
    return center_point

# 判断瑞幸咖啡店是否在星巴克方圆500m范围内
def is_inside(data):
    polygon = data['Polygon']
    # 判断坐标是否在区域内
    n = 0
    luckin_city = luckin[luckin['城市']==data['城市']]
    for point in luckin_city['Point']:
        is_inside = polygon.contains(point)
        # 打印判断结果
        if is_inside:
            n = n + 1
    return n

# 根据星巴克门店坐标位置绘制方圆半径为500米的地理区域
starbucks['Polygon'] = starbucks.apply(circle,axis=1,args=(500,))

# 根据瑞幸门店经纬度构建坐标点
luckin['Point'] = luckin.apply(point, axis=1)

# 判断瑞幸门店是否在星巴克门店方圆500米范围内
starbucks['Luckin_numbers'] = starbucks.apply(is_inside, axis=1)


# 第四步：分析数据

# 方圆500米范围内，全国平均每个星巴克门店周边有0.6个瑞幸门店
starbucks['Luckin_numbers'].mean()
# 输出：0.6

# 方圆500米范围内，最多的星巴克门店周边有7个瑞幸门店
starbucks['Luckin_numbers'].max()
# 输出：7

# 方圆500米范围内，星巴克门店周边平均瑞幸门店数各城市排名
# 最多的是临沂市平均每个星巴克门店周边有1.8个瑞幸门店
city_list = []
for city in pd.unique(starbucks['城市']):
    avg_luckin_numbers = starbucks[starbucks['城市']==city]['Luckin_numbers'].mean()
    starbucks_nums = starbucks[starbucks['城市']==city]['名称'].count()
    city_list.append([city,starbucks_nums,avg_luckin_numbers])

df = pd.DataFrame(city_list,columns=['city','starbucks_nums','avg_luckin_numbers'])
df.sort_values(by=['avg_luckin_numbers'],axis=0,ascending=False)