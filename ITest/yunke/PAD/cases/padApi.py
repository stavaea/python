#coding:utf-8

from yunke.PAD.Provide import Configuration, TestProvide
import unittest
import time, requests, sys, pymysql
import imp, importlib
imp.reload(sys)
importlib.reload(sys)

class common_functions(object):
    def __init__(self):
        self.conn = pymysql.connect(
            host='114.115.236.182',
            port='3306',
            user='devgn100',
            password='devgn100',
            db='db_cousre_log'
        )
        self.cur = self.conn.cursor

    def execute_sqlscript_fetchall_contents(self, sqlscript):
        self.cur.execute(sqlscript)
        contents = self.cur.fetchall()
        return contents

    def execute_sqlscript_fetchall_content(self, sqlscript):
        contents = self.execute_sqlscript_fetchall_contents(sqlscript)
        for row in contents:
            data = row[0]
        return data

    def calculate_sharecycle(self, open_time, clean_time):
        sql_sharecycle = "select count(*) from 表名 WHERE open_day >= left(" + open_time + ", 8) and open_day <= left(" + clean_time + ",8)"
        sharecycle = self.execute_sqlscript_fetchall_content(sql_sharecycle)
        if open_time[8:12] >= '2100':
            sharecycle = sharecycle - 1
        if clean_time[3][8:12] >= '2100':
            sharecycle = sharecycle + 1

