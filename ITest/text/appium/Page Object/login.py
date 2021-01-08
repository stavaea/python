#coding:utf-8

import ConfigParser
from selenium import webdriver
import unittest

class LoginPage(object):
    '''登录页面'''

    def __init__(self, driver):
        self.driver = driver

    def phone_ele(self):
        '''返回页面手机号输入框元素'''
        ele = self.driver.find_element_by_id('phone_id')
        return ele

    def pwd_ele(self):
        '''返回页面密码输入框元素'''
        ele = self.driver.find_element_by_id('password_id')
        return ele

    def login_ele(self):
        '''返回页面登录按钮元素'''
        ele = self.driver.find_element_by_id('login_id')
        return ele

    def login_by_pwd(self, phone, pwd):
        '''登录业务'''
        phone_ele = self.phone_ele()
        phone_ele.send_keys(phone)
        pwd_ele = self.pwd_ele()
        pwd_ele.send_keys(pwd)
        login_button = self.login_ele()
        login_button.click()

class LoginTest(unittest.TestCase):
    '''登录页面测试'''

    def setUp(self):
        '''初始化app driver'''
        self.driver = webdriver.Firefox()
        self.driver.get('url')

    def test_login_01(self):
        '''测试用户名密码正确登录'''
        LoginPage(self.driver).login('phone', 'pwd')

    def test_login_01(self):
        '''测试用户名密码错误登录'''
        LoginPage(self.driver).login('phone', 'pwd')