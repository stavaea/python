#coding:utf-8

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

# driver = webdriver.Chrome(executable_path='D:\Python310\chromedriver.exe')
# driver = webdriver.Firefox(executable_path='E:\Fox\\firefox.exe')
# driver = webdriver.Firefox()
# driver.maximize_window()

# driver.implicitly_wait(3)

s = Service(executable_path="D:\Python310\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get('http://www.baidu.com')
driver.find_elements_by_id('kw').send_keys('python+selenium')

driver.find_element_by_id('su').click()

# driver.quit()