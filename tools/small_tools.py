# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2022/6/16 14:25
# @Author : waxberry
# @File : small_tools.py
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

    print ('操作系统：{os_name}')
    print ('cpu：{processor.Name}')
    print ('内存：{ram}GB')
    print ('显卡：{gpu.Name}')

    print ('\n计算机信息如上⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆')

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
        print ('Temp:{cpu.temperature}℃')
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
print ('original text:' + str(text))

checked = textblob.TextBlob(text)
print ('corrected text:' + str(checked.correct()))


import autocorrect
spell = autocorrect.Speller(lang='en')
print (spell('cmputr'))
print (spell('watr'))
print (spell('survice'))



# 批量抠图
import os
import paddlehub as hub

humanseg = hub.Module(name='deeplabv3p_xception65_humanseg')# 加载模型
path = './heben/'# 文件目录

files = [path + i for i in os.listdir(path)]# 获取文件列表
results = humanseg.segmentation(data={'image': files})# 抠图
for result in results:
    print(result)

# 自然语言处理
senta = hub.Module(name='senta_lstm')        # 加载模型
sentence = [    # 准备要识别的语句
    '你好漂亮', '你真难看呀', '他好难过', '我不开心', '这是一款什么游戏，真垃圾', '这个游戏太好玩了',
]
results = senta.sentiment_classify(data={'text':sentence})    # 情绪识别
for result in results: # 输出识别结果
    print(result)

# 人脸识别
module = hub.Module(name='pyramidbox_lite_mobile_mask')# 加载模型
image_list = ['face2.jpg']# 图片列表
input_dict = {'image':image_list}# 获取图片字典
module.face_detection(data=input_dict)# 检测是否带了口罩

# 人脸关键点检测
face_landmark = hub.Module(name="face_landmark_localization")

image = 'face.jpg'
result = face_landmark.keypoint_detection(images=[cv2.imread(image)], visualization=True)
print(result)

# 猫脸识别
ImagePath = './cat/cat.jpg'# 待检测的图片路径
image = cv2.imread(ImagePath)# 读取图片
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)# 把图片转换为灰度模式
face_cascade = cv2.CascadeClassifier(r'./haarcascade_frontalcatface.xml')# 探测图片中的猫脸
faces = face_cascade.detectMultiScale(gray,scaleFactor=1.15,minNeighbors=5,minSize=(3, 3))# 获取训练好的猫脸的参数数据,进行猫脸检测
search_info = "Find %d face."%len(faces) if len(faces) <= 1 else "Find %d faces."%len(faces)
for (x, y, w, h) in faces:# 绘制猫脸的矩形区域(红色边框)
    cv2.rectangle(image, (x,y), (x+w,y+h), (0,0,255), 2)
# cv2.imshow('Find faces!', image)
# cv2.waitKey(0)
cv2.imwrite("./cat/cat2.jpg", image)# 显示图片


# 获取摄像头人脸
detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detector.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    cv2.imshow('frame', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()


# 快速生成动图
import imageio

image_list = ['image/1.jpg','image/2.jpg', 'image/3.jpg', 'image/4.jpg']
gif_name = 'dongtu.gif'
duration = 1
frames = []
for image_name in image_list:
    frames.append(imageio.imread(image_name))
imageio.mimsave(gif_name, frames, "GIF", duration=duration)

# ftp 服务器
# python -m http.server 8090


# 字符画
IMG = "3.jpg"
WIDTH = 80
HEIGHT = 40
OUTPUT = "./ascii/ascii.txt"

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
def get_char(r, g, b, alpha = 256):# 将256灰度映射到70个字符上
    if alpha == 0:
        return ' '
    length = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.7122 * b)
    unit = (256.0 + 1)/length
    return ascii_char[int(gray/unit)]

im = Image.open(IMG)
im = im.resize((WIDTH, HEIGHT), Image.NEAREST)
txt = ""
for i in range(HEIGHT):
    for j in range(WIDTH):
        txt += get_char(*im.getpixel((j, i)))
    txt += '\n'
