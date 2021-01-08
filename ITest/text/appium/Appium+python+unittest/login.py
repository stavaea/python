#coding:utf-8

import unittest
from appium import webdriver

class Login(unittest.TestCase):
    '''登录测试'''
    def setUp(self):
        '''初始化app driver'''
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['deviceName'] = 'deviceID'
        desired_caps['platformVersion'] = 'android os'
        desired_caps['appPackage'] = 'packageName'
        desired_caps['appActivity'] = 'app main activity'
        desired_caps['chromeOptions'] = {'androidProcess': 'com.jsxfedu.bsszjc_android'}
        desired_caps['receateChromeDriverSeeions'] = True
        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeyboard'] = True
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    def test_login_by_pwd(self):
        '''测试密码登录'''
        phone_ele = self.driver.find_element_by_id('phone_id')
        phone_ele.send_keys('phoneNum')
        pwd_ele = self.driver.find_element_by_id('password_id')
        pwd_ele.send_keys('pwd')
        login_button = self.driver.find_element_by_id('login_button_id')
        login_button.click()


class login(unittest.TestCase):
    '''初始化app driver'''
    desired_caps_01 = IniHelper