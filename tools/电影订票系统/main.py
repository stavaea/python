# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2023/5/31 11:06
# @Author : waxberry
# @File : main.py
# @Software : PyCharm


import time
from tools.电影订票系统.infos import infos
from tools.电影订票系统.film_selector import FilmSelector
from tools.电影订票系统.seat_book import SeatBooking

class Controller:
    def __init__(self, infos):
        self.films = infos  #电影库所有电影
        # 打印欢迎语
        self.welcome()
        # 用户选择想观看的电影
        self.choose_film()
        # 根据用户选择,执行不同流程
        if self.choice != 'x':
            # 为指定场次预订座位
            self.choose_seat()
        # 打印结束语
        self.bye()

    # 用户选择想观看的电影
    def choose_seat(self):
        # 取出用户所选择的电影
        film = self.films[int(self.choice) - 1]
        # 取出所选择电影的电影名、座位表、宣传画
        name = film['name']
        seats_list = film['seats']
        symbol = film['symbol']

        # 打印提示信息和电影宣传画
        print('正在为您预订电影《{}》的座位'.format(name))
        time.sleep(0.7)
        print(symbol)
        time.sleep(0.7)

        # 打印预订座位的方法列表
        print('支持的座位预订方式如下：')
        time.sleep(0.7)
        print('+=============================+')
        print('1 - 指定行列号预订座位')
        print('2 - 给我预订一个最靠前的座位')
        print('+=============================+')
        time.sleep(0.7)
        print('')

        # 获取座位预订方式
        method = input('请选择座位预订方式')
        # 定义符合要求输入列表 valid_method
        valid_method = ['1', '2']
        # 当不符合要求时,循环获取新的选项
        while method not in valid_method:
            method = input('没有按照要求输入哦，请重新输入')


        # 实例化SeatBooking类
        booking = SeatBooking()
        # 打印所有座位的预订信息
        booking.check_booking(seats_list)
        # 方法1：指定行列号
        if method == '1':
            booking.check_booking(seats_list)
        # 方法2：预订最靠前的座位
        else:
            booking.book_seat_at_front(seats_list)


    # 打印欢迎语
    def welcome(self):
        print('+===============================+')
        print('+        欢迎来到时光电影院      +')
        print('+===============================+')
        print('')
        time.sleep(0.7)


    # 打印结束语
    def bye(self):
        print('')
        time.sleep(0.7)
        print('+===============================+')
        print('+    已经退出影院系统，下次见！👋    ')
        print('+===============================+')

# 实例化Controller类
s = Controller(infos)