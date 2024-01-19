# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2024/1/19 9:18
# @Author : waxberry
# @File : client.py
# @Software : PyCharm


import socket

# 返回主动套接字
client = socket.socket(socket.AF_INET,
                       socket.SOCK_STREAM)

# 连接服务端
client.connect(('localhost', 12345))
while True:
    # 发送消息
    data = input('请输入内容：')
    if data.strip().lower() in ('q', 'quit', 'exit'):
        client.close()
        print('Bye~~~')
        break
    client.send(data.encode('utf-8'))
    print(client.recv(1024).encode('utf-8'))