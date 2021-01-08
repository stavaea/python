#coding:utf-8

from PageObject.LoginPage import *
from selenium import webdriver

def login(driver, username, password):
    lp = LoginPage(driver)
    driver.swicth_to.frame(lp.getFrame())
    lp.getUserName().clear()
    lp.getUserName().send_keys(username)
    lp.getPassword().send_keys(password)
    lp.getLoginButton().click()

if __name__ == '__main__':
    #测试代码
    driver=webdriver.Chrome(executable_path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver.exe")
    driver.get("http://mail.126.com")
    login(driver, "stavaea", "wxy900418")