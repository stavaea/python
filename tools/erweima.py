# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2023/3/13 15:00
# @Author : waxberry
# @File : erweima.py
# @Software : PyCharm
import qrcode
import segno
#一个简单的二维码
import ssid as ssid
from django.utils.termcolors import background

price_tag = segno.make('£9.99')
price_tag.save('Price Tag.png')

# 用于分享url的QR码
video = segno.make('https://www.youtube.com/watch')
video.save('Video.png', scale=4)

# 一个更加丰富多彩的QR码
piet = segno.make('htts://esolangs.org/wiki/Piet', error='h')
piet.to_artistic(background='background.png', target='Piet.png', scale=16)

# 携带WIFI详细信息的QR码

wifi_settings = {
    ssid: 'wifi name',
    'password': 'wifi password',
    'security': 'WPA'
}

wifi = segno.helpers.make_wifi(**wifi_settings)
wifi.save('wifi.png', dark='yellow', light='#323524', scale=8)


# 联系信息的二维码
vcard = segno.helpers.make_vcard(
    name='Pxxx;Jxxx',
    displayname='Times Tables Furniture',
    email='jxxxpxxx@timestables.furniture',
    url=[
        'https://www.etsy.com/uk/shop/TimesTablesFurniture',
        'https://www.facebook.com/profile.php?id=100083448533180'
    ],
    phone='+44xxxxxxxx',
)
img = vcard.to_pil(scale=6, dark='#FF7D92').rotate(45, expend=True)
img.save('Etsy.png')

# 自己的VCard，选择添加公司的标志作为背景
awsom =segno.helpers.make_vcard(
    name='Fison;Pete',
    displayname='AWSOM Solutions Ltd.',
    email=('pxxxfxxx@awsom.solutions'),
    url=[
        'https://twitter.com/awsom_solutions',
        'https://medium.com/@petefison',
        'https://github.com/pfython'
    ],
    phone="+44xxxxxxxxxx",
)

awsom.to_artistic(background="logo.png",
                  target='AWSOM.png',
                  scale=6,
                  quiet_zone="#D29500"
)

'''
segno API还允许你做以下事情。

segno.helpers.make_email : 发送一封预先准备好主题和内容的电子邮件。对于订阅新闻简报，或者从邮件服务器上触发任何可能的行动，都是非常好的。

segno.helpers.make_epc_qr: 发起一个电子支付。

segno.helpers.make_geo: 在一个特定的经度和纬度打开默认的地图应用。

segno.make_sequence : 使用 "结构化附加 "模式创建一个QR码序列
'''


# 把所有东西都保存在内存中
import io
beatle = segno.make('Paul McCartney')
beatle = qrcode.to_pil()

beatle = segno.make('Paul McCartney')
buff = io.BytesIO()
beatle.save(buff, kind='svg')

# 直接从URL中加载背景图片到内存中，而不是先在硬盘或服务器上创建一个文件
from urllib.request import urlopen

beatle = segno.make('Ringo Starr', error='h')
url = 'https://media.giphy.com/media/HNo1tVKdFaoco/giphy.gif'
bg_file = urlopen(url)
beatle.to_artistic(background=bg_file, target='ringo.gif', scale=10)