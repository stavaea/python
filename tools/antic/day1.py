# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2022/8/29 9:08
# @Author : waxberry
# @File : day1.py
# @Software : PyCharm

def get_str():
    f = open(path, encoding='utf-8')
    data = f.read()
    f.close()
    return data

import re
def get_phone_number(str):
    res = re.findall(r'(13\d{9}|14[5|7]\d{8}|15\d{9}|166{\d{8}|17[3|6|7]{\d{8}|18\d{9})', str)
    return res


def save_res(res, save_path):
    save_file = open(save_path, 'w')
    for phone in res:
        save_file.write(phone)
        save_file.write('\n')
    save_file.write('\n号码共计:' + str(len(res)))
    save_file.close()
    print ('号码读取ok，号码共计：' + str(len(res)))

path = input('请输入文件路径：')
save_path = input('请输入文件保存路径：')
# read_str = get_str(path)
res = get_phone_number(get_str(path))
save_res(res, save_path)