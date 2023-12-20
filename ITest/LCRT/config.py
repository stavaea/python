# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2023/12/12 14:27
# @Author : waxberry
# @File : config.py
# @Software : PyCharm

import numpy as np
import time
import pyvisa


GPIB_83630B = 'GPIB0::24::INSTR'
ip_spec = 'TCPIP0::192.168.1.6::INSTR'

rm = pyvisa.ResourceManager()
keysight8360B = rm.open_resource(GPIB_83630B)
N9020A = rm.open_resource(ip_spec)
N9020A.write('*IDN?')
print(N9020A.read())
keysight8360B.write()
print(keysight8360B.read())