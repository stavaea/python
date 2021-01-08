#coding:utf-8
import unittest
import requests

class TestBase(unittest.TestCase):

    def setUp(self):
        url = 'http://139.199.132.220:8000/event/api/register/'
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        paras = {'username': 'huice', 'password': 'MTIzaHVpY2VodWljZSFAIw=='}
        response = requests.post(url=url, headers=headers, data=paras)
        self.token = response.json().get('token')