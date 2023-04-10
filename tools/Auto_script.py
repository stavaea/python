# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2022/8/22 10:25
# @Author : waxberry
# @File : Auto_script.py
# @Software : PyCharm


# 自动化阅读网页新闻
import pyttsx3
import requests
from bs4 import BeautifulSoup

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
newVoiceRate = 130
engine.setProperty('rate', newVoiceRate)
engine.setProperty('voice', voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

text = str(input('paste article\n'))
res = requests.get(text)
soup = BeautifulSoup(res.text, 'html.parser')

articles = []
for i in range(len(soup.select('.p'))):
    article = soup.select('.p')[i].getText().strip()
    articles.append(article)

text = ''.join(articles)
speak(text)
# engine.save_to_file(text, 'test.mp3')
engine.runAndWait()




# 自动生成素描草图
'''photo sketching using python'''
import cv2

img = cv2.imread('elon.jpg')

# image to gray image
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# gray image to inverted gray image
inverted_gray_image = 255-gray_image

# blurring the inverted gray image
blurred_inverted_gray_image = cv2.GaussianBlur(inverted_gray_image, (19, 19), 0)

# inverting the blurred image
inverted_blurred_image = 255-blurred_inverted_gray_image

# preparing photo shetching
sketck = cv2.divide(gray_image, inverted_blurred_image, scale=256.0)

cv2.imshow("Original Image", img)
cv2.imshow("Pencil Sketch", sketck)
cv2.waitKey(0)


# 自动发送多封邮件
import smtplib
from email.message import EmailMessage
import pandas as pd

def send_email(remail, rsubject, rcontent):
    email = EmailMessage()
    email['from'] = 'The Pythoneer Here'
    email['to'] = remail
    email['subject'] = rsubject
    email.set_content(rcontent)
    with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login('deltadelta371@gmail.com', 'delta@371')    #user  and   password
        smtp.send_message(email)
        print ('email send to', remail)

if __name__ == '__main__':
    df = pd.read_excel('list.xlsx')
    length = len(df) + 1

    for index, item in df.iterrows():
        email = item[0]
        subject = item[1]
        content = item[2]

        send_email(email, subject, content)



# 自动化数据探索
import seaborn as sns

print (sns.get_dataset_names())

df = sns.load_dataset('titanic')

import dtale
dtale.show(df)


# 自动桌面提示
import time
from win10toast import ToastNotifier

toaster = ToastNotifier()

header = input('What You Want Me To Remember\n')
text = input('Releated Message\n')
time_min = float(input('In how many minutes?\n'))


time_min = time_min * 60
print ('Setting up reminder..')
time.sleep(2)
print ('all set!')
time.sleep(time_min)
toaster.show_toast(f"{header}", f"{text}", duration=10, threaded=True)
while toaster.notification_active(): time.sleep(0.005)