class TestApi(unittest.TestCase, common_functions):

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

    def test_TeacherTable(self):
        '''老师课表'''
        params = {}
        timeStamp = int(time.time())
        params["time"] = self.timeStamp
        params["u"] = "i"
        params["v"] = "2"
        params["params"] = {
                "userId": "411a57847031451896280d6958fec402",
                "schoolId": "b31a941c23ed4cc5a158dd77f583f5ec"
            }
        params["key"] = TestProvide.key(timeStamp, params["params"])
        print (params)

        headers = {"Content-Type": "application/json"}
        url = Configuration.HostUrl + "/interface/teacher/IpadTableBydate"
        response = requests.post(url=url, json=params, headers=headers)

        res = response.text
        print (res)

        message = response.json()["message"]
        status_code = response.status_code

        self.assertEqual("success", message, "fail")
        self.assertEqual(200, status_code, "fail")

        print ('老师课表接口正确')

    def test_student_TeacherTable(self):
        '''学生身份访问老师课表接口'''
        params = {}
        timeStamp = int(time.time())
        params["time"] = self.timeStamp
        params["u"] = "i"
        params["v"] = "2"
        params["params"] = {
                "userId": "e93f7a9628a441f0bbbdae759578d658",
                "schoolId": "b31a941c23ed4cc5a158dd77f583f5ec"
            }
        params["key"] = TestProvide.key(timeStamp, params["params"])
        print (params)

        headers = {"Content-Type": "application/json"}
        url = Configuration.HostUrl + "/interface/teacher/IpadTableBydate"
        response = requests.post(url=url, json=params, headers=headers)

        res = response.text
        print (res)

        message = response.json()["message"]
        errMsg = response.json()["errMsg"]
        status_code = response.status_code

        # self.assertEqual("success", message, "fail")
        self.assertEqual("获取数据失败", errMsg, "success")
        # self.assertEqual("success", message, "fail")
        self.assertEqual(200, status_code, "fail")

        print ('学生访问失败')


    def test_jiayou(self):
        '''点赞、加油、鼓励'''
        params = {}
        timeStamp = int(time.time())
        params["time"] = self.timeStamp
        params["u"] = "i"
        params["v"] = "2"
        params["params"] = {
            "teacherId": "411a57847031451896280d6958fec402",
            "studentId": "e93f7a9628a441f0bbbdae759578d658",
            "planId": 152,
            "jiayou": 5,
            "zan": 0,
            "guli": 0,
            "token": "66bab2bbabb80505fc17d51d543db453"
        }
        params["key"] = TestProvide.key(timeStamp, params["params"])
        # params["token"] = TestProvide.get_t_token(timeStamp, params["params"])
        print (params)

        headers = {"Content-Type": "application/json"}
        url = Configuration.HostUrl + "/interface/ipadstudent/UpdateUserComment"
        response = requests.post(url=url, json=params, headers=headers)

        res = response.text
        print (res)

        message = response.json()["message"]
        status_code = response.status_code

        self.assertEqual("success", message, "fail")
        self.assertEqual(200, status_code, "fail")

        print ('加油正确')

    def test_dianzan(self):
        '''点赞、加油、鼓励'''
        params = {}
        timeStamp = int(time.time())
        params["time"] = self.timeStamp
        params["u"] = "i"
        params["v"] = "2"
        params["params"] = {
            "teacherId": "411a57847031451896280d6958fec402",
            "studentId": "e93f7a9628a441f0bbbdae759578d658",
            "planId": 152,
            "jiayou": 0,
            "zan": 1,
            "guli": 0,
            "token": "66bab2bbabb80505fc17d51d543db453"
        }
        params["key"] = TestProvide.key(timeStamp, params["params"])
        # params["token"] = TestProvide.get_t_token(timeStamp, params["params"])
        print (params)

        headers = {"Content-Type": "application/json"}
        url = Configuration.HostUrl + "/interface/ipadstudent/UpdateUserComment"
        response = requests.post(url=url, json=params, headers=headers)

        res = response.text
        print (res)

        message = response.json()["message"]
        status_code = response.status_code

        self.assertEqual("success", message, "fail")
        self.assertEqual(200, status_code, "fail")

        print ('点赞正确')

    def test_guli(self):
        '''点赞、加油、鼓励'''
        params = {}
        timeStamp = int(time.time())
        params["time"] = self.timeStamp
        params["u"] = "i"
        params["v"] = "2"
        params["params"] = {
            "teacherId": "411a57847031451896280d6958fec402",
            "studentId": "e93f7a9628a441f0bbbdae759578d658",
            "planId": 152,
            "jiayou": 0,
            "zan": 0,
            "guli": 1,
            "token": "66bab2bbabb80505fc17d51d543db453"
        }
        params["key"] = TestProvide.key(timeStamp, params["params"])
        # params["token"] = TestProvide.get_t_token(timeStamp, params["params"])
        print (params)

        headers = {"Content-Type": "application/json"}
        url = Configuration.HostUrl + "/interface/ipadstudent/UpdateUserComment"
        response = requests.post(url=url, json=params, headers=headers)

        res = response.text
        print (res)

        message = response.json()["message"]
        status_code = response.status_code

        self.assertEqual("success", message, "fail")
        self.assertEqual(200, status_code, "fail")

        print ('鼓励正确')

    def test_UserComment(self):
        '''点赞、加油、鼓励同时操作'''
        params = {}
        timeStamp = int(time.time())
        params["time"] = self.timeStamp
        params["u"] = "i"
        params["v"] = "2"
        params["params"] = {
            "teacherId": "411a57847031451896280d6958fec402",
            "studentId": "e93f7a9628a441f0bbbdae759578d658",
            "planId": 152,
            "jiayou": 1,
            "zan": 1,
            "guli": 1,
            "token": "66bab2bbabb80505fc17d51d543db453"
        }
        params["key"] = TestProvide.key(timeStamp, params["params"])
        # params["token"] = TestProvide.get_t_token(timeStamp, params["params"])
        print (params)

        headers = {"Content-Type": "application/json"}
        url = Configuration.HostUrl + "/interface/ipadstudent/UpdateUserComment"
        response = requests.post(url=url, json=params, headers=headers)

        res = response.text
        print (res)

        message = response.json()["message"]
        errMsg = response.json()["errMsg"]
        status_code = response.status_code

        # self.assertEqual("success", message, "fail")
        self.assertEqual("请求key验证失败", errMsg, "success")
        self.assertEqual(200, status_code, "fail")

        print ('验证失败，不可同时操作点赞，鼓励，加油')


    def test_StudentRoster(self):
        '''花名册'''
        params = {}
        timeStamp = int(time.time())
        params["time"] = self.timeStamp
        params["u"] = "i"
        params["v"] = "2"
        params["params"] = {
            "userId": "411a57847031451896280d6958fec402",
            "classId": "52e4a8315fdc488b971cd9d1dfde7c9b",
            "planId": 152,
            "token": "66bab2bbabb80505fc17d51d543db453"
        }
        params["key"] = TestProvide.key(timeStamp, params["params"])
        # params["token"] = TestProvide.get_t_token(timeStamp, params["params"])
        print (params)

        headers = {"Content-Type": "application/json"}
        url = Configuration.HostUrl + "/interface/ipadstudent/GetStudentRoster"
        response = requests.post(url=url, json=params, headers=headers)

        res = response.text
        print (res)

        message = response.json()["message"]
        status_code = response.status_code

        self.assertEqual("success", message, "fail")
        self.assertEqual(200, status_code, "fail")

        print ('花名册接口正确')