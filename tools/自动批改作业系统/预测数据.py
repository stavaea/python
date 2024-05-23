#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2024/5/23 14:41
@Author  : waxberry
@File    : 预测数据.py
@Software: PyCharm
"""


# 设置待识别的图片
img1=cv2.imread('img1.png',0)
img2=cv2.imread('img2.png',0)
imgs = np.array([img1,img2])
# 构建模型
model = create_model()
# 加载前期训练好的权重
model.load_weights('checkpoint/char_checkpoint')
# 读出图片分类
class_name = np.load('class_name.npy')
# 预测图片，获取预测值
predicts = model.predict(imgs)
results = [] # 保存结果的数组
for predict in predicts: #遍历每一个预测结果
    index = np.argmax(predict) # 寻找最大值
    result = class_name[index] # 取出字符
    results.append(result)
print(results)