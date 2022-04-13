#coding:utf-8

import unittest
import time
from GetOptionSengMail import GetOption
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import traceback

class Visit163ByFireFox(unittest.TestCase):

    def setUp(self):
        # 启动IE浏览器
        self.obj = GetOption
        self.driver = webdriver.Firefox(executable_path='F:\\firefox+firebug+yslow')
        # self.driver = webdriver.IE(executable_path='F:\\firefox+firebug+yslow')


    def test_HandleIFrame(self):
        url = "https://mail.126.com"
        # 访问自动以测试网页
        self.driver.get(url)
        try:
            username = self.obj.getOption("mailaccount", "username")
            print "username:", username
            password = self.obj.getOption("mailaccount", "password")
            print "password:", password
            attachname = self.obj.getOption("attachment", "directory")
            print "attachname:", attachname
            mailtoaddress = self.obj.getOption("mailto", "address")
            print "mailtoaddress:", mailtoaddress
            # 显示等待
            wait = WebDriverWait(self.driver, 15, 0.2)
            # 切换frame
            self.driver.switch_to.frame(self.driver.file_element_by_xpayh("//*[@id='x-URS-iframe']"))
            # self.driver.switch_to.frame("x-URS-iframe")
            # 显示等待用户获取用户名输入框元素
            name = wait.until(lambda x: x.find_element_by_xpath("//*[@class='j-inputtext dlemail']"))
            name.send_keys(username)
            # 显示等待获取密码输入框元素
            passwd = wait.until(lambda x: x.find_element_by_xpath("//*[@class='j-inputtext dlpwd']"))
            passwd.send_keys(password)
            # 登录
            login = wait.until(lambda x: x.find_element_by_id("dologin"))
            login.click()
            # 切回到默认framae
            self.driver.switch_to.default_content()
            # 获取写信按钮元素
            iwrite = wait.until(lambda x: x.find_element_by_xpath("//li[@id='_mail_component_74_74']/*[@class='oz0']"))
            iwrite.click()
            # 获取收件人输入框元素
            receiver = wait.until(lambda x: x.find_element_by_xpath("//input[@class='nui-editableAddr-ipt' and @role='combobox']"))
            # receiver.click()
            receiver.send_keys(mailtoaddress)
            # 获取主题输入框元素
            theme = wait.until(lambda x: x.find_element_by_xpath("//input[@class='nui-ipt-input' and @type='text' and @maxlength='256']"))
            # theme.click()
            theme.send_keys(u'这是第一个自动化发邮件脚本')
            # 发送附件，找添加附件的元素，直接send_keys（“目录”）即可，无需点击操作
            attach = wait.until(lambda x: x.find_element_by_xpath("//div[@class='by0']//input[@class='O0']"))
            attach.send_keys(attachname)
            # 切到写信内容部分的frame
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//*[@class='APP-editor-iframe']"))
            # 获取写信区域的元素
            editBox = wait.until(lambda x: x.find_element_by_xpath("/html/body"))
            editBox.click()
            editBox.send_keys(u'这是第一个自动化发邮件脚本')
            # 切回默认的frame
            self.driver.switch_to.default_content()
            # 获取发送按钮元素
            send = wait.until(lambda x: x.find_element_by_xpath("//*[@class='jp0']//*[@role='button']//*[.='发送']"))
            send.click()
        except TimeoutException, e:
            # 捕获TimeoutException异常
            print traceback.print_exc()
        except NoSuchElementException, e:
            # 捕获NoSuchElementException异常
            print traceback.print_exc()
        except Exception, e:
            # 捕获其他异常
            print traceback.print_exc()

if __name__ == '__main__':
    unittest.main()