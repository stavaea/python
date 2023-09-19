# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2023/9/19 9:30
# @Author : waxberry
# @File : 5个实用的Python自动化脚本.py
# @Software : PyCharm


# 1、自动化阅读网页新闻
import pyttsx3
import requests
from bs4 import BeautifulSoup
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
newVoiceRate = 130                       ## Reduce The Speech Rate
engine.setProperty('rate',newVoiceRate)
engine.setProperty('voice', voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
text = str(input("Paste article\n"))
res = requests.get(text)
soup = BeautifulSoup(res.text,'html.parser')

articles = []
for i in range(len(soup.select('.p'))):
    article = soup.select('.p')[i].getText().strip()
    articles.append(article)
text = " ".join(articles)
speak(text)
# engine.save_to_file(text, 'test.mp3') ## If you want to save the speech as a audio file
engine.runAndWait()



# 2、自动生成素描草图
""" Photo Sketching Using Python """
import cv2

img = cv2.imread("elon.jpg")

## Image to Gray Image
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

## Gray Image to Inverted Gray Image
inverted_gray_image = 255 - gray_image

## Blurring The Inverted Gray Image
blurred_inverted_gray_image = cv2.GaussianBlur(inverted_gray_image, (19, 19), 0)

## Inverting the blurred image
inverted_blurred_image = 255 - blurred_inverted_gray_image

### Preparing Photo sketching
sketck = cv2.divide(gray_image, inverted_blurred_image, scale=256.0)

cv2.imshow("Original Image", img)
cv2.imshow("Pencil Sketch", sketck)
cv2.waitKey(0)


# 3、自动发送多封邮件
import smtplib
from email.message import EmailMessage
import pandas as pd

def send_email(remail, rsubject, rcontent):
    email = EmailMessage()                          ## Creating a object for EmailMessage
    email['from'] = 'The Pythoneer Here'            ## Person who is sending
    email['to'] = remail                            ## Whom we are sending
    email['subject'] = rsubject                     ## Subject of email
    email.set_content(rcontent)                     ## content of email
    with smtplib.SMTP(host='smtp.gmail.com',port=587)as smtp:
        smtp.ehlo()                                 ## server object
        smtp.starttls()                             ## used to send data between server and client
        smtp.login("deltadelta371@gmail.com","delta@371") ## login id and password of gmail
        smtp.send_message(email)                    ## Sending email
        print("email send to ",remail)              ## Printing success message

if __name__ == '__main__':
    df = pd.read_excel('list.xlsx')
    length = len(df)+1

    for index, item in df.iterrows():
        email = item[0]
        subject = item[1]
        content = item[2]

        send_email(email,subject,content)


# 4、自动化数据探索
### Importing Seaborn Library For Some Datasets
import seaborn as sns

### Printing Inbuilt Datasets of Seaborn Library
print(sns.get_dataset_names())


### Loading Titanic Dataset
df=sns.load_dataset('titanic')

### Importing The Library
import dtale

#### Generating Quick Summary
dtale.show(df)


# 5、自动桌面提示
from win10toast import ToastNotifier
import time
toaster = ToastNotifier()

header = input("What You Want Me To Remember\n")
text = input("Releated Message\n")
time_min=float(input("In how many minutes?\n"))

time_min = time_min * 60
print("Setting up reminder..")
time.sleep(2)
print("all set!")
time.sleep(time_min)
toaster.show_toast(f"{header}", f"{text}", duration=10, threaded=True)
while toaster.notification_active(): time.sleep(0.005)
