# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2024/1/8 14:58
# @Author : waxberry
# @File : db.py
# @Software : PyCharm



CREATE TABLE message(
    id INT NOT NULL AUTO_INCREMENT,
    subject VARCHAR(100) NOT NULL,
    reply_to INT,
    text MEDIUMTEXT NOT NULL,
    PRIMARY KEY(id)
)