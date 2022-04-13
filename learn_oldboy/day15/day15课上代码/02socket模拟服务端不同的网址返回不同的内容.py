# coding=utf-8
"""
使用socket,简单的模拟一下web 服务端
实现不同的网址返回不同的内容
"""

import socket

sk = socket.socket()
sk.bind(("127.0.0.1", 8080))
sk.listen(5)


def home(url):
    return b"this is home page!"


def index(url):
    return b"this is index page!"


while 1:
    # 建立连接
    conn, addr = sk.accept()
    # 收消息
    data = conn.recv(8096)
    data_str = str(data, encoding="utf8")
    url = data_str.split("\r\n")[0].split()[1]
    if url == "/index/":
        msg = index(url)
    elif url == "/home/":
        msg = home(url)
    else:
        msg = b"404!"
    # 回复消息
    conn.send(b"HTTP/1.1 200 OK\r\n\r\n")  # 响应行
    conn.send(msg)  # 发送相应体
    conn.close()
