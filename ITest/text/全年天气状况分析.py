#coding:utf-8

import requests, bs4, pandas, matplotlib, seaborn, pyecharts

# 默认返回北京市2018年1月到12月的 url
def get_url(city='beijing'):
    for time in range(201801,201813):
        url = "http://lishi.tianqi.com/{}/{}.html".format(city, time)
        yield url


html = requests.get(url=url, headers=header, cookies=cookie)
soup = BeautifulSoup(html.content, 'html.parser')
date = soup.select("#tool_site > div.tqtongji2 > ul > li:nth-of-type(1) > a")
max_temp = soup.select("#tool_site > div.tqtongji2 > ul > li:nth-of-type(2)")
min_temp = soup.select("#tool_site > div.tqtongji2 > ul > li:nth-of-type(3)")
weather = soup.select("#tool_site > div.tqtongji2 > ul > li:nth-of-type(4)")
wind_direction = soup.select("#tool_site > div.tqtongji2 > ul > li:nth-of-type(5)")
date = [x.text for x in date]
max_temp = [x.text for x in max_temp[1:]]
min_temp = [x.text for x in min_temp[1:]]
weather = [x.text for x in weather[1:]]
wind_direction = [x.text for x in wind_direction[1:]]
data = pd.DataFrame([date, max_temp, min_temp, weather, wind_direction]).T

# 平均温度的分布
seaborn.distplot(result['平均温度'])
# 按月查看温度走势
result.groupby(result['日期'].apply(lambda x: x.month)).mean().plot(kind='line')
# 天气状况分布
seaborn.countplot(result['天气状况'])
# 各月降水天数统计
line = pyecharts.Line("各月降水天数统计")
line.add("降水天数", month, is_rain, is_fill=True, area_opacity=0.7, is_stack=True)
line.add("未降水天数", month, no_rain, is_fill=True, area_opacity=0.7, is_stack=True)
# 风向统计
directions = ['北风', '西北风', '西风', '西南风', '南风', '东南风', '东风', '东北风']
schema = []
v = []
days = result['风向'].value_counts()
for d in directions:
    schema.append((d,100))
    v.append(days[d])
v = [v]
radar = pyecharts.Radar()
radar.config(schema)
radar.add("风向统计", v, is_axisline_show=True)