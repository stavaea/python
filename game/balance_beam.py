# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2022/7/20 14:51
# @Author : waxberry
# @File : balance_beam.py
# @Software : PyCharm


import cfg
from modules import breakoutClone

'''主函数'''
def main():
    game = breakoutClone(cfg)
    game.run()

if __name__ == '__main__':
    main()