# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2024/1/19 9:23
# @Author : waxberry
# @File : Multithreading_server.py
# @Software : PyCharm


import socket
import threading


server = socket.socket()
server.setsockopt(socket.SOL_SOCKET,
                  socket.SO_REUSEADDR, True)
server.bind(('localhost', 12345))
server.listen(5)


def handle_message(conn, addr):
    while True:
        msg = conn.recv(1024)
        if not msg:
            print(f"客户端(ip: {addr[0]}, port: {addr[1]}) 已经断开连接")
            conn.close()
            break
        print(f"客户端(ip: {addr[0]}, port: {addr[1]}) 发来消息:", msg.decode('utf-8'))
        conn.send("服务端收到, 你发的消息是: ".encode('utf-8') + msg)

while True:
    conn, addr = server.accept()
    threading.Thread(
        target=handle_message,
        args=(conn, addr)
    ).start()