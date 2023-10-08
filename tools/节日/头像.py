# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2023/9/28 13:49
# @Author : waxberry
# @File : 头像.py
# @Software : PyCharm


import cv2
# 读取头像和国旗图案
img_head = cv2.imread('head.jpg')
img_flag = cv2.imread('flag.png')
# 获取头像和国旗图案宽度
w_head, h_head = img_head.shape[:2]
w_flag, h_flag = img_flag.shape[:2]
# 计算图案缩放比例
scale = w_head / w_flag / 4
# 缩放图案
img_flag = cv2.resize(img_flag, (0, 0), fx=scale, fy=scale)
# 获取缩放后新宽度
w_flag, h_flag = img_flag.shape[:2]
# 按3个通道合并图片
for c in range(0, 3):
    img_head[w_head - w_flag:, h_head - h_flag:, c] = img_flag[:, :, c]
# 保存最终结果
cv2.imwrite('new_head.jpg', img_head)









# 国庆头像
from PIL import Image

# 加载图片
flag = Image.open('国旗1024.png')
avatar = Image.open('avatar.jpg')
# 将国旗尺寸调整为头像大小
flag.resize(avatar.size)
# 遍历国旗头像的每个像素点,修改透明度
for i in range(flag.size[0]):
    for j in range(flag.size[1]):
        r, g, b, _ = flag.getpixel((i, j))
        # 透明度值
        alpha = max(0, 255 - i // 5 - j // 7)
        # 重新填充像素
        flag.putpixel((i, j), (r, g, b, alpha))
# 将国旗头像粘贴到头像上面
avatar.paste(flag, (0, 0), flag)
# 保存为新图
avatar.save('flag_avatar.png')