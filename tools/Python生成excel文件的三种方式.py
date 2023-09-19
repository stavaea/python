# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2023/9/19 10:08
# @Author : waxberry
# @File : Python生成excel文件的三种方式.py
# @Software : PyCharm


# xlrd是python的第3方库，需要通过pip进行安装
# pip install xlrd


# xlwt属于python的第3方库，需要通过pip进行安装
# pip install xlwt


# openpyxl是python的第3方库，需要通过pip进行安装
# pip install openpyxl


# pandas
# 写入Excel中数据的除了xlwt和openpyxl之外。Pandas也是可以实现这种功能的。
#
# 它纳入了大量库和一些标准的数据模型，提供了高效地操作大型数据集所需的工具，能使我们快速便捷地处理数据。接下来我们就看看如何用pandas读写excel。
#
# 1. 读取excel
# 读取excel主要通过read_excel函数实现，除了pandas还需要安装第三方库xlrd。
#
# 2. 写入excel
# 写入excel主要通过pandas构造DataFrame，调用to_excel方法实现。

# 标题列表
columns = []
# 数据列表
datas = []

with open('二手车.txt', encoding='utf-8') as fin:
    # 首行判断
    is_first_line = True
    for line in fin:
        line = line[:-1]
        if is_first_line:
            is_first_line = False
            columns = line.split('\t')
            continue
        datas.append(line.split('\t'))

ic(columns)
ic(datas)



# 使用xlwt生成xls的excel文件

# 使用xlwt生成xls的excel文件
import xlwt

workbook = xlwt.Workbook(encoding='utf-8')
sheet = workbook.add_sheet('瓜子二手车')

for col, column in enumerate(columns):
    sheet.write(0, col, column)

for row, data in enumerate(datas):
    for col, column_data in enumerate(data):
        sheet.write(row+1, col, column_data)

workbook.save('瓜子二手车1.xls')




# 使用openpyxl生成xlsx的excel文件

# 使用openpyxl生成xlsx的excel文件
from openpyxl import Workbook
workbook = Workbook()

sheet = workbook.active
sheet.title = '默认title'
sheet.append(columns)
for data in datas:
    sheet.append(data)
workbook.save('瓜子二手车2.xlsx')



# 使用pandas生成xlsx的excel文件

# 使用pandas生成xlsx的excel文件
import pandas as pd
rcv_data = pd.read_csv('二手车.txt', sep='\t')
rcv_data.head()
ic(rcv_data)
rcv_data.to_excel('瓜子二手车3.xlsx', index = False)