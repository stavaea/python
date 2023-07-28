# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2023/7/26 11:47
# @Author : waxberry
# @File : handle_allure.py
# @Software : PyCharm


import subprocess
from base.base_path import *


class HandleAllure(object):
    def execute_command(self):
        subprocess.call(allure_command, shell=True)

handle_allure = HandleAllure()