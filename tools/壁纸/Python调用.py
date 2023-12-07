# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2023/12/7 14:11
# @Author : waxberry
# @File : Python调用.py
# @Software : PyCharm

# 接口使用
'''
1、传入 resolution 参数可以指定壁纸图像的分辨率。默认为1920x1080，可选值如下：
UHD
1920x1200
1920x1080
1366x768
1280x768
1024x768
800x600
800x480
768x1280
720x1280
640x480
480x800
400x240
320x240
240x320
2、传入 index 可以获取某一天的图片，0 表示今天，1 表示昨天，以此类推，index=random 表示随机一天。
3、传入 date 可以获取从某一天到今天的图片，比如 data=20210401。
4、传入 w 和 h 可以指定图片的宽度和高度。
5、传入 qlt 可以指定图片的质量，取值范围是 0 到 100。
举个例子,直接在浏览器输入如下地址
http://bingw.jasonzeng.dev?resolution=UHD&index=random&w=1000&format=json

也可以直接在 css 当中使用
background-image: url(https://bingw.jasonzeng.dev/?index=random);
height: 100%;
background-position: center;
background-repeat: no-repeat;
background-size: cover;
'''


# Python 调用
import requests

def get_wallpaper():
    for i in range(30):
        url = "https://bingw.jasonzeng.dev?resolution=UHD&index=%s" % str(i)
        print(url)
        res = requests.get(url)
        with open("wallpaper/" + "%s.jpg" % str(i), "wb") as w:
            w.write(res.content)
if __name__ == '__main__':
    get_wallpaper()