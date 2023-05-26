# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2023/5/24 9:45
# @Author : waxberry
# @File : login.py
# @Software : PyCharm


from selenium import webdriver
import os
import time
from selenium.webdriver.chrome.service import Service

# def main():
#     global driver
#     chromedriver_path = r"D:\Python310\chromedriver.exe"
#     driver = webdriver.Chrome(executable_path=chromedriver_path)
#     # 打开页面
#     page = driver.get('http://checkup-peis.test.thorgene.com/login')
#
#     driver.find_elements_by_xpath=("//*[@id='account']").sendkeys('xsnq')
#     driver.find_element_by_id = ('"password"').sendkeys('1')
#     driver.find_element_by_id =("app").click
#
# if __name__ == "__main__":
#     main()
from selenium.webdriver.common.by import By

s = Service(executable_path="D:\Python310\chromedriver.exe")
driver = webdriver.Chrome(service=s)
# driver = webdriver.Chrome(r"F:\python3\chromedriver.exe")
# driver = webdriver.Chrome(googledriver)
# 注意http不可以省略
url = 'http://checkup-peis.test.thorgene.com/login'
time.sleep(3)
driver.get(url)
time.sleep(10)
driver.find_elements_by_xpath=("//*[@id='account']").sendkeys('xsnq')
# driver.findElement(By.xpath("//*[@id='account'] and text()='xsnq']")).click()
driver.find_element_by_id = ('"password"').sendkeys('1')
driver.find_element_by_id =("app").click
time.sleep(20)
