# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2023/5/26 13:57
# @Author : waxberry
# @File : DateToday.py
# @Software : PyCharm

import os
import time
from tools.快速冒烟测试小工具.Config.ProjVar import *

# 创建日期格式文件夹
def make_date_dir(dir_path):
    if os.path.exists(dir_path):
        # 获取当前时间
        timeTup = time.localtime()
        # 转为xxxx年xx月xx日的格式
        currenDate = str(timeTup.tm_year) + '年' + str(timeTup.tm_mon) + '月' + str(timeTup.tm_mday) + '日'
        # 用目标目录拼接日期得到绝对路径
        path = os.path.join(dir_path, currenDate)
        if not os.path.exists(path):
            os.mkdir()
    else:
        raise Exception('dir_path does not exist')
    return path

# 创建日期文件夹下多次执行的目录
def make_report_dir():
    # 先创建一个日期格式为名称的文件夹
    date_path = make_date_dir(result_path)
    # 判断当前目录已有文件夹数,加1得到新文件夹名并创建
    report_path = os.path.join(date_path, '第' + str(len(os.listdir(date_path)) + 1) + '次测试')
    os.mkdir(report_path)
    # 进入到新创建文件夹并获取当前的绝对路径,作为后面存放测试结果的文件夹
    os.chdir(report_path)
    result_report_path = os.getcwd()
    return result_report_path