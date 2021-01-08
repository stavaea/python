#coding:utf-8

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
import time
import traceback
from PageObject.LoginPage import *
from Action.login import *


class AddressBook(object):
    def __init__(self):
        self.driver = driver
        self.parse_config_file = ParsePageObjectRepositoryConfig()
        self.address_book_page = self.parse_config_file.getItemsFromSetion("126mail_homepage")
        print "self.address_book_page", self.address_book_page
        self.address_book_page_items = self.parse_config_file.getItemsFromSetion("126mail_addcontactspage")
        print "self.address_book_page_items", self.address_book_page_items

    def address_book_link(self):
        locateType, locateExpression = self.address_book_page['homepage.addressbook'].split('>')
        print locateType, locateExpression
        return getElement(self.driver, "xpath", "//div[text()='通讯录']")

    def add_content_button(self):
        locateType, locateExpression = self.address_book_page_items['addcontacts_page.createcontactsbtn'].split('>')
        print locateType, locateExpression
        return getElement(self.driver, locateType, locateExpression)

    def contact_name(self):
        locateType, locateExpression = self.address_book_page_items['addcontacts_page.contactpersonname'].split('>')
        print locateType, locateExpression
        return getElement(self.driver, locateType, locateExpression)

    def contact_email(self):
        locateType, locateExpression = self.address_book_page_items['addcontacts_page.contactpersonemail'].split('>')
        print locateType, locateExpression
        return getElement(self.driver, locateType, locateExpression)

    def contact_is_star(self):
        locateType, locateExpression = self.address_book_page_items['addcontacts_page.starcontacts'].split('>')
        print locateType, locateExpression
        return getElement(self.driver, locateType, locateExpression)

    def contact_mobile(self):
        locateType, locateExpression = self.address_book_page_items['addcontacts_page.contactpersonmobile'].split('>')
        print locateType, locateExpression
        return getElement(self.driver, locateType, locateExpression)

    def contact_other_info(self):
        locateType, locateExpression = self.address_book_page_items['addcontacts_page.contactpersoncomment'].split('>')
        print locateType, locateExpression
        return getElement(self.driver, locateType, locateExpression)

    def contact_save_button(self):
        locateType, locateExpression = self.address_book_page_items['addcontacts_page.savecontactperson'].split('>')
        print locateType, locateExpression
        return getElement(self.driver, locateType, locateExpression)

if __name__ == '__main__':
    driver = webdriver.Chrome(executable_path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver.exe")
    driver.get("http://mail.126.com")
    login(driver, "stavaea", "wxy900418")
    addressbook = AddressBook(driver)
    time.sleep(5)
    addressbook.address_book_link().click()
    addressbook.add_content_button().click()
    addressbook.contact_name().send_keys(u'王xx')
    addressbook.contact_email().send_keys('451009894@qq.com')
    addressbook.contact_is_star().click()
    addressbook.contact_mobile().send_keys('18511437672')
    addressbook.contact_other_info().send_keys('my life')
    addressbook.contact_save_button().click()

#     def add_content(self):
#         try:
#             wait = WebDriverWait(self.driver, 10, 0.2)
#             address_book_link = wait.until(lambda x: x.find_element_by_xpath("//div[text()='通讯录']"))
#             address_book_link.click()
#             # assert u'新建联系人' in driver.page_source
#             add_content_button = wait.until(lambda x: x.find_element_by_xpath("//span[text()='新建联系人']"))
#             add_content_button.click()
#             content_name = wait.until(lambda x: x.find_element_by_xpath("//a[@title='编辑详细姓名']/preceding-sibling::div/input"))
#             content_name.send_keys(u'王xx')
#             content_email = wait.until(lambda x: x.find_element_by_xpath("//*[@id='iaddress_MAIL_wrap']//input"))
#             content_email.send_keys('451009894@qq.com')
#             content_is_star = wait.until(lambda x: x.find_element_by_xpath("//span[@text()='设为星标联系人']/preceding-sibling::span/b"))
#             content_is_star.click()
#             content_mobile = wait.until(lambda x: x.find_element_by_xpath("//*[@id='iaddress_TEL_wrap']//dd/input"))
#             content_mobile.send_keys('18511437672')
#             content_other_info = wait.until(lambda x: x.find_element_by_xpath("//textarea"))
#             content_other_info.send_keys('my life')
#             content_save_button = wait.until(lambda x: x.find_element_by_xpath("//span[.='确定']"))
#             content_save_button.click()
#
#
#         except TimeoutException, e:
#             #捕获TimeoutException异常
#             print traceback.print_exc()
#
#         except NoSuchElementException, e:
#             #捕获NoSuchElementException异常
#             print traceback.print_exc()
#
#         except Exception, e:
#             #捕获其他异常
#             print traceback.print_exc()
#
# if __name__ == '__main__':
#     # driver = webdriver.Firefox(executable_path='F:\\Mozilla Firefox')
#     driver = webdriver.Chrome(executable_path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver.exe")
#     driver.get('http://mail.126.com')
#     lp = LoginPage(driver)
#     lp.login()
#     ab = AddressBook(driver)
#     ab.add_content()