# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2023/4/11 9:41
# @Author : waxberry
# @File : 降雨天气查询.py
# @Software : PyCharm

import requests
from parsel import Selector
import json

# 获取省份信息
def getProvinces():
    province = []
    url_province = 'http://www.weather.com.cn/weathern/101070201.shtml'
    re = requests.get(url=url_province)
    select = Selector(re.content.decode('utf-8'))#构建selector
    result_province = select.xpath("/html/body/div[4]/div[1]/div/div/a")#使用上图中复制的xpath获取所有的a标签数据
    for url_province in result_province:
        url = url_province.xpath('@href').extract_first()#获取每个a标签的网址,省气象网站
        text = url_province.xpath('text()').extract_first()#获取每个a标签的文本内容，省
        province.append(text)
    return province

# 获取天气数据存放到本地
def getWeather(provinces, key):
    for province in provinces:
        url_citys = f'https://geoapi.qweather.com/v2/city/lookup?location={province}&key={key}'
        res_city = requests.get(url_citys)
        data_city = json.loads(res_city.text)#城市id数据
        for city in data_city['location']:
            if city['country'] == '中国' and province in city['adm1']:#过滤其他国家的数据
                url_weather = f"https://devapi.qweather.com/v7/weather/3d?location={city['id']}&key={key}"
                res_weather = requests.get(url_weather)
                data_city = json.loads(res_weather.text)#城市天气数据
                try:
                    for day in data_city['daily']:
                        if day['fxDate'] == '2023-04-05':#只获取清明节当天的数据
                            textDay = day['textDay']#白天天气情况
                            tempMax = day['tempMax']#最高温
                            tempMin = day['tempMin']#最低温
                            precip = day['precip']#总降水量
                            path = r'C:\Users\edz\Desktop\excel\weather.csv'#存放地址
                            with open(path, 'a+') as f:
                                line = province + ',' + city['name'] + ',' + textDay + ',' + tempMin + ',' + tempMax + ',' + precip + '\n'
                            f.write(line)
                except Exception as e:
                    print('error: %s' % e)

# 执行
if __name__ == '__main__':
    key = '73d20be1a74a43fea3894f72d8fbc845'
    provinces = getProvinces()
    getWeather(provinces, key)