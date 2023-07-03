# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2023/5/24 9:45
# @Author : waxberry
# @File : login.py
# @Software : PyCharm
from pywinauto import keyboard
from selenium import webdriver
from pynput.keyboard import Key, Controller
from selenium.webdriver.common.keys import Keys
import os
import time
import datetime
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains


def today():
    now = datetime.datetime.now()
    return now.strftime('%Y%m%d%H')


# 登录
# s = Service(executable_path="D:\Python310\chromedriver.exe")
driver = webdriver.Chrome(executable_path="D:\Python27\chromedriver.exe")
# driver = webdriver.Chrome(service=s)
# 注意http不可以省略
url = 'http://checkup-peis.test.thorgene.com/login'
time.sleep(3)
driver.get(url)
time.sleep(5)
driver.find_element_by_xpath("//*[@id='account']").send_keys('xsnq')
driver.find_element_by_id("password").send_keys('1')
driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div/form/div[4]/div/div/div/button").send_keys(Keys.ENTER)
# driver.find_element_by_xpath("//span[text(), '登 录']").click()
# driver.find_element_by_xpath("//*[@id='app']/div/div/div/div[2]/div/form/div[4]/div/div/div/button").click()
# driver.find_element_by_css_selector("[class='ant-btn ant-btn-primary ant-btn-lg ant-btn-block']").click()
# driver.find_element_by_xpath("//*[contains(text(), '登 录']/../button").click()
time.sleep(3)

# 创建单位
driver.find_element_by_xpath("/html/body/div[1]/section/section/aside/div/div[2]/div[1]/div/ul/li[1]/ul/li[1]").click()
# driver.switch_to.frame()
# driver.find_element_by_xpath("//*[contains(text(),'新建单位')]").click()
driver.find_element_by_xpath("/html/body/div[1]/section/section/section/div[3]/div[1]/div/div/div/div/div/div[1]/div/div[1]/div[1]/button").click()
driver.find_element_by_id("fname").send_keys('测试'+today())
driver.find_element_by_xpath("//*[@id='name']").click()
driver.find_element_by_xpath("//*[@id='htmlRoot']").click()

# /html/body/div[1]/section/section/section/div[3]/div[1]/div/div/div/div/div/div[1]/div/div[1]/div[1]/button
