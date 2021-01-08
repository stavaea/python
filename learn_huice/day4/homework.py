#coding:utf-8
import time
import random

'''1.编写一个方法，接受参数为一个列表：[2017, 01, 15] (不考虑1970.1.1之前的时间点)
随机输出2017.1.15日 00:00:00 之前的一个时间点，格式为：2017-01-01_13:59:06'''

def get_random_time(time_tuple):
    date_start = (1970, 1, 1, 8, 0, 0, -1, -1, -1)
    time_start = time.mktime(date_start)

    date_end = (time_tuple[0], time_tuple[1], time_tuple[2], 0, 0, 0, -1, -1, -1)
    time_end = time.mktime(date_end)

    random_time = random.uniform(time_start, time_end)
    result = time.strftime('%Y-%m-%d_%H:%M:%S', time.localtime(random_time))
    return result

print get_random_time([1980, 10, 01])

'''2.用python脚本，写一个斗地主的发牌程序
3个人每人17张，三张底牌归地主所有
要求：函数返回一个字典，{地主：[], 农民1:[], 农民2:[]}'''
result = {}
all = ['大王', '小王']
for x in ['红桃', '黑桃', '梅花', '方块']:
    for i in range(1, 14):
        all.append(x + str(i))

random.shuffle(all)
dipai = all[-3:]
all = all[:-3]

dizhu = all[::3] + dipai
nongmin1 = all[1::3]
nongmin2 = all[2::3]
result = {'地主': dizhu, '农民1': nongmin1, '农民2': nongmin2}

for key, value in result.items():
    print key + ':',
    for pai in value:
        print pai,
    print ''