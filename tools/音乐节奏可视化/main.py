# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2023/6/2 17:06
# @Author : waxberry
# @File : main.py
# @Software : PyCharm
from networkx import radius

from tools.音乐节奏可视化.AudioAnalyzer import *
import random
import colorsys

# 想要将你的音乐用这份代码进行可视化，仅需要修改main.py的第5行代码
filename = 'mp3存放路径'

# 优化生成的动态图像的颜色，可以修改rnd_color函数，该函数控制图形颜色的变化：
def rnd_color():
    h, s, l = random.random(), 0.5 + random.random() / 2.0, 0.4 + random.random() / 5.0
    return [int(256 * i) for i in colorsys.hls_to_rgb(h, l, s)]

# 修改生成的动态图像的形状，比如说去掉中间那个圆，仅需要这么改
pygame.draw.circle(screen, circle_color, (circleX, circleY), int(radius))
# 将radius直接设为0，或者直接将这行代码注释掉即可
pygame.draw.circle(screen, circle_color, (circleX, circleY), 0)