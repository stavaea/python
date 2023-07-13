# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2023/7/11 16:42
# @Author : waxberry
# @File : 将所选文件夹下所有的Excel文件中的sheet表保存为单独的Excel文件.py
# @Software : PyCharm


import PySimpleGUI as sg
from pathlib import Path
import xlwings as xw


# 选择输入文件夹
INPUT_DIR = sg.popup_get_folder('文件夹路径')
if not INPUT_DIR:
    sg.popup('cancel', 'no folder selected')
    raise SystemExit('cancelling:no folder selected')
else:
    INPUT_DIR = Path(INPUT_DIR)

# 选择输出文件夹
OUTPUT_DIR = sg.popup_get_folder('文件夹路径')
if not OUTPUT_DIR:
    sg.popup('cancel', 'no folder selected')
    raise SystemExit('cancelling:no folder selected')
else:
    OUTPUT_DIR = Path(OUTPUT_DIR)

# 获取输入文件夹中所有xls格式文件的路径列表
files = list(INPUT_DIR.rglob('.xls'))

with xw.App(visible=False) as app:
    for index, file in enumerate(files):
        # 显示进度
        sg.one_line_progress_meter('current progress', index + 1, len(files))
        wb = app.books.open(file)
        # 提取sheet表为单独的excel表格
        for sheet in wb.sheets:
            wb_new = app.books.add()
            sheet.copy(after=wb_new.sheets[0])
            wb_new.sheets[0].delete()
            wb_new.save(OUTPUT_DIR / f'{file.stem}_{sheet.name}.xlsx')
            wb_new.close()
sg.popup_ok('Task Done')