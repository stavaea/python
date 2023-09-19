# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2023/9/4 11:08
# @Author : waxberry
# @File : cpu2.py
# @Software : PyCharm

import os

def load_stat():
    loadavg = {}
    f = open('/proc/loadavg')
    con = f.read().split()
    f.close()
    loadavg['lavg_1'] = con[0]
    loadavg['lavg_5'] = con[1]
    loadavg['lavg_15'] = con[2]
    loadavg['nr'] = con[3]
    loadavg['last_pid'] = con[4]
    return loadavg
print('loadavg', load_stat()['lavg_15'])

# 可以使用 Python 命令运行脚本 cpu2.py 结果如下，
# [root@node6 py]# python cpu2.py