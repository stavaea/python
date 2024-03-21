# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2024/3/21 15:17
# @Author : waxberry
# @File : AD_DA.py
# @Software : PyCharm

# 放在显控data文件夹下执行

import configparser
conf = configparser.ConfigParser()
conf.add_section("PHASE")
conf.set( "PHASE", 'AD', '0')
conf.set( "PHASE", 'DA', '03')
conf.write(open("RTS.ini", "w", encoding="utf-8"))
