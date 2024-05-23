#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2024/5/23 14:43
@Author  : waxberry
@File    : 根据投影找区域.py
@Software: PyCharm
"""


# 图片获取文字块，传入投影列表，返回标记的数组区域坐标[[左，上，右，下]]
def img2rows(a, w, h):
    ### 根据投影切分图块 ###
    inLine = False  # 是否已经开始切分
    start = 0  # 某次切分的起始索引
    mark_boxs = []
    for i in range(0, len(a)):
        if inLine == False and a[i] > 10:
            inLine = True
            start = i
        # 记录这次选中的区域[左，上，右，下]，上下就是图片，左右是start到当前
        elif i - start > 5 and a[i] < 10 and inLine:
            inLine = False
            if i - start > 10:
                top = max(start - 1, 0)
                bottom = min(h, i + 1)
                box = [0, top, w, bottom]
                mark_boxs.append(box)

    return mark_boxs