#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2024/5/23 14:42
@Author  : waxberry
@File    : 投影大法.py
@Software: PyCharm
"""

import numpy as np
import cv2
from PIL import Image, ImageDraw, ImageFont
import PIL
import matplotlib.pyplot as plt
import os
import shutil
from numpy.core.records import array
from numpy.core.shape_base import block
import time

# 要看垂直方向的投影，代码如下：

# 整幅图片的Y轴投影，传入图片数组，图片经过二值化并反色
def img_y_shadow(img_b):
    ### 计算投影 ###
    (h,w)=img_b.shape
    # 初始化一个跟图像高一样长度的数组，用于记录每一行的黑点个数
    a=[0 for z in range(0,h)]
    # 遍历每一列，记录下这一列包含多少有效像素点
    for i in range(0,h):
        for j in range(0,w):
            if img_b[i,j]==255:
                a[i]+=1
    return a


# 展示图片
def img_show_array(a):
    plt.imshow(a)
    plt.show()


# 展示投影图， 输入参数arr是图片的二维数组，direction是x,y轴
def show_shadow(arr, direction='x'):
    a_max = max(arr)
    if direction == 'x':  # x轴方向的投影
        a_shadow = np.zeros((a_max, len(arr)), dtype=int)
        for i in range(0, len(arr)):
            if arr[i] == 0:
                continue
            for j in range(0, arr[i]):
                a_shadow[j][i] = 255
    elif direction == 'y':  # y轴方向的投影
        a_shadow = np.zeros((len(arr), a_max), dtype=int)
        for i in range(0, len(arr)):
            if arr[i] == 0:
                continue
            for j in range(0, arr[i]):
                a_shadow[i][j] = 255

    img_show_array(a_shadow)