# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2023/6/16 9:57
# @Author : waxberry
# @File : autoPiano.py
# @Software : PyCharm

import time
import webbrowser

from pynput.keyboard import Key, Controller
from pywinauto import keyboard
from selenium.webdriver.common.keys import Keys



def play_piano(music, keytime):
    for n in music:
        if n.isupper():
            keyboard.press(Key.shift)
            time.sleep(0.001)
            keyboard.press(n.lower())
            time.sleep(keytime - 0.001)
            keyboard.release(n.lower())
            keyboard.release(Key.shift)
        elif n == "|" or n ==")":
            pass
        elif n in "!@$%^*(":
            keyboard.press(Key.shift)
            time.sleep(0.001)
            keyboard.press("1245689"["!@$%^*(".index(n)])
            time.sleep(keytime - 0.001)
            keyboard.release("1245689"["!@$%^*(".index(n)])
            keyboard.release(Key.shift)
        elif n != " " and n != '-':
            keyboard.press(n)
            if music.index(n) != len(music) -1 and music[music.index(n) + 1] == ")":
                time.sleep(keytime / 2)
            else:
                time.sleep(keytime)
            keyboard.release(n)
        elif n == "-":
            time.sleep(2 * keytime)
        else:
            time.sleep(keytime)

right = "s-as f |a --u |p -ops |" \
        "o --uu|i-uis-|u - sss|a-Ii a |" \
        "a --|"
left = "etu --|0wr --|qet --|" \
       "80w --|9qe --|80w --|7Qr --|" \
       "370Wr |"


def thread_play(play_piano, param, right, left):
    thread_play(play_piano, 0.3, right, left)
    right = "---op|s-as f |a --u |p -ops |" \
            "o --uu|i-uis-|u - sss|a-Ii a |" \
            "a --pa|s-as f |a --u |p -ops |"
    left = "----|etu --|0wr --|qet --|" \
           "80w --|9qe --|80w --|7Qr --|" \
           "370Wr u |etu --|0wr --|qet --|"
    thread_play(play_piano, 0.25, right, left)
    right = "o --uu|i sa-s |d fs--|sap a O |" \
            "p --sd|f-df h |d --o |s-as f |" \
            "f --oo|pas asd |s-oo- |d s a p |"
    left = "80w --|9qe --|680 --|9ey 0 -|" \
           "e ---|89w -t |579 --|60e -t |" \
           "370 w -|q -q -|0 ---|9 ---|"
    rightThumb = "----|----|----|--W -|" \
                 "s ---|----|----|----|" \
                 "----|----|----|g f d s |"
    rightIndexFinger = "----|----|----|--r -|" \
                       "u ---|----|----|----|" \
                       "----|e -r -|w ---|e ---|"
    leftThumb = "----|----|----|----|" \
                "----|----|----|----|" \
                "----|t -y -|t ---|t ---|"
    thread_play(play_piano, 0.25, right, left, rightThumb, rightIndexFinger, leftThumb)
    right = "a --f |j -h -|fds -s |d-sd h |" \
            "f --f |j -h -|"
    left = "3 %70Wru|60e 37w |48qer w |59q e t |" \
           "80wty -|60e 37w |"
    rightThumb = "f ---|----|----|----|" \
                 "----|----|"
    rightIndexFinger = "----|----|----|----|" \
                       "----|----|"
    leftThumb = "----|----|----|----|" \
                "----|----|"
    thread_play(play_piano, 0.25, right, left, rightThumb, rightIndexFinger, leftThumb)
    # 右手
    right = "fds -s |d-sd a |u --op|"
    # 左手
    left = "48qer w |7 -7 % |6 ---|"
    # 右拇指
    rightThumb = "----|9 ---|8"
    # 右食指
    rightIndexFinger = "----|q ---|0"
    # 左拇指
    leftThumb = "----|----|p"
    # 多线程模拟手指弹琴，按键时间为0.3s
    thread_play(play_piano, 0.3, right, left, rightThumb, rightIndexFinger, leftThumb)
    right = "s-as f |a --u |p -ops |" \
            "o --uu|i-uis-|u - sss|a-Ii a |" \
            "a --|"
    left = "etu --|0wr --|qet --|" \
           "80w --|9qe --|80w --|7Qr --|" \
           "370Wr |"
    thread_play(play_piano, 0.4, right, left)


if __name__ == '__main__':
    # 准备演奏
    # # 控制键盘
    keyboard = Controller()
    # # 切换到vue键盘钢琴(auto piano)网页
    # keyboard.press(Key.cmd)
    # time.sleep(1)
    # keyboard.press("d")
    # keyboard.release("d")
    # keyboard.release(Key.cmd)
    # # 链接的方式点击桌面任务栏的正在运行程序print_control_identifiers()
    # dlg = Desktop(backend="uia").任务栏.运行中的程序.child_window(title="Google Chrome - 1 个运行窗口", auto_id="Chrome",
    #                                                      control_type="Button").click()
    chromePath = r'D:\Python310\chromedriver.exe'
    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chromePath))
    webbrowser.get('chrome').open('http://www.autopiano.cn', new=1, autoraise=True)