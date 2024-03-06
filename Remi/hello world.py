# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2024/3/6 14:38
# @Author : waxberry
# @File : hello world.py
# @Software : PyCharm


import remi.gui as gui
from remi import start, App

class MyApp(App):
    def __init__(self, *args):
        super(MyApp, self).__init__(*args)

    def main(self):
        container = gui.VBox(width=120, height=100)
        self.lbl = gui.Label('Hello World')
        self.bt = gui.Button('Press me!')

        # 为鼠标点击按钮创造一个监听事件
        self.bt.onclick.do(self.on_button_pressed)

        # 添加部件
        container.append(self.lbl)
        container.append(self.bt)

        # 返回到根部件
        return container
    # 鼠标点击按钮的事件
    def on_button_pressed(self, widget):
        self.lbl.set_text('Button pressed!')
        self.bt.set_text('Hi!')

# 开启服务器
start(MyApp)#端口是可以设置的start(MyApp, address='0.0.0.0', port=8081)address是你设置的IP地址，port即为端口