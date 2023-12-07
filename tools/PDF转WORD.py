# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2023/12/7 11:17
# @Author : waxberry
# @File : PDF转WORD.py
# @Software : PyCharm


# pip install pdf2docx

from pdf2docx import parse

pdf_file = '/path/to/sample.pdf'
docx_file = 'path/to/sample.docx'

# convert pdf to docx
parse(pdf_file, docx_file)