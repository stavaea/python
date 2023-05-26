# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2023/5/19 10:00
# @Author : waxberry
# @File : tt.py
# @Software : PyCharm


from selenium import webdriver

# driver = webdriver.Edge(executable_path='D:\Python310\MicrosoftWebDriver.exe')
# # driver = webdriver.Firefox
# # driver = webdriver.Chrome()
# driver.get('http://www.baidu.com/')


driver = webdriver.firefox()
driver.get('http://www.baidu.com/')
