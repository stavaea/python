#coding:utf-8

from selenium.webdriver.support.ui import WebDriverWait
import ConfigParser
import os
from selenium import webdriver

class GetOption(object):
    def __init__(self):
        # 获取存放页面元素定位表达方式及定位表达式的配置文件所在绝对路径
        # os.path.abspath(__file__)表示获取当前文件所在路径目录
        self.uiObjMapPath = os.path.dirname(os.path.abspath(__file__)) + "\\UiObjectMapSendMail.ini"
        # print self.uiObjMapPath

    def getOption(self, setionName, optionName):
        try:
            # 创建一个读取配置文件的实例
            cf = ConfigParser.ConfigParser()
            # 将配置文件加载到内存
            cf.read(self.uiObjMapPath)
            # 根据setion和option获取配置文件中的配置信息
            setion = cf.get(setionName, optionName)
            # print "setion:", setion
        except Exception as e:
            raise e
        else:
            # 当页面元素被找到后，将该页面元素对象返回给调用者
            return setion

if __name__ == '__main__':
    getoption = GetOption
    print (getoption.getOption("mailaccount", "username"))