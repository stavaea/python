# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2022/8/18 11:12
# @Author : waxberry
# @File : chat.py
# @Software : PyCharm

import json

def chat(self, data_dict):    #聊天逻辑
    message = data_dict['message'].strip()
    for user in self.users.keys():    #遍历所有的连接对象
        data = {}
        data['type'] = 'chat'
        current_nickname = self.users[self]
        data['nickname'] = '%s' % current_nickname    #获取当前发送消息客户端的昵称
        data['isMy'] = 'no'    #ismy字段默认为no
        if user == self:    #如果遍历的对象与发消息的客户端是同一个，则将ismy字段设为yes，便于前端用来判断展示不同的字体样式
            data['isMy'] = 'yes'
        data['message'] = message
        data = json.dumps(data)
        user.sendLine(data.encode('utf-8'))    #遍历将消息发送给每一个连接对象
