# coding=utf-8
"""
根据URL中不同的路径返回不同的内容--函数进阶版
返回HTML页面
让网页动态起来
wsgiref模块版
"""

import time
from wsgiref.simple_server import make_server


# 将返回不同的内容部分封装成函数
def index(url):
    with open("index.html", "r", encoding="utf8") as f:
        s = f.read()
        now = str(time.time())
        s = s.replace("@@oo@@", now)
    return bytes(s, encoding="utf8")


def home(url):
    with open("home.html", "r", encoding="utf8") as f:
        s = f.read()
    return bytes(s, encoding="utf8")


# 定义一个url和实际要执行的函数的对应关系
list1 = [
    ("/index/", index),
    ("/home/", home),
]


def run_server(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html;charset=utf8'), ])  # 设置HTTP响应的状态码和头信息
    url = environ['PATH_INFO']  # 取到用户输入的url

    func = None
    for i in list1:
        if i[0] == url:
            func = i[1]
            break
    if func:
        response = func(url)
    else:
        response = b"404 not found!"
    return [response, ]


if __name__ == '__main__':
    httpd = make_server('127.0.0.1', 8090, run_server)
    print("我在8090等你哦...")
    httpd.serve_forever()
