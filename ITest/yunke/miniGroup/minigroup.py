#coding:utf-8
# from key import key,get_token
from yunke.Provide import Configuration, TestProvide
import unittest
import time
import json
import HTMLTestReportCN
import requests
import sys,importlib
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

    def test_MyOrder(self):
        '''我的待支付订单'''
        params = {}
        timeStamp = int(time.time())
        token = TestProvide.get_token(timeStamp, params["params"])
        params["time"] = self.timeStamp
        params["u"] = "a"
        params["params"] = {
                "userId": "4096133",
                "page": "1",
                "length": "20",
                "type": "1",  #1.待支付，2.已支付，3.失效
                "token": token
            }
        params["apphash"] = TestProvide.key(timeStamp, params["params"])
        # print params
        #params["token"] = TestProvide.get_token(timeStamp, params["params"])

        headers = {"Content-Type": "application/json"}
        url = Configuration.HostUrl + "/openapi/student/myorder "
        response = requests.post(url=url, json=params, headers=headers)

        #res = response.text
        # print res

        message = response.json()["message"]
        result = response.json()["result"]
        code = response.code

        self.assertEqual("success", message, "fail")
        self.assertEqual(0, code, "fail")
        self.assertEqual('initoal', result['list']['status'], 'fail')

        print ('我的订单接口正确')

    def test_My_Order(self):
        '''我的已支付订单'''
        params = {}
        timeStamp = int(time.time())
        token = TestProvide.get_token(timeStamp, params["params"])
        params["time"] = self.timeStamp
        params["u"] = "a"
        params["params"] = {
                "userId": "4096133",
                "page": "1",
                "length": "20",
                "type": "2",  #1.待支付，2.已支付，3.失效
                "token": token
            }
        params["apphash"] = TestProvide.key(timeStamp, params["params"])
        # print params
        #params["token"] = TestProvide.get_token(timeStamp, params["params"])

        headers = {"Content-Type": "application/json"}
        url = Configuration.HostUrl + "/openapi/student/myorder "
        response = requests.post(url=url, json=params, headers=headers)

        #res = response.text
        # print res

        message = response.json()["message"]
        result = response.json()["result"]
        code = response.code

        self.assertEqual("success", message, "fail")
        self.assertEqual(0, code, "fail")
        self.assertEqual('success', result['list']['status'], 'fail')

        print ('我的订单接口正确')

    def test_My__Order(self):
        '''我的失效订单'''
        params = {}
        timeStamp = int(time.time())
        token = TestProvide.get_token(timeStamp, params["params"])
        params["time"] = self.timeStamp
        params["u"] = "a"
        params["params"] = {
                "userId": "4096133",
                "page": "1",
                "length": "20",
                "type": "3",  #1.待支付，2.已支付，3.失效
                "token": token
            }
        params["apphash"] = TestProvide.key(timeStamp, params["params"])
        # print params
        #params["token"] = TestProvide.get_token(timeStamp, params["params"])

        headers = {"Content-Type": "application/json"}
        url = Configuration.HostUrl + "/openapi/student/myorder "
        response = requests.post(url=url, json=params, headers=headers)

        #res = response.text
        # print res

        message = response.json()["message"]
        result = response.json()["result"]
        code = response.code

        self.assertEqual("success", message, "fail")
        self.assertEqual(0, code, "fail")
        self.assertEqual('expired', result['list']['status'], 'fail')

        print ('我的订单接口正确')


    def test_AddOrder(self):
        '''提交订单返回正确'''
        params = {}
        timeStamp = int(time.time())
        params["time"] = self.timeStamp
        params["u"] = "a"
        params["params"] = {
            "userId": "4096133",
            "classId": "59",
            "courseId": "94",
            "price": "30.01",
            "priceOld": "0",
            "groupId": "0",
            "code": " ",
            "deviceType": "x"
        }
        params["apphash"] = TestProvide.key(timeStamp, params["params"])
        #params["token"] = TestProvide.get_token(timeStamp, params["params"])
        # print params

        headers = {"Content-Type": "application/json"}
        url = Configuration.HostUrl + "/openapi/order/AddOrder"
        response = requests.post(url=url, json=params, headers=headers)

        #res = response.text
        # print res

        message = response.json()["message"]
        result = response.json()["result"]
        code = response.code
        order = result["orderId"]

        self.assertEqual("success", message, "fail")
        self.assertEqual(0, code, "fail")
        self.assertEqual(order, result['orderId'], 'fail')

        print ('提交订单接口正确')

    def test_Add_Order(self):
        '''提交订单返回错误'''
        params = {}
        timeStamp = int(time.time())
        params["time"] = self.timeStamp
        params["u"] = "a"
        params["params"] = {
            "userId": "4096133",
            "classId": "59",
            "courseId": "95",
            "price": "30.01",
            "priceOld": "0",
            "groupId": "0",
            "code": " ",
            "deviceType": "x"
        }
        params["apphash"] = TestProvide.key(timeStamp, params["params"])
        #params["token"] = TestProvide.get_token(timeStamp, params["params"])
        # print params

        headers = {"Content-Type": "application/json"}
        url = Configuration.HostUrl + "/openapi/order/AddOrder"
        response = requests.post(url=url, json=params, headers=headers)

        #res = response.text
        # print res

        message = response.json()["message"]
        code = response.json()['code']
        errmsg = response.json()["errMsg"]

        self.assertEqual("system error", message, "fail")
        self.assertEqual(4003, code, "fail")
        self.assertEqual('价格不满足优惠', errmsg, 'fail')

        print ('提交订单接口正确')

    def test_CheckOrder(self):
        '''验证订单'''
        params = {}
        timeStamp = int(time.time())
        token = TestProvide.get_token(timeStamp, params["params"])
        params["time"] = self.timeStamp
        params["u"] = "a"
        params["params"] = {
            "userId": "4096133",
            "courseId": "94",
            "token": token
        }
        params["apphash"] = TestProvide.key(timeStamp, params["params"])
        # print params

        headers = {"Content-Type": "application/json"}
        url = Configuration.HostUrl + "/openapi/order/checkorder "
        response = requests.post(url=url, json=params, headers=headers)

        #res = response.text
        # print res

        message = response.json()["message"]
        result = response.json()["result"]
        code = response.code
        order = result["orderId"]

        self.assertEqual("success", message, "fail")
        self.assertEqual(order, result['orderId'], 'fail')
        self.assertEqual(0, code, "fail")

        print ('验证订单接口正确')

    def test_DiscountTicket(self):
        '''查询课程下有可用优惠码'''
        params = {}
        timeStamp = int(time.time())
        token = TestProvide.get_token(timeStamp, params["params"])
        params["time"] = self.timeStamp
        params["u"] = "a"
        params["params"] = {
            "userId": "4096133",
            "objectId": "630",
            "token": token
        }
        params["apphash"] = TestProvide.key(timeStamp, params["params"])
        # print params

        headers = {"Content-Type": "application/json"}
        url = Configuration.HostUrl + "/openapi/order/checkorder "
        response = requests.post(url=url, json=params, headers=headers)

        #res = response.text
        # print res

        message = response.json()["message"]
        result = response.json()["result"]
        code = response.code

        self.assertEqual("success", message, "fail")
        self.assertEqual('4', result['count'], 'fail')
        self.assertEqual(0, code, "fail")

        print('查询优惠码接口正确')

    def test_DiscountTicket(self):
        '''查询课程下无可用优惠码'''
        params = {}
        timeStamp = int(time.time())
        token = TestProvide.get_token(timeStamp, params["params"])
        params["time"] = self.timeStamp
        params["u"] = "a"
        params["params"] = {
            "userId": "4096133",
            "objectId": "94",
            "token": token
        }
        params["apphash"] = TestProvide.key(timeStamp, params["params"])
        # print params

        headers = {"Content-Type": "application/json"}
        url = Configuration.HostUrl + "/openapi/order/checkorder "
        response = requests.post(url=url, json=params, headers=headers)

        #res = response.text
        # print res

        code = response.code
        msg = response.json()["msg"]
        errmsg = response.json()["errMsg"]

        self.assertEqual(4002, code, 'fail')
        self.assertEqual("没有可用的优惠券", msg, 'fail')
        self.assertEqual("没有可用的优惠券", errmsg, 'fail')

        print('查询优惠码接口正确')

    def test_OnLineVeriy(self):
        '''核对信息'''
        params = {}
        timeStamp = int(time.time())
        token = TestProvide.get_token(timeStamp, params["params"])
        params["time"] = self.timeStamp
        params["u"] = "a"
        params["params"] = {
            "userId": "4096133",
            "classId": "59",
            "courseId": "94",
            "token": token
        }
        params["apphash"] = TestProvide.key(timeStamp, params["params"])
        # print params

        headers = {"Content-Type": "application/json"}
        url = Configuration.HostUrl + "/openapi/order/checkorder "
        response = requests.post(url=url, json=params, headers=headers)

        #res = response.text
        # print res

        message = response.json()["message"]
        result = response.json()["result"]
        code = response.code

        self.assertEqual("success", message, "fail")
        self.assertEqual('94', result['courseId'], 'fail')
        self.assertEqual(0, code, "fail")

        print('核对信息接口正确')

    def test_OrderInfo (self, checkOrder):
        '''支付页面'''
        params = {}
        timeStamp = int(time.time())
        params["time"] = self.timeStamp
        params["u"] = "a"
        params["params"] = {
            "userId": "4096133",
            "courseId": "94",
            "orderId": checkOrder.order
        }
        params["apphash"] = TestProvide.key(timeStamp, params["params"])
        # print params

        headers = {"Content-Type": "application/json"}
        url = Configuration.HostUrl + "/openapi/order/checkorder "
        response = requests.post(url=url, json=params, headers=headers)

        #res = response.text
        # print res

        message = response.json()["message"]
        result = response.json()["result"]
        code = response.code

        self.assertEqual("success", message, "fail")
        self.assertEqual('94', result['courseId'], 'fail')
        self.assertEqual('59', result['classId'], 'fail')
        self.assertEqual(0, code, "fail")

        print('核对信息接口正确')
#
# if __name__ == "__main__":
#     unittest.main()