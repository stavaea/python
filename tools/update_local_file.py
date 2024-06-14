#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2024/6/5 11:30
@Author  : waxberry
@File    : update_local_file.py
@Software: PyCharm
"""
import json

# 定义文件名和要修改的字段路径（例如，'data.field'）
filename = 'config.json'
field_path = 'config.SystemParameters.SystemVibration'  # 假设要修改的字段是嵌套在'data'下的'field'
new_value = '24'

# 读取JSON文件内容
with open(filename, 'r') as file:
    data = json.load(file)

# 使用点表示法或字典的get方法修改嵌套字段
# 注意：这里需要处理可能的KeyError或AttributeError
keys = field_path.split('.')
current_level = data
for key in keys[:-1]:
    current_level = current_level.get(key, {})
current_level[keys[-1]] = new_value

# 写入修改后的JSON内容到文件
with open(filename, 'w') as file:
    json.dump(data, file, indent=4)  # indent=4 用于美化输出，可选
