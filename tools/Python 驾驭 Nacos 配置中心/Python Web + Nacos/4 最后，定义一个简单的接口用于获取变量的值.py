# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2023/8/9 11:03
# @Author : waxberry
# @File : 4 最后，定义一个简单的接口用于获取变量的值.py
# @Software : PyCharm


# 定义一个全局变量
arg1 = ''

@app.get("/")
async def index():
    global arg1
    return {"message": arg1}