# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2023/8/9 10:55
# @Author : waxberry
# @File : 3通过分组名和服务 ID，使用 Nacos 连接信息添加一个监听事件，这样当 Nacos 配置变动时，程序能及时获取变动后的数据.py
# @Software : PyCharm


# Nacos数据变动时触发
def nacos_data_change_callback(config):
    # 数据解析
    nacos_data = yaml.load(config['content'], Loader=yaml.FullLoader)

    # 读取键值
    result = nacos_data['arg1']['arg2']
    print(result)

# 监听Nacos数据变动
def add_nacos_listener(data_id, group):
    client.add_config_watcher(data_id=data_id, group=group, cb=nacos_data_change_callback)

# 添加监听事件
add_nacos_listener(data_id, group)