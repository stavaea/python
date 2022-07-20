# ！/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2022/7/1 15:13
# @Author : waxberry
# @File : xmindData.py
# @Software : PyCharm


import jsonpath

from xmindparser import xmind_to_dict

class XMindData(object):
    '''xmind数据处理'''

    def __init__(self):
        '''定义两个list数组'''
        #存放每一条用例
        self.case:list = []
        #存放所有的用例list
        self.list_data:list = []

    @staticmethod
    def read_XMind_to_list(XMindname) ->list:
        '''读取xmind文件所有的内容
        :param XMindname
        :return：list'''
        return xmind_to_dict(XMindname)

    def __data__processing(self,data:dict):
        '''私有方法，采用递归处理数据
        :param data:dice类型
        :return:'''
        self.case.append(data['title'])

        #通过json_path判断该data是否包含topics节点（包含返回数据，不包含则返回false
        #如果找到的话返回的结果是一个列表
        result = jsonpath.jsonpath(data,'$.topics')

        if type(result) != bool:
            for xm in result:
                for m in xm:
                    self.__data__processing(m)
            self.case = self.case[:-1]
        else:
            self.lists_data.append(self.case)
            self.case = self.case[-1:]

        def get_list_data(self,data) -> list:
            '''循环调用递归函数，读取数据
            :param data:传的数据参数是第一个画布的头节点：data = allData[0]['topic']['topics']
            :return:list 嵌套list，每一个嵌套的list就是一条测试用例
            '''
            title = data
            return title

        def clear_init_list_data(self):
            '''
            清空初始化列表数据，避免后面数据出现脏数据
            :return:
            '''
            self.case.clear()
            self.lists_data.clear()
