#coding:utf-8
from flask import Flask, render_template, request
import json

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'hello,world'

@app.route('/hello')
def hello():
    peoples = ['zhangsan', 'lisi', '234']
    # return render_template('hello.html', text='hello Kugou')
    return render_template('hello.html', peoples=peoples)

@app.route('/city_code', methods=['POST', 'GET'])
def hi():
    None
    json.loads(request.get_data())#转json
    print request.args.get('name')#get
    print request.form.get('name')#post
    print request.get_data()#raw(数组)
    peoples = ['zhangsan', 'lisi', '234']
    return render_template('hello.html', peoples=peoples)

@app.route('/')
def demo():
    return render_template('demo.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)