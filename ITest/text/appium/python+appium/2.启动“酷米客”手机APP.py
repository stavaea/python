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
            'appPackage': 'com.coomix.app.bus',
            'appActivity': '.activity.WelcomeActivity',
            'appWaitActivity': '.activity.MainActivity'
        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def test_sample(self):
        e1 = self.driver.find_element_by_id('com.coomix.app.bus:id/item_main_top_subway')
        e1.click()
        time.sleep(3)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main