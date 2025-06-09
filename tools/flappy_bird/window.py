# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2025/6/9 9:27
# @Author : waxberry
# @File : window.py
# @Software : PyCharm


import pygame

pygame.init()
screen = pygame.display.set_mode((400, 600))
pygame.display.set_caption('flappy_bird')
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    pygame.display.flip()

pygame.quit()