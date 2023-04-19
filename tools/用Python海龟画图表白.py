# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2023/4/17 11:14
# @Author : waxberry
# @File : 用Python海龟画图表白.py
# @Software : PyCharm


import turtle
import random


# 输入你爱人的姓名:
my_love = ''

def love(x, y):
    lv = turtle.Turtle()
    lv.hideturtle()
    lv.up()
    lv.goto(x, y) #定位到x,y
    def curvemove(): #画圆弧
        for i in range(20):
            lv.right(10)
            lv.forward(2)

    lv.color('red', 'pink')
    lv.speed(10000)
    lv.pensize(1)

    # 开始画爱心
    lv.down()
    lv.begin_fill()
    lv.left(140)
    lv.forward(22)
    curvemove()
    lv.left(120)
    curvemove()
    lv.forward(22)
    lv.write(my_love, font=('Arial', 12, 'normal'), align='center')
    lv.left(140)
    lv.end_fill()

def tree(branchlen, t):
    if branchlen > 5:
        if branchlen < 20:
            t.color('blue')
            t.pensize(random.uniform((branchlen + 5)/4-2, (branchlen+6)/4+5))
            t.down()

            t.forward(branchlen)
            love(t.xcor(), t.ycor())
            t.up()

            t.backward(branchlen)
            t.color('brown')
            return

    t.pensize(random.uniform((branchlen+5)/4-2, (branchlen+6)/4+5))
    t.down()
    t.forward(branchlen)

    # 递归
    ang = random.uniform(15, 45)
    t.right(ang)
    tree(branchlen-random.uniform(12, 16), t)
    t.left(2*ang)
    tree(branchlen-random.uniform(12, 16), t)
    t.right(ang)
    t.up()
    t.backward(branchlen)


myWin = turtle.Screen()
t = turtle.Turtle()
t.hideturtle()
t.speed(100)

t.left(90)
t.up()
t.backward(200)
t.down()
t.color('brown')
t.pensize(32)
t.forward(60)
tree(100, t)
myWin.exitonclick()