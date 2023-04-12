#coding:utf-8

from ConfigParser import ConfigParser
from ProjectVar.var import page_object_repository_path#新加的

class ParsePageObjectRepositoryConfig(object):

    def __init__(self):#去掉config_path参数
        self.cf = ConfigParser()#生成解析器
        self.cf.read(page_object_repository_path)#直接用变量代替

    def getItemSetion(self, setionName):
        print (self.cf.items(setionName))
        return dict(self.cf.items(setionName))

    def getOptionValue(self, setionName, optionName):#返回一个字典
        print (self.cf.get(setionName, optionName))
        return self.cf.get(setionName, optionName)

if __name__ == '__main__':
    # pp = ParsePageObjectRepositoryConfig("G:\python\-dataDrivenTestPractice1\conf\PageObjectRepository.ini")
    pp = ParsePageObjectRepositoryConfig()#在构造函数中已经把配置文件的地址变量初始化了
    print (pp.getItemSetion("126mail_login"))

    print (pp.getOptionValue("126mail_login", "login_page.username"))