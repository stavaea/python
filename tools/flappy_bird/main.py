# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2025/6/9 9:25
# @Author : waxberry
# @File : main.py
# @Software : PyCharm


import pygame
import random

# 初始化pygame
pygame.init()

# 游戏窗口设置
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Flappy Bird')
clock = pygame.time.Clock()
fps = 60

# 颜色
WHITE = (255, 255, 255)

# 加载资源
try:
    BIRD_IMG = pygame.image.load('assets/bird.PNG').convert_alpha()
    PIPE_IMG = pygame.image.load('assets/pipe.PNG').convert_alpha()
    BG_IMG = pygame.image.load('assets/background.PNG').convert()
    BASE_IMG = pygame.image.load('assets/base.PNG').convert_alpha()
except FileNotFoundError:
    print('资源文件未找到，请确保assets有bird.png, pipe.png, background.png, base.png')
    pygame.quit()
    exit()

try:
    JUMP_SOUND = pygame.mixer.Sound('assets/jump.wav')
    HIT_SOUND = pygame.mixer.Sound('assets/hit.wav')
    POINT_SOUND = pygame.mixer.Sound('assets/point.wav')
except FileNotFoundError:
    print('音效文件未找到')

# 游戏变量
GRAVITY = 0.5
JUMP_HEIGHT = -10
PIPE_GAP = 150
PIPE_SPEED = 3

# 小鸟逻辑
# 创建一个 Bird 类，管理小鸟的位置、速度和绘制：
class Bird:
    def __init__(self):
        self.x = 100
        self.y = SCREEN_HEIGHT // 2
        self.velocity = 0
        self.image = BIRD_IMG
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

    def jump(self): #按空格键或点击时，设置向上的速度
        self.velocity = JUMP_HEIGHT
        JUMP_SOUND.play()

    def update(self): #每帧更新小鸟位置，模拟重力
        self.velocity += GRAVITY
        self.y += self.velocity
        self.rect.y =self.y

    def draw(self, screen): #绘制小鸟到屏幕
        screen.blit(self.image, self.rect)

    # 没有图片，可以用矩形代替：
    # 替代图片pygame.draw.rect(screen, (255,255,0), (self.x, self.y,30,30))

# 管道逻辑
# 创建一个 Pipe 类，管理管道的生成和移动
class Pipe:
    def __init__(self):
        self.x = SCREEN_WIDTH
        self.height = random.randint(150, 400) #管道随机生成高度（150-400 像素），上下管道间距为 PIPE_GAP
        self.speed = False
        self.top_rect = PIPE_IMG.get_rect(bottomleft=(self.x, self.height - PIPE_GAP))
        self.bottom_rect = PIPE_IMG.get_rect(topleft=(self.x, self.height))

    def update(self): #使管道向左移动
        self.x -= PIPE_SPEED
        self.top_rect.x = self.bottom_rect.x = self.x

    def draw(self, screen): #绘制上下管道（上管道翻转图片）
        screen.blit(PIPE_IMG, self.top_rect)
        flipped_pipe = pygame.transform.flip(PIPE_IMG, False, True)
        screen.blit(flipped_pipe, self.bottom_rect)

    # 如果没有管道图片，可用绿色矩形：
    # pygame.draw.rect(screen, (0,255, 0), (self.x,0, 50, self.height - PIPE_GAP))
    # pygame.draw.rect(screen, (0,255, 0), (self.x, self.height,50, SCREEN_HEIGHT - self.height))

# 游戏循环
# 整合小鸟、管道、背景和地面，添加游戏循环：

# 地面类
class Base:
    def __init__(self):
        self.x = 0
        self.y = SCREEN_HEIGHT - 100
        self.image = BASE_IMG
        self.width = self.image.get_width()

    def update(self):
        self.x -= PIPE_SPEED
        if self.x <= -self.width:
            self.x += self.width

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
        screen.blit(self.image, (self.x + self.width, self.y))

    # 如果没有地面图片，可用灰色矩形：
    # pygame.draw.rect(screen, (100,100, 100), (self.x, self.y, self.width,100))

# 主游戏循环
bird = Bird()
pipes = []
base = Base()
score = 0
font = pygame.font.SysFont('Arial', 30)
pipe_timer = 0
running = True

game_state = 'start'
start_text = font.render(game_state, True, WHITE)
game_over_text = font.render('Game Over', True, WHITE)

while running:
    # 事件处理
    for event in pygame.event.get(): #事件处理：响应关闭窗口、空格键或鼠标点击
        if event.type == pygame.QUIT:
            running = False
        if game_state == 'start' and event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            game_state = 'playing'
        if game_state == 'game_over' and event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            bird = Bird()
            pipes = []
            score = 0
            game_state = 'playing'

    if game_state == 'start':
        screen.blit(BG_IMG, (0, 0))
        screen.blit(start_text, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2))
    elif game_state == 'playing':
        while running:
            # 事件处理
          for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_state = 'game_over'
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        bird.jump()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    bird.jump()
    elif game_state == 'game_over':
        screen.blit(BG_IMG, (0, 0))
        screen.blit(game_over_text, (SCREEN_WIDTH // 2 - 80, SCREEN_HEIGHT // 2))
        final_score = font.render(f'score:{score}', True, WHITE)
        screen.blit(final_score, (SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 2 + 50))

    pygame.display.flip()

    # 更新
    bird.update()
    base.update()

    # 生成管道
    pipe_timer += 1  #管道生成：每 1.5 秒（90 帧）生成一对管道，移除超出屏幕的管道
    if pipe_timer >= 90: # 每 1.5 秒生成一对管道
        pipes.append(Pipe())
        pipe_timer = 0

    # 更新管道
    for pipe in pipes[:]:
        pipe.update()
        if pipe.x < -pipe.top_rect.width:
            pipes.remove(pipe)
        if not pipe.passed and pipe.x < bird.x:
            pipes.passed = True
            score += 1
            POINT_SOUND.play()

    # 碰撞检测
    for pipe in pipes: #碰撞检测：检查小鸟与管道或边界的碰撞
        if bird.rect.colliderect(pipe.top_rect) or bird.rect.colliderect(pipe.bottom_rect):
            game_state = 'game_over'
            HIT_SOUND.play()
    if bird.y <= 0 or bird.y >= SCREEN_HEIGHT - 100:
        game_state = 'game_over'
        HIT_SOUND.play()

    # 绘制
    screen.blit(BG_IMG, (0, 0)) #绘制：按顺序绘制背景、管道、地面、小鸟和得分
    for pipe in pipes:
        pipe.draw(screen)
    base.draw(screen)
    bird.draw(screen)

    # 显示得分
    score_text = font.render(str(score), True, WHITE)
    screen.blit(score_text, (SCREEN_WIDTH // 2 , 50))

    pygame.display.flip()
    clock.tick(fps)

pygame.quit()