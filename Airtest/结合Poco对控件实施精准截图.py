# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2024/1/12 17:43
# @Author : waxberry
# @File : 结合Poco对控件实施精准截图.py
# @Software : PyCharm



from airtest.core.api import *
from airtest.aircv import *

auto_setup(__file__)

from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

#获取屏幕分辨率
android = device()
xy = android.get_current_resolution()

screen = G.DEVICE.snapshot()

#使用poco去寻找控件
if poco(text='游戏增强器').exists():
    a = poco(text='游戏增强器').get_position()#获取控件的中心坐标
    b = poco(text='游戏增强器').get_size()#获取控件的实际长宽

    # 计算左上角坐标，转化成绝对坐标
    x1 = int((a[0] - 0.5 * b[0]) * xy[0])
    y1 = int((a[1] - 0.5 * b[1]) * xy[1])

    # 计算右下角坐标，转化成绝对坐标
    x2 = int((a[0] - 0.5 * b[0]) * xy[0])
    y2 = int((a[1] - 0.5 * b[1]) * xy[1])

    # 局部截图
    screen = aircv.crop_image(screen, (x1, y1, x2, y2))
    # 保存局部截图到log文件夹中
    try_log_screen(screen)