#coding:utf-8
import HTMLTestRunnerCN
import requests
from TestBase import TestBase

class Test(TestBase):
    '''查询会议详细信息接口会议不存在分支'''
    def test_eventdetail01(self):
        url = 'http://139.199.132.220:8000/event/api/get_eventdetail/'
        headers = {'token': self.token, 'random': '12345'}
        paras = {'id': 3, 'username': 'huice', 'sign': '3285cffdeba75dc3572ec7dfc1bf7ed5'}
        response = requests.get(url=url, params=paras, headers=headers)
        error_code = response.json().get('error_code')

        self.assertEqual(error_code, 10004, u'id不存在')

        # print error_code
        print ('查询会议详细信息接口会议不存在分支流程正确')