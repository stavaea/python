# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2022/6/13 9:30
# @Author : waxberry
# @File : 批量生成图片.py
# @Software : PyCharm

import threading
from PIL import Image

image_size = range(1, 1001)

def start():
    for size in image_size:
        t = threading.Thread(target=create_image, args=(size,))
        t.start()

def create_image(size):
    pri_image = Image.open("origin.png")
    pri_image.resize((size, size), Image.ANTIALIAS).save("img/png_%d.png" % size) #存储路径

if __name__ == '__main__':
    start()


