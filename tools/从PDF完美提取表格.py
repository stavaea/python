# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2023/9/5 9:18
# @Author : waxberry
# @File : 从PDF完美提取表格.py
# @Software : PyCharm


import fitz

doc = fitz.open('filename')
page = doc[4]# 下标从0开始,第五页对应4
tables = page.find_tables()
df = tables[0].to_pandas()
df.to_excel('table.xlsx', index=False)