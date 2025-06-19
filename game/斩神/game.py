# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2025/6/19 9:27
# @Author : waxberry
# @File : game.py
# @Software : PyCharm


import pygame
import sys
import random
from enemy import Enemy
from players import Player
from equipment import GameState

class ZSGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption('斩神')
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont('SimHei', 24)
        self.small_font = pygame.font.SysFont('SimHei', 18)

        self.state = GameState.MAIN_MENU
        self.player = None
        self.current_enemy = None
        self.battle_log = []

        # 创建新玩家
        self.create_new_player()

        # 游戏地图
        self.locations = [
            "新手村", "迷雾森林", "神陨峡谷", "天界之门",
            "神明大殿", "深渊牢狱", "混沌之海", "终焉之地"
        ]

        # 敌人类型
        self.enemy_types = [
            "小妖", "地精战士", "堕落天使", "暗影刺客",
            "火焰巨人", "寒冰女王", "雷霆神使", "混沌魔神"
        ]

    def create_new_player(self):
        # 创建新玩家
        conn = sqlite3.connect('zsl_game.db')
        c = conn.cursor()
        c.execute("INSERT INTO players (name) VALUES ('斩神者')")
        player_id = c.lastrowid

        # 添加初始装备
        c.execute("INSERT INTO player_items (player_id, item_id) VALUES (?, 1)", (player_id,))  # 新手剑
        c.execute("INSERT INTO player_items (player_id, item_id) VALUES (?, 2)", (player_id,))  # 布衣
        c.execute("INSERT INTO player_items (player_id, item_id) VALUES (?, 3)", (player_id,))  # 小恢复药
        c.execute("INSERT INTO player_items (player_id, item_id) VALUES (?, 3)", (player_id,))  # 小恢复药
        c.execute("INSERT INTO player_items (player_id, item_id) VALUES (?, 4)", (player_id,))  # 小魔法药

        # 添加初始技能
        c.execute("INSERT INTO player_skills (player_id, skill_id) VALUES (?, 1)", (player_id,))  # 基础斩击

        conn.commit()
        conn.close()

        self.player = Player(player_id)
        self.player.equip_item(1)  # 装备新手剑
        self.player.equip_item(2)  # 装备布衣

    def handle_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.player.save()
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if self.state == GameState.MAIN_MENU:
                    if event.key == pygame.K_RETURN:
                        self.state = GameState.PLAYING

                elif self.state == GameState.PLAYING:
                    if event.key == pygame.K_i:
                        self.state = GameState.INVENTORY
                    elif event.key == pygame.K_c:
                        self.state = GameState.CHARACTER
                    elif event.key == pygame.K_s:
                        self.state = GameState.SKILLS
                    elif event.key == pygame.K_SPACE:
                        self.start_battle()

                elif self.state == GameState.BATTLE:
                    if event.type == pygame.K_1:
                        self.player_attack()
                    elif event.type == pygame.K_2:
                        self.state = GameState.SKILLS
                    elif event.type == pygame.K_3:
                        self.state = GameState.INVENTORY
                    elif event.key == pygame.K_4:
                        self.try_escape()

                elif self.state == GameState.INVENTORY:
                    if event.type == pygame.K_SPACE:
                        self.state = GameState.PLAYING
                    elif pygame.K_1 <= event.key <= pygame.K_9:
                        item_index = event.key - pygame.K_1
                        inventory = self.player.get_inventory()
                        if item_index < len(inventory):
                            item_id = inventory[item_index][0]
                            self.player.user_item(item_id)

                elif self.state == GameState.SKILLS:
                    if event.key == pygame.K_SPACE:
                        if self.state_prev == GameState.BATTLE:
                            self.state = GameState.BATTLE
                        else:
                            self.state = GameState.PLAYING
                    elif pygame.K_1 <= event.key <= pygame.K_9:
                        skill_index = event.key - pygame.K_1
                        if skill_index < len(self.player.skills):
                            self.use_skill(skill_index)

                elif self.state == GameState.GAME_OVER:
                    if event.key == pygame.K_r:
                        # 重新开始游戏
                        self.create_new_player()
                        self.state = GameState.PLAYING

    def start_battle(self):
        # 根据玩家等级生成敌人
        enemy_level = max(1, self.player.level + random.randint(-1, 2))
        enemy_type = self.enemy_types[min(enemy_level - 1, len(self.enemy_types) - 1)]

        self.current_enemy = Enemy(enemy_type, enemy_level)
        self.state = GameState.BATTLE
        self.state_prev = GameState.PLAYING
        self.battle_log = [f"遭遇了{enemy_type}（Lv.{enemy_level}）！"]

    def player_attack(self):
        player_attack = self.player.get_total_attack()
        damage = self.current_enemy.take_damage(player_attack)
        self.battle_log.append(f"你对{self.current_enemy.name}造成了{damage}点伤害！")

        if self.current_enemy.hp <= 0:
            self.battle_log.append(f"你击败了{self.current_enemy.name}！")
            self.player.add_exp(self.current_enemy.exp_reward)
            self.player.gold += self.current_enemy.gold_reward
            self.battle_log.append(f"获得{self.current_enemy.exp_reward}经验值和{self.current_enemy.gold_reward}金币！")
            self.state = GameState.PLAYING
            self.player.save()
            return

        # 敌人反击
        enemy_damage = max(1, self.current_enemy.attack - self.player.get_total_defense() // 2)
        self.player.hp -= enemy_damage
        self.battle_log.append(f"{self.current_enemy.name}对你造成了{enemy_damage}点伤害！")

        if self.player.hp <= 0:
            self.battle_log.append("你被击败了...")
            self.state = GameState.GAME_OVER

    def use_skill(self, skill_index):
        skill = self.player.skills[skill_index]
        if self.player.mp < skill['mp_cost']:
            self.battle_log.append("魔法值不足！")
            self.state = GameState.BATTLE
            return

        self.player.mp -= skill['mp_cost']
        player_attack = self.player.get_total_attack()
        damage = int(player_attack * skill['damage_multiplier'])
        actual_damage = self.current_enemy.take_damage(damage)

        self.battle_log.append(f"你使用了{skill['name']}！")
        self.battle_log.append(f"对{self.current_enemy.name}造成了{actual_damage}点伤害！")

        if self.current_enemy.hp <= 0:
            self.battle_log.append(f"你击败了{self.current_enemy.name}！")
            self.player.add_exp(self.current_enemy.exp_reward)
            self.player.gold += self.current_enemy.gold_reward
            self.battle_log.append(f"获得{self.current_enemy.exp_reward}经验值和{self.current_enemy.gold_reward}金币！")
            self.state = GameState.PLAYING
            self.player.save()
            return

        # 敌人反击
        enemy_damage = max(1, self.current_enemy.attack - self.player.get_total_defense() // 2)
        self.player.hp -= enemy_damage
        # self.battle_log.append(f"{极}")
        self.battle_log.append(f"{self.current_enemy.name}对你造成了{enemy_damage}点伤害！")

        if self.player.hp <= 0:
            self.battle_log.append("你被击败了...")
            self.state = GameState.GAME_OVER
        else:
            self.state = GameState.BATTLE

    def try_escape(self):
        escape_chance = 0.7  # 70%逃脱几率
        if random.random() < escape_chance:
            self.battle_log.append("你成功逃脱了战斗！")
            self.state = GameState.PLAYING
        else:
            self.battle_log.append("逃脱失败！")
            # 敌人攻击
            # enemy_damage = max(1, self.current_enemy)
            enemy_damage = max(1, self.current_enemy.attack - self.player.get_total_defense() // 2)
            self.player.hp -= enemy_damage
            self.battle_log.append(f"{self.current_enemy.name}对你造成了{enemy_damage}点伤害！")

            if self.player.hp <= 0:
                self.battle_log.append("你被击败了...")
                self.state = GameState.GAME_OVER

    def draw_main_menu(self):
        self.screen.fill((20, 20, 40))

        title = self.font.render("斩神：神明之战", True, (220, 180, 60))
        self.screen.blit(title, (400 - title.get_width() // 2, 150))

        subtitle = self.small_font.render("在诸神统治的世界中，成为斩神者，挑战神明的权威！", True, (200, 200, 200))
        self.screen.blit(subtitle, (400 - subtitle.get_width() // 2, 200))

        prompt = self.font.render("按 Enter 键开始游戏", True, (100, 200, 100))
        self.screen.blit(prompt, (400 - prompt.get_width() // 2, 300))

        controls = [
            "游戏控制:",
            "空格键 - 探索/战斗",
            "I 键 - 打开背包",
            "C 键 - 查看角色",
            "S 键 - 查看技能"
        ]

        for i, text in enumerate(controls):
            ctrl = self.small_font.render(text, True, (180, 180, 220))
            self.screen.blit(ctrl, (100, 400 + i * 30))

    def draw_playing_screen(self):
        self.screen.fill((30, 30, 50))

        # 绘制顶部状态栏
        pygame.draw.rect(self.screen, (40, 40, 70), (0, 0, 800, 40))
        name_text = self.font.render(f"{self.player.name} Lv.{self.player.level}", True, (220, 220, 100))
        self.screen.blit(name_text, (20, 5))

        # HP/MP条
        pygame.draw.rect(self.screen, (80, 20, 20), (200, 10, 200, 20))
        pygame.draw.rect(self.screen, (200, 30, 30), (200, 10, 200 * self.player.hp / self.player.max_hp, 20))
        # hp_text = self.small_font.render(f"HP: {self.player.h极
        hp_text = self.small_font.render(f"HP: {self.player.hp}/{self.player.max_hp}", True, (240, 240, 240))
        self.screen.blit(hp_text, (410, 10))

        pygame.draw.rect(self.screen, (20, 40, 80), (200, 35, 200, 15))
        pygame.draw.rect(self.screen, (30, 120, 220), (200, 35, 200 * self.player.mp / self.player.max_mp, 15))
        mp_text = self.small_font.render(f"MP: {self.player.mp}/{self.player.max_mp}", True, (240, 240, 240))
        self.screen.blit(mp_text, (410, 35))

        # 金币和经验
        gold_text = self.small_font.render(f"金币: {self.player.gold}", True, (220, 180, 50))
        self.screen.blit(gold_text, (600, 10))

        exp_needed = self.player.level * 100
        exp_text = self.small_font.render(f"经验: {self.player.exp}/{exp_needed}", True, (180, 220, 120))
        self.screen.blit(exp_text, (600, 35))

        # 绘制位置信息
        location_text = self.font.render(f"当前位置: {self.player.location}", True, (180, 200, 240))
        self.screen.blit(location_text, (400 - location_text.get_width() // 2, 100))

        # 绘制操作提示
        prompt = self.font.render("按 空格键 探索区域", True, (150, 200, 150))
        self.screen.blit(prompt, (400 - prompt.get_width() // 2, 300))

        # 绘制装备信息
        weapon = self.player.weapon['name'] if self.player.weapon else "无"
        armor = self.player.armor['name'] if self.player.armor else "无"

        equip_text = self.small_font.render(f"武器: {weapon}    防具: {armor}", True, (200, 200, 180))
        self.screen.blit(equip_text, (400 - equip_text.get_width() // 2, 180))

        # 绘制控制提示
        controls = [
            "I: 背包  C: 角色  S: 技能"
        ]

        for i, text in enumerate(controls):
            ctrl = self.small_font.render(text, True, (180, 180, 220))
            self.screen.blit(ctrl, (400 - ctrl.get_width() // 2, 500 + i * 30))

    def draw_battle_screen(self):
        self.screen.fill((40, 20, 30))

        # 绘制玩家状态
        pygame.draw.rect(self.screen, (50, 30, 40), (0, 0, 800, 40))
        name_text = self.font.render(f"{self.player.name} Lv.{self.player.level}", True, (220, 220, 100))
        self.screen.blit(name_text, (20, 5))

        # HP/MP条
        pygame.draw.rect(self.screen, (80, 20, 20), (200, 10, 200, 20))
        pygame.draw.rect(self.screen, (200, 30, 30), (200, 10, 200 * self.player.hp / self.player.max_hp, 20))
        hp_text = self.small_font.render(f"HP: {self.player.hp}/{self.player.max_hp}", True, (240, 240, 240))
        self.screen.blit(hp_text, (410, 10))

        pygame.draw.rect(self.screen, (20, 40, 80), (200, 35, 200, 15))
        pygame.draw.rect(self.screen, (30, 120, 220), (200, 35, 200 * self.player.mp / self.player.max_mp, 15))
        mp_text = self.small_font.render(f"MP: {self.player.mp}/{self.player.max_mp}", True, (240, 240, 240))
        self.screen.blit(mp_text, (410, 35))

        # 敌人信息
        enemy_text = self.font.render(f"{self.current_enemy.name} Lv.{self.current_enemy.level}", True, (220, 100, 100))
        self.screen.blit(enemy_text, (400 - enemy_text.get_width() // 2, 100))

        # 敌人HP条
        pygame.draw.rect(self.screen, (80, 20, 20), (200, 150, 400, 20))
        pygame.draw.rect(self.screen, (200, 30, 30),
                         (200, 150, 400 * self.current_enemy.hp / self.current_enemy.max_hp, 20))
        enemy_hp = self.small_font.render(f"HP: {self.current_enemy.hp}/{self.current_enemy.max_hp}", True,
                                          (240, 240, 240))
        self.screen.blit(enemy_hp, (350, 150))

        # 绘制战斗日志
        pygame.draw.rect(self.screen, (20, 20, 30), (50, 200, 700, 200))
        for i, log in enumerate(self.battle_log[-5:]):
            log_text = self.small_font.render(log, True, (220, 220, 180))
            self.screen.blit(log_text, (70, 220 + i * 30))

        # 绘制战斗选项
        pygame.draw.rect(self.screen, (30, 40, 50), (0, 420, 800, 180))
        options = [
            "1. 攻击",
            "2. 技能",
            "3. 物品",
            "4. 逃跑"
        ]

        for i, option in enumerate(options):
            opt_text = self.font.render(option, True, (180, 200, 240))
            self.screen.blit(opt_text, (100 + i * 180, 450))

    def draw_inventory(self):
        self.screen.fill((30, 30, 50))

        # 标题
        title = self.font.render("背包", True, (220, 180, 60))
        self.screen.blit(title, (400 - title.get_width() // 2, 30))

        # 获取背包物品
        inventory = self.player.get_inventory()

        # 绘制物品列表
        if not inventory:
            empty_text = self.font.render("背包空空如也", True, (180, 180, 200))
            self.screen.blit(empty_text, (400 - empty_text.get_width() // 2, 200))
        else:
            for i, item in enumerate(inventory):
                item_id, name, item_type, attack, defense, hp_restore, mp_restore, value, quantity = item
                item_text = f"{i + 1}. {name}"
                if item_type == 'potion':
                    if hp_restore > 0:
                        item_text += f" (恢复HP: {hp_restore})"
                    if mp_restore > 0:
                        item_text += f" (恢复MP: {mp_restore})"
                elif item_type == 'weapon':
                    item_text += f" (攻击: {attack})"
                elif item_type == 'armor':
                    item_text += f" (防御: {defense})"

                item_text += f" x{quantity}"

                color = (200, 200, 180) if item_type == 'weapon' else \
                    (180, 200, 220) if item_type == 'armor' else \
                        (180, 220, 180)  # potion

                item_surf = self.small_font.render(item_text, True, color)
                self.screen.blit(item_surf, (100, 100 + i * 40))

        # 提示
        prompt = self.small_font.render("按数字键使用物品，ESC返回", True, (180, 200, 200))
        self.screen.blit(prompt, (400 - prompt.get_width() // 2, 500))

    def draw_character_screen(self):
        self.screen.fill((30, 30, 50))

        # 标题
        # title = self.font.render("角色信息", True, (220, 180, 极
        title = self.font.render("角色信息", True, (220, 180, 60))
        self.screen.blit(title, (400 - title.get_width() // 2, 30))

        # 基本信息
        info = [
            f"名称: {self.player.name}",
            f"等级: {self.player.level}",
            f"生命: {self.player.hp}/{self.player.max_hp}",
            f"魔法: {self.player.mp}/{self.player.max_mp}",
            f"攻击: {self.player.get_total_attack()}",
            f"防御: {self.player.get_total_defense()}",
            f"金币: {self.player.gold}",
            f"位置: {self.player.location}"
        ]

        for i, text in enumerate(info):
            info_text = self.small_font.render(text, True, (200, 200, 180))
            self.screen.blit(info_text, (150, 100 + i * 40))

            # 装备信息
        weapon = self.player.weapon['name'] if self.player.weapon else "无"
        armor = self.player.armor['name'] if self.player.armor else "无"

        equip_title = self.small_font.render("装备:", True, (180, 200, 240))
        self.screen.blit(equip_title, (150, 420))

        weapon_text = self.small_font.render(f"武器: {weapon}", True, (220, 200, 150))
        self.screen.blit(weapon_text, (180, 450))

        armor_text = self.small_font.render(f"防具: {armor}", True, (150, 200, 220))
        self.screen.blit(armor_text, (180, 480))

        # 提示
        prompt = self.small_font.render("按 ESC 键返回", True, (180, 200, 200))
        self.screen.blit(prompt, (400 - prompt.get_width() // 2, 550))

    def draw_skills_screen(self):
        self.screen.fill((30, 30, 50))

        # 标题
        title = self.font.render("技能", True, (220, 180, 60))
        self.screen.blit(title, (400 - title.get_width() // 2, 30))

        # 技能列表
        if not self.player.skills:
            empty_text = self.font.render("尚未学会任何技能", True, (180, 180, 200))
            self.screen.blit(empty_text, (400 - empty_text.get_width() // 2, 200))
        else:
            for i, skill in enumerate(self.player.skills):
                skill_text = f"{i + 1}. {skill['name']} - 伤害: {skill['damage_multiplier']}x 消耗MP: {skill['mp_cost']}"
                skill_surf = self.small_font.render(skill_text, True, (180, 220, 200))
                self.screen.blit(skill_surf, (100, 100 + i * 40))

        # 提示
        if self.state_prev == GameState.BATTLE:
            prompt = self.small_font.render("按数字键使用技能，ESC返回战斗", True, (180, 200, 200))
        else:
            prompt = self.small极
            prompt = self.small_font.render("按 ESC 键返回", True, (180, 200, 200))
        self.screen.blit(prompt, (400 - prompt.get_width() // 2, 500))

    def draw_game_over(self):
        self.screen.fill((20, 10, 20))

        title = self.font.render("游戏结束", True, (200, 50, 50))
        self.screen.blit(title, (400 - title.get_width() // 2, 150))

        score = self.small_font.render(f"最终等级: {self.player.level}", True, (200, 150, 150))
        self.screen.blit(score, (400 - score.get_width() // 2, 220))

        prompt = self.font.render("按 R 键重新开始游戏", True, (150, 200, 150))
        # self.screen.blit(prompt, (400 - prompt.get_width() // 2极
        self.screen.blit(prompt, (400 - prompt.get_width() // 2, 300))

    def draw(self):
        if self.state == GameState.MAIN_MENU:
            self.draw_main_menu()
        elif self.state == GameState.PLAYING:
            self.draw_playing_screen()
        # elif self.state == GameState.BATT极
        elif self.state == GameState.BATTLE:
            self.draw_battle_screen()
        elif self.state == GameState.INVENTORY:
            self.draw_inventory()
        elif self.state == GameState.CHARACTER:
            self.draw_character_screen()
        elif self.state == GameState.SKILLS:
            self.draw_skills_screen()
        elif self.state == GameState.GAME_OVER:
            self.draw_game_over()

        pygame.display.flip()

    def run(self):
        while True:
            self.handle_event()
            self.draw()
            self.clock.tick(30)