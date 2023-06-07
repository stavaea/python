# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2023/5/6 9:19
# @Author : waxberry
# @File : 小脚本.py
# @Software : PyCharm

# 网址缩短器
import pyshorteners
s = pyshorteners.Shortener(api_key='your_api_key')
long_url = input('Enter the URL to shorten:')
short_url = s.bitly.short(long_url)
print('The shortened URL is: ' + short_url)

# 创建伪信息
import pandas as pd
from faker import Faker

# create object
fake = Faker()
# Generate data
fake.name()
fake.text()
fake.address()
fake.email()
fake.date()
fake.country()
fake.phone_number()
fake.random_number(digits=5)

# Dataframe creation
fakeDataframe = pd.DataFrame({'date': [fake.date() for i in range],
                              'name': [fake.name() for i in range(5)],
                              'email': [fake.email() for i in range(5)],
                              'text': [fake.text() for i in range(5)]})
print(fakeDataframe)


# 优酷视频下载器
from pytube import YouTube

link = input('Enter a youtube video URL:') #i.e. https://youtu.be/dQw4w9WgXcQ

yt = YouTube(link)
yt.streams.first().download()
print('downloaded', link)

# 北约音标加密器
def encrypt_message(message):
    nato_alphabet = {'A': 'Alfa', 'B': 'Bravo', 'C': 'Charlie', 'D': 'Delta',
                     'E': 'Echo', 'F': 'Foxtrot', 'G': 'Golf', 'H': 'Hotel',
                     'I': 'India', 'J': 'Juliet', 'K': 'Kilo', 'L': 'Lima',
                     'M': 'Mike', 'N': 'November', 'O': 'Oscar', 'P': 'Papa',
                     'Q': 'Quebec', 'R': 'Romeo', 'S': 'Sierra', 'T': 'Tango',
                     'U': 'Uniform', 'V': 'Victor', 'W': 'Whiskey', 'X': 'Xray',
                     'Y': 'Yankee', 'Z': 'Zulu'
                     }

    encrypted_message = ""
    # Iterate through each letter in the message
    for letter in message:
    # If the letter is in the dictionary, add the corresponding codeword to the encrypted message
        if letter.upper() in nato_alphabet:
            encrypted_message += nato_alphabet[letter.upper()] + ""
    # If the letter is not in the dictionary, add the original letter to the encrypted message
        else:
            encrypted_message += letter

    return encrypted_message

message = "Hello World"
encrypted_message = encrypt_message(message)
print("Encrypted message: ", encrypted_message)


# 社交媒体登录自动化
from selenium import webdriver

driver = webdriver.Firefox()
driver.get('http://www.facebook.com/')
# Find the email or phone field and enter the email or phone number
email_field = driver.find_element_by_id('email')
email_field.send_keys('your_email_or_phone')

# Find the password field and enter the password
password_field = driver.find_element_by_id('pass')
password_field.send_keys('your_password')

# Find the login button and click it
login_button = driver.find_element_by_id('loginbutton')
login_button.click()


# 图片优化器
# image optimizing
# pip install Pillow
import PIL

# croping
im = PIL.Image.open('Image1.jpg')
im = im.crop(34, 23, 100, 100)

# resizing
im = PIL.Image.open('Image1.jpg')
im = im.resize((50, 50))

# flipping
im = PIL.Image.open('Image1.jpg')
im = im.transpose(PIL.Image.FLIP_LEFT_RIGHT)

# rotating
im = PIL.Image.open('Image1.jpg')
im = im.rotate(360)

# compressing
im = PIL.Image.open('Image1.jpg')
im.save('Image1.jpg', optimize=True, quality=90)

# bluring
im = PIL.Image.open('Image1.jpg')
im = im.filter(PIL.ImageFilter.BlUR)

# Sharpening
im = PIL.Image.open("Image1.jpg")
im = im.filter(PIL.ImageFilter.SHARPEN)

# Set Brightness
im = PIL.Image.open("Image1.jpg")
im = PIL.ImageEnhance.Brightness(im)
im = im.enhance(1.5)

# Set Contrast
im = PIL.Image.open("Image1.jpg")
im = PIL.ImageEnhance.Contrast(im)
im = im.enhance(1.5)

# Adding Filters
im = PIL.Image.open("Image1.jpg")
im = PIL.ImageOps.grayscale(im)
im = PIL.ImageOps.invert(im)
im = PIL.ImageOps.posterize(im, 4)

# Saving
im.save("Image1.jpg")


