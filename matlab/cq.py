# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2024/2/23 14:44
# @Author : waxberry
# @File : cq.py
# @Software : PyCharm


# 指定要读取的文件路径
source_file_path = 'D:\work\脚本\\acceptance_test\E_2G\program\data\\testg.m'
# 指定要保存的新文件路径
destination_file_path = 'D:\Python\python\matlab\单模块入库测试\E_2G\\testg.m'

try:
    # 打开源文件以读取内容
    with open(source_file_path, 'r', encoding='gbk') as source_file:
        # 读取文件内容
        content = source_file.read()

        # 打开目标文件以写入内容
    with open(destination_file_path, 'w') as destination_file:
        # 将内容写入目标文件
        destination_file.write(content)

    print(f"文件内容已成功从 '{source_file_path}' 提取并保存到 '{destination_file_path}'。")

except FileNotFoundError:
    print(f"文件 '{source_file_path}' 未找到，请检查文件路径是否正确。")
except IOError as e:
    print(f"发生I/O错误: {e}")