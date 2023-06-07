# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2023/6/2 16:57
# @Author : waxberry
# @File : AudioAnalyzer.py
# @Software : PyCharm


import pygame
import sys
pygame.init()

display = pygame.display.set_mode((300, 300))
display.fill((255, 255, 255))

pygame.draw.polygon(display, (0, 0, 255),
                    [(120, 120), (40, 160), (40, 220),
                     (200, 220), (200, 160)], width=0)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()



pygame.mixer.music.load(filename)
pygame.mixer.music.play(0)

running = True
while running:
    avg_bass = 0
    poly = []

    # ticks
    t = pygame.time.get_ticks()
    deltaTime = (t - getTicksLastFrame) / 1000.0
    getTicksLastFrame = t