# 视频优化器
# Video Optimizer
# pip install moviepy
import moviepy.editor as pyedit
# Load the Video
video = pyedit.VideoFileClip("vid.mp4")
# Trimming
vid1 = video.subclip(0, 10)
vid2 = video.subclip(20, 40)
final_vid = pyedit.concatenate_videoclips([vid1, vid2])
# Speed up the video
final_vid = final_vid.speedx(2)
# Adding Audio to the video
aud = pyedit.AudioFileClip("bg.mp3")
final_vid = final_vid.set_audio(aud)
# Reverse the Video
final_vid = final_vid.fx(pyedit.vfx.time_mirror)
# Merge two videos
vid1 = pyedit.VideoFileClip("vid1.mp4")
vid2 = pyedit.VideoFileClip("vid2.mp4")
final_vid = pyedit.concatenate_videoclips([vid1, vid2])
# Add VFX to Video
vid1 = final_vid.fx(pyedit.vfx.mirror_x)
vid2 = final_vid.fx(pyedit.vfx.invert_colors)
final_vid = pyedit.concatenate_videoclips([vid1, vid2])
# Add Images to Video
img1 = pyedit.ImageClip("img1.jpg")
img2 = pyedit.ImageClip("img2.jpg")
final_vid = pyedit.concatenate_videoclips([img1, img2])
# Save the video
final_vid.write_videofile("final.mp4")


# pdf转换图片
# pip install PyMuPDF
import fitz

def pdf_to_images(pdf_file):
    doc = fitz.open(pdf_file)
    for p in doc:
        pix = p.get_pixmap()
        output = f'page{p.number}.png'
        pix.writePNG(output)

pdf_to_images('test.pdf')


# 获取api数据
# pip install urllib3
import urllib3
# Fetch API data
url = 'https://api.github.com/users/psf/repos'
http = urllib3.PoolManager()
response = http.request('GET', url)
print(response.status)
print(response.data)

# Post api data
url = 'https://httpbin.org/post'
http = urllib3.PoolManager()
response = http.request('POST', url, fields={'hello': 'world'})
print(response.status)


# 电池指示灯
# pip instal plyer
from plyer import notification
import psutil
from time import sleep

while True:
    battery = psutil.sensors_battery()
    life = battery.percent
    if life < 50:
        notification.notify(
            title='Battery Low',
            message="Please connect to power source",
            timeout=10
        )
    sleep(60)


# 语法固定器
# Grammer Fixer
# pip install happytransformer

from happytransformer import HappyTextToText as HappyTTT
from happytransformer import TTSettings


def Grammer_Fixer(Text):
    Grammer = HappyTTT("T5","prithivida/grammar_error_correcter_v1")
    config = TTSettings(do_sample=True, top_k=10, max_length=100)
    corrected = Grammer.generate_text(Text, args=config)
    print("Corrected Text: ", corrected.text)
    Text = "This is smple tet we how know this"
Grammer_Fixer(Text)

# 拼写修正
# pip install textblob
from textblob import *

# Fixing Paragraph Spells
def fix_paragraph_words(paragraph):
    sentence = TextBlob(paragraph)
    correction = sentence.correct()
    print(correction)

# Fixing Words Spells
def fix_word_spell(word):
    word = Word(word)
    correction = word.correct()
    print(correction)
fix_paragraph_words("This is sammple tet!!")
fix_word_spell("maangoo")

# 互联网下载器
# pip install internetdownloadmanager
import internetdownloadmanager as idm

def Download(url, output):
    pydownloader = idm.Downloader(
        worker=20,
        part_size=1024*1024*10,
        resumable=True
    )
    pydownloader.download(url, output)
Downloader("Link url", "image.jpg")
Downloader("Link url", "video.mp4")

# 获取世界新闻
# pip install requests
import requests
ApiKey = "YOUR_API_KEY"
url = "https://api.worldnewsapi.com/search-news?text=hurricane&api-key={ApiKey}"
headers = {
    'Accept': 'application/json'
}
response = requests.get(url, headers=headers)
print("News: ", response.json())


# PySide2 GUI
# pip install PySide2
from PySide6.QtWidgets import *
from PySide6.QtGui import *
import sys
app = QApplication(sys.argv)
window = QWidget()
# Resize the Window
window.resize(500, 500)
# Set the Window Title
window.setWindowTitle("PySide2 Window")
# Add Buttons
button = QPushButton("Click Me", window)
button.move(200, 200)
# Add Label Text
label = QLabel("Hello Medium", window)
label.move(200, 150)
# Add Input Box
input_box = QLineEdit(window)
input_box.move(200, 250)
print(input_box.text())
# Add Radio Buttons
radio_button = QRadioButton("Radio Button", window)
radio_button.move(200, 300)
# Add Checkbox
checkbox = QCheckBox("Checkbox", window)
checkbox.move(200, 350)
# Add Slider
slider = QSlider(window)
slider.move(200, 400)
# Add Progress Bar
progress_bar = QProgressBar(window)
progress_bar.move(200, 450)
# Add Image
image = QLabel(window)
image.setPixmap(QPixmap("image.png"))
# Add Message Box
msg = QMessageBox(window)
msg.setText("Message Box")
msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
window.show()
sys.exit(app.exec())