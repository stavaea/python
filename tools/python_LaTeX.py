#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2024/5/23 14:25
@Author  : waxberry
@File    : python_LaTeX.py
@Software: PyCharm
"""


import math
import numpy as np
import latexify

@latexify.function
def solve(a, b, c):
  return (-b + math.sqrt(b**2 - 4*a*c)) / (2*a)

print(solve(1, 4, 3))
print(solve)