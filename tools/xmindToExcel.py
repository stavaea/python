# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2022/7/1 15:41
# @Author : waxberry
# @File : xmindToExcel.py
# @Software : PyCharm

import openpyxl
from tools import xmindData

str = '文件已打开，请关闭重试'

try:
    list1 = xmindData.XMindData.read_XMind_to_list('xmind文件,绝对路径')
    xm = xmindData.XMindData()
    title = xm.get_lists_title(list1[0]['topic']['title']) + '测试用例'

    wb = openpyxl.Workbook()
    sheet = wb.active
    for row in xm.get_lists_data(list1[0]['topic']['topics']):
        sheet.append(row)
    wb.save('excel.xlsx保存路径'.format(title))

except Exception:
    raise str