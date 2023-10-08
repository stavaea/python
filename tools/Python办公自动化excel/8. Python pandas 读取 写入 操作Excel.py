# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2023/7/31 14:39
# @Author : waxberry
# @File : 8. Python pandas 读取 写入 操作Excel.py
# @Software : PyCharm

import pandas as pd
from pandas import DataFrame

# 8.2 pandas读写Excel
# 程序示例：
# 3.8.2 pandas读写Excel
def fun3_8_2():
    data = pd.read_excel('3_8 pandas 修改操作练习.xlsx', sheet_name='Sheet1')
    print(data)

    # 增加行数据，在第5行新增
    data.loc[4] = ['4', 'john', 'pandas']

    # 增加列数据，给定默认值None
    data['new_col'] = None

    # 保存数据
    DataFrame(data).to_excel('new.xlsx', sheet_name='Sheet1', index=False, header=True)

if __name__ == '__main__':
    fun3_8_2()