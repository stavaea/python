#coding:utf-8
import unittest
import requests

class EventTest(unittest.TestCase):

    def test_login01(self):
        url = 'http://139.199.132.220:8000/event/api/register/'
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        paras = {'username': 'huice', 'password': 'MTIzaHVpY2VodWljZSFAIw=='}
        response = requests.post(url=url, headers=headers, data=paras)
        token = response.json().get('token')
        print (token)

    def test_login02(self):
        url = 'http://139.199.132.220:8000/event/api/register/'
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        paras = {'username': 'huice', 'password': 'MTIzaHVpY2VodWljZSUyMUAlMjM='}
        response = requests.post(url=url, headers=headers, data=paras)
        error_code = response.json().get('error_code')
        print (error_code)

    def eventdetail01(self):
        url = 'http://139.199.132.220:8000/event/api/get_eventdetail/'
        headers = {'token': '2469df3cd860bb70196867fa019189f618364608', 'random': '12345'}
        paras = {'id': 1, 'username': 'huice', 'sign': '77a40284931ee0ea6eec6e580c2293fb'}
        response = requests.get(url=url, params=paras, headers=headers)
        event_detail = response.json().get('event_detail')
        if event_detail:
            id = event_detail.get('id')
        else:
            id = None
        print (id)

    def eventdetail02(self):
        url = 'http://139.199.132.220:8000/event/api/get_eventdetail/'
        headers = {'token': '2469df3cd860bb70196867fa019189f618364608', 'random': '12345'}
        paras = {'id': 3, 'username': 'huice', 'sign': '3285cffdeba75dc3572ec7dfc1bf7ed5'}
        response = requests.get(url=url, params=paras, headers=headers)
        error_code = response.json().get('error_code')
        print (error_code)

if __name__ == '__main__':
    unittest.main()