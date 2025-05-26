# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2025/5/26 11:41
# @Author : waxberry
# @File : config_reader.py
# @Software : PyCharm



import configparser

def read_config():
    config = configparser.ConfigParser()
    config.read('config/config.ini')
    return config