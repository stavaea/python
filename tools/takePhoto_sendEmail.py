# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2022/8/24 14:54
# @Author : waxberry
# @File : takePhoto_sendEmail.py
# @Software : PyCharm

import cv2
import smtplib
import sys
import os
import time
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

smtpserver = 'smtp.163.com'
username = 'xxxx@163.com'
password = 'xxxx'
sender = '发件人名称'
addressee = '收件人'
exit_count = 5    #尝试联网次数
path = os.getcwd()    #获取图片保存路径


#实现拍照
def getPicture():
    cap = cv2.VideoCapture()
    ret, frame = cap.read()
    cv2.imwrite(path+'/person.jpg', frame)
    cap.release()

# 构造邮件内容
def setMsg():
    #下面依次为邮件类型，主题，发件人和收件人
    msg = MIMEMultipart('mixed')
    msg['Subject'] = '电脑已经启动'
    msg['From'] = 'xxxx@163.com <xxxx@163.com>'
    msg['To'] = addressee
    #下面为邮件的正文
    text = '你的电脑已开机！照片如下！'
    text_plain = MIMEText(text, 'plain', 'utf-8')
    msg.attach(text_plain)

    #构造图片连接
    sendimagefile = open(path+'/person.jpg', 'rb').read()
    image = MIMEImage(sendimagefile)
    #下面一句将收件人看到的附件照片名称改为people.png
    image['Content-Disposition'] = 'attachment; filename="people.png"'
    return msg.as_string()


# 实现邮件发送
def sendEmail(msg):
    # 发送邮件
    smtp = smtplib.SMTP()
    smtp.connect('smtp.163.com')
    smtp.login(username, password)
    smtp.sendmail(sender, addressee, msg)
    smtp.quit()

# 判断网络状态,成功返回0,失败1
# Linux中ping命令不会自动停止,需要加入参数 -c 4,表示在发送指定数目的包后停止
def isLink():
    return os.system('ping -c 4 www.baidu.com')

# 主函数逻辑,如果网络正常,发送邮件,不正常则等待10s再次测试;如果等待次数超过设置的最大次数，则退出程序
def main():
    reconnect_times = 0
    while isLink():
        time.sleep(10)
        reconnect_times += 1
        if reconnect_times == exit_count:
            sys.exit()

    getPicture()
    msg = setMsg()
    sendEmail(msg)

