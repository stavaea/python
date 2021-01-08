#coding:utf-8

import re

def fetchStringByBoundary(data, LB=None, RB=None):
    rule = LB + r'(.*?)' + RB
    slotList = re.findall(rule, data)
    return slotList