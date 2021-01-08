#coding:utf-8

'''验证vivo应用商城的热门应用中排列前五的应用
是否是'抖音短视频-记录美好生活'、'今日头条'、u'知乎'、u'拼多多'、u'唯品会'''

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
        time.sleep(1)
        e2 = self.driver.find_element_by_id('com.bbk.store:id/go_recommend_text')
        e2.click()
        time.sleep(3)

    def test_sample(self):
        fileName = 'd:\\screenshot\\t01.png'
        self.driver.get_screenshot_as_file(fileName)
        result = ['抖音短视频-记录美好生活', '今日头条', u'知乎', u'拼多多', u'唯品会']
        e4 = self.driver.find_element_by_xpath('//android.widget.ListView/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.TextView[@index=0]')
        for i in range(5):
            print e4[i].text
            self.assertIn(e4[i].text, result)
        time.sleep(3)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main