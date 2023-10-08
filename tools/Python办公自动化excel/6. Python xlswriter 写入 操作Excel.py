# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2023/7/31 10:59
# @Author : waxberry
# @File : 6. Python xlswriter 写入 操作Excel.py
# @Software : PyCharm
import datetime

import XlsxWriter

# 2.创建excel文件
# 创建文件
workbook = XlsxWriter.workbook('new_excel.xlsx')

# 3.创建sheet
# 创建sheet
worksheet = workbook.add_workbook('first_sheet')

# 4.写入数据
# （1）写入文本
# 方法一
worksheet.write('A1', 'write something')
# 方法二
worksheet.write(1, 0, 'hello world')

# （2）写入数字
worksheet.write(0, 1, 32)
worksheet.write(1, 1, 32.3)

# （3）写入函数
worksheet.write(2, 1, '=sum(B1:B2)')

# （4）写入图片
# 插入图片
worksheet.insert_image(0, 5, 'test.png')
worksheet.insert_image(0, 5, 'test.png', {'url': 'http://httpbin.org'})

# （5）写入日期
d = workbook.add_format({'num_format': 'yyyy-mm-dd'})
worksheet.write(0, 2, datetime.datetime.strptime('2023-07-31', '%Y-%m-%d'), d)

# （6）设置行、列属性
# 设置行属性，行高设置为40
worksheet.set_row(0, 40)
# 设置列属性，把A到B列宽设置为20
worksheet.set_column('A:B', 20)


# 5.自定义格式
'''常用格式：
字体颜色：color
字体加粗：bold
字体大小：font_site
日期格式：num_format
超链接：url
下划线设置：underline
单元格颜色：bg_color
边框：border
对齐方式：align'''
# 自定义格式
f = workbook.add_format({'border': 1, 'font_size': 13, 'bold': True, 'align': 'center', 'bg_color': 'cccccc'})
worksheet.write('A3', 'python excel', f)
worksheet.set_row(0, 40, f)
worksheet.set_column('A:E', 20, f)


# 6.批量往单元格写入数据
# 批量往单元格写入数据
worksheet.write_column('A15', [1, 2, 3, 4, 5])  # 列写入，从A15开始
worksheet.write_row('A12', [6, 7, 8, 9])# 行写入，从A12开始


# 7.合并单元格写入
worksheet.merge_range(7, 5, 11, 8, 'merge_range')

# 8.关闭文件

workbook.close()



# 6.3 xlswriter 生成折线图
# 示例代码：
import xlsxwriter

# 创建一个excel
workbook = xlsxwriter.Workbook('chart_line.xlsx')
# 创建一个sheet
worksheet = workbook.add_worksheet()
# worksheet = workbook.add_worksheet("bug_analysis")

# 自定义样式，加粗
bold = workbook.add_format({'bold': 1})

# --------1、准备数据并写入excel---------------
# 向excel中写入数据，建立图标时要用到
heading = ['Number', 'testA', 'testB']
data = [
    ['2017-9-1', '2017-9-2', '2017-9-3', '2017-9-4', '2017-9-5', '2017-9-6'],
    [10, 40, 50, 20, 10, 50],
    [30, 60, 70, 50, 40, 30],
]

# 写入表头
worksheet.write_row('A1', headings, bold)
# 写入数据
worksheet.write_column('A2', data[0])
worksheet.write_column('B2', data[1])
worksheet.write_column('C2', data[2])

# --------2、生成图表并插入到excel---------------
# 创建一个柱状图(line chart)
chart_col = workbook.add_chart({'type': 'line'})

# 配置第一个系列数据
chart_col.add_series({
    # 这里的sheet1是默认的值，因为我们在新建sheet时没有指定sheet名
    # 如果我们新建sheet时设置了sheet名，这里就要设置成相应的值
    'name': '=Sheet1!$B$1',
    'categories': '=Sheet1!$A$2:$A$7',
    'values':   '=Sheet1!$B$2:$B$7',
    'line': {'color': 'red'},
})
# 配置第二个系列数据
chart_col.add_series(
    {
    'name': '=Sheet1!$C$1',
    'categories':  '=Sheet1!$A$2:$A$7',
    'values':   '=Sheet1!$C$2:$C$7',
    'line': {'color': 'yellow'},
    }
)
# 配置第二个系列数据(用了另一种语法)
# chart_col.add_series({
#     'name': ['Sheet1', 0, 2],
#     'categories': ['Sheet1', 1, 0, 6, 0],
#     'values': ['Sheet1', 1, 2, 6, 2],
#     'line': {'color': 'yellow'},
# })

# 设置图表的title 和 x，y轴信息
chart_col.set_title({'name': 'The xxx site Bug Analysis'})
chart_col.set_x_axis({'name': 'Test number'})
chart_col.set_y_axis({'name': 'Sample length(mm)'})

# 设置图表的风格
chart_col.set_style(1)

# 把图表插入到worksheet并设置偏移
worksheet.insert_chart('A10', chart_col, {'x_offset': 25, 'y_offset': 10})

