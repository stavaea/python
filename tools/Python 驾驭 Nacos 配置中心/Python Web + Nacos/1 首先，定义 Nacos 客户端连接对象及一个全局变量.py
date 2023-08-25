# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2023/8/9 11:01
# @Author : waxberry
# @File : 1 首先，定义 Nacos 客户端连接对象及一个全局变量.py
# @Software : PyCharm

import nacos

client = nacos.NacosClient(f'{SERVER_ADDRESSES}:{SERVER_PORT}', namespace=NAMESPACE, username=USERNAME,
                           password=PASSWORD)

# 定义一个全局变量
arg1 = ''
