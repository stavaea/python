#coding:utf-8

import unittest
from appium import webdriver

class BaseAction(object):
    '''对元素操作的公共方法进行封装，并增加日志记录处理'''

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, ele_type, value):
        '''查询页面元素，增加显性时间等待机制
        Args:
            ele_type(str):元素定位方式
            value(str):元素定位属性值
        Returns:
            ele(WebElement):返回查找到的元素对象
        '''
        ele = None
        try:
            if ele_type == 'id':
                WebdriverWait(self.driver, 15).until(lambda driver: driver.find_element_by_id(value))
                ele = self.driver.find_element_by_id(value)
            elif ele_type =='name':
                WebdriverWait(self.driver, 15).until(lambda driver: driver.find_element_by_name(value))
                ele = self.driver.find_element_by_name(value)
            elif ele_type =='link_text':
                WebdriverWait(self.driver, 15).until(lambda driver: driver.find_element_by_link_text(value))
                ele = self.driver.find_element_by_link_text(value)
            elif ele_type =='partial_link_text':
                WebdriverWait(self.driver, 15).until(lambda driver: driver.find_element_by_partial_link_text(value))
                ele = self.driver.find_element_by_partial_link_text(value)
            elif ele_type == 'tag_name':
                WebdriverWait(self.driver, 15).until(lambda driver: driver.find_element_by_tag_name(value))
                ele = self.driver.find_element_by_tag_name(value)
            elif ele_type == 'xpath':
                WebdriverWait(self.driver, 15).until(lambda driver: driver.find_element_by_xpath(value))
                ele = self.driver.find_element_by_xpath(value)
            else:
                print ('没有这种元素定位方式｛｝'.format(ele_type))
        except (NoSuchElementException) as e:
            print (e.msg)
        except (TimeoutException) as e:
            print (e.msg)
        else:
            return ele