import pygame
import sys
import random
import json
import os
from pygame.locals import *
from datetime import datetime

# 初始化pygame
pygame.init()
pygame.mixer.init()

# 屏幕设置
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 700
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("情侣情感升温飞行棋 - 爱的旅程")

# 颜色定义
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
PINK = (255, 182, 193)
LIGHT_BLUE = (173, 216, 230)
GOLD = (255, 215, 0)
PURPLE = (147, 112, 219)
LIGHT_PINK = (255, 209, 220)

# 字体
font = pygame.font.SysFont('simhei', 24)
title_font = pygame.font.SysFont('simhei', 36)
small_font = pygame.font.SysFont('simhei', 18)

# 尝试加载音效
try:
    dice_sound = pygame.mixer.Sound('dice.wav')
    win_sound = pygame.mixer.Sound('win.wav')
    special_sound = pygame.mixer.Sound('special.wav')
    bg_music = pygame.mixer.Sound('bg_music.mp3')
    bg_music.play(-1)  # 循环播放背景音乐
    has_sound = True
except:
    has_sound = False
    print("音效文件未找到，游戏将以静音模式运行")


class CoupleFlightChess:
    def __init__(self):
        self.player1_name = ""
        self.player2_name = ""
        self.player1_pos = 0
        self.player2_pos = 0
        self.current_player = 1
        self.game_started = False
        self.showing_history = False
        self.customizing = False
        self.history = []
        self.background_image = None
        self.board_color = LIGHT_BLUE
        self.player_colors = {
            1: RED,
            2: PINK
        }

        # 扩展的特殊格子任务
        self.special_cells = {
            5: {"task": "分享你们第一次约会的故事", "effect": "前进2格"},
            10: {"task": "给对方一个拥抱", "effect": "获得额外一次掷骰子机会"},
            15: {"task": "互相夸奖对方三个优点", "effect": "双方各前进1格"},
            20: {"task": "模仿对方的习惯动作", "effect": "让对方后退1格"},
            25: {"task": "分享一件你最感激对方的事", "effect": "前进到下一个特殊格子"},
            30: {"task": "轻轻捏对方的脸颊", "effect": "无效果，纯甜蜜互动"},
            35: {"task": "对视10秒不许笑", "effect": "笑的人后退2格"},
            40: {"task": "胜利终点！", "effect": "游戏结束"}
        }

        # 加载游戏记录
        self.load_history()

    def load_history(self):
        try:
            with open('game_history.json', 'r') as f:
                self.history = json.load(f)
        except:
            self.history = []

    def save_history(self, winner):
        game_record = {
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "player1": self.player1_name,
            "player2": self.player2_name,
            "winner": winner,
            "special_interactions": []
        }

        # 记录所有触发的特殊互动
        for cell in sorted(self.special_cells.keys()):
            if cell <= max(self.player1_pos, self.player2_pos):
                game_record["special_interactions"].append({
                    "cell": cell,
                    "task": self.special_cells[cell]["task"]
                })

        self.history.append(game_record)

        # 只保留最近10条记录
        if len(self.history) > 10:
            self.history = self.history[-10:]

        with open('game_history.json', 'w') as f:
            json.dump(self.history, f, indent=2)

    def draw_start_screen(self):
        # 绘制背景
        if self.background_image:
            screen.blit(self.background_image, (0, 0))
        else:
            screen.fill(PINK)

        # 绘制半透明遮罩
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        overlay.fill((255, 255, 255, 180))
        screen.blit(overlay, (0, 0))

        # 游戏标题
        title = title_font.render("情侣情感升温飞行棋", True, PURPLE)
        subtitle = font.render("爱的旅程", True, PURPLE)
        screen.blit(title, (SCREEN_WIDTH // 2 - title.get_width() // 2, 80))
        screen.blit(subtitle, (SCREEN_WIDTH // 2 - subtitle.get_width() // 2, 130))

        # 绘制输入框
        pygame.draw.rect(screen, WHITE, (300, 200, 300, 40), 2)
        pygame.draw.rect(screen, WHITE, (300, 280, 300, 40), 2)

        # 绘制标签
        label1 = font.render("玩家1名字:", True, PURPLE)
        label2 = font.render("玩家2名字:", True, PURPLE)
        screen.blit(label1, (200, 210))
        screen.blit(label2, (200, 290))

        # 显示输入的文字
        name1 = font.render(self.player1_name, True, BLACK)
        name2 = font.render(self.player2_name, True, BLACK)
        screen.blit(name1, (310, 210))
        screen.blit(name2, (310, 290))

        # 开始按钮
        pygame.draw.rect(screen, LIGHT_BLUE, (350, 350, 200, 50), border_radius=10)
        start_text = font.render("开始游戏", True, BLACK)
        screen.blit(start_text, (450 - start_text.get_width() // 2, 365))

        # 历史记录按钮
        pygame.draw.rect(screen, LIGHT_PINK, (350, 420, 200, 50), border_radius=10)
        history_text = font.render("历史记录", True, BLACK)
        screen.blit(history_text, (450 - history_text.get_width() // 2, 435))

        # 自定义按钮
        pygame.draw.rect(screen, GOLD, (350, 490, 200, 50), border_radius=10)
        custom_text = font.render("自定义设置", True, BLACK)
        screen.blit(custom_text, (450 - custom_text.get_width() // 2, 505))

        # 音效提示
        if has_sound:
            sound_text = small_font.render("音效: 开启", True, PURPLE)
        else:
            sound_text = small_font.render("音效: 关闭", True, PURPLE)
        screen.blit(sound_text, (50, 650))

    def draw_game_board(self):
        # 绘制背景
        if self.background_image:
            screen.blit(self.background_image, (0, 0))
        else:
            screen.fill(self.board_color)

        # 绘制棋盘
        board_width = 700
        board_height = 500
        board_x = (SCREEN_WIDTH - board_width) // 2
        board_y = (SCREEN_HEIGHT - board_height) // 2 - 30

        pygame.draw.rect(screen, WHITE, (board_x, board_y, board_width, board_height), border_radius=10)

        # 绘制格子
        cell_size = 60
        for i in range(1, 41):
            row = (i - 1) // 10
            col = (i - 1) % 10

            if row % 2 == 0:
                x = board_x + col * cell_size + 20
            else:
                x = board_x + (9 - col) * cell_size + 20

            y = board_y + row * (board_height // 4) + 20

            pygame.draw.rect(screen, BLACK, (x, y, cell_size, cell_size), 1)

            # 标记特殊格子
            if i in self.special_cells:
                pygame.draw.circle(screen, GOLD, (x + cell_size // 2, y + cell_size // 2), 15)

            # 显示格子编号
            cell_text = font.render(str(i), True, BLACK)
            screen.blit(cell_text, (x + 5, y + 5))

            # 绘制玩家位置
            if i == self.player1_pos:
                pygame.draw.circle(screen, self.player_colors[1], (x + cell_size // 2, y + cell_size // 2 - 15), 10)
            if i == self.player2_pos:
                pygame.draw.circle(screen, self.player_colors[2], (x + cell_size // 2, y + cell_size // 2 + 15), 10)

        # 显示当前玩家信息
        current_player_text = font.render(
            f"当前回合: {self.player1_name if self.current_player == 1 else self.player2_name}", True, BLACK)
        screen.blit(current_player_text, (50, 50))

        # 显示玩家位置信息
        player1_info = font.render(f"{self.player1_name}: 第 {self.player1_pos} 格", True, self.player_colors[1])
        player2_info = font.render(f"{self.player2_name}: 第 {self.player2_pos} 格", True, self.player_colors[2])
        screen.blit(player1_info, (50, 100))
        screen.blit(player2_info, (50, 130))

        # 掷骰子按钮
        pygame.draw.rect(screen, PINK, (350, 600, 200, 50), border_radius=10)
        dice_text = font.render("掷骰子", True, BLACK)
        screen.blit(dice_text, (450 - dice_text.get_width() // 2, 615))

        # 返回按钮
        pygame.draw.rect(screen, LIGHT_BLUE, (50, 600, 100, 40), border_radius=5)
        back_text = font.render("返回", True, BLACK)
        screen.blit(back_text, (100 - back_text.get_width() // 2, 615))

    def draw_history_screen(self):
        # 绘制背景
        screen.fill(LIGHT_PINK)

        # 标题
        title = title_font.render("游戏历史记录", True, PURPLE)
        screen.blit(title, (SCREEN_WIDTH // 2 - title.get_width() // 2, 50))

        # 显示历史记录
        if not self.history:
            no_history = font.render("暂无游戏记录", True, BLACK)
            screen.blit(no_history, (SCREEN_WIDTH // 2 - no_history.get_width() // 2, 150))
        else:
            for i, record in enumerate(reversed(self.history)):
                date_text = font.render(record["date"], True, BLACK)
                winner_text = font.render(f"获胜者: {record[record['winner']]}", True, GOLD)
                players_text = small_font.render(f"{record['player1']} vs {record['player2']}", True, BLACK)

                screen.blit(date_text, (100, 120 + i * 100))
                screen.blit(winner_text, (100, 150 + i * 100))
                screen.blit(players_text, (100, 180 + i * 100))

                # 显示互动数量
                interactions = small_font.render(f"甜蜜互动: {len(record['special_interactions'])}次", True, PURPLE)
                screen.blit(interactions, (500, 150 + i * 100))

                # 返回按钮
                pygame.draw.rect(screen, LIGHT_BLUE, (350, 600, 200, 50), border_radius=10)
                back_text = font.render("返回主菜单", True, BLACK)
                screen.blit(back_text, (450 - back_text.get_width() // 2, 615))

    def draw_customize_screen(self):
        # 绘制背景
        screen.fill(LIGHT_BLUE)

        # 标题
        title = title_font.render("自定义设置", True, PURPLE)
        screen.blit(title, (SCREEN_WIDTH // 2 - title.get_width() // 2, 50))

        # 背景颜色选择
        color_text = font.render("选择棋盘背景颜色:", True, BLACK)
        screen.blit(color_text, (100, 120))

        colors = [LIGHT_BLUE, LIGHT_PINK, WHITE, (200, 230, 200), (230, 200, 230)]
        color_names = ["浅蓝", "粉红", "白色", "薄荷绿", "淡紫色"]

        for i, (color, name) in enumerate(zip(colors, color_names)):
            pygame.draw.rect(screen, color, (100 + i * 120, 160, 100, 50))
            name_text = small_font.render(name, True, BLACK)
            screen.blit(name_text, (100 + i * 120 + 50 - name_text.get_width() // 2, 220))

        # 玩家颜色选择
        player1_text = font.render(f"{self.player1_name}颜色:", True, BLACK)
        player2_text = font.render(f"{self.player2_name}颜色:", True, BLACK)
        screen.blit(player1_text, (100, 270))
        screen.blit(player2_text, (100, 340))

        player_colors = [RED, PINK, PURPLE, GOLD, (0, 128, 0), (0, 0, 128)]
        color_names = ["红色", "粉色", "紫色", "金色", "绿色", "蓝色"]

        for i, (color, name) in enumerate(zip(player_colors, color_names)):
            # 玩家1颜色选项
            pygame.draw.rect(screen, color, (100 + i * 100, 300, 80, 30))

            # 玩家2颜色选项
            pygame.draw.rect(screen, color, (100 + i * 100, 370, 80, 30))

            # 显示颜色名称
            name_text = small_font.render(name, True, BLACK)
            screen.blit(name_text, (100 + i * 100 + 40 - name_text.get_width() // 2, 335))
            screen.blit(name_text, (100 + i * 100 + 40 - name_text.get_width() // 2, 405))

        # 返回按钮
        pygame.draw.rect(screen, PINK, (350, 600, 200, 50), border_radius=10)
        back_text = font.render("保存并返回", True, BLACK)
        screen.blit(back_text, (450 - back_text.get_width() // 2, 615))

    def roll_dice(self):
        if has_sound:
            dice_sound.play()
        return random.randint(1, 6)

    def apply_special_effect(self, cell, player):
        effect = self.special_cells[cell]["effect"]

        if "前进" in effect:
            if "2格" in effect:
                if player == 1:
                    self.player1_pos += 2
                else:
                    self.player2_pos += 2
            elif "下一个特殊格子" in effect:
                next_special = min([c for c in self.special_cells.keys() if
                                    c > (self.player1_pos if player == 1 else self.player2_pos)])
                if player == 1:
                    self.player1_pos = next_special
                else:
                    self.player2_pos = next_special
        elif "后退" in effect:
            if player == 1:
                self.player2_pos = max(0, self.player2_pos - 1)
            else:
                self.player1_pos = max(0, self.player1_pos - 1)
        elif "额外一次" in effect:
            self.current_player = player  # 保持当前玩家不变

    def show_special_task(self, cell, player):
        task_info = self.special_cells.get(cell, {})
        if not task_info:
            return

        if has_sound:
            special_sound.play()

        # 创建一个半透明覆盖层
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 180))
        screen.blit(overlay, (0, 0))

        # 显示任务框
        pygame.draw.rect(screen, WHITE, (150, 200, 600, 250), border_radius=10)

        # 显示标题
        title = title_font.render("甜蜜互动任务", True, PURPLE)
        screen.blit(title, (450 - title.get_width() // 2, 220))

        # 显示当前玩家
        player_text = font.render(f"玩家: {self.player1_name if player == 1 else self.player2_name}", True, BLACK)
        screen.blit(player_text, (450 - player_text.get_width() // 2, 270))

        # 显示任务内容
        task_text = font.render(task_info["task"], True, BLACK)
        screen.blit(task_text, (450 - task_text.get_width() // 2, 320))

        # 显示效果
        effect_text = font.render(f"效果: {task_info['effect']}", True, GOLD)
        screen.blit(effect_text, (450 - effect_text.get_width() // 2, 370))

        # 确定按钮
        pygame.draw.rect(screen, LIGHT_BLUE, (350, 450, 200, 50), border_radius=10)
        ok_text = font.render("完成任务", True, BLACK)
        screen.blit(ok_text, (450 - ok_text.get_width() // 2, 465))

        pygame.display.update()

        # 等待用户点击确定
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if 350 <= mouse_pos[0] <= 550 and 450 <= mouse_pos[1] <= 500:
                        waiting = False
                        self.apply_special_effect(cell, player)

    def check_winner(self):
        if self.player1_pos >= 40:
            return 1
        if self.player2_pos >= 40:
            return 2
        return 0

    def show_winner(self, winner):
        if has_sound:
            win_sound.play()

        # 保存游戏记录
        self.save_history("player1" if winner == 1 else "player2")

        # 创建一个半透明覆盖层
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 180))
        screen.blit(overlay, (0, 0))

        # 显示获胜信息
        pygame.draw.rect(screen, WHITE, (200, 200, 500, 300), border_radius=10)

        winner_name = self.player1_name if winner == 1 else self.player2_name
        congrats_text = title_font.render(f"恭喜 {winner_name} 获胜!", True, GOLD)
        screen.blit(congrats_text, (450 - congrats_text.get_width() // 2, 250))

        # 统计互动次数
        interactions = 0
        for cell in sorted(self.special_cells.keys()):
            if cell <= max(self.player1_pos, self.player2_pos):
                interactions += 1

        stats_text = font.render(f"本次游戏共完成 {interactions} 次甜蜜互动", True, BLACK)
        screen.blit(stats_text, (450 - stats_text.get_width() // 2, 320))

        message_text = font.render("爱的旅程永无止境，继续创造美好回忆吧!", True, PURPLE)
        screen.blit(message_text, (450 - message_text.get_width() // 2, 370))

        # 返回按钮
        pygame.draw.rect(screen, PINK, (350, 450, 200, 50), border_radius=10)
        back_text = font.render("返回主菜单", True, BLACK)
        screen.blit(back_text, (450 - back_text.get_width() // 2, 465))

        pygame.display.update()

        # 等待用户点击返回
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if 350 <= mouse_pos[0] <= 550 and 450 <= mouse_pos[1] <= 500:
                        waiting = False
                        self.__init__()  # 重置游戏


def main():
    game = CoupleFlightChess()
    input_active = 0  # 0无输入，1玩家1输入，2玩家2输入
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if not game.game_started and not game.showing_history and not game.customizing:
                if event.type == MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    # 检查是否点击了开始按钮
                    if 350 <= mouse_pos[0] <= 550 and 350 <= mouse_pos[1] <= 400:
                        if game.player1_name and game.player2_name:
                            game.game_started = True
                    # 检查是否点击了历史记录按钮
                    elif 350 <= mouse_pos[0] <= 550 and 420 <= mouse_pos[1] <= 470:
                        game.showing_history = True
                    # 检查是否点击了自定义按钮
                    elif 350 <= mouse_pos[0] <= 550 and 490 <= mouse_pos[1] <= 540:
                        if game.player1_name and game.player2_name:
                            game.customizing = True
                    # 检查是否点击了输入框
                    elif 300 <= mouse_pos[0] <= 600 and 200 <= mouse_pos[1] <= 240:
                        input_active = 1
                    elif 300 <= mouse_pos[0] <= 600 and 280 <= mouse_pos[1] <= 320:
                        input_active = 2
                    else:
                        input_active = 0

                if event.type == KEYDOWN and input_active > 0:
                    if input_active == 1:
                        if event.key == K_BACKSPACE:
                            game.player1_name = game.player1_name[:-1]
                        elif len(game.player1_name) < 10:
                            game.player1_name += event.unicode
                    elif input_active == 2:
                        if event.key == K_BACKSPACE:
                            game.player2_name = game.player2_name[:-1]
                        elif len(game.player2_name) < 10:
                            game.player2_name += event.unicode

            elif game.showing_history:
                if event.type == MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    # 检查是否点击了返回按钮
                    if 350 <= mouse_pos[0] <= 550 and 600 <= mouse_pos[1] <= 650:
                        game.showing_history = False

            elif game.customizing:
                if event.type == MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    # 检查是否点击了返回按钮
                    if 350 <= mouse_pos[0] <= 550 and 600 <= mouse_pos[1] <= 650:
                        game.customizing = False

                    # 检查背景颜色选择
                    colors = [LIGHT_BLUE, LIGHT_PINK, WHITE, (200, 230, 200), (230, 200, 230)]
                    for i in range(len(colors)):
                        if 100 + i * 120 <= mouse_pos[0] <= 200 + i * 120 and 160 <= mouse_pos[1] <= 210:
                            game.board_color = colors[i]

                    # 检查玩家1颜色选择
                    player_colors = [RED, PINK, PURPLE, GOLD, (0, 128, 0), (0, 0, 128)]
                    for i in range(len(player_colors)):
                        if 100 + i * 100 <= mouse_pos[0] <= 180 + i * 100 and 300 <= mouse_pos[1] <= 330:
                            game.player_colors[1] = player_colors[i]

                    # 检查玩家2颜色选择
                    for i in range(len(player_colors)):
                        if 100 + i * 100 <= mouse_pos[0] <= 180 + i * 100 and 370 <= mouse_pos[1] <= 400:
                            game.player_colors[2] = player_colors[i]

            elif game.game_started:
                if event.type == MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    # 检查是否点击了掷骰子按钮
                    if 350 <= mouse_pos[0] <= 550 and 600 <= mouse_pos[1] <= 650:
                        dice = game.roll_dice()
                        if game.current_player == 1:
                            game.player1_pos += dice
                            # 检查特殊格子
                            if game.player1_pos in game.special_cells:
                                game.show_special_task(game.player1_pos, 1)
                            # 检查是否获胜
                            winner = game.check_winner()
                            if winner:
                                game.show_winner(winner)
                            else:
                                game.current_player = 2
                        else:
                            game.player2_pos += dice
                            # 检查特殊格子
                            if game.player2_pos in game.special_cells:
                                game.show_special_task(game.player2_pos, 2)
                            # 检查是否获胜
                            winner = game.check_winner()
                            if winner:
                                game.show_winner(winner)
                            else:
                                game.current_player = 1
                    # 检查是否点击了返回按钮
                    elif 50 <= mouse_pos[0] <= 150 and 600 <= mouse_pos[1] <= 640:
                        game.__init__()  # 重置游戏

        # 绘制当前屏幕
        if game.showing_history:
            game.draw_history_screen()
        elif game.customizing:
            game.draw_customize_screen()
        elif not game.game_started:
            game.draw_start_screen()
        else:
            game.draw_game_board()

        pygame.display.update()
        clock.tick(30)


if __name__ == "__main__":
    main()