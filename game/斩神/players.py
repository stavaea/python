# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2025/6/18 17:36
# @Author : waxberry
# @File : players.py
# @Software : PyCharm


import sqlite3
from equipment import GameState

class Player:
    def __init__(self, player_id):
        self.conn = sqlite3.connect('zsl_game.db')
        self.c = self.conn.cursor()
        self.load_player(player_id)

    def load_player(self, player_id):
        self.c.execute('SELECT * FROM players WHERE player_id=?', (str(player_id),))
        player_data = self.c.fetchone()

        if player_data:
            self.id = player_data[0]
            self.name = player_data[1]
            self.level = player_data[2]
            self.exp = player_data[3]
            self.hp = player_data[4]
            self.max_hp = player_data[5]
            self.mp = player_data[6]
            self.max_mp = player_data[7]
            self.attack = player_data[8]
            self.defense = player_data[9]
            self.gold = player_data[10]
            self.location = player_data[11]

            # 加载装备
            self.weapon = None
            self.armor = None
            self.load_equipment()

            # 加载技能
            self.skills = []
            self.load_skills()

    def load_equipment(self):
        self.c.execute('''SELECT items.* FROM player_items 
                       JOIN items ON player_items.item_id = items.id
                       WHERE player_items.player_id=? AND (items.type='weapon' OR items.type='armor')''', (self.id,))

        equipment = self.c.fetchall()

        for item in equipment:
            item_id, name, item_type, attack, defense, hp_restore, mp_restore, value = item
            if item_type == 'weapon':
                self.weapon = {
                    'id': item_id,
                    'name': name,
                    'attack': attack,
                    'value': value
                }
            elif item_type == 'armor':
                self.armor = {
                    'id': item_id,
                    'name': name,
                    'defense': defense,
                    'value': value
                }

    def load_skills(self):
        self.c.execute('''SELECT skills.* FROM player_skills 
                       JOIN skills ON player_skills.skill_id = skills.id
                       WHERE player_skills.player_id=?''', (self.id,))

        skills = self.c.fetchall()

        for skill in skills:
            skill_id, name, damage_multiplier, mp_cost, level_required = skill
            self.skills.append({
                'id': skill_id,
                'name': name,
                'damage_multiplier': damage_multiplier,
                'mp_cost': mp_cost,
            })

    def save(self):
        self.c.execute('''UPDATE players SET 
                       level=?, exp=?, hp=?, max_hp=?, mp=?, max_mp=?, 
                       attack=?, defense=?, gold=?, location=?
                       WHERE id=?''',
                       (self.level, self.exp, self.hp, self.max_hp, self.mp, self.max_mp,
                        self.attack, self.defense, self.gold, self.location, self.id))
        self.conn.commit()

    def add_exp(self, amount):
        self.exp += amount
        exp_needed = self.level * 100
        if self.exp > exp_needed:
            self.level_up()

    def level_up(self):
        self.level += 1
        self.exp = self.exp - (self.level - 1) * 100
        self.max_hp += 20
        self.hp = self.max_hp
        self.max_mp += 10
        self.mp = self.max_mp
        self.attack += 3
        self.defense += 2
        self.save()

    def user_item(self, item_id):
        self.c.execute('SELECT * FROM items WHERE id=?', (str(item_id),))
        item = self.c.fetchone()

        if item:
            _, name, item_type, attack, defense, hp_restore, mp_restore, value = item
            if item_type == 'potion':
                if hp_restore > 0:
                    self.hp = min(self.max_hp, self.hp + hp_restore)
                if mp_restore > 0:
                    self.mp = min(self.max_mp, self.mp + mp_restore)
                self.remove_item(item_id, 1)
                self.save()
                return True
        return False

    def add_item(self, item_id, quantity=1):
        self.c.execute("SELECT * FROM player_items WHERE player_id=? AND item_id=?", (self.id, item_id))
        existing = self.c.fetchone()

        if existing:
            new_quantity = existing[2] + quantity
            self.c.execute("UPDATE player_items SET quantity=? WHERE player_id=? AND item_id=?",
                          (new_quantity, self.id, item_id))
        else:
            self.c.execute("INSERT INTO player_items (player_id, item_id, quantity) VALUES (?, ?, ?)",
                          (self.id, item_id, quantity))
        self.conn.commit()

    def remove_item(self, item_id, quantity=1):
        self.c.execute("SELECT quantity FROM player_items WHERE player_id=? AND item_id=?", (self.id, item_id))
        existing = self.c.fetchone()

        if existing:
            current_quantity = existing[0]
            if current_quantity <= quantity:
                self.c.execute("DELETE FROM player_items WHERE player_id=? AND item_id=?", (self.id, item_id))
            else:
                self.c.execute("UPDATE player_items SET quantity=? WHERE player_id=? AND item_id=?",
                              (current_quantity - quantity, self.id, item_id))
            self.conn.commit()
            return True
        return False

    def equip_item(self, item_id):
        self.c.execute("SELECT * FROM items WHERE id=?", (item_id,))
        item = self.c.fetchone()

        if item:
            _, name, item_type, attack, defense, hp_restore, mp_restore, value = item
            if item_type == 'weapon':
                if self.weapon:
                    # 卸下当前武器
                    pass
                self.weapon = {
                    'id': item_id,
                    'name': name,
                    'attack': attack,
                    'value': value
                }
            elif item_type == 'armor':
                if self.armor:
                    # 卸下当前防具
                    pass
                self.armor = {
                    'id': item_id,
                    'name': name,
                    'attack': attack,
                    'value': value
                }
            self.save()
            return True
        return False

    def get_total_attack(self):
        back_attack = self.attack
        weapon_attack = self.weapon['attack'] if self.weapon else 0
        return back_attack + weapon_attack

    def get_total_defense(self):
        base_defense = self.defense
        armor_defense = self.armor['defense'] if self.armor else 0
        return base_defense + armor_defense

    def get_inventory(self):
        self.c.execute('''SELECT items.*, player_items.quantity 
                       FROM player_items 
                       JOIN items ON player_items.item_id = items.id
                       WHERE player_items.player_id=?''', (self.id,))
        return self.c.fetchone()