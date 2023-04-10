# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2022/8/18 10:22
# @Author : waxberry
# @File : server_event_driven.py
# @Software : PyCharm

from twisted.internet.protocol import Factory
from twisted.protocols.basic import LineReceiver   #事件处理器
from twisted.internet import reactor
from model import login_model,register_model,chat_model
import json

class Chat(LineReceiver):
    def __init__(self, users):
        self.users = users

    def connectionLost(self, reason):   #断开链接时自动触发,从users字典去掉链接对象
        if self in self.users.keys():
            # print ('%断开链接' % self.users[self])
            del self.users[self]

    def dataReceived(self, data):    #对返回内容开始做处理,只要收到客户端消息,自动触发此文件
        data = data.decode('utf-8')
        data_dict = json.loads(data)
        # 根据type字段的值,进入对应的逻辑
        if data_dict['type'] == 'login':
            login_model.login(self, data_dict)
        elif data_dict['type'] == 'register':
            register_model.register(self, data_dict)
        elif data_dict['type'] == 'chat':
            chat_model.chat(self, data_dict)

class ChatFactory(Factory):
    def __init__(self):
        self.users = {}    #昵称映射到聊天实例,key-->登录成功的链接对象,value：昵称

    def buildProtocol(self, addr):  #此方法必须要实现
        print (addr)
        return Chat(self.users)    #返回一个处理具体业务请求的对象，参数传递了字典，存所有登录成功的连接对象

if __name__ == '__main__':
    reactor.listenTCP(1200, ChatFactory())    #使用tcp协议，实例化ChatFactory
    print ('开始进入监听状态')
    reactor.run()