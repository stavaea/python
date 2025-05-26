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
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("亲密飞行棋 - 爱欲之旅")

# 颜色定义
COLORS = {
    "white": (255, 255, 255),
    "black": (0, 0, 0),
    "pink": (255, 182, 193),
    "red": (255, 0, 0),
    "purple": (147, 112, 219),
    "gold": (255, 215, 0),
    "light_blue": (173, 216, 230),
}
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

# 加载配置
with open('config.json', 'r', encoding='utf-8') as f:
    CONFIG = json.load(f)


class IntimacyGame:
    def __init__(self):
        self.load_resources()
        self.reset_game()
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

    def load_resources(self):
        # 加载音效
        self.sounds = {}
        for sound in CONFIG['sounds']:
            try:
                self.sounds[sound['name']] = pygame.mixer.Sound(sound['file'])
            except:
                print(f"无法加载音效: {sound['file']}")

        # 加载背景
        self.backgrounds = {}
        for bg in CONFIG['backgrounds']:
            try:
                self.backgrounds[bg['name']] = pygame.image.load(bg['file'])
            except:
                print(f"无法加载背景: {bg['file']}")

        # 加载任务
        self.tasks = CONFIG['tasks']
        self.toys = CONFIG['toys']
        self.roleplays = CONFIG['roleplays']

    def reset_game(self):
        self.players = {
            1: {"name": "", "position": 0, "color": COLORS['red'], "toys": []},
            2: {"name": "", "position": 0, "color": COLORS['pink'], "toys": []}
        }
        self.current_player = 1
        self.intimacy_level = 1
        self.desire_temp = 50
        self.safe_word = CONFIG['settings']['safe_word']
        self.history = []
        self.game_state = "start"
        self.selected_toy = None
        self.background = self.backgrounds.get(CONFIG['settings']['default_background'], None)

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
    def draw_rounded_rect(self, surface, color, rect, radius=10):
        """绘制圆角矩形"""
        x, y, w, h = rect
        pygame.draw.circle(surface, color, (x + radius, y + radius), radius)
        pygame.draw.circle(surface, color, (x + w - radius, y + radius), radius)
        pygame.draw.circle(surface, color, (x + radius, y + h - radius), radius)
        pygame.draw.circle(surface, color, (x + w - radius, y + h - radius), radius)
        pygame.draw.rect(surface, color, (x + radius, y, w - 2 * radius, h))
        pygame.draw.rect(surface, color, (x, y + radius, w, h - 2 * radius))

    def show_dialog(self, title, content, options):
        """显示通用对话框"""
        # 半透明背景
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 180))
        screen.blit(overlay, (0, 0))

        # 主对话框
        dialog_rect = (200, 150, 600, 400)
        self.draw_rounded_rect(screen, COLORS['white'], dialog_rect, 15)

        # 标题
        title_text = pygame.font.SysFont('simhei', 32).render(title, True, COLORS['purple'])
        screen.blit(title_text, (500 - title_text.get_width() // 2, 180))

        # 内容
        y_pos = 230
        for line in content.split('\n'):
            text = pygame.font.SysFont('simhei', 24).render(line, True, COLORS['black'])
            screen.blit(text, (500 - text.get_width() // 2, y_pos))
            y_pos += 35

        # 选项按钮
        option_buttons = []
        x_start = 500 - (len(options) * 120) // 2
        for i, (opt_text, opt_color) in enumerate(options.items()):
            btn_rect = (x_start + i * 140, 450, 120, 50)
            self.draw_rounded_rect(screen, opt_color, btn_rect, 10)
            text = pygame.font.SysFont('simhei', 20).render(opt_text, True, COLORS['black'])
            screen.blit(text, (x_start + i * 140 + 60 - text.get_width() // 2, 465))
            option_buttons.append((opt_text, btn_rect))

        pygame.display.update()

        while True:
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN:
                    mx, my = pygame.mouse.get_pos()
                    for opt, rect in option_buttons:
                        x, y, w, h = rect
                        if x <= mx <= x + w and y <= my <= y + h:
                            return opt
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

    def handle_special_cell(self, cell_type):
        """处理特殊格子事件"""
        task = random.choice(self.tasks[cell_type])
        result = self.show_dialog(
            "亲密任务",
            f"{task['description']}\n\n难度等级: {task['level']}",
            {"接受": COLORS['light_blue'], "拒绝": COLORS['pink']}
        )

        if result == "接受":
            self.play_sound("accept")
            self.desire_temp = min(100, self.desire_temp + task['desire_effect'])
            if random.random() < task.get('toy_drop_chance', 0):
                new_toy = random.choice(self.toys)
                self.players[self.current_player]['toys'].append(new_toy)
                self.show_dialog("获得道具",
                                 f"获得 {new_toy['name']}!\n{new_toy['description']}",
                                 {"确定": COLORS['gold']})
            return True
        else:
            self.play_sound("reject")
            self.desire_temp = max(0, self.desire_temp - 10)
            return False

    def use_toy(self):
        """使用道具界面"""
        toys = self.players[self.current_player]['toys']
        if not toys:
            self.show_dialog("提示", "没有可用道具", {"确定": COLORS['pink']})
            return None

        options = {toy['name']: COLORS['gold'] for toy in toys}
        selected = self.show_dialog("选择道具", "请选择要使用的道具：", options)
        return next((t for t in toys if t['name'] == selected), None)

    def play_sound(self, sound_name):
        """播放音效"""
        if sound_name in self.sounds and CONFIG['settings']['sound_enabled']:
            self.sounds[sound_name].play()

    def game_loop(self):
        clock = pygame.time.Clock()
        while True:
            # 事件处理
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

                # 处理鼠标点击
                if event.type == MOUSEBUTTONDOWN:
                    mx, my = pygame.mouse.get_pos()
                    # 处理开始界面点击

            # 游戏状态处理
            if self.game_state == "playing":
                self.draw_game_screen()
            else:
                self.draw_start_screen()

            pygame.display.update()
            clock.tick(30)


if __name__ == "__main__":
    game = IntimacyGame()
    game.game_loop()