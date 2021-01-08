# coding=utf-8
from flask import Flask, url_for
from flask import render_template, request
from models import User

app = Flask(__name__)# 创建了一个Flask类的实例__name__是自定义的名称，也可以用其他的，如__main__等


# @app.route('/user/') # 用route()装饰器来自定义自己的URL
# # def hello_world():
# #     return 'Hello World!'
#
# def test():# 创建一个函数，返回一个值
#     return 'hello user'
#
# @app.route('/reverse_url')# 用route()装饰器来自定义自己的URL
# def reverse_url():# 创建一个函数，返回一个值
#     return 'reverse_url:' + url_for('uesr')


@app.route('/user/')
def user():
    fuser = User('12345', 'Michael')
    return render_template('index.html', user=fuser)
@app.route('/', methods=['GET', 'POST'])
def login():
    return render_template('login.html', thismethod=request.method)

if __name__ == '__main__':
    app.debug = True
    app.run()
