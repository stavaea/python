# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2023/4/12 9:23
# @Author : waxberry
# @File : DBtest.py
# @Software : PyCharm

import unittest
from sqlalchermy import create_engine
from sqlalchermy.engine import reflection

class TestMysqlEngine(unittest.Test):
    def setUp(self):
        # 创建链接
        self.engine = create_engine('mysql+pymysql://root:12345678@127.0.0.1:3306/mysql')
        # 创建inspector对象
        self.insp = reflection.Inspector.from_engine(self.engine)

    def test_table_name(self):
        # 判断user表是否在mysql这个实例库中
        self.assertIn('user', self.insp.get_table_name())

    def test_column(self):
        # user表中是否有user字段
        User = None
        columns = self.insp.get_columns('user')
        for col in columns:
            if 'User' == col['name']:
                User = col['name']
        self.assertIsNotNone(User)

    def test_keyprimary(self):
        # 验证user表中user字段是否为主键
        k = self.insp.get_pk_constraint('user')
        self.assertIn('User', k['constrained_columns'])

if __name__ == '__main__':
    unittest.main()