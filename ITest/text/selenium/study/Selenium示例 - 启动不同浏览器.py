#coding:utf-8
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import os
import time

'''【浏览器驱动】
1. 下载：
    FireFox的驱动，gechodriver（蜥蜴驱动？！），找如下链接里面对应操作系统的：
        https://github.com/mozilla/geckodriver/releases
    IE的驱动，edge（边界？！），找如下链接里面的Download：
        https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
    Chrome驱动，比较朴素地依旧命名为chromedriver：
        https://sites.google.com/a/chromium.org/chromedriver/
    其它的驱动，参考官网，能想到的驱动都在这里了。
        http://www.seleniumhq.org/download/
2. 配置：
    直接将下载的chromedriver.exe路径加到
        driver = webdriver.Chrome(r"E:\Tools\Python\seleniumDriver\chromedriver.exe")
    或者直接改变环境变量
        import os
        os.environ["webdriver.chrome.driver"] = "E:\Tools\Python\seleniumDriver\chromedriver.exe"
'''
# 一、启动firefox浏览器
# 不需要下载任何驱动，原生支持firefox，但要注意firefox浏览器的版本，如果出现启动firefox失败的情况，请降低或升级firefox版本。
# # 1、firefox安装在默认路径，启动代码如下：
# driver = webdriver.Firefox()
# # 注意http不可以省略
# url = 'http://www.baidu.com'
# driver.get(url)
# driver.close()
#
# # 2、指定firefox的安装路径启动，代码如下：
# # firefox 实际安装路径
# ffdriver = "C:\Program Files\Mozilla Firefox"
# os.environ["webdriver.firefox.driver"] = ffdriver
# driver = webdriver.Firefox(ffdriver)
# # 注意http不可以省略
# url = 'http://www.baidu.com'
# driver.get(url)
# driver.close()

# 二、启动google浏览器
# 需要下载相应的驱动，下载地址：
# http: // chromedriver.storage.googleapis.com / index.html
#
# 参考代码如下：
# chromedriver.exe  实际安装路径, 笔者这里放置在C盘根目录
# googledriver = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver.exe"
# os.environ["webdriver.chrome.driver"] = googledriver
# driver = webdriver.Chrome(executable_path="E:\Google\Chrome\Application\chrome.exe")
# driver = webdriver.Chrome(executable_path="D:\Python310\chromedriver.exe")
s = Service(executable_path="D:\Python310\chromedriver.exe")
driver = webdriver.Chrome(service=s)
# driver = webdriver.Chrome(r"F:\python3\chromedriver.exe")
# driver = webdriver.Chrome(googledriver)
# 注意http不可以省略
url = 'http://www.baidu.com'
time.sleep(3)
driver.get(url)
# driver.close()

# from selenium import webdriver
#
# # chromedriver_path = r"D:\Python310\chromedriver.exe"
# # driver = webdriver.Chrome(executable_path=chromedriver_path)
# # 登陆百度
# def main():
#     global driver
#     chromedriver_path = r"D:\Python310\chromedriver.exe"
#     driver = webdriver.Chrome(executable_path=chromedriver_path)
#     # 打开页面
#     page = driver.get('https://www.baidu.com/')
#
# if __name__ == "__main__":
#     main()

# 三、启动IE浏览器
# 需要下载相应的驱动，下载地址：
# http: // selenium - release.storage.googleapis.com / index.html
#
# 参考代码如下：
# iedriver.exe  实际安装路径, 笔者这里放置在C盘根目录
# iedriver = "C:\\iedriver.exe"
# os.environ["webdriver.ie.driver"] = iedriver
# driver = webdriver.Chrome(iedriver)
# # 注意http不可以省略
# url = 'http://www.baidu.com'
# driver.get(url)
# driver.close()
