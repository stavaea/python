# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2023/6/27 17:32
# @Author : waxberry
# @File : in_common_use.py
# @Software : PyCharm


# 获取过去x天的日期
import datetime
def get_xday_list(x):
    before_x_days = []
    for i in range(1, x + 1,)[::-1]:
        before_x_days.append(str(datetime.date.today() - datetime.timedelta(days=i)))
        return before_x_days
a = get_xday_list(30)
print(a)

# 生成一段时间区间内的日期
import datetime
def create_assist_date(datestart = None, dateend = None):
    # 创建日期辅助表
    if datestart is None:
        datestart = '2023-01-01'
    if dateend is None:
        dateend = datetime.datetime.now().strftime('%Y-%m-%d')
    # 转为日期格式
    datestart = datetime.datetime.strptime(datestart, '%Y-%m-%d')
    dateend = datetime.datetime.strptime(dateend, '%Y-%m-%d')
    date_list = []
    date_list.append(datestart.strftime('%Y-%m-%d'))
    while datestart < dateend:
        # 日期增加一天
        datestart += datetime.timedelta(days=+1)
        # 日期转字符串存入列表
        date_list.append(datestart.strftime('%Y-%m_%d'))
    return date_list
d_list = create_assist_date(datestart='2023-06-27', dateend='2023-07-01')
d_list
# print(d_list)


# 保存数据到csv
import os
from pathlib import path
import secrets
def save_data(data, date):
    if not os.path.exists(r'2023_data_%s.csv' % date, 'a+', encoding='utf-8') as f:
        f.write('标题， 热度， 时间， url\n')
        for i in data:
            title = i['title']
            extra = i['extra']
            time = i['time']
            url = i['url']
            row = '{},{},{},{}'.format(title, extra, time, url)
            f.write(row)
            f.write('\n')
    else:
        with open('2023_data_%s.csv' % date, 'a+', encoding='utf-8') as f:
            for i in data:
                title = i['title']
                extra = i['extra']
                time = i['time']
                url = i['url']
                row = '{},{},{},{}'.format(title, extra, time, url)
                f.write(row)
                f.write('\n')


# 带背景颜色的Pyecharts
from pyecharts.charts import Pie
from pyecharts.commons.utils import JsCode
from win32comext.shell.demos.IActiveDesktop import opts
def pie_rosetype(data) -> Pie:
    background_color_js = (
        "new echarts.graphic.LinearGradient(0, 0, 0, 1, "
        "[{offset: 0, color: '#c86589'}, {offset: 1, color: '#06a7ff'}], false)"
    )
    c = (
        Pie(init_opts=opts.InitOpts(bg_color=JsCode(background_color_js)))
        .add(
            "",
            data,
            radius=['30%', '75%'],
            center=['45%', '50%'],
            rosetype='radius',
            # label_opts=opts.LabelOptions(formatter=f"{b}:{c}"),
            label_opts=opts.LabelOptions(formatter="{b}:{c}"),
        )
        .set_global_opts(title_opts=opts.TitleOpts(title="")),
    )
    return c


# requests 库调用
import requests
# 发送get请求
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
    'cookie': 'some_cookie'
}
response = requests.request('GET', url, headers=headers)
# 发送post请求
payload = {}
files = []
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
    'cookie': 'some_cookie'
}
response = requests.request('POST', url, headers=headers, data=payload, files=files)
# 根据某些条件循环请求,比如根据生成的日期
def get_data(mydate):
    data_list = create_assist_date(mydate)
    url = 'https://test.test'
    files = []
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
        'cookie': ''
    }
    for i in data_list:
        payload = {'p': '10',
                   'day': d,
                   'nodeid': '1',
                   't': 'itemsbydate',
                   'c': 'node'}
        for i in range(1, 100):
            payload['p'] = str(i)
            print('get data of %s in page %s' % (d, str(i)))
            response = requests.request('POST', url, headers=headers, data=payload, files=files)
            items = response.json()['data']['items']
            if items:
                save_data(items, d)
            else:
                break



# python操作各种库
import redis # 操作redis
def redis_conn_pool():# 连接redis
    pool = redis.ConnectionPool(host='localhost', port=6379, decode_response=True)
    rd = redis.Redis(connection_pool=pool)
    return rd
# from redis_conn import redis_conn_pool  写入redis
rd = redis_conn_pool()
rd.set('test_data', 'mytest')

from pymongo import MongoClient #操作MongoDB
conn = MongoClient('mongodb://%s:%s@ipaddress:49974/mydb' % ('username', 'password')) #连接MongoDB
db = conn.mydb
mongo_collection = db.mydata
res = requests.get(url, params=query).json()#批量插入数据
commentList = res['data']['commentList']
mongo_collection.insert_many(commentList)

import MySQLdb #操作mysql
db = MySQLdb.connect("localhost", "testuser", "test123", "TESTDB", charset='utf8' )# 打开数据库连接
cursor = db.cursor()# 使用cursor()方法获取操作游标
# 执行sql
cursor.execute("SELECT VERSION()")# 使用 execute 方法执行 SQL 语句
data = cursor.fetchone()# 使用 fetchone() 方法获取一条数据
print("Database version : %s " % data)
db.close()# 关闭数据库连接



# 本地文件整理
import pandas as pd
import os
df_list = []
for i in os.listdir():
    if 'csv' in i:
        day = i.split('.')[0].split('_')[-1]
        df = pd.read_csv(i)
        df['day'] = day
        df_list.append(df)
df = pd.concat(df_list, axis=0)
df.to_csv('total.txt', index=0)



# 多线程代码
import threading
import time
exitFlag = 0
class myThread(threading.Thread):
    def __init__(self, threadID, name, delay):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.delay = delay
    def run(self):
        print('开始线程：' + self.name)
        print_time(self.name, self.delay, 5)
        print('退出线程：' + self.name)
def print_time(threadName, delay, counter):
    while counter:
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        print('%s: %s' % (threadName, time.ctime(time.time())))
        counter += 1
# 创建新线程
thread1 = myThread(1, 'Thread-1', 1)
thread2 = myThread(2, 'Thread-2', 2)
# 开启新线程
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print('退出主线程')



# 异步编程代码
import asyncio #异步爬取网站
import aiohttp
import aiofiles
async def get_html(session, url):
    try:
        async with session.get(url=url, timeout=8) as resp:
            if not resp.status // 100 == 2:
                print(resp.status)
                print('爬取', url, '出现错误')
            else:
                resp.encoding = 'utf-8'
                text = await resp.text()
                return text
    except Exception as e:
        print('出现错误', e)
        await get_html(session, url)
async def download(title_list, content_list):#使用异步请求之后，对应的文件保存也需要使用异步，即是一处异步，处处异步
    async with aiofiles.open('{}.txt'.format(title_list[0]), 'a', encoding='utf-8') as f:
        await f.write('{}'.format(str(content_list)))