#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2024/5/23 14:41
@Author  : waxberry
@File    : 训练数据.py
@Software: PyCharm
"""



# 统计文件夹下的所有图片数量
data_dir = pathlib.Path('dataset')
# 从文件夹下读取图片，生成数据集
train_ds = tf.keras.preprocessing.image_dataset_from_directory(
    data_dir, # 从哪个文件获取数据
    color_mode="grayscale", # 获取数据的颜色为灰度
    image_size=(24, 24), # 图片的大小尺寸
    batch_size=32 # 多少个图片为一个批次
)
# 数据集的分类，对应dataset文件夹下有多少图片分类
class_names = train_ds.class_names
# 保存数据集分类
np.save("class_name.npy", class_names)
# 数据集缓存处理
AUTOTUNE = tf.data.experimental.AUTOTUNE
train_ds = train_ds.cache().shuffle(1000).prefetch(buffer_size=AUTOTUNE)
# 创建模型
model = create_model()
# 训练模型，epochs=10，所有数据集训练10遍
model.fit(train_ds,epochs=10)
# 保存训练后的权重
model.save_weights('checkpoint/char_checkpoint')