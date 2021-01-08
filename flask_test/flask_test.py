#coding:utf-8
from flask import Flask  # 导入Flask类，这个类的实例化就是wsgi的应用
from flask_bootstrap import Bootstrap
from flask import render_template

app = Flask(__name__, static_folder='', template_folder='') #创建了一个类的实例，创建flask实例的过程中，
# 可以执行静态代码默认目录，模版文件默认目录等

bootstrap = Bootstrap()
bootstrap.init_app(app)

@app.route('/') #路由路径，就是下面访问下面方法的路径，这里就单一个/，代码域名主页
def hello_world():
    # return 'Hello World!'   #hello world方法的实现，这里是返回一个字符串
    return render_template('hello_world.html')

def schedule_list():
    schedules = [
        {'id': 1, 'date': '2018-04-16', 'name': 'first_thing', 'desc': 'first_thing_desc', 'priority': 'P0',},
        {'id': 1, 'date': '2018-04-16', 'name': 'second_thing', 'desc': 'second_thing_desc', 'priority': 'P0',}
    ]
    return render_template('schedule_list.html', schedules=schedules)
if __name__ == '__main__':  #启动应用的命令
    app.run()
