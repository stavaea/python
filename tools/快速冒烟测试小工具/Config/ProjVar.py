# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2023/5/26 11:16
# @Author : waxberry
# @File : ProjVar.py
# @Software : PyCharm

import os
proj_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
conf_path = os.path.join(proj_path, '')
dbuser_ini_path = os.path.join(proj_path, '', 'Config/DbUser.ini')
driver_path = os.path.join(proj_path, '../Driver')
logger_path = os.path.join(proj_path, '', 'Logger.conf')
result_path = os.path.join(proj_path, '../TestResults')
testscript_path = os.path.join(proj_path, '../TestScripts')