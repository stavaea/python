# coding=utf-8
"""
使用socket,简单的模拟一下web 服务端
"""

import socket

sk = socket.socket()
sk.bind(("127.0.0.1", 8080))
sk.listen(5)

while 1:
    # 建立连接
    conn, addr = sk.accept()
    # 收消息
    data = conn.recv(8096)
    print(data)
    # 回复消息
    conn.send(b"HTTP/1.1 200 OK\r\n\r\n")
    conn.send(b"<h1>O98K</h1>")
    conn.close()