print("txt")

with open(OUTPUT, 'w') as f:#字符画输出到文件
    f.write(txt)







# 使用 Python 进行速度测试
import speedtest
speedTest = speedtest.Speedtest()
print(speedTest.get_best_server())
print(speedTest.download())#Check download speed
print(speedTest.upload())#Check upload speed
import pyspeedtest # Method 2
st = pyspeedtest.SpeedTest()
st.ping()
st.download()
st.upload()

# 在谷歌上搜索
from googlesearch import search
query = 'Medium.com'
for url in search(query):
    print(url)


# 制作网络机器人
import time
from selenium import webdriver
from selenium.webdriver.common.keys
import Keysbot = webdriver.Chrome("chromedriver.exe")
bot.get('http://www.google.com')
search = bot.find_element_by_name('q')
search.send_keys("@codedev101")
search.send_keys(Keys.RETURN)
time.sleep(5)
bot.quit()

# 获取歌曲歌词
import lyricsgenius
api_key = 'xxxxxxxxxxx'
genius = lyricsgenius.Genius(api_key)
artist = genius.search_artist('Pop Smoke', max_songs=5, sort='title')
song = artist.song('100k On a Coupe')
print(song.lyrics)

# 获取照片的Exif数据
import PIL.Image
import PIL.ExifTags
img = PIL.Image.open('Img.jpg')
exif_data = {
    PIL.ExifTags.TAGS[i]:j
    for i, j in img.getexif().items()
    if i in PIL.ExifTags.TAGS
}
print(exif_data)

import exifread# Method 2
filename = open(path_name, 'rb')
tags = exifread.process_file(filename)
print(tags)

# 提取图像中的 OCR 文本
import pytesseract
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  #必须从 Github 下载 tesseract.exe
t=Image.open("img.png")
text = pytesseract.image_to_string(t, config='')
print(text)


# 将照片转换为Cartonize
import cv2
img = cv2.imread('img.jpg')
grayimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
grayimg = cv2.medianBlur(grayimg, 5)
edges = cv2.Laplacian(grayimg, cv2.CV_8U, ksize=5)
r, mask = cv2.threshold(edges, 100, 255, cv2.THRESH_BINARY_INV)
img2 = cv2.bitwise_and(img, img, mask=mask)
img2 = cv2.medianBlur(img2, 5)
cv2.imwrite('cartooned.jpg', mask)

# 清空回收站
import winshell
try:
    # winshell.recycle_bin().empty(confirm=False, / show_progress = False, sound = True)
    winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
    print("Recycle bin is emptied Now")
except:
    print("Recycle bin already empty")


# Python 图像增强
from PIL import Image, ImageFilter
from PIL import ImageEnhance
im = Image.open('img.jpg')
en = ImageEnhance.Color(im)
en = ImageEnhance.Contrast(im)
en = ImageEnhance.Brightness(im)
en = ImageEnhance.Sharpness(im)
en.enhance(1.5).show('enhanced')

# 获取 Window 版本
data = wmi.WMI()
for os_name in data.Win32_OperatingSystem():
    print(os_name.Caption)


# 将 PDF 转换为图像
import fitz
pdf = 'sample_pdf.pdf'
doc = fitz.open(pdf)
for page in doc:
    pix = page.getPixmap(alpha=False)
    pix.writePNG('page-%i.png' % page.number)


# 转换：十六进制到 RGB
def Hex_to_Rgb(hex):
    h = hex.lstrip('#')
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))
print(Hex_to_Rgb('#c96d9d'))
print(Hex_to_Rgb('#fa0515'))



# 网站状态
import urllib.request
from urllib.request import Request, urlopen
req = Request('https://medium.com/@pythonians', headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).getcode()
print(webpage)

import requests #method 2
r = requests.get('https://medium.com/@pythonians')
print(r.status_code) #200