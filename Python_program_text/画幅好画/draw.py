# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2023/12/28 11:15
# @Author : waxberry
# @File : draw.py
# @Software : PyCharm


from urllib import urlopen
from reportlib.graphics.shapes import *
from reportlib.graphics.charts.lineplots import LinePlot
from reportlib.graphics.charts.textlables import Label
from reportlib.graphics import renderPDF

URL = ' http://www.swpc.noaa.gov/ftpdir/weekly/Predict.txt'
COMMENT_CHARS = '#:'

drawing = Drawing(400, 200)
data = []
for line in urlopen(URL).readlines():
    if not line.isspace() and not line[0] in COMMENT_CHARS:
        data.append([float(n) for n in line.split()])

pred = [row[2] for row in data]
high = [row[3] for row in data]
low = [row[4] for row in data]
times = [row[0] + row[1]/12.0 for row in data]
lp = LinePlot
lp.x = 50
lp.y = 50
lp.height = 125
lp.width = 300
lp.data = [zip(times, pred), zip(times, high), zip(times, low)]
lp.lines[0].storkeColor = colors.blue
lp.lines[1].storkeColor = colors.red
lp.lines[2].storkeColor = colors.green

drawing.add(lp)
drawing.add(String(250, 150, 'Sunsports', fontSize=14, fillColor=colors.red))

renderPDF.drawToFile(drawing, 'report3.pdf', 'Sunsports')