# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2023/9/4 11:12
# @Author : waxberry
# @File : mem.py
# @Software : PyCharm


from __future__ import  print_function
from collections import OrderedDict

def meminfo():
    ''' Return the information in /proc/meminfo
    as a dictionary
    '''
    meminfo = OrderedDict()
    with open('/proc/meminfo') as f:
        for line in f:
            meminfo[line.split(':')[0]] = line.split(':')[1].strip()
    return meminfo

if __name__ == '__main__':
    # print(meminfo())
    meminfo = meminfo()
    print('Total memory: {0}'.format(meminfo['MemTotal']))
    print('Free memory: {0}'.format(meminfo['MemFree']))

# 可以使用 Python 命令运行脚本 mem.py 结果如下，
# [root@node6 py]# python mem.py