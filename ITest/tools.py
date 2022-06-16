# ！/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2022/6/16 14:25
# @Author : waxberry
# @File : tools.py
# @Software : PyCharm

# 图片格式转换
from PIL import Image

img = Image.open('图片名.jpg')
img.save('图片名.png')

from cv2 import imread, imwrite

image = imread('图片名.jpg', 1)
imwrite('图片名.png', image)

# pdf加密解密
import pikepdf

# 加密
pdf = pikepdf.open('文件名.pdf')
pdf.save('encrypt.pdf', encryption=pikepdf.Encryption(owner='your_password',user='your_password', R=4))
pdf.close()

# 解密
pdf = pikepdf.open('文件名.pdf', password='your_password')
pdf.save('decrypt.pdf')
pdf.close()

# 获取电脑配置
import wmi

def System_spec():
    pc = wmi.WMI()
    os_info = pc.Win32_OperatingSystem()[0]
    processor = pc.Win32_Processor()[0]
    gpu = pc.Win32_VideoController()[0]
    os_name = os_info.Name.encode('utf-8').split(b'|')[0]
    ram = float(os_info.TotalVisibleMemorySize) / 1048576

    print '操作系统：{os_name}'
    print 'cpu：{processor.Name}'
    print '内存：{ram}GB'
    print '显卡：{gpu.Name}'

    print '\n计算机信息如上⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆'

# 解压文件
from zipfile import ZipFile

unzip = ZipFile('文件名.zip', 'r')
unzip.extractall('output Floder')

# excel工作表合并
import pandas as pd

# 文件名
filename = 'xx.xlsx'
# 表格数量
T_sheets = 5

df = []
for i in range(1, T_sheets+1):
    sheet_data = pd.read_excel(filename, sheet_name=i, header=None)
    df.append(sheet_data)

# 合并表格
output = 'merged.xlsx'
df = pd.concat(df)
df.to_excel(output)


# 图像转换为素描图
import cv2

img = cv2.imread('img.jpg')
grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
invert = cv2.bitwise_not(grey)
blur_img = cv2.GaussianBlur(invert, (7, 7), 0)
inverse_blur = cv2.bitwise_not(blur_img)
sketch_img = cv2.divide(grey, inverse_blur, scale=256.0)
cv2.imwrite('sketch_img', sketch_img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# 获取cpu温度
from time import sleep
from pyspectator.processor import Cpu

cpu = Cpu(monitoring_latency=1)
with cpu:
    while True:
        print 'Temp:{cpu.temperature}℃'
        sleep(2)

# 提取pdf表格
import camelot

tables = camelot.read_pdf('tables.pdf')
print (tables)
tables.export('extracted.csv', f='csv', compress=True)


import tabula
tabula.read_pdf('xx.pdf', pages='all')
tabula.convert_into('xx.pdf', 'output.csv', output_format='csv', pages='all')

# 截图
from mss import mss
with mss() as screenshot:
    screenshot.shot(output='scr.png')


import PIL.ImageGrab
scr = PIL.ImageGrab.grab()
scr.save('scr.png')


# 拼写检查器
import textblob
text = 'mussage'
print 'original text:' + str(text)

checked = textblob.TextBlob(text)
print 'corrected text:' + str(checked.correct())


import autocorrect
spell = autocorrect.Speller(lang='en')
print spell('cmputr')
print spell('watr')
print spell('survice')