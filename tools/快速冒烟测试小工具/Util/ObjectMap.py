# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2023/5/26 11:31
# @Author : waxberry
# @File : ObjectMap.py
# @Software : PyCharm

from selenium.webdriver.support.ui import WebDriverWait
import configparser, os
from selenium import webdriver
from Config.ProjVar import *
from Util.ReadConfig import read_ini_file

class ObjectMap(object):
    def __init__(self):
        # 存放页面元素定位表达方式及定位表达式的配置文件所在绝对路径
        self.uiObjectMapPath = objectmap_ini_path

    def getElementObject(self, driver, webSiteName, elementName):
        try:
            locators = read_ini_file(self.uiObjectMapPath, webSiteName, elementName).split(">")
            # 得到定位方式
            locatorMethod = locators[0]
            # 得到定位表达式
            locatorExpression = locators[1]
            print(locatorMethod, locatorExpression)
            # 通过显示等待方式获取页面元素
            element = WebDriverWait(driver, 10).until(lambda x: x.find_element(locatorMethod, locatorExpression))
        except Exception as e:
            raise e
        else:
            # 当页面元素被找到后,将该页面元素对象返回给调用者
            return element