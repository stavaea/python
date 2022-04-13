# coding=utf-8
"""
使用socket,简单的模拟一下web 服务端
实现不同的网址返回不同的内容
返回具体的HTML网页
返回动态的网页
"""

import socket
import time

sk = socket.socket()
sk.bind(("127.0.0.1", 8080))
sk.listen(5)


def home(url):
    with open("home.html", "r") as f:
        html_msg = f.read()

    now = time.time()
    msg = html_msg.replace("@@xx@@", str(now))  # 进行字符串替换

    return bytes(msg, encoding="utf8")  # 转成bytes类型返回


def index(url):
    return b"this is index page!"

def user(url):
    return b"This is user page!"

# 定义一个URL和函数的对应关系
url_func = [
    ("/index/", index),
    ("/home/", home),
    ("/user/", user),
]


while 1:
    # 建立连接
    conn, addr = sk.accept()
    # 收消息
    data = conn.recv(8096)
    data_str = str(data, encoding="utf8")
    # 拿到用户访问的具体URL
    url = data_str.split("\r\n")[0].split()[1]

    func = None
    for i in url_func:
        if i[0] == url:
            func = i[1]
            break
    if func:
        msg = func(url)
    else:
        msg = b"404!"
    # 回复消息
    conn.send(b"HTTP/1.1 200 OK\r\n\r\n")  # 响应行
    conn.send(msg)  # 发送相应体
    conn.close()
