# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2023/7/26 11:44
# @Author : waxberry
# @File : handle_config.py
# @Software : PyCharm

import configparser

# 配置文件类
class HandleConfig:
    def operation_config(self, conf_file, section, option):
        cf = configparser.ConfigParser() #实例化
        cf.read(conf_file)
        value = cf.get(section, option) #定位
        return value


handle_config = HandleConfig()


if __name__ == '__main__':
    from base.base_path import *
    base_url = handle_config.operation_config(conf_path, 'BASEURL', 'base_url')
    print(base_url)
