# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2023/7/28 14:06
# @Author : waxberry
# @File : 1. Python xlrd 读取 操作Excel.py
# @Software : PyCharm

import xlrd

# 打开Excel文件读取数据
data = xlrd.open_workbook(r'filename')#文件名以及路径，如果路径或者文件名有中文给前面加一个 r

# （1）获取book（excel文件）中一个工作表
table = data.sheets()[0] #通过索引顺序获取
table = data.sheet_by_index(sheet_index) #通过索引顺序获取
table = data.sheet_by_name('sheet_name')#通过名称获取

    # 以上三个函数都会返回一个xlrd.sheet.Sheet()对象
names = data.sheet_names()#返回book中所有工作表的名字
data.sheet_loaded(sheet_name_or index) # 检查某个sheet是否导入完毕

# （2） 行的操作
nrows = table.nrows  # 获取该sheet中的行数，注，这里table.nrows后面不带().
table.row(rowx)# 返回由该行中所有的单元格对象组成的列表,这与tabel.raw()方法并没有区别。
table.row_slice(rowx) # 返回由该行中所有的单元格对象组成的列表
table.row_types(rowx, start_colx=0, end_col=None) # 返回由该行中所有单元格的数据类型组成的列表；返回值为逻辑值列表，若类型为empy则为0，否则为1
table.row_values(rowx, start_colx=0, end_colx=None) # 返回由该行中所有单元格的数据组成的列表
table.row_len(rowx)# 返回该行的有效单元格长度，即这一行有多少个数据

# （3）列（colnum）的操作
ncols = table.ncols# 获取列表的有效列数
table.col(colx, start_rowx=0, end_rowx=None) # 返回由该列中所有的单元格对象组成的列表
table.col_slice(colx, start_rowx=0, end_rowx=None)# 返回由该列中所有的单元格对象组成的列表
table.col_types(colx, start_rowx=0, end_rowx=None)# 返回由该列中所有单元格的数据类型组成的列表
table.col_values(colx, start_rowx=0, end_rowx=None)# 返回由该列中所有单元格的数据组成的列表

# （4）单元格的操作
table.cell(rowx, colx) # 返回单元格对象
table.cell_type(rowx, colx)# 返回对应位置单元格中的数据类型
table.cell_value(rowx, colx) # 返回对应位置单元格中的数据


# 1.4 实战训练
# 使用xlrd模块进行读取
xlsx = xlrd.open_workbook('filename_path')#./xxx.xlsx
# 通过sheet名查找：xlsx.sheet_by_name("sheet1")
# 通过索引查找：xlsx.sheet_by_index(3)
table = xlsx.sheet_by_index(0)

# 获取单个表格值 (2,1)表示获取第3行第2列单元格的值
value = table.cell_value(2, 1)
print('第3行2列的值为', value)

# 获取表格行数
nrows = table.nrows
print('表格一共有', nrows, '行')

# 获取第4列所有值（列表生成式）   列表生成式学习链接：https://www.liaoxuefeng.com/wiki/1016959663602400/1017317609699776
name_list = [str(table.cell_value(i, 3)) for i in range(1, nrows)]
print('第4列所有的值：', name_list)