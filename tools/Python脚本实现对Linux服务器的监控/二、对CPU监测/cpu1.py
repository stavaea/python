# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2023/9/4 10:59
# @Author : waxberry
# @File : cpu1.py
# @Software : PyCharm

from __future__ import print_function
from collections import OrderedDict
import pprint

def CPUinfo():
    ''' Return the information in /proc/CPUinfo
    as a dictionary in the following format:
    CPU_info['proc0']={...}
    CPU_info['proc1']={...}
    '''
    CPUinfo = OrderedDict()
    procinfo = OrderedDict()
    nprocs = 0
    with open('/proc/cpuinfo') as f:
        for line in f:
            if not line.strip():
                # end of one processor
                CPUinfo['proc%s' % nprocs] = procinfo
                nprocs = nprocs + 1
                # Reset
                procinfo = OrderedDict()
            else:
                if len(line.split(':')) == 2:
                    procinfo[line.split(':')[0].strip()] = line.split(':')[1].strip()
                else:
                    procinfo[line.split(':')[0].strip()] = ''
    return CPUinfo

if __name__ == '__main__':
    CPUinfo = CPUinfo()
    for processor in CPUinfo.keys():
        print(CPUinfo[processor]['model name'])


# 可以使用 Python 命令运行脚本 cpu1.py 结果如下，
# [root@node6 py]# python cpu1.py

# 也可以使用 chmod 命令添加权限收直接运行 cpu1.py结果如下，
# [root@node6 py]# chmod +x cpu1.py
# [root@node6 py]# ./cpu1.py