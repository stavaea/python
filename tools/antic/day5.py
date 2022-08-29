# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2022/8/29 9:59
# @Author : waxberry
# @File : day5.py
# @Software : PyCharm

import hashlib, os

def getMD5(filepath):
    f = open(filepath, 'rb')
    md5obj = hashlib.md5()
    md5obj.update(f.read())
    hash = md5obj.hexdigest()
    f.close()
    return str(hash).upper()

path = input('请输入需要重复文件过滤文件夹路径：')
file_list = os.listdir(path)
file_md5 = []

for filename in file_list:
    md5val = getMD5(path+filename)
    if md5val in file_md5:
        os.remove(path + filename)
    else:
        file_md5.append(md5val)
print ('处理完毕...')