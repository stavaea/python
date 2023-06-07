# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2023/5/31 10:13
# @Author : waxberry
# @File : seat_book.py
# @Software : PyCharm

import time

from traits.trait_types import self


class SeatBooking:
    # 展示所有座位的预定信息
    def check_booking(self, seats):
        print("正在为您查询该场次电影的预订状态...")
        time.sleep(0.7)
        print("从上到下为1~6排，从左至右为1~8座")
        print("====================")
        for row in seats:
            time.sleep(0.1)
            print(''.join(row))
        print("====================")
        time.sleep(0.7)

    # 获取符合要求的行索引
    def get_row(self):
        input_row = input("预订第几排的座位呢？请输入1~6之间的数字")
        valid_row = [str(i + 1) for i in range(6)]

        while input_row not in valid_row:
            input_row = input("没有按要求输入哦，请输入1~6之间的数字")

        row = int(input_row) - 1
        return row

    # 获取符合要求的列索引
    def get_col(self):
        input_col = input("预订这一排的第几座呢？请输入1~8之间的数字")
        valid_col = [str(i + 1) for i in range(8)]

        while input_col not in valid_col:
            input_col = input("没有按要求输入哦，请输入1~8之间的数字")

        col = int(input_col) - 1
        return col

    # 预订指定座位
    def book_seat(self, seats):
        while True:
            row = self.get_row()
            col = self.get_col()
            # 指定座位没有被预订
            if seats[row][col] == 'o':
                print("正在为您预定指定座位...")
                time.sleep(0.7)
                seats[row][col] == '●'
                print("预订成功！座位号：{}排{}座".format(row + 1, col + 1))
                break   #结束循环，退出选座
            # 指定的座位已经被预订了
            else:
                print("这个座位已经被预订了哦，试试别的吧")
                time.sleep(0.7)

    # 预订最靠前的座位
    def book_seat_at_front(self, seats):
        print("正在为您预订最靠前的座位...")
        time.sleep(0.7)
        # 外循环：遍历seats的行
        for row in range(6):
            # 内循环：遍历seats的列
            for col in range(8):
                # 若碰到没有被预订的座位
                if seats[row][col] == "o":
                    seats[row][col] == '●' #预订该座位
                    print("预订成功！座位号：{}排{}座".format(row + 1, col + 1))
                    return #结束函数的执行，返回到它被调用的地方
        # 没有在循环内部结束程序,说明不存在没有被预订的座位
        print("非常抱歉🥺，所有座位都被订满了，无法为您保留座位")