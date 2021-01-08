#coding:utf-8
import requests
from TestBase import TestBase

class Test(TestBase):
    '''查询会议详细信息接口正向流程'''
    def test_eventdetail01(self):
        url = 'http://139.199.132.220:8000/event/api/get_eventdetail/'
        headers = {'token': self.token, 'random': '12345'}
        paras = {'id': 1, 'username': 'huice', 'sign': '77a40284931ee0ea6eec6e580c2293fb'}
        response = requests.get(url=url, params=paras, headers=headers)
        event_detail = response.json().get('event_detail')
        if event_detail:
            id = event_detail.get('id')
        else:
            id = None

        # assert id == 1, u'fail'
        # print id
        self.assertEqual(id, 1, 'fail')
        self.assertEqual(response.status_code, 200, 'fail')
        print ('查询会议详细信息接口正向流程正确')