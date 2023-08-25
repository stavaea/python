# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2023/8/9 10:55
# @Author : waxberry
# @File : 2通过分组名和服务 ID 解析出某个服务的配置.py
# @Software : PyCharm


import yaml


# 初始化
def init(data_id, group):
    config = client.get_config(data_id, group)

    # 配置数据解析（YAML）
    config_data = yaml.load(config, Loader=yaml.FullLoader)

    # 通过键路径，解析出数据
    result = config_data['arg1']['arg2']

    print(result)

# 服务id（键）
data_id = "service_name"

# 分组名称，默认为：DEFAULT_GROUP
group = "DEFAULT_GROUP"

# 初始化解析
init(data_id, group)