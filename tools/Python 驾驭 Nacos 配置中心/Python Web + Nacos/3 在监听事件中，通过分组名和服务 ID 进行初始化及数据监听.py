# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2023/8/9 11:03
# @Author : waxberry
# @File : 3 在监听事件中，通过分组名和服务 ID 进行初始化及数据监听.py
# @Software : PyCharm

# Nacos初始化
async def init(data_id, group):
    global arg1
    # 换行符进行分割，存入列表中
    config_list = client.get_config(data_id, group).split("\n")
    ...
    # 配置的地址
    arg1 = properties['address']

    print("arg1:", arg1)

# Nacos数据变动时触发
def nacos_data_change_callback(config):
    global arg1
    config_list = config['content'].split("\n")
    ...
    # 配置的地址
    arg1 = properties['address']

    print("arg1:", arg1)


async def event_listener():
    data_id = "service_name"
    group = "DEFAULT_GROUP"

    # 初始化
    await  init(data_id, group)

    # Nacos配置监听，用于数据变动监听
    client.add_config_watcher(data_id=data_id, group=group, cb=nacos_data_change_callback)