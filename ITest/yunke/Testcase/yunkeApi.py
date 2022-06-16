#coding:utf-8
# from key import key,get_token
from yunke.Provide import Configuration, TestProvide
import unittest
import time
import json
import HTMLTestReportCN
import requests
import sys, importlib
importlib.reload(sys)



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

    def test_StudyCenter(self):
        '''学习中心'''
        params = {}
        timeStamp = int(time.time())
        params["time"] = self.timeStamp
        params["u"] = "a"
        params["params"] = {
                "userId": "4096133"
            }
        params["key"] = TestProvide.key(timeStamp, params["params"])
        # print params

        headers = {"Content-Type": "application/json"}
        url = Configuration.HostUrl + "/interface/student/StudyCenter"
        response = requests.post(url=url, json=params, headers=headers)

        res = response.text
        # print res

        message = response.json()["message"]
        status_code = response.status_code

        self.assertEqual("success", message, "fail")
        self.assertEqual(200, status_code, "fail")

        print ('学习中心接口正确')


    def test_CourseList(self):
        '''我的课程列表'''
        params = {}
        timeStamp = int(time.time())
        params["time"] = self.timeStamp
        params["u"] = "a"
        params["params"] = {
            "userId": "4096133"
        }
        params["key"] = TestProvide.key(timeStamp, params["params"])
        params["token"] = TestProvide.get_token(timeStamp, params["params"])
        # print params

        headers = {"Content-Type": "application/json"}
        url = Configuration.HostUrl + "/interface/student/courselist"
        response = requests.post(url=url, json=params, headers=headers)

        # res = response.text
        # print res

        message = response.json()["message"]
        status_code = response.status_code

        self.assertEqual("success", message, "fail")
        self.assertEqual(200, status_code, "fail")

        print ('我的课程列表接口正确')


    def test_StatList(self):
        '''学习报告'''
        params = {}
        timeStamp = int(time.time())
        params["time"] = self.timeStamp
        params["u"] = "a"
        params["params"] = {
            "userId": "4096133"
        }
        params["key"] = TestProvide.key(timeStamp, params["params"])
        # print params

        headers = {"Content-Type": "application/json"}
        url = Configuration.HostUrl + "/interface/student/statlist"
        response = requests.post(url=url, json=params, headers=headers)

        res = response.text
        # print res

        message = response.json()["message"]
        status_code = response.status_code

        self.assertEqual("success", message, "fail")
        self.assertEqual(200, status_code, "fail")

        print ('学习报告接口正确')


    def test_Message(self):
        '''系统消息'''
        params = {}
        timeStamp = int(time.time())
        params["time"] = self.timeStamp
        params["u"] = "a"
        params["params"] = {
            "userId": "4096133",
            "maxId": "1000"
        }
        params["key"] = TestProvide.key(timeStamp, params["params"])
        # print params

        headers = {"Content-Type": "application/json"}
        url = Configuration.HostUrl + "/interface/message/getdialoglistV2"
        response = requests.post(url=url, json=params, headers=headers)

        res = response.text
        # print res

        message = response.json()["message"]
        status_code = response.status_code

        self.assertEqual("success", message, "fail")
        self.assertEqual(200, status_code, "fail")

        print ('''系统消息接口正确''')


    def test_CenterTopNew(self):
        '''用户中心头部'''
        params = {}
        timeStamp = int(time.time())
        params["time"] = self.timeStamp
        params["u"] = "a"
        params["params"] = {
            "userId": "4096133"
        }
        params["key"] = TestProvide.key(timeStamp, params["params"])
        # print params

        headers = {"Content-Type": "application/json"}
        url = Configuration.HostUrl + "/interface/student/centertopNew"
        response = requests.post(url=url, json=params, headers=headers)

        res = response.text
        # print res

        message = response.json()["message"]
        status_code = response.status_code

        self.assertEqual("success", message, "fail")
        self.assertEqual(200, status_code, "fail")

        print ('用户中心头部接口正确')


    def test_MyDetailTop(self):
        '''我的课程详情头部信息'''
        params = {}
        timeStamp = int(time.time())
        params["time"] = self.timeStamp
        params["u"] = "a"
        params["params"] = {
            "userId": "4096133",
            "courseId": "596"
        }
        params["key"] = TestProvide.key(timeStamp, params["params"])
        # print params

        headers = {"Content-Type": "application/json"}
        url = Configuration.HostUrl + "/interface/course/MyDetailTop"
        response = requests.post(url=url, json=params, headers=headers)

        res = response.text
        # print res

        message = response.json()["message"]
        status_code = response.status_code

        self.assertEqual("success", message, "fail")
        self.assertEqual(200, status_code, "fail")

        print ('我的课程详情头部信息接口正确')


    def test_CommentNew(self):
        '''课程评论列表'''
        params = {}
        timeStamp = int(time.time())
        params["time"] = self.timeStamp
        params["u"] = "a"
        params["params"] = {
            "courseId": "596",
            "planId": "10578",
            # "userId": "4096133"
        }
        params["key"] = TestProvide.key(timeStamp, params["params"])
        # print params

        headers = {"Content-Type": "application/json"}
        url = Configuration.HostUrl + "/interface/course/CommentNew"
        response = requests.post(url=url, json=params, headers=headers)

        res = response.text
        # print res

        message = response.json()["message"]
        status_code = response.status_code

        self.assertEqual("success", message, "fail")
        self.assertEqual(200, status_code, "fail")

        print ('课程评论列表接口正确')


    def test_DetailPlans(self):
        '''课程详情排课列表'''
        params = {}
        timeStamp = int(time.time())
        params["time"] = self.timeStamp
        params["u"] = "a"
        params["params"] = {
            "userId": "4096133",
            "courseId": "596",
            "classId": "737",
            "page": "1",
            "length": "20"
        }
        params["key"] = TestProvide.key(timeStamp, params["params"])
        # print params

        headers = {"Content-Type": "application/json"}
        url = Configuration.HostUrl + "/interface/course/detailplans"
        response = requests.post(url=url, json=params, headers=headers)

        res = response.text
        # print res

        message = response.json()["message"]
        status_code = response.status_code

        self.assertEqual("success", message, "fail")
        self.assertEqual(200, status_code, "fail")

        print ('课程详情排课列表接口正确')

#
# if __name__ == "__main__":
#     unittest.main()