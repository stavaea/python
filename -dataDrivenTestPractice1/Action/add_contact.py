#coding:utf-8

from PageObject.AddressBook import *
from selenium import webdriver

def add_contact(driver, name="", email="", is_star=True, mobile="", otherinfo=""):
    driver.switch_to.default_contact()
    addressbook = AddressBook(driver)
    addressbook.address_book_link().click()
    addressbook.add_content_button().click()
    addressbook.contact_name().send_keys(name)
    addressbook.contact_email().send_keys(email)
    if is_star==True:
        addressbook.contact_is_star().click()
    addressbook.contact_mobile().send_keys(mobile)
    addressbook.contact_other_info().send_keys(otherinfo)
    addressbook.contact_save_button().click()

if __name__ == '__main__':
    driver = webdriver.Chrome(executable_path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver.exe")
    driver.get("http://mail.126.com")
    login(driver, "stavaea", "wxy900418")
    add_contact(driver, '王xx', '451009894@qq.com', True, '18511437672', 'my life')
    driver.quit()