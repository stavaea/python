# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2024/1/8 17:55
# @Author : waxberry
# @File : objects.py
# @Software : PyCharm



import pygame, os
from python.Python_program_text.DIY街机游戏.config import *
from random import randrange

class SquishSprite(pygame.sprite.Sprite):
    def __init__(self, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image).convert()
        self.rect = self.image.get_rect()
        screen = pygame.display.get_surface()
        shrink = -config.margin * 2
        self.area = screen.get_rect().inflate(shrink, shrink)

class Weight(SquishSprite):
    def __init__(self, speed):
        SquishSprite.__init__(self, config.weight_image)
        self.speed = speed
        self.reset()
    def reset(self):
        x =randrange(self.area.left, self.area.right)
        self.rect.midbottom = x, 0
    def update(self):
        self.rect.top += self.speed
        self.landed = self.rect.top >= self.area.bottom

class Banana(SquishSprite):
    def __init__(self):
        SquishSprite.__init__(self, config.banana_image)
        self.rect.bottom = self.area.bottom
        self.pad_top = config.banana_pad_top
        self.pad_size = config.banan_pad_size
    def update(self):
        self.rect.centerx = pygame.mouse.get_pos()[0]
        self.rect = self.rect.clamp(self.area)
    def touches(self, other):
        bounds = self.rect.inflate(-self.pad_size, -self.pad_top)
        bounds.bottom = self.rect.bottom
        return bounds.colliderect(other.rect)