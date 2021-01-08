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
            'unicodeKeyboard': True,
            'resetKeyboard': True
        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        time.sleep(3)
        e1 = self.driver.find_element_by_id('com.bbk.store:id/wlan_choose_page_btn')
        e1.click()
        time.sleep(1)
        e2 = self.driver.find_element_by_id('com.bbk.store:id/go_recommend_text')
        e2.click()
        time.sleep(3)

    def test_sample02(self):
        result = []
        e6 = self.driver.find_element_by_id('com.bbk.store:id/key_label')
        e6.click()
        time.sleep(1)
        e7 = self.driver.find_element_by_id('com.bbk.store:id/serach_input')
        e7.clear()
        e7.send_keys('光荣之路')
        time.sleep(5)
        e8 = self.driver.find_element_by_id('com.bbk.store:id/serach_box')
        e8.clear()
        time.sleep(2)
        e9 = self.driver.find_elements_by_xpath('//android.widget.ListView/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.TextView')
        for i in e9:
            print i.text
            result.append(i.text)
        self.driver.swipe(500, 1700, 500, 180, 2000)
        time.sleep(2)
        e9 = self.driver.find_elements_by_xpath(
            '//android.widget.ListView/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.TextView')
        for i in e9:
            print i.text
            result.append(i.text)
        time.sleep(2)
        self.assertIn('光荣之路', result)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main