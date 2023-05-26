# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2023/5/24 9:13
# @Author : waxberry
# @File : bsApi.py
# @Software : PyCharm

import unittest
import json
import HTMLTestRunnerCN
import requests
import sys
import importlib
import time
importlib.reload(sys)

class TestApi(unittest.TestCase):
    def setUp(self):
        self.timeStamp = time.time()
        self.params = {}
        self.params['time'] = self.timeStamp

        print("\n"+"*"*20+"Test Start"+"*"*20+"\n")

    def tearDown(self):
        print("\n"+"*"*20+"Test End"+"*"*20+"\n")

