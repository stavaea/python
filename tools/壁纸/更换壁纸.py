# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2023/12/7 14:16
# @Author : waxberry
# @File : 更换壁纸.py
# @Software : PyCharm

import os
import time

def windows_img(paper_path):
    k = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER,"Control panel\\Desktop", 0, win32con.KEY_SET_VALUE) # 在注册表中写入属性值
    win32api.RegSetValueEx(k, "wapaperStyle", 0, win32con.REG_SZ,"2")  # 0 代表桌面居中 2 代表拉伸桌面
    win32api.RegSetValueEx(k, "Tilewallpaper", 0, win32con.REG_SZ,"0")
    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, paper_path, win32con.SPIF_SENDWININICHANGE) # 刷新桌面

# 然后就是从已经下载的壁纸当中选择图片
def change_wallpaper():
    pic_list = os.listdir("wallpaper")  # 得到文件路径下的图片，列表类型
    i=0
    print(pic_list)
    while True:
        pic = "wallpaper"+'\{}'.format(pic_list[i])
        abspath_pic = os.path.abspath(pic)
        windows_img(abspath_pic)
        print(abspath_pic)
        time.sleep(1000)  # 设置壁纸更换间隔
        i += 1
        if i==len(pic_list):  # 如果是最后一张图片，则重新到第一张
            i=0

if __name__ == '__main__':
    change_wallpaper()