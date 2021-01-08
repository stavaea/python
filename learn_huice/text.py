#coding:utf-8

from selenium import webdriver
from time import sleep
import os,random,time
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox
time.sleep(3)
# browser.maximize_window()
# time.sleep(3)
browser.quit()