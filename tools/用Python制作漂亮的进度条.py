# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2024/1/12 17:55
# @Author : waxberry
# @File : 用Python制作漂亮的进度条.py
# @Software : PyCharm


# Progress
# 第一个要介绍的 Python 库是 Progress。
# 你只需要定义迭代的次数、进度条类型并在每次迭代时告知进度条。

import timefrom progress.bar
import IncrementalBarmylist = [1,2,3,4,5,6,7,8]
bar = IncrementalBar( Countdown , max = len(mylist))
for item in mylist:
  bar.next()
  time.sleep(1)
  bar.finish()



# tqdm
# 下面我们看一下 tqdm 库。
# 和之前见过的库差不多，这两行代码也非常相似，在设置方面有一点点不同：

import timefrom tqdm
import tqdmmylist = [1,2,3,4,5,6,7,8]
for i in tqdm(mylist):
  time.sleep(1)



# Alive Progress
# 顾名思义，这个库可以使得进度条变得生动起来，它比原来我们见过的进度条多了一些动画效果。
# 从代码角度来说比较相似：
from alive_progress import alive_barimport
timemylist = [1,2,3,4,5,6,7,8]
with alive_bar(len(mylist)) as bar:
  for i in mylist:
    bar()
    time.sleep(1)



# PySimpleGUI
# 为了实现上述内容，我们需要的代码是：
import PySimpleGUI as sgimport
timemylist = [1,2,3,4,5,6,7,8]
for i, item in enumerate(mylist):
  sg.one_line_progress_meter( This is my progress meter! , i+1, len(mylist),  -key- )
  time.sleep(1)


# PySimpleGUI 应用程序中的进度条项目作者之前曾经在 GitHub 上讨论过「如何快速启动 Python UI，然后使用 UI 创建比较工具」。
# 在这个项目里，作者还讨论了一下如何集成进度条。
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