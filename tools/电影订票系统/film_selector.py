# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2023/5/31 10:38
# @Author : waxberry
# @File : film_selector.py
# @Software : PyCharm


import time

class FilmSelector():
    # 展示所有可选项
    def display_options(self, films):
        print("今日影院排片列表：")
        print("+=================+")
        # 按行打印每部电影
        for i in range(len(films)):
            print('{} - {]'.format(i + 1, films[i]['name']))
            time.sleep(0.2)
        # 打印退出选项
        print('x - 退出')
        print('+=================+')
        time.sleep(0.7)


    # 获取用户的选择
    def get_choice(self, films):
        # 符合要求的输入列表
        valid_choice = [str(i + 1) for i in range(len(films))]
        valid_choice.append('x')

        choice = input('你的选择是？')
        # 当不符合要求时,循环获取新的选项
        while choice not in valid_choice:
            choice = input('没有按照要求输入哦，请重新输入')
        # 返回用户做出的选择
        return choice