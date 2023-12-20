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


# 1. 批量修改文件扩展名
import os

def rename_file_extensions(folder_path, old_ext, new_ext):
    for filename in os.listdir(folder_path):
        if filename.endswith(old_ext):
            base = os.path.splitext(filename)[0]
            new_filename = base + new_ext
            os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))
rename_file_extensions('/path/to/folder', '.txt', '.md')# 使用示例：将所有.txt文件改为.md


# 2. 自动创建多个文件夹
import os

def create_folders(base_path, prefix, count):
    for i in range(1, count + 1):
        os.makedirs(os.path.join(base_path, f"{prefix}{i}"))
create_folders('/path/to/base', 'Folder', 10)# 使用示例：在指定路径下创建10个名为"Folder1"到"Folder10"的文件夹

# 3. 下载网络图片
import requests

def download_images(url_list, save_folder):
    for url in url_list:
        img_data = requests.get(url).content
        filename = url.split('/')[-1]
        with open(os.path.join(save_folder, filename), 'wb') as file:
            file.write(img_data)
url_list = ['http://example.com/image1.jpg', 'http://example.com/image2.jpg']# 使用示例
download_images(url_list, '/path/to/save/folder')

# 4. 简单的文件搜索工具
import os

def search_files(directory, text):
    for filename in os.listdir(directory):
        if text in filename:
            print(os.path.join(directory, filename))
search_files('/path/to/directory', 'report')# 使用示例：在目录中搜索包含"report"的文件

# 5. 批量删除特定扩展名的文件
import os

def delete_files_by_extension(folder_path, extension):
    for filename in os.listdir(folder_path):
        if filename.endswith(extension):
            os.remove(os.path.join(folder_path, filename))
delete_files_by_extension('/path/to/folder', '.tmp')# 使用示例：删除所有扩展名为.tmp的文件

# 6. CSV文件转换为JSON
import csv
import json

def csv_to_json(csv_file_path, json_file_path):
    with open(csv_file_path, 'r') as csv_file, open(json_file_path, 'w') as json_file:
        reader = csv.DictReader(csv_file)
        json_data = [row for row in reader]
        json.dump(json_data, json_file, indent=4)
csv_to_json('/path/to/file.csv', '/path/to/file.json')# 使用示例

# 7. 监控文件夹变化
import time
import os

def monitor_folder_changes(folder_path):
    initial_files = set(os.listdir(folder_path))
    while True:
        current_files = set(os.listdir(folder_path))
        new_files = current_files - initial_files
        deleted_files = initial_files - current_files
        if new_files:
            print(f"Added: {new_files}")
        if deleted_files:
            print(f"Deleted: {deleted_files}")
        initial_files = current_files
        time.sleep(1)
monitor_folder_changes('/path/to/monitor')# 使用示例：监控指定文件夹

# 8. 简单的网页内容抓取
import requests
from bs4 import BeautifulSoup

