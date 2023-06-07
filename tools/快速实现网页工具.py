# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2023/6/2 17:14
# @Author : waxberry
# @File : 快速实现网页工具.py
# @Software : PyCharm

import streamlit as st
import pandas as pd
import numpy as np

# 设置页面标题
st.title("Streamlit 应用示例")

# 添加文本说明
st.write("这是一个使用 Streamlit 构建的简单应用示例。")

# 添加标题
st.header("用户输入")

# 添加输入框，并获取用户输入的文本
user_input = st.text_input("请输入您的姓名")
st.write("您输入的姓名是:", user_input)

# 添加滑动条，并获取用户选择的值
user_age = st.slider("请选择您的年龄", 0, 100, 25)
st.write("您选择的年龄是:", user_age)

# 添加按钮
btn_clicked = st.button("点击这里")
if btn_clicked:
    st.write("按钮被点击了！")

# 添加进度条
progress = st.progress(0)
for i in range(100):
    # 更新进度条的值
    progress.progress(i + 1)

# 添加图表
st.header("数据可视化")

# 创建示例数据
data = pd.DataFrame({
    'x': np.random.randn(100),
    'y': np.random.randn(100)
})

# 绘制折线图
st.subheader("折线图")
st.line_chart(data)