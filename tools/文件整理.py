# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2023/4/21 9:42
# @Author : waxberry
# @File : 文件整理.py
# @Software : PyCharm


import os
import shutil

files = os.listdir('.')

for f in files:
    if os.path.isfile(f) and not f.startswith('.'):
        size = os.path.getsize(f)
        if size < 1000:
            folder_name ='Under_one_MB'
            if not os.path.exists(folder_name):
                os.mkdir(folder_name)
                shutil.copy(f, folder_name)
            else:
                shutil.copy(f, folder_name)
        elif 10000 <= size < 2000:
            folder_name ='Under_two_MB'
            if not os.path.exists(folder_name):
                os.mkdir(folder_name)
                shutil.copy(f, folder_name)
            else:
                shutil.copy(f, folder_name)