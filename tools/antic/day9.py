# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2022/8/29 10:13
# @Author : waxberry
# @File : day9.py
# @Software : PyCharm

from translate import Translator

translator = Translator(to_lang='Chinese')

def get_str(path):
    f = open(path)
    data = f.read()
    f.close()
    return data

path = input('请输入文件路径：')
text = get_str(path)

translation = translator.translate(text)
print (translation)
