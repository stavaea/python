# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2022/8/29 10:10
# @Author : waxberry
# @File : day8.py
# @Software : PyCharm

import imageio

image_list = [r'图片路径', r'图片路径']
gif_name = r'gif图路径'
frames = []

for image_name in image_list:
    frames.append(imageio.imread(image_name))

imageio.mimsave(gif_name, frames, 'GIF', duration=2)