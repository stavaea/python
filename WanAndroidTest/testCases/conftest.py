# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2023/7/26 11:50
# @Author : waxberry
# @File : conftest.py
# @Software : PyCharm


import pytest
from base.base_path import *
from utils.handle_logger import logger
from utils.handle_allure import handle_allure
from utils.handle_sendEmail import HandleSendEmail

'''
1. 构造测试数据??
2. fixture 替代 setup,teardown
3. 配置 pytest
'''

def pytest_collection_modifyitems(items):
    """
    测试用例收集完成时，将收集到的item的name和nodeid的中文显示在控制台上
    """
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode_escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode_escape')
        # print(item.nodeid)

@pytest.fixture(scope='session', autouse=True)
def send_mail():
    logger.info('------session级,执行wanAndroid测试用例------')
    yield
    logger.info('------session级,wanAndroid用例执行结束,发送邮件:------')
    """执行alllure命令 """
    handle_allure.execute_command()
    # 发邮件
    part_text = '附件为自动化测试报告,框架使用了pytest+allure'
    attachment_list = [report_path]
    password = ''
    user_list = ['']
    HandleSendEmail(part_text, attachment_list, password, user_list).send_email()
