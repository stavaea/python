#coding:utf-8

import unittest
from ConfigParser import ConfigParser
from appium import webdriver

class login(unittest.TestCase):
    '''登录测试'''
    def setUp(self):
        '''初始化app driver'''
        desired_caps_01 = IniHelper('cfginfo.ini').get_section_dic('desired_caps_01')
        desired_caps_02 = IniHelper('cfginfo.ini').get_boolean_section_dic('desired_caps_02')
        chrome_options = IniHelper('cfginfo.ini').get_section_dic('chromeOptions')
        self.desired_caps = dict(desired_caps_01, **desired_caps_02)
        self.desired_caps['chromeOptions'] = chrome_options
        self.base_url = IniHelper('cfginfo.ini').get_value('appium', 'base_url')
        self.driver = webdriver.Remote(self.base_url, self.desired_caps)

    def test_login_by_pwd(self):
        '''测试密码登录'''
        ele_dic = IniHelper('控件.ini', '个人中心/').get_section_dic('登录')
        value_dic = IniHelper('数据.ini', '个人中心/').get_section_dic('登录')
        BaseAction(self.driver).set_values(ele_dic, value_dic)
        ele_dic = IniHelper('控件.ini', '个人中心/').get_section_dic('确认登录')
        BaseAction(self.driver).ele_click(ele_dic)