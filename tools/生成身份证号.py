# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2023/5/24 11:56
# @Author : waxberry
# @File : 生成身份证号.py
# @Software : PyCharm

import datetime
import random

def get_validate_checkout(id17):
    '''获得校验码算法'''
    '''十七位数字本体码权重'''
    weight = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
    '''mod11，对应校验码字符值'''
    validate = ['1', '0', 'X', '9', '8', '7', '5', '4', '3', '2']
    sum = 0
    for i in range(0, len(id17)):
        sum = sum + int(id17[i]*weight[i])
    mode = sum % 11
    return validate[mode]

def get_random_idnumber():
    '''产生随机可用身份证号，sex=1表示男性，sex=0表示女性'''
    '''地址码产生'''

    id_number = '110108'
    '''生日起止日期'''
    start, end = '1960-01-01', '2002-12-31'
    days = (datetime.datetime.strptime(end, '%Y-%m-%d') - datetime.datetime.strptime(start, '%Y-%m-%d')).days + 1
    birth_days = datetime.datetime.strptime(datetime.datetime.strptime(start, '%Y-%m-%d') + datetime.timedelta(random.randint(0, days)), '%Y-%m-%d')

    id_number = id_number + str(birth_days)
    '''顺序码'''
    for i in range(2):
        '''最后一个值可以包括'''
        n = random.randint(0, 9)
        id_number = id_number + str(n)

    '''性别码'''
    sex_id = random.randint(1, 2)
    id_number = id_number + str(sex_id)
    '''校验码'''
    check_out = get_validate_checkout(id_number)
    id_number = id_number + str(check_out)
    return id_number