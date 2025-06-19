# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2025/6/18 16:55
# @Author : waxberry
# @File : equipment.py
# @Software : PyCharm

from enum import Enum

class GameState(Enum):
    MAIN_MENU = 1
    PLAYING = 2
    BATTLE = 3
    INVENTORY = 4
    CHARACTER = 5
    SKILLS = 6
    GAME_OVER = 7