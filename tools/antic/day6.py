# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2022/8/29 10:03
# @Author : waxberry
# @File : day6.py
# @Software : PyCharm

import re
def get_str(path):
    f = open(path)
    data = f.read()
    f.close()
    return data

path = input('请输入文件路径：')
word = re.findall('([\u4e00-\u9fa5])', get_str(path))
print ('中文字符，除特殊字符外共：', len(word))