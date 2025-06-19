# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2025/6/19 9:23
# @Author : waxberry
# @File : enemy.py
# @Software : PyCharm


import random

class Enemy:
    def __init__(self, name, level):
        self.name = name
        self.level = level
        self.max_hp = 50 + level * 20
        self.hp = self.max_hp
        self.attack = 8 + level * 3
        self.defense = 4 + level * 2
        self.exp_reward = random.randint(5, 15) + level * 5

    def take_damage(self, damage):
        actual_damage = max(1, damage - self.defense // 2)
        self.hp -= actual_damage
        if self.hp < 0:
            self.hp = 0
        return actual_damage