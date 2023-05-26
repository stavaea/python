# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2023/5/26 11:21
# @Author : waxberry
# @File : ReadConfig.py
# @Software : PyCharm

import configparser
import os
import platform
from tools.快速冒烟测试小工具.Config.ProjVar import *

def read_ini_file(ini_file_path, section_name, option_name):
    # 创建一个读取配置文件的实例
    cf = configparser.ConfigParser()
    # 将配置文件内容加载到内存
    cf.read(ini_file_path)
    try:
        # 根据section和option获取配置文件中的数据
        value = cf.get(section_name, option_name)
    except:
        print("the specific section or the specific option does't exit!")
        return None
    else:
        return value