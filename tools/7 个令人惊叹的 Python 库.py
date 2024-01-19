# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2024/1/19 15:23
# @Author : waxberry
# @File : 7 个令人惊叹的 Python 库.py
# @Software : PyCharm



# Pendulum
# 2、实例化时区和时区换算：
# 导入库
# import library
import pendulum
dt = pendulum.datetime(2023, 6, 8)
print(dt)

# 2.2 local() 使用本地时区
#local() 使用本地时区
local = pendulum.local(2023, 6, 8)
print("本地时间：", local)
print("本地时区：", local.timezone.name)

# 2.3 创建日期时间实例
# Printing UTC time
utc = pendulum.now('UTC')
print("Current UTC time:", utc)

# 2.4 将 UTC 时区转换为欧洲/巴黎时间
# 将UTC 时区转换为欧洲/巴黎时间
europe = utc.in_timezone('Europe/Paris')
print("巴黎当前时间：", europe)




# FTFY
# 例
print(ftfy.fix_text('Correct the sentence using â€œftfyâ€\x9d.'))
print(ftfy.fix_text('âœ” No problems with text'))
print(ftfy.fix_text('Ã perturber la rÃ©flexion'))






# Sketch
# 为用户的查询提供基于文本的响应。
# Importing libraries
import sketch
import pandas as pd
file = "D://7 Datasciense//DS_visilization//altair//airports.csv"
# Reading the data (using twitter data as an example)
df = pd.read_csv(file)
print(df)

# 问表单有哪些项目
df.sketch.ask("Which columns are category type?")
# iata, name, city, state, country

# 合并到下一个命令输出截图
# 描述表单的形状行和列的大小
df.sketch.ask("What is the shape of the dataframe")

# 请用一段代码实现可视化
df.sketch.howto("Visualize the emotions")




# pgeocode 地理编码
# 获取特定邮政编码的地理信息
# Checking for country "India"
nomi = pgeocode.Nominatim('In')
# Getting geo information by passing the postcodes
nomi.query_postal_code(["620018", "620017", "620012"])

# 通过将国家和邮政编码作为输入来计算两个邮政编码之间的距离，结果以公里为单位：
# 两个邮政编码之间的物理距离
distance = pgeocode.GeoDistance('In')
distance.query_postal_code("620018", "620012")




# rembg
# 例
# Importing libraries
from rembg import remove
import cv2
# path of input image (my file: image.jpeg)
input_path = 'image.jpeg'
# path for saving output image and saving as a output.jpeg
output_path = 'output.jpeg'
# Reading the input image
input = cv2.imread(input_path)
# Removing background
output = remove(input)
# Saving file
cv2.imwrite(output_path, output)





# Humanize
# 示例-整数
# Importing library
import humanize
import datetime as dt
# Formatting  numbers with comma
a =  humanize.intcomma(951009)
# converting numbers into words
b = humanize.intword(10046328394)
#printing
print(a)
print(b)

# 示例日期和时间
import humanize
import datetime as dt
a = humanize.naturaldate(dt.date(2012, 6, 5))
b = humanize.naturalday(dt.date(2012, 6, 5))
print(a)
print(b)





# 开放街道地图 OSM 数据
# 必要的模块
import os
from os.path import join
import osmnx
import pandas as pd

# 全局路径变量
main_path = "your_main_path"
data_path = join(main_path, "data")

# 为感兴趣的数据指定所有相关参数，包括我们要提取的地点类型以及地理位置。
cities = ["Berlin, Germany", "Hamburg, Germany"]
places = ["restaurant", "bar"]

# 自动设置文件夹结构。
for p in places:
    isExist = os.path.exists(join(data_path, p))
    if not isExist:
        os.makedirs(join(data_path, p))

# 定义了一个时间戳，即检索OSM快照的时间点。这是按如下方式完成的：
# 设置时间戳
settings = '[out:json][timeout:180][date:"{year}-12-31T00:00:00Z"]'

# 定义的最后一个参数是时间范围。
years = ["2020", "2021"]

# 列表来存储收集的数据。
# 用于存储数据
extracted_data = []

# 遍历所有选项。
# 循环年份并在地点获取时间快照：
#   对于城市中的城市： 对于年份：
# 定义标签标签

for place in places:
    for city in cities:
        for year in years:
            # 定义标签
            tag = {"amenity" : place}

             # 设置提取年份
            osmnx.settings.overpass_settings = settings.format(year = year)

            # 提取标签和年份的数据
            tagged_data = osmnx.geometries_from_place(city, tags = tag)

            # 添加快照年份
            tagged_data["snap_year"] = year

             # 导出数据
            filename = str(place) + "_" + str(year) + "_" + str(city) + ".csv"
            path = join(data_path, place)
            tagged_data.to_csv(join(path, filename))

             # 打印以查看代码在打印时
            extracted_data.append(tagged_data)

            # 追加列表以存储数据
            print(f"Extraction of {year} and {city} for {tag} completed")