# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2023/5/6 9:19
# @Author : waxberry
# @File : 小脚本.py
# @Software : PyCharm

# 网址缩短器
import re

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



# 抓取知乎图片
from selenium import webdriver
import time
import urllib.request

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.zhihu.com/question/29134042')
i = 0
while i < 10:
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    time.sleep(2)
    try:
        driver.find_element_by_css_selector('button.QuestionMainAction').click()
        print('page' + str(i))
        time.sleep(1)
    except:
        break
result_raw = driver.page_source
content_list = re.findall("img src=\"(.+?)\" ", str(result_raw))
n = 0
while n < len(content_list):
    i = time.time()
    local = (r'%s.jpg' % (i))
    urllib.request.urlretrieve(content_list[n], local)
    print('编号' + str(i))
    n = n + 1


# 聊天机器人互相聊天
from time import sleep
import requests

s = input('请主人输入话题：')
while True:
    resp = requests.post("http://www.tuling123.com/openapi/api",
                         data={"key": "4fede3c4384846b9a7d0456a5e1e2943", "info": s, }
                         )
    resp = resp.json()
    sleep(1)
    print('小鱼', resp['text'])
    s = resp['text']
    resp = requests.get("http://api.qingyunke.com/api.php", {'key': 'free', 'appid':0, 'msg': s})
    resp.encoding = 'utf8'
    resp = resp.json()
    sleep(1)
    print('菲菲：', resp['content'])
# 网上还有一个据说智商比较高的小i机器人，用爬虫的功能来实现一下：
import urllib.request
import re
while True:
    x = input("主人：")
    x = urllib.parse.quote(x)
    link = urllib.request.urlopen(
        "http://nlp.xiaoi.com/robot/webrobot?&"
        "callback=__webrobot_processMsg&"
        "data=%7B%22sessionId%22%3A%22ff725c236e5245a3ac825b2dd88a7501%22%2C%22robotId%22%3A%22webbot%22%2C%22userId%22%3A%227cd29df3450745fbbdcf1a462e6c58e6%22%2C%22body%22%3A%7B%22content%22%3A%22"
        + x + "%22%7D%2C%22type%22%3A%22txt%22%7D")
    html_doc = link.read().decode()
    reply_list = re.findall(r'\"content\":\"(.+?)\\r\\n\"', html_doc)
    print("小i：" + reply_list[-1])

# 分析唐诗的作者是李白还是杜甫
import jieba
from nltk.classify import NaiveBayesClassifier
# 需要提前把李白的诗收集一下，放在libai.txt文本中。
text1 = open(r'libai.txt', 'rb').read()
list1 = jieba.cut(text1)
result1 = ''.join(list1)
# 需要提前把李白的诗收集一下，放在libai.txt文本中。
text2 = open(r'dufu.txt', 'rb').read()
list2 = jieba.cut(text2)
result2 = ''.join(list2)
# 数据准备
libai = result1
dufu = result2
# 特征提取
def word_feats(words):
    return dict([(word, True) for word in words])
libai_features = [(word_feats(lb), 'lb') for lb in libai]
dufu_features = [(word_feats(df), 'df') for df in dufu]
train_set = libai_features + dufu_features
# 训练决策
classifier = NaiveBayesClassifier.train(train_set)
# 分析测试
sentence = input('请输入一句你喜欢的诗：')
print('\n')
seg_list = jieba.cut(sentence)
result1 = ''.join(seg_list)
words = result1.split(' ')
# 统计结果
lb = 0
df = 0
for word in words:
    classResult = classifier.classify(word_feats(word))
    if classResult == 'lb':
        lb = lb + 1
    if classResult == 'df':
        df = df + 1
# 呈现比例
x = float(str(float(lb) / len(words)))
y = float(str(float(df) / len(words)))
print('李白的可能性：%.2f%%' % (x * 100))
print('杜甫的可能性：%.2f%%' % (y * 100))


# 彩票随机生成35选7
import random
temp = [i + 1 for i in range(35)]
random.shuffle(temp)
i = 0
list = []
while i < 7:
    list.append(temp[i])
    i = i + 1
list.sort()
print('\033[0;31;;1m')
print(*list[0:6], end="")
print('\033[0;34;;1m', end=" ")
print(list[-1])


# 自动写检讨书
import random
import xlrd
ExcelFile = xlrd.open_workbook(r'test.xlsx')
sheet = ExcelFile.sheet_by_name('Sheet1')
i = []
x = input('请输入具体事件：')
y = int(input('老师要求的字数：'))
while len(str(i)) < y * 1.2:
    s = random.randint(1, 60)
    rows = sheet.row_values(s)
    i.append(*rows)
print('' * 8 + '检讨书' + '\n' + '老师：')
print('我不应该' + str(x) + ',', *i)
print('再次请老师原谅！')
'''
以下是样稿：

请输入具体事件：抽烟
老师要求的字数：200
        检讨书
老师：
我不应该抽烟， 学校一开学就三令五申，一再强调校规校纪，提醒学生不要违反校规，可我却没有把学校和老师的话放在心上，没有重视老师说的话，没有重视学校颁布的重要事项，当成了耳旁风，这些都是不应该的。同时也真诚地希望老师能继续关心和支持我，并却对我的问题酌情处理。 无论在学习还是在别的方面我都会用校规来严格要求自己，我会把握这次机会。 但事实证明，仅仅是热情投入、刻苦努力、钻研学业是不够的，还要有清醒的政治头脑、大局意识和纪律观念，否则就会在学习上迷失方向，使国家和学校受损失。
再次请老师原谅！
'''



# 屏幕录相机，抓屏软件
from time import sleep
from PIL import ImageGrab
m = int(input('请输入想抓屏几分钟：'))
m = m * 60
n = 1
while n < m:
    sleep(0.02)
    im = ImageGrab.grab()
    local = (r'%s.jpg' % (n))
    im.save(local, 'jpeg')
    n = n + 1


# 制作Gif动图
from PIL import Image
im = Image.open('1.jpg')
images = []
images.append(Image.open('2.jpg'))
images.append(Image.open('3.jpg'))
im.save('gif.gif', save_all=True, append_images=images, loop=1, duration=1, comment=b'aaabb')

