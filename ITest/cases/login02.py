#coding:utf-8
import requests
from TestBase import TestBase

class Test(TestBase):
    '''登录接口密码错误分支流程'''
    def test_login02(self):
        url = 'http://139.199.132.220:8000/event/api/register/'
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        paras = {'username': 'huice', 'password': 'MTIzaHVpY2VodWljZSUyMUAlMjM='}
        response = requests.post(url=url, headers=headers, data=paras)
        error_code = response.json().get('error_code')

        self.assertEqual(error_code, 10000, u'用户名或密码错误')
        # print error_code
        print ('登录接口密码错误分支流程正确')

