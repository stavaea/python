# -*-coding:utf-8-*-
import time
import random

print time.time()
print time.ctime()
print time.ctime(1)
print time.asctime([2017, 10, 13, 13, 29, 18, 4, 286, 0])
print time.mktime(time.localtime())

# tuple_time可以不传，不传返回当前时间格式化后的结果
print time.strftime('%Y-%m-%d %H:%M:%S')
print time.strftime('%H:%M:%S %m/%d/%Y')
print time.strftime('%Y-%m-%d')

# 获取一个小时前的时间
print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()-3600))

print time.strptime('2017-03-15 08:00:00', '%Y-%m-%d %H:%M:%S')
print time.strptime('17:27:33 03/18/2017', '%H:%M:%S %m/%d/%Y')

'''0.编写一个方法，输出当前时间三天前的时间点，格式：2017-05-01_13:59:06 '''

def get_before3days():
    return time.strftime('%Y-%m-%d_%H:%M:%S', time.localtime(time.time()-259200))

print get_before3days()

'''1.编写一个方法，根据传入的美式时间字符串(13:28:06_12/21/2018)，生成标准时间字符串(2018-12-21_13:28:06)'''

def get_format_day(day):
    try:
        time_tuple = time.strptime(day, '%H:%M:%S_%m/%d/%Y')
        return time.strftime('%Y-%m-%d_%H:%M:%S', time_tuple)
    except:
        print '输入的日期字符串格式不正确："小时:分钟:秒数_月_天_年"'

print get_format_day('13:28:06_12/21/2018')

print random.randint(0, 10)
print random.random()
print random.randrange(0, 10)
print random.randrange(2, 12, 2)

array = [2, 3, 4, 5]
print random.sample(array, 2)