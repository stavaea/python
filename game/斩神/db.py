# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2025/6/18 16:55
# @Author : waxberry
# @File : db.py
# @Software : PyCharm


import sqlite3

def init_db():
    conn = sqlite3.connect('zsl_game.db')
    c = conn.cursor()

    # 创建玩家表
    c.execute('''CREATE TABLE IF NOT EXISTS players (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    level INTEGER DEFAULT 1,
                    exp INTEGER DEFAULT 0,
                    hp INTEGER DEFAULT 100,
                    max_hp INTEGER DEFAULT 100,
                    mp INTEGER DEFAULT 50,
                    max_mp INTEGER DEFAULT 50,
                    attack INTEGER DEFAULT 10,
                    defense INTEGER DEFAULT 5,
                    gold INTEGER DEFAULT 100,
                    location TEXT DEFAULT '新手村'
                    )''')

    # 创建物品表
    c.execute('''CREATE TABLE IF NOT EXISTS items (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    type TEXT NOT NULL,  -- weapon/armor/potion
                    attack INTEGER DEFAULT 0,
                    defense INTEGER DEFAULT 0,
                    hp_restore INTEGER DEFAULT 0,
                    mp_restore INTEGER DEFAULT 0,
                    value INTEGER NOT NULL
                    )''')

    # 创建玩家物品表
    c.execute('''CREATE TABLE IF NOT EXISTS player_items (
                    player_id INTEGER,
                    item_id INTEGER,
                    quantity INTEGER DEFAULT 1,
                    FOREIGN KEY(player_id) REFERENCES players(id),
                    FOREIGN KEY(item_id) REFERENCES items(id)
                    )''')

    # 创建技能表
    c.execute('''CREATE TABLE IF NOT EXISTS skills (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    damage_multiplier REAL DEFAULT 1.0,
                    mp_cost INTEGER DEFAULT 10,
                    level_required INTEGER DEFAULT 1
                    )''')

    # 创建玩家技能表
    c.execute('''CREATE TABLE IF NOT EXISTS player_skills (
                    player_id INTEGER,
                    skill_id INTEGER,
                    FOREIGN KEY(player_id) REFERENCES players(id),
                    FOREIGN KEY(skill_id) REFERENCES skills(id)
                    )''')

    # 插入初始数据
    # 初始物品
    initial_items = [
        ('新手剑', 'weapon', 5, 0, 0, 0, 20),
        ('布衣', 'armor', 0, 3, 0, 0, 15),
        ('小恢复药', 'potion', 0, 0, 20, 0, 10),
        ('小魔法药', 'potion', 0, 0, 0, 15, 12),
        ('斩神之刃', 'weapon', 15, 0, 0, 0, 200),
        ('神明铠甲', 'armor', 0, 12, 0, 0, 180),
    ]

    c.executemany(
        'INSERT INTO items (name, type, attack, defense, hp_restore, mp_restore, value) VALUES (?, ?, ?, ?, ?, ?, ?)',
        initial_items)

    # 初始技能
    initial_skills = [
        ('基础斩击', 1.0, 5, 1),
        ('神威斩', 1.8, 15, 5),
        ('灭神一击', 2.5, 30, 10),
        ('天罚', 3.2, 50, 15),
    ]

    c.executemany('INSERT INTO skills (name, damage_multiplier, mp_cost, level_required) VALUES (?, ?, ?, ?)',
                  initial_skills)

    conn.commit()
    conn.close()