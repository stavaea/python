#coding:utf-8

from appium import webdriver
import time
import unittest

class APPCenter(unittest.TestCase):
    def setUp(self):
        desired_caps = {
            'platforName': 'Android',
            'platforVersion': '7.1.1',
            'deviceName': '60c9dcf1',
            'appPackage': 'com.bbk.store',
            'appActivity': '.ui.Appstore',
        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        time.sleep(3)
        e1 = self.driver.find_element_by_id('com.bbk.store:id/wlan_choose_page_btn')
        e1.click()
        time.sleep(3)
        e2 = self.driver.find_element_by_id('com.bbk.store:id/go_recommend_text')
        e2.click()
        time.sleep(3)

    def test_sample02(self):
        e6 = self.driver.find_element_by_id('com.bbk.store:id/key_label')
        e6.click()
        time.sleep(1)
        e7 = self.driver.find_element_by_id('com.bbk.store:id/serach_input')
        e7.send_keys('music')
        time.sleep(1)
        e8 = self.driver.find_element_by_id('com.bbk.store:id/search_box')
        e8.click()
        time.sleep(1)
        e9 = self.driver.find_element_by_xpath('//android.widget.ListView/android.widget.RelativeLayout[2]/android.widget.TextView')
        e9.click()
        time.sleep(20)
        print self.driver.is_app_installed('com.xiaochang.easylive')
        self.driver.remove_app('com.xiaochang.easylive')
        print self.driver.is_app_installed('com.xiaochang.easylive')

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main