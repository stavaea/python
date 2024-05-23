#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2024/5/23 14:44
@Author  : waxberry
@File    : 识别.py
@Software: PyCharm
"""

all_mark_boxs,all_char_imgs,img_o = divImg(path,save)
model = cnn.create_model()
model.load_weights('checkpoint/char_checkpoint')
class_name = np.load('class_name.npy')

# 遍历行
for i in range(0,len(all_char_imgs)):
    row_imgs = all_char_imgs[i]
    # 遍历块
    for j in range(0,len(row_imgs)):
        block_imgs = row_imgs[j]
        block_imgs = np.array(block_imgs)
        results = cnn.predict(model, block_imgs, class_name)
        print('recognize result:',results)