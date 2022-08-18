# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2022/8/18 11:40
# @Author : waxberry
# @File : db.py
# @Software : PyCharm

from db import handle_mysql

def checkUser(account):    #通过account查询用户信息
    mysql = handle_mysql.MySQL()
    sql_select_account = "select account, password, nickname from user where account = '%s'" % account
    userInfo = mysql.select(sql_select_account)
    mysql.conn_close()
    return userInfo


def insertUser(account, password, nickname):    #插入用户信息
    mysql = handle_mysql.MySQL()
    sql_insert = "Insert INTO user(account, password, nickname) VALUES ('%s', '%s', '%s')" % (account, password, nickname)
    mysql.insert(sql_insert)
    mysql.conn_close()