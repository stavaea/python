# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2023/7/26 10:04
# @Author : waxberry
# @File : bath_path.py
# @Software : PyCharm

import os


# 项目根路径
_root_path = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]

# 报告路径
report_path = os.path.join(_root_path, 'testReport', 'report.html')

# 日志路径
log_path = os.path.join(_root_path, 'logs/')

# 配置文件路径
conf_path = os.path.join(_root_path, 'conf', 'auto_test.conf')

# 测试数据路径
testdatas_path = os.path.join(_root_path, 'testDatas')

# allure相关配置
_result_path = os.path.join(_root_path, 'testReport', 'result')
_allure_html_path = os.path.join(_root_path, 'testReport', 'allure_html')
allure_command = 'allure generate {} -o {} --clean'.format(_result_path, _allure_html_path)