def fetch_webpage_title(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup.title.text
title = fetch_webpage_title('http://example.com')# 使用示例
print(title)

# 9. 批量修改图片尺寸
from PIL import Image
import os

def resize_images(folder_path, output_folder, size):
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            img = Image.open(os.path.join(folder_path, filename))
            img = img.resize(size, Image.ANTIALIAS)
            img.save(os.path.join(output_folder, filename))
resize_images('/path/to/images', '/path/to/output', (500, 500))# 使用示例：将所有图片尺寸修改为500x500

# 10. 批量压缩PDF文件
from PyPDF2 import PdfFileReader, PdfFileWriter
import os

def compress_pdf(input_folder, output_folder):
    for filename in os.listdir(input_folder):
        if filename.endswith('.pdf'):
            pdf_reader = PdfFileReader(os.path.join(input_folder, filename))
            pdf_writer = PdfFileWriter()

            for page_num in range(pdf_reader.getNumPages()):
                pdf_writer.addPage(pdf_reader.getPage(page_num))

            with open(os.path.join(output_folder, filename), 'wb') as out:
                pdf_writer.write(out)
compress_pdf('/path/to/pdf/folder', '/path/to/output/folder')# 使用示例



# 01、解析和提取 HTML

# Parse and Extract HTML
# pip install gazpacho
import gazpacho
# Extract HTML from URL
url = 'https://www.example.com/'
html = gazpacho.get(url)
print(html)
# Extract HTML with Headers
headers = {'User-Agent': 'Mozilla/5.0'}
html = gazpacho.get(url, headers=headers)
print(html)
# Parse HTML
parse = gazpacho.Soup(html)
# Find single tags
tag1 = parse.find('h1')
tag2 = parse.find('span')
# Find multiple tags
tags1 = parse.find_all('p')
tags2 = parse.find_all('a')
# Find tags by class
tag = parse.find('.class')
# Find tags by Attribute
tag = parse.find("div", attrs={"class": "test"})
# Extract text from tags
text = parse.find('h1').text
text = parse.find_all('p')[0].text
# 02、二维码扫描仪

# Qrcode Scanner
# pip install qrtools
from qrtools import Qr
def Scan_Qr(qr_img):
    qr = Qr()
    qr.decode(qr_img)
    print(qr.data)
    return qr.data
print("Your Qr Code is: ", Scan_Qr("qr.png"))
# 03、截图

# Grab Screenshot
# pip install pyautogui
# pip install Pillow
from pyautogui import screenshot
import time
from PIL import ImageGrab
# Grab Screenshot of Screen
def grab_screenshot():
    shot = screenshot()
    shot.save('my_screenshot.png')
# Grab Screenshot of Specific Area
def grab_screenshot_area():
    area = (0, 0, 500, 500)
    shot = ImageGrab.grab(area)
    shot.save('my_screenshot_area.png')
# Grab Screenshot with Delay
def grab_screenshot_delay():
    time.sleep(5)
    shot = screenshot()
    shot.save('my_screenshot_delay.png')
# 04、创建有声读物

# Create Audiobooks
# pip install gTTS
# pip install PyPDF2
from PyPDF2 import PdfFileReader as reader
from gtts import gTTS
def create_audio(pdf_file):
    read_Pdf = reader(open(pdf_file, 'rb'))
    for page in range(read_Pdf.numPages):
        text = read_Pdf.getPage(page).extractText()
        tts = gTTS(text, lang='en')
        tts.save('page' + str(page) + '.mp3')
create_audio('book.pdf')
# 05、PDF 编辑器

# PDF Editor
# pip install PyPDf4
import PyPDF4
# Parse the Text from PDF
def parse_text(pdf_file):
    reader = PyPDF4.PdfFileReader(pdf_file)
    for page in reader.pages:
        print(page.extractText())
# Remove Page from PDF
def remove_page(pdf_file, page_numbers):
    filer = PyPDF4.PdfReader('source.pdf', 'rb')
    out = PyPDF4.PdfWriter()
    for index in page_numbers:
        page = filer.pages[index]
        out.add_page(page)
with open('rm.pdf', 'wb') as f:
        out.write(f)
# Add Blank Page to PDF
def add_page(pdf_file, page_number):
    reader = PyPDF4.PdfFileReader(pdf_file)
    writer = PyPDF4.PdfWriter()
    writer.addPage()
    with open('add.pdf', 'wb') as f:
        writer.write(f)
# Rotate Pages
def rotate_page(pdf_file):
    reader = PyPDF4.PdfFileReader(pdf_file)
    writer = PyPDF4.PdfWriter()
    for page in reader.pages:
        page.rotateClockwise(90)
        writer.addPage(page)
    with open('rotate.pdf', 'wb') as f:
        writer.write(f)
# Merge PDFs
def merge_pdfs(pdf_file1, pdf_file2):
    pdf1 = PyPDF4.PdfFileReader(pdf_file1)
    pdf2 = PyPDF4.PdfFileReader(pdf_file2)
    writer = PyPDF4.PdfWriter()
    for page in pdf1.pages:
        writer.addPage(page)
    for page in pdf2.pages:
        writer.addPage(page)
    with open('merge.pdf', 'wb') as f:
        writer.write(f)
# 06、迷你 Stackoverflow

# Automate Stackoverflow
# pip install howdoi
# Get Answers in CMD
#example 1
> howdoi how do i install python3
# example 2
> howdoi selenium Enter keys
# example 3
> howdoi how to install modules
# example 4
> howdoi Parse html with python
# example 5
> howdoi int not iterable error
# example 6
> howdoi how to parse pdf with python
# example 7
> howdoi Sort list in python
# example 8
> howdoi merge two lists in python
# example 9
>howdoi get last element in list python
# example 10
> howdoi fast way to sort list
# 07、自动化手机

# Automate Mobile Phones
# pip install opencv-python
import subprocess
def main_adb(cm):
    p = subprocess.Popen(cm.split(' '), stdout=subprocess.PIPE, shell=True)
    (output, _) = p.communicate()
    return output.decode('utf-8')
# Swipe
def swipe(x1, y1, x2, y2, duration):
    cmd = 'adb shell input swipe {} {} {} {} {}'.format(x1, y1, x2, y2, duration)
    return main_adb(cmd)
# Tap or Clicking
def tap(x, y):
    cmd = 'adb shell input tap {} {}'.format(x, y)
    return main_adb(cmd)
# Make a Call
def make_call(number):
    cmd = f"adb shell am start -a android.intent.action.CALL -d tel:{number}"
    return main_adb(cmd)
# Send SMS
def send_sms(number, message):
    cmd = 'adb shell am start -a android.intent.action.SENDTO -d  sms:{} --es sms_body "{}"'.format(number, message)
    return main_adb(cmd)
# Download File From Mobile to PC
def download_file(file_name):
    cmd = 'adb pull /sdcard/{}'.format(file_name)
    return main_adb(cmd)
# Take a screenshot
def screenshot():
    cmd = 'adb shell screencap -p'
    return main_adb(cmd)
# Power On and Off
def power_off():
    cmd = '"adb shell input keyevent 26"'
    return main_adb(cmd)
# 08、监控 CPU/GPU 温度

# Get CPU/GPU Temperature
# pip install pythonnet
import clr
clr.AddReference("OpenHardwareMonitorLib")
from OpenHardwareMonitorLib import *
spec = Computer()
spec.GPUEnabled = True
spec.CPUEnabled = True
spec.Open()
# Get CPU Temp
def Cpu_Temp():
    while True:
        for cpu in range(0, len(spec.Hardware[0].Sensors)):
            if "/temperature" in str(spec.Hardware[0].Sensors[cpu].Identifier):
                print(str(spec.Hardware[0].Sensors[cpu].Value))
# Get GPU Temp
def Gpu_Temp()
    while True:
        for gpu in range(0, len(spec.Hardware[0].Sensors)):
            if "/temperature" in str(spec.Hardware[0].Sensors[gpu].Identifier):
                print(str(spec.Hardware[0].Sensors[gpu].Value))
# 09、Instagram 上传机器人

# Upload Photos and Video on Insta
# pip install instabot
from instabot import Bot
def Upload_Photo(img):
    robot = Bot()
    robot.login(username="user", password="pass")
    robot.upload_photo(img, caption="Medium Article")
    print("Photo Uploaded")
def Upload_Video(video):
    robot = Bot()
    robot.login(username="user", password="pass")
    robot.upload_video(video, caption="Medium Article")
    print("Video Uploaded")
def Upload_Story(img):
    robot = Bot()
    robot.login(username="user", password="pass")
    robot.upload_story(img, caption="Medium Article")
    print("Story Photos Uploaded")
Upload_Photo("img.jpg")
Upload_Video("video.mp4")

# 10、视频水印
# Video Watermark with Python
# pip install moviepy
from moviepy.editor import *

clip = VideoFileClip("myvideo.mp4", audio=True)
width,height = clip.size
text = TextClip("WaterMark", font='Arial', color='white', fontsize=28)
set_color = text.on_color(size=(clip.w + text.w, text.h-10), color=(0,0,0), pos=(6,'center'), col_opacity=0.6)
set_textPos = set_color.set_pos( lambda pos: (max(width/30,int(width-0.5* width* pos)),max(5*height/6,int(100* pos))) )
Output = CompositeVideoClip([clip, set_textPos])
Output.duration = clip.duration
Output.write_videofile("output.mp4", fps=30, codec='libx264')