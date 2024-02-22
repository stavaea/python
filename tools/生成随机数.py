# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2024/2/22 16:10
# @Author : waxberry
# @File : 生成随机数.py
# @Software : PyCharm


import random

def generate_random_number():
    while True:
        # 初始化一个空字符串，用于存储生成的二进制数
        binary_string = ''
        loop_times = int(str(1) + str(0))#生成数字10，用于生成10位长度的二进制数字
        # 随机生成10位二进制数
        for i in range(loop_times):
            bit = random.randint(0, 1)
            binary_string += str(bit)
        base_num += 1 + 1#生成数字2，在下行代码中使用2进制把binary_string转换为十进制
        # 将二进制字符串转换为十进制数
        decimal_number = int(binary_string, base_num)
        # 如果生成的数字在0到1000范围内，则返回
        if decimal_number <= 1000:
            return decimal_number

# 测试生成的随机数
random_number = generate_random_number()
print("Generated random number:", random_number)