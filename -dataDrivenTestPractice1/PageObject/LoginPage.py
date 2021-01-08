#coding:utf-8

from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import traceback
from Util.ParsePageObjectRepository import *#新加的
from ProjectVar.var import * #新加的
from Util.ObjectMap import *

class LoginPage(object):
    def __init__(self, driver):
        self.driver = driver
        self.parse_config_file = ParsePageObjectRepositoryConfig()#获取配置文件信息
        self.login_page_items = self.parse_config_file.getItemSetion("126mail_login")#新加的
        print "self.login_page_items:", self.login_page_items
        self.wait = WebDriverWait(self, 10, 0.2)#显示等待

    def getFrame(self):#locateType, locateExpression参数去掉，在里面处理
        locateType, locateExpression = self.login_page_items['login_page.frame'].split('>')#id>x-URS-iframe
        # frame = self.wait.until(lambda x: x.find_element(by=locateType, value=locateExpression))#"//iframe[@id='x-URS-iframe']"
        frame = getElement(self.driver, locateType, locateExpression)
        return frame

    def getUserName(self):#locateType, locateExpression参数去掉，在里面处理
        locateType, locateExpression = self.login_page_items['login_page.username'].split('>')#xpath>//input[@name='email']
        # username = self.wait.until(lambda x: x.find_element(by=locateType, value=locateExpression))#"//input[@placeholder='邮箱帐号或手机号' and @name='email']"
        username = getElement(self.driver, locateType, locateExpression)
        return username

    def getPassword(self):#locateType, locateExpression参数去掉，在里面处理
        locateType, locateExpression = self.login_page_items['login_page.password'].split('>')# xpath>//input[@name='password']
        # password = self.wait.until(lambda x: x.find_element(by=locateType, value=locateExpression))#"//input[@placeholder='密码']"
        password = getElement(self.driver, locateType, locateExpression)
        return password

    def getLoginButton(self):#locateType, locateExpression参数去掉，在里面处理
        locateType, locateExpression = self.login_page_items['login_page.loginbutton'].split('>')#id>dologin
        # loginbutton = self.wait.until(lambda x: x.find_element(by=locateType, value=locateExpression))#"//a[@id='dologin']"
        loginbutton = getElement(self.driver, locateType, locateExpression)
        return loginbutton

    def login(self):
        self.driver.switch_to.frame(self.getFrame())
        self.getUserName().clear()
        self.getUserName().send_keys('stavaea')
        self.getPassword().send_keys('wxy900418')
        self.getLoginButton().click()

    # def login(self, locate_type, locate_expression):
    #     try:
    #         wait = WebDriverWait(driver, 10, 0.2)
    #         self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='x-URS-iframe']"))#切换到用户名和密码输入框所在的frame元素
    #         name = wait.until(lambda x: x.find_element_by_xpath("//input[@placeholder='邮箱帐号或手机号' and @name='email']"))
    #         name.send_keys('stavaea')
    #         password = wait.until(lambda x: x.find_element_by_xpath("//input[@placeholder='密码']"))
    #         password.send_keys('wxy900418')
    #         submit = wait.until(lambda x: x.find_element_by_xpath("//a[@id='dologin']"))
    #         submit.click()
    #         self.driver.switch_to.default_content()#在pycharm里用switch_to_default_content会被加删除线
    #         time.sleep(5)
    #         assert u'退出' in self.driver.page_source, "no exist in page_source"
    #     except TimeoutException, e:
    #         #捕获TimeoutException异常
    #         print traceback.print_exc()
    #
    #     except NoSuchElementException, e:
    #         #捕获NoSuchElementException异常
    #         print traceback.print_exc()
    #
    #     except Exception, e:
    #         #捕获其他异常
    #         print traceback.print_exc()


if __name__ == '__main__':
    # driver = webdriver.Firefox(executable_path='F:\\Mozilla Firefox')
    driver = webdriver.Chrome(executable_path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver.exe")
    driver.get("http:\\mail.126.com")
    # login = LoginPage(driver)
    # login.login()
    lp = LoginPage(driver)
    lp.login()
    # driver.switch_to.frame(lp.getFrame("xpath", "//iframe[@id='x-URS-iframe']"))
    # time.sleep(2)
    # lp.getUserName("xpath", "//input[@placeholder='邮箱帐号或手机号' and @name='email']").clear()
    # lp.getUserName("xpath", "//input[@placeholder='邮箱帐号或手机号' and @name='email']").send_keys('stavaea')
    # lp.getPassword("xpath", "//input[@placeholder='密码']").send_keys('wxy900418')
    # lp.getLoginButton("xpath", "//a[@id='dologin']").click()
    # driver.switch_to.default_content()
    # time.sleep(5)
    # driver.switch_to.frame(lp.getFrame())
    # time.sleep(2)
    # lp.getUserName().clear()
    # lp.getUserName().send_keys('stavaea')
    # lp.getPassword().send_keys('wxy900418')
    # lp.getLoginButton().click()
    # driver.switch_to.default_content()
    # time.sleep(5)
    # assert u'退出' in driver.page_source, 'no exist in page_source'