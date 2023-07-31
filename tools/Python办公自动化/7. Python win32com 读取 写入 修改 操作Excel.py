# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2023/7/31 14:30
# @Author : waxberry
# @File : 7. Python win32com 读取 写入 修改 操作Excel.py
# @Software : PyCharm

import pypiwin32

# 7.2 Python使用win32com读写Excel
# 程序示例：
import win32com
from win32com.client import Dispatch, constants
import os

# 获取当前脚本路径
def getScriptPath():
    nowpath = os.path.split(os.path.realpath(__file__))[0]
    print(nowpath)
    return nowpath

# 3.7.2 Python使用win32com读写Excel
def fun3_7_2():
    app = win32com.client.Dispatch('Excel.Application')

    # 后台运行，不显示，不警告
    app.Visible = 0
    app.DisplayAlerts = 0

    # 创建新的Excel
    # WorkBook = app.Workbooks.Add()
    # 新建sheet
    # sheet = WorkBook.Worksheets.Add()

    # 打开已存在表格，注意这里要用绝对路径
    WorkBook = app.Workbooks.Open(getScriptPath() + '\\3_7 win32com修改操作练习.xlsx')
    sheet = WorkBook.Worksheets('sheet1')

    # 获取单元格信息 第n行n列，不用-1
    cell01_value = sheet.Cells(1, 2).Value
    print("cell01的内容为：", cell01_value)

    # 写入表格的信息
    sheet.Cells(2, 1).Value = 'win32com'

    # 保存表格
    # WorkBook.Save()

    # 另存为实现拷贝
    WorkBook.SaveAs(getScriptPath() + '\\new.xlsx')

    # 关闭表格
    WorkBook.close()
    app.quit()

if __name__ == '__main__':
    fun3_7_2()