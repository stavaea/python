# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2024/1/8 11:46
# @Author : waxberry
# @File : server.py
# @Software : PyCharm


import socket

mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysocket.bind(('', 8888))
mysocket.listen(5)

while True:
    connection, addr = mysocket.accept()
    revStr = connection.recv(1024)
    connection.send('Server:' + revStr)
    connection.close()