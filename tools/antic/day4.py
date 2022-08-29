# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2022/8/29 9:54
# @Author : waxberry
# @File : day4.py
# @Software : PyCharm

import cv2
import os

path = input('请输入需要加水印的文件夹路径：')
file_list = os.listdir(path)

for filename in file_list:
    img1 = cv2.imread(path+filename, cv2.IMREAD_COLOR)
    cv2.putText(img1, 'CSDN', (10, 10), 1, 1, (255, 255, 255), 1)
    cv2.imwrite(path+filename, img1)
