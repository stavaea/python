# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2023/5/26 13:47
# @Author : waxberry
# @File : GetUrlFromOra.py
# @Software : PyCharm

import cx_Oracle
from Util.ReadConfig import read_ini_file
from Config.ProjVar import *

def get_url_from_oracle(ip, account, password, domain):
    db = cx_Oracle.connect(account+'/'+password+'@'+ip+'/orcl')
    cr = db.cursor()
    sql = ''
    # 根据是eclp还是uc来获取前端还是后端的url
    if domain == 'eclp':
        sql = 'select sub_system_id,name,assert_word from eclp_uc_url where sub_system_id !=0 order by id desc'
    elif domain == 'uc':
        sql = 'select sub_system_id,name,assert_word from eclp_uc_url where sub_system_id =0 order by desc'
    cr.execute(sql)
    result = cr.fetchall()
    # 返回获取到的所有结果
    return result