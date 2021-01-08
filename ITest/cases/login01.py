#coding:utf-8
import requests
from TestBase import TestBase

class Test(TestBase):
    '''登录接口'''
    def test_login01(self):
        '''登录正向流程'''
        url = 'http://139.199.132.220:8000/event/api/register/'
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        paras = {'username': 'huice', 'password': 'MTIzaHVpY2VodWljZSFAIw=='}
        response = requests.post(url=url, headers=headers, data=paras)
        # print response.text
        token = response.json().get('token')
        error_code = response.json().get('error_code')
        self.assertEqual(error_code, 0, 'fail')
        self.assertNotEqual(token, None, 'token为空')
        # print token
        print ('登录接口正向流程正确')
