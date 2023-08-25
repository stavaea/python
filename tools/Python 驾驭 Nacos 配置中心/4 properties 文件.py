# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2023/8/9 10:56
# @Author : waxberry
# @File : 4 properties 文件.py
# @Software : PyCharm

import nacos

# 解析Properties配置文件（Nacos）

# 初始化
def init(data_id, group):
    # 换行符进行分割，存入列表中
    config_list = client.get_config(data_id, group).split("\n")

    properties = {}
    for config_item in config_list:
        # 过滤有用的键值对
        if config_item.find('=') > 0:
            strs = config_item.replace('\n', '').split('=')
            properties[strs[0]] = strs[1]

    # 配置的地址
    address = properties['address']
    print(address)

# Nacos数据变动时触发
def nacos_data_change_callback(config):
    config_list = config['content'].split("\n")

    properties = {}
    for config_item in config_list:
        # 过滤有用部分
        if config_item.find('=') > 0:
            strs = config_item.replace('\n', '').split('=')
            properties[strs[0]] = strs[1]

    # 配置的地址
    address = properties['address']
    print("Nacos数据变动了，address：", address)