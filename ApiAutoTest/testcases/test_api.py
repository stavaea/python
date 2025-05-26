# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2025/5/26 11:42
# @Author : waxberry
# @File : test_api.py
# @Software : PyCharm


import requests
from utils.config_reader import read_config

def test_get_user_info():
    config = read_config()
    base_url = config.get('api', 'base_url')
    url = base_url + '/user_info'  #假设接口路径为user_info
    headers = {'Content-Type': 'application/json'}
    response = requests.get(url, headers=headers)
    assert response.status_code == 200    #断言接口响应状态码为200