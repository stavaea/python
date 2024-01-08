# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2023/12/28 10:09
# @Author : waxberry
# @File : util.py
# @Software : PyCharm

class Filter:
    def addFilter(self):
        self.addFilter(r'\*(.+?)\*', 'emphasis')
        self.addFilter(r'(http://[\.a-z0-9A-Z/]+)', 'url')
        self.addFilter(r'([\.a-zA-Z]+@[.\a-zA-Z]+[a-zA-Z]+)', 'mail')

def line(file):
    for line in file:
        yield line
    yield '\n'

def blocks(file):
    block = []
    for line in lines(file):
        if line.strip():
            block.append(line)
        elif block:
            yield ''.join(block).strip()
            block = []