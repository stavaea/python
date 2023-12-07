# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2023/12/7 14:19
# @Author : waxberry
# @File : 制作进度条.py
# @Software : PyCharm


# 4 个常用的 Python 进度条库：

# Progress
import timefrom progress.bar
import IncrementalBarmylist = [1,2,3,4,5,6,7,8]
import time
bar = IncrementalBar( Countdown , max = len(mylist))
for item in mylist:
  bar.next()
  time.sleep(1)
  bar.finish()


# tqdm
import timefrom tqdm
import tqdmmylist = [1,2,3,4,5,6,7,8]
for i in tqdm(mylist):
  time.sleep(1)


# Alive Progress
from alive_progress import alive_barimport
timemylist = [1,2,3,4,5,6,7,8]
with alive_bar(len(mylist)) as bar:
  for i in mylist:
    bar()
    time.sleep(1)


# PySimpleGUI
import PySimpleGUI as sgimport
timemylist = [1,2,3,4,5,6,7,8]
for i, item in enumerate(mylist):
  sg.one_line_progress_meter( This is my progress meter! , i+1, len(mylist),  -key- )
  time.sleep(1)

# 如何集成进度条
import PySimpleGUI as sgimport
timemylist = [1,2,3,4,5,6,7,8]
progressbar = [ [sg.ProgressBar(len(mylist), orientation= h , size=(51, 10), key= progressbar )]]
outputwin = [ [sg.Output(size=(78,20))]]
layout = [ [sg.Frame( Progress ,layout= progressbar)], [sg.Frame( Output , layout = outputwin)], [sg.Submit( Start ),sg.Cancel()]]
window = sg.Window( Custom Progress Meter , layout)
progress_bar = window[ progressbar ] while True:
  event, values = window.read(timeout=10)
  if event ==  Cancel  or event is None:
    break
  elif event ==  Start :
    for i,item in enumerate(mylist):
      print(item)
      time.sleep(1)
      progress_bar.UpdateBar(i + 1)window.close()