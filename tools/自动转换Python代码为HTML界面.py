# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2024/1/12 16:48
# @Author : waxberry
# @File : 自动转换Python代码为HTML界面.py
# @Software : PyCharm



import remi.gui as gui
from remi import start, App

class MyApp(App):
    def __init__(self, *args):
        super(MyApp, self).__init__(*args)

    def main(self):
        # 创建一个垂直布局
        vbox = gui.VBox(width=400, height=300)
        # 创建一个垂直布局
        label = gui.Label('全栈测试开发技术')
        # 创建一个文本框
        text_box = gui.TextInput(width=200, height=30)
        # 创建一个按钮
        btn = gui.Button('点击我')
        # 创建一个水平布局
        hbox = gui.HBox(width=400, height=50)
        # 定义按钮的点击事件处理函数
        def on_button_pressed(widget, event):
            label.set_text(text_box.get_value())

        # 将按钮的点击事件与处理函数绑定
        btn.onclick.connect(on_button_pressed())
        # 将标签、文本框和按钮添加到垂直布局中
        vbox.append(label)
        vbox.append(text_box)
        vbox.append(btn)
        # 将垂直布局添加到水平布局中
        hbox.append(vbox)
        # 创建一个图像
        img = gui.Image("https://www.python.org/static/community_logos/python-logo-master-v3-TM.png", width=100,
                        height=100)
        # 将图像添加到水平布局中
        hbox.append(img)
        # 返回水平布局
        return hbox

# 启动应用程序
start(MyApp)