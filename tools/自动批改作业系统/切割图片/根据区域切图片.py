#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2024/5/23 14:43
@Author  : waxberry
@File    : 根据区域切图片.py
@Software: PyCharm
"""

# 裁剪图片,img 图片数组， mark_boxs 区域标记
def cut_img(img, mark_boxs):

    img_items = [] # 存放裁剪好的图片
    for i in range(0,len(mark_boxs)):
        img_org = img.copy()
        box = mark_boxs[i]
        # 裁剪图片
        img_item = img_org[box[1]:box[3], box[0]:box[2]]
        img_items.append(img_item)
    return img_items


# 保存图片
def save_imgs(dir_name, imgs):
    if os.path.exists(dir_name):
        shutil.rmtree(dir_name)
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)

    img_paths = []
    for i in range(0, len(imgs)):
        file_path = dir_name + '/part_' + str(i) + '.jpg'
        cv2.imwrite(file_path, imgs[i])
        img_paths.append(file_path)

    return img_paths


# 切图并保存
row_imgs = cut_img(img, row_mark_boxs)
imgs = save_imgs('rows', row_imgs)  # 如果要保存切图
print(imgs)