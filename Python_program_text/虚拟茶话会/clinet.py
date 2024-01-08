# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2024/1/8 13:40
# @Author : waxberry
# @File : clinet.py
# @Software : PyCharm



import socket
import time

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

clientsocket.connect(('', 8888))
while True:
    time.sleep(2)
    clientsocket.send('hello the5fire')
    print(clientsocket.recv(1024))
clientsocket.close()