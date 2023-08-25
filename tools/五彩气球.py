# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2023/8/17 9:39
# @Author : waxberry
# @File : 五彩气球.py
# @Software : PyCharm


import turtle as tu
import random as ra
import math

tu.setup(1.0, 1.0)
t = tu.Pen()
t.ht() #隐藏小海龟

colors = ['red', 'skyblue', 'orange', 'yellow', 'lime', 'pink', 'violet']

class Balloon():#每个气球（气球类）

    def __init__(self):
        self.r = ra.randint(12, 20)#气球的半径
        self.x = ra.randint(-1000, 1000) #气球的横坐标
        self.y = ra.randint(-500, 500)#气球的纵坐标
        self.f = ra.uniform(-3.14, 3.14)#气球左右移动呈正弦函数
        self.speed = ra.randint(5, 10)#气球移动速度
        self.color = ra.choice(colors)#气球的颜色
        self.outline = 1 #气球的外框大小（可不要）

    def move(self):#气球移动函数
        if self.y <= 500: #当气球还在画布中时
            self.y += self.speed#设置上下移动速度
            self.x += self.speed * math.sin(self.f) #设置左右移动速度
            self.f += 0.1 #可以理解成标志，改变左右移动的方向
        else:
            self.r = ra.randint(12, 20)
            self.x = ra.randint(-1000, 1000)
            self.y = -500
            self.f = ra.uniform(-3.14, 3.14)
            self.speed = ra.randint(5, 10)
            self.color = ra.choice(colors)
            self.outline = 1

    def draw(self): #画气球函数，就是用turtle画气球
        t.penup()
        t.goto(self.x, self.y)
        t.pendown()
        t.color(self.color)
        t.left(45)
        t.begin_fill()
        t.fillcolor(self.color)
        for i in range(2):
            t.circle(self.r * 2, 90)
            t.circle(self.r, 90)
        t.end_fill()
        t.hideturtle()
        t.circle(self.r, -45)
        t.right(90)
        t.circle(20, 90)

Balloons = [] #用列表保存所有气球
for i in range(100):
    Balloons.append(Balloon())
tu.bgcolor('black')
while True: #开始漂浮
    tu.tracer(0)
    t.clear()
    for i in range(50):#在画布中设置50个漂浮的气球
        Balloons[i].move()
        Balloons[i].draw()
    tu.penup() #写祝福
    tu.goto(-250, 20)
    tu.pendown()
    tu.color('skyblue')
    tu.write('祝你快乐每一天！', font=('黑体', 80, 'italic'))#"italic"表示斜体
    tu.hideturtle()
    tu.update()
tu.mainloop()