#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2024/5/23 14:35
@Author  : waxberry
@File    : 构建模型.py
@Software: PyCharm
"""

import tensorflow as tf
import numpy as np
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential
import pathlib
import cv2

# 构建模型
def create_model():
    model = Sequential([
        layers.experimental.preprocessing.Rescaling(scale=1./255, input_shape=(24, 24, 3)),
        layers.Conv2D(24, 3, activation='relu'),
        layers.MaxPooling2D((2, 2)),
        layers.Conv2D(64, 3, activation='relu'),
        layers.MaxPooling2D((2, 2)),
        layers.Flatten(),
        layers.Dense(128, activation='relu'),
        layers.Dense(15)]
    )

    model.compile(optimizer='adam',
                  loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
                  metrics=['accuracy'])

    return model