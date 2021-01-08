#coding:utf-8

import xlwings as xw

app = xw.App(visible=True, add_book=False)
wb = app.books.add()
wb = app.books.open(r'C:\Users\HP\Desktop\新建 Microsoft Excel 工作表.xlsx')

sht = wb.sheets[1]