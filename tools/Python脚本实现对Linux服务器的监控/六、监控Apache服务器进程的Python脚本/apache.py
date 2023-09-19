# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2023/9/4 11:26
# @Author : waxberry
# @File : apache.py
# @Software : PyCharm


import os, sys, time

while True:
    time.sleep(4)
    try:
        ret = os.popen("ps -C apache -o pid, cmd").readlines()
        if len(ret) < 2:
            print('apache 进程异常退出， 4 秒后重新启动')
            time.sleep(3)
            os.system('service apache2 restart')
    except:
        print('Error', sys.exc_info()[1])