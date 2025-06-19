# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2025/6/18 16:53
# @Author : waxberry
# @File : main.py
# @Software : PyCharm


from db import init_db
from game import ZSGame

# 初始化数据库
init_db()

# 启动游戏
if __name__ == '__main__':
    game = ZSGame()
    game.run()