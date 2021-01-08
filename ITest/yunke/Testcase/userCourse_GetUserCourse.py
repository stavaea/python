#coding:utf-8
from Provide import Configuration, TestProvide
import unittest
import time
import json
import HTMLTestRunnerCN
import requests
import sys
reload(sys)

class TestApi(unittest.TestCase):

    def setUp(self):
        # self.url = "http://dev.gn100.com/interface/"

        # self.res = TestProvide.login(self.res)
        self.timeStamp = int(time.time())
        self.params = {}
        self.params["time"] = self.timeStamp
        self.params["u"] = "a"
        self.params["v"] = "2"

        print ("\n"+"*"*20+"Test start"+"*"*20+"\n")

    def tearDown(self):
        print ("\n"+"*"*20+"Test end"+"*"*20+"\n")

    def test_GetUserCourse(self):
        '''我的课程'''
        params = {}
        timeStamp = int(time.time())
        params["time"] = self.timeStamp
        params["u"] = "a"
        params["params"] = {
                "userId": "751828",
                "subjectId": 0,
                "gradeId": 0,
                "pageNo": 1,
                "pageSize": 10
        }
        params["key"] = TestProvide.key(timeStamp, params["params"])
        print (params)

        headers = {"Content-Type": "application/json"}
        url = Configuration.HostUrl + "/interface/student/StudyCenter"
        response = requests.post(url=url, json=params, headers=headers)

        res = response.text
        # print res

        message = response.json()["message"]
        status_code = response.status_code

        self.assertEqual("success", message, "fail")
        self.assertEqual(200, status_code, "fail")

        print ('接口正确')