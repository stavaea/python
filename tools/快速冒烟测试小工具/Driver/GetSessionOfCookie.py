# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2023/5/26 11:45
# @Author : waxberry
# @File : GetSessionOfCookie.py
# @Software : PyCharm

from selenium import webdriver
import requests, time, os
from tools.快速冒烟测试小工具.Config.ProjVar import *
from tools.快速冒烟测试小工具.Util.ReadConfig import read_ini_file
from tools.快速冒烟测试小工具.Util.ObjectMap import *

def get_session_of_cookie(domain, url, account, password):
    # 从配置文件获取配置的浏览器类型,并对应去登录获取cookie
    browser = read_ini_file(dbuser_ini_path, "driver", "browser")
    if browser.lower() == "chrome":
        driverpath = os.path.join(driver_path, "chromedriver.exe")
        driver = webdriver.Chrome(executable_path=driverpath)
    elif browser.lower() == "firefox":
        driverpath = os.path.join(driver_path, "geckodriver.exe")
        driver = webdriver.Firefox(executable_path=driverpath)
    elif browser.lower() == "ie":
        driverpath = os.path.join(driver_path, "IEDriverServer.exe")
        driver = webdriver.Ie(executable_path=driverpath)
    driver.maximize_window()
    time.sleep(1)
    # 打开前后台登录页面
    driver.get(url)
    driver.implicitly_wait(5)
    # 获取登录页面元素传值登录
    objmap = ObjectMap()
    if domain == 'eclp':
        objmap.getElementObject(driver, 'eclp', 'LoginAccount').sendkeys(account)
        objmap.getElementObject(driver, 'eclp', 'LoginPassword').sendkeys(password)
        objmap.getElementObject(driver, 'eclp', 'LoginButton').click()
    elif domain == 'uc':
        objmap.getElementObject(driver, 'uc', 'LoginAccount').sendkeys(account)
        objmap.getElementObject(driver, 'uc', 'LoginPassword').sendkeys(password)
        objmap.getElementObject(driver, 'uc', 'LoginButton').click()
    time.sleep(3)
    # 获取登录后的cookies
    allcookies = driver.get_cookies()
    print('获取到登录后的cookies: %s' % allcookies)
    driver.quit()
    # 把上面获取的cookies添加到s中
    s = requests.session()
    try:
        # 添加到cookies到CookieJar
        c = requests.cookies.RequestsCookieJar()
        for i in allcookies:
            c.set(i['name'], i['value'])
        # 更新session里cookiles
        s.cookies.update(c)
    except Exception as e:
        print(u'添加cookies报错：%s' % str(e))
    print('查看添加后s的cookies')
    print(s.cookies)
    return s