workbook.close()



 # 6.4 xlswriter 生成柱状图
# 示例代码：
import xlsxwriter

# 创建一个excel
workbook = xlsxwriter.Workbook('chart_column.xlsx')
# 创建一个sheet
worksheet = workbook.add_worksheet()
# worksheet = workbook.add_worksheet("bug_analysis")

# 自定义样式，加粗
bold = workbook.add_format({'bold': 1})

# --------1、准备数据并写入excel---------------
# 向excel中写入数据，建立图标时要用到
headings = ['Number', 'TestA', 'TestB']
data = [
    ['2017-9-1', '2017-9-2', '2017-9-3', '2017-9-4', '2017-9-5', '2017-9-6'],
    [10, 40, 50, 20, 10, 50],
    [30, 60, 70, 50, 40, 30],
]

# 写入表头
worksheet.write_row('A1', headings, bold)

# 写入数据
worksheet.write_column('A2', data[0])
worksheet.write_column('B2', data[1])
worksheet.write_column('C2', data[2])

# --------2、生成图表并插入到excel---------------
# 创建一个柱状图(column chart)
chart_col = workbook.add_chart({'type': 'column'})

# 配置第一个系列数据
chart_col.add_series({
    # 这里的sheet1是默认的值，因为我们在新建sheet时没有指定sheet名
    # 如果我们新建sheet时设置了sheet名，这里就要设置成相应的值
    'name': '=Sheet1!$B$1',
    'categories': '=Sheet1!$A$2:$A$7',
    'values': '=Sheet1!$B$2:$B$7',
    'line': {'color': 'red'},
})

# 配置第二个系列数据(用了另一种语法)
chart_col.add_series({
    'name': '=Sheet1!$C$1',
    'categories':  '=Sheet1!$A$2:$A$7',
    'values':   '=Sheet1!$C$2:$C$7',
    'line': {'color': 'yellow'},
})

# 配置第二个系列数据(用了另一种语法)
# chart_col.add_series({
#     'name': ['Sheet1', 0, 2],
#     'categories': ['Sheet1', 1, 0, 6, 0],
#     'values': ['Sheet1', 1, 2, 6, 2],
#     'line': {'color': 'yellow'},
# })

# 设置图表的title 和 x，y轴信息
chart_col.set_title({'name': 'The xxx site Bug Analysis'})
chart_col.set_x_axis({'name': 'Test number'})
chart_col.set_y_axis({'name': 'Sample length(mm)'})

# 设置图表的风格
chart_col.set_style(1)
# 把图表插入到worksheet以及偏移
worksheet.insert_chart('A10', chart_col, {'x_offset': 25, 'y_offset': 10})

workbook.close()



# 6.5 xlswriter 生成饼图
# 示例代码：
import xlsxwriter

# 创建一个excel
workbook = xlsxwriter.Workbook('chart_pie.xlsx')
# 创建一个sheet
worksheet.workbook.add_sheet()

# 自定义样式，加粗
bold = workbook.add_format({'bold': 1})

# --------1、准备数据并写入excel---------------
# 向excel中写入数据，建立图标时要用到
data = [
    ['closed', 'active', 'reopen', 'NT'],
    [1012, 109, 123, 131],
]

# 写入数据
worksheet.write_row('A1', data[0], bold)
worksheet.write_row('A2', data[1])

# --------2、生成图表并插入到excel---------------
# 创建一个柱状图(pie chart)
chart_col = workbook.add_chart({'type': 'pie'})

# 配置第一个系列数据
chart_col.add_series({
    'name': 'Bug Analysis',
    'categories': '=Sheet1!$A$1:$D$1',
    'values': '=Sheet1!$A$2:$D$2',
    'points': [
        {'fill': {'color': '#00CD00'}},
        {'fill': {'color': 'red'}},
        {'fill': {'color': 'yellow'}},
        {'fill': {'color': 'gray'}},
    ],

})

# 设置图表的title 和 x，y轴信息
chart_col.set_title({'name': 'Bug Analysis'})
# 设置图表的风格
chart_col.set_style(10)
# 把图表插入到worksheet以及偏移
worksheet.insert_chart('B10', chart_col, {'x_offset': 25, 'y_offset': 10})
workbook.close()



# 6.6 实战训练
# 1.xlswriter新建并写入Excel
# 程序示例：
# 3.6.2 xlswriter新建并写入Excel
import xlsxwriter

def fun3_6_2():
    # 创建Exce并添加sheet
    workbook.xlsxwrite.Workbook('demo1.xlsx')
    worksheet = workbook.add_worksheet()
    # 设置列宽
    worksheet.set_column('A:A', 20)
    # 设置格式
    bold = workbook.add_format({'bold': True})
    # 添加文字内容
    worksheet.write('A1', 'Hello')
    # 按格式添加内容
    worksheet.write('A2', 'World', bold)
    # 写一些数字
    worksheet.write(2, 0, 123)
    worksheet.write(3, 0, 123.456)
    # 添加图片
    worksheet.insert_image('B5', 'demo.png')

    workbook.close()