# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2023/8/9 10:54
# @Author : waxberry
# @File : 1YAML 配置文件.py
# @Software : PyCharm

import nacos

# 连接地址
SERVER_ADDRESSES = "192.*.*.*"
SERVER_PORT = '8848'

# 命名空间
NAMESPACE = "public"

# 账号信息
USERNAME = 'nacos'
PASSWORD = 'nacos'

# 创建一个连接对象
client = nacos.NacosClient(f'{SERVER_ADDRESSES}:{SERVER_PORT}', namespace=NAMESPACE, username=USERNAME,
                           password=PASSWORD)