# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2022/8/29 10:07
# @Author : waxberry
# @File : day7.py
# @Software : PyCharm

import qrcode

qr = qrcode.QRCode(
    version=2,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=1
)

qr.add_data('http://www.csdn.net')
img = qr.make_image()
img.save('指定路径')
