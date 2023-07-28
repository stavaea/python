# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2023/7/26 10:25
# @Author : waxberry
# @File : base_requests.py
# @Software : PyCharm


import json
import allure
import urllib3
import requests
import warnings
from bs4 import BeautifulSoup
from base.base_path import *
from requests.adapters import HTTPAdapter
from utils.handle_logger import logger
from utils.handle_config import handle_config as hc


class BaseRequests:
    def __init__(self, case, proxies=None, headers=None, cookies=None, timeout=15, max_retries=3)
        '''
        :param case: 测试用例
        :param proxies: The result is displayed in fiddler：
        {"http": "http://127.0.0.1:8888", "https": "https://127.0.0.1:8888"}
        :param headers: 请求头
        :param cookies: cookies
        :param timeout: 请求默认超时时间15s
        :param max_retries: 请求超时后默认重试3次
        '''
        self.case = case
        self.proxies = proxies
        self.headers = headers
        self.cookies = cookies
        self.timeout = timeout
        self.max_retries = max_retries
        self.base_url = hc.operation_config(conf_path, 'BASEURL', 'base_url')

    def get_response(self):
        '''获取请求结果'''
        response = self._run_main()
        return response

    def _run_main(self):
        '''发送请求'''
        method = self.case['method']
        url = self.base_url + self.case['url']
        if self.case['parameter']:
            data = eval(self.case['parameter'])
        else:
            data = None

        s = requests.session()
        s.mount('http://', HTTPAdapter(max_retries=self.max_retries))
        s.mount('https://', HTTPAdapter(max_retries=self.max_retries))
        urllib3.disable_warnings()# 忽略浏览器认证(https认证)警告
        warnings.simplefilter('ignore', ResourceWarning)# 忽略 ResourceWarning警告

        res = ''
        if method.upper() == 'POST':
            try:
                res = s.request(method='post', url=url, data=data, verify=False, proxies=self.proxies,
                                headers=self.headers, cookies=self.cookies, timeout=self.timeout)
            except Exception as e:
                logger.error('POST请求出错，错误信息为：{0}'.format(e))
        elif method.upper == 'GET':
            try:
                res = s.request(method='get', url=url, params=data, verify=False, proxies=self.proxies,
                                headers=self.headers, cookies=self.cookies, timeout=self.timeout)
            except Exception as e:
                logger.error('GET请求出错，错误信息为：{0}'.format(e))
        else:
            raise ValueError('method方法为get和post')
        logger.info(f'请求方法:{method}，请求路径:{url}, 请求参数:{data}, 请求头:{self.headers}, cookies:{self.cookies}')

        # with allure.step('接口请求信息：'):
        #     allure.attach(f'请求方法:{method}，请求路径:{url}, 请求参数:{data}, 请求头:{headers}')

        # 拓展:是否需要做全量契约验证?响应结果是不同类型时,如何处理响应?)
        return res

if __name__ == '__main__':
    # case = {'method': 'get', 'url': '/article/top/json', 'parameter': ''}
    case = {'method': 'get', 'url': '/user/login', 'parameter':'{"username": "xbc", "password": "123456"}'}
    response = BaseRequests(case).get_response()
    print(response.json())