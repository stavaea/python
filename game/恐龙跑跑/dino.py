# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2023/7/3 10:51
# @Author : waxberry
# @File : dino.py
# @Software : PyCharm
import sys

import best as best
import pygame

# 初始化
pygame.init()
pygame.mixer.init()
# 设置窗口大小
screen = pygame.display.set_mode((900, 200))
# 设置标题
pygame.display.set_caption('恐龙跳跳')
# 使用系统自带的字体
my_font = pygame.font.SysFont('arial', 20)
score = 0
# 背景色
bg_color = (218, 220, 225)

# 加载正常恐龙
dino_list = []
temp = ''
for i in range(1, 7):
    temp = pygame.image.load(f'dino/dino_run{i}.png')
    dino_list.append(temp)
dino_rect = temp.get_rect()
index = 0

# x 初始值
dino_rect.x = 100
# y 初始值
dino_rect.y = 150
# print(dino_rect)

# 设置y轴上的初始值为0
y_speed = 0
# 起跳初速度
jumpSpeed = -20
# 模拟重力
gravity = 2

# 加载地面
ground = pygame.image.load('dino/ground.png')

# 加载仙人掌
cactus = pygame.image.load('dino/cactus1.png')
cactus_rect = cactus.get_rect()
cactus_rect.x, cactus_rect.y = 900, 140

# 加载重新再来
restart = pygame.image.load('dino/restart.png')
restart_rect = restart.get_rect()
restart_rect.x, restart_rect.y = (900-restart.get_rect().width)/2, (200-restart.get_rect().height)/2+50
# 加载 gameover
gameover =pygame.image.load('dino/gameover.png')
gameover_rect = gameover.get_rect()
gameover_rect.x, gameover_rect.y = (900-gameover_rect().width)/2, (200-gameover_rect().height)/2

# 地面移动速度与距离
ground_speed = 10
ground_move_distance = 0

# 时钟
clock = pygame.time.Clock()

# 重新再来一次
is_restart = False
text_color = (0, 0, 0)

while True:
    # 每秒30次
    clock.tick(30)
    ...

    # 事件侦测
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            if result_flag:
                with open('result.ini', 'w+') as f:
                    f.write(str(best))
            sys.exit()
        # 空格键侦测
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and dino_rect.y == 150:
                y_speed = jumpSpeed

    # 碰撞检测
    if dino_rect.collidedict(cactus_rect):
        while not is_restart:
            # 事件侦测
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    if result_flag:
                        with open("result.ini", "w+") as f:
                            f.write(str(best))
                    sys.exit()
                # 空格键侦测
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        is_restart = True
                        bg_color = (218, 220, 225)
                        ground_speed = 10
            # 设置重新再来图片
            screen.blit(restart, restart_rect)
            screen.blit(gameover, gameover_rect)
            pygame.display.update()

    # 统计距离
    score += ground_speed
    score_surface = my_font.render('Distance:' + str(score), True, text_color)
    # 计算最好成绩
    result_flag = False
    if score >= best:
        best = score
        result_flag = True
    best_result = my_font.render('Best Result:' + str(best), True, text_color)
    # 更换背景色,成绩大于4000
    if score > 4000:
        bg_color = (55, 55, 55)
        ground_speed = 15
        text_color = (255, 255, 255)
    # 更换背景色,成绩大于8000
    if score > 8000:
        bg_color = (220, 20, 60)
        ground_speed = 20
        text_color = (255, 255, 255)
    # 更换背景色,成绩大于12000
    if score > 12000:
        bg_color = (25, 25, 112)
        ground_speed = 25
        text_color = (255, 255, 255)
    # 设置背景色
    screen.fill(bg_color)
    # 设置地面图片1
    screen.blit(ground, (0-ground_move_distance, 180))
    # 设置地面图片2，在右边边界外
    screen.blit(ground, (900 - ground_move_distance, 180))
    # 设置恐龙图片
    screen.blit(dino_list[index % 6], dino_rect)
    # 设置仙人掌图片
    screen.blit(cactus, cactus_rect)
    # 设置分数
    screen.blit(score_surface, (780, 20))
    # 设置最好成绩
    screen.blit(best_result, (20, 20))

    pygame.display.update()

pygame.mixer.music.load('background.mp3')
pygame.mixer.music.play(-1, 0)
sound = pygame.mixer.Sound('preview.mp3')