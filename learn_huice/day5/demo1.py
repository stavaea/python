#!/usr/bin/env python
#-*- coding:utf-8 -*-
import os

'''report文件夹中，是所有自动化测试报告的存放路径。
编写new_report函数，传入路径。返回最新一份报告的文件名(完整路径+文件名)
    1.报告以时间戳命名
    *2.报告不以时间戳命名'''

# path = 'C:\Users\HP\Desktop\\report\\'
# list = os.listdir(path)
# result = []
# for l in list:
#     if os.path.isfile(path+l):
#         result.append(l)
# print path + sorted(result, reverse=True)[0]

def new_report(path):
    # path = 'C:\Users\HP\Desktop\\report\\'
    list = os.listdir(path)
    result = []
    for l in list:
        if os.path.isfile(path):
            result.append(l)
    path + result.sort(key=lambda x: os.path.getmtime(path), reverse=True)
    print(os.path.join(path, list[0]))

new_report('C:\Users\HP\Desktop\\report\\')