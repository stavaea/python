#coding:utf-8

from Provide import Configuration, TestProvide
import unittest
import time
import json
import HTMLTestRunnerCN
import requests
import sys,importlib
importlib.reload(sys)

# class Api(unittest.TestCase):
#     def test_StudyCenter(self):
#         '''学习中心'''
#         params = {}
#         timeStamp = int(time.time())
#         params["appid"] = '101'
#         params["params"] = {
#                 "subname": "大步机构",
#                 "subdomain": "yoube",
#                 "scopes": "1,2",
#                 "real_name": "王大拿",
#                 "mobile": 18810300001
#             }
#         params["apphash"] = TestProvide.key(timeStamp, params["params"])
#         print params
#
#         headers = {"Content-Type": "application/json"}
#         url = Configuration.HostUrl + "openapi/org/addorg"
#         response = requests.post(url=url, json=params, headers=headers)
#
#         res = response.text
#         print res
#
#         message = response.json()["message"]
#         status_code = response.status_code
#
#         self.assertEqual("success", message, "fail")
#         self.assertEqual(200, status_code, "fail")
#
#         print '学习中心接口正确'


A = [5, 4]
B = A[:]
print (B)
B[1] = 2
print (A)