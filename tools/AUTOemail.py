# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2023/4/12 9:49
# @Author : waxberry
# @File : AUTOemail.py
# @Software : PyCharm

import cv2
import smtplib
import sys
import os
import time
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from tools.takePhoto_sendEmail import exit_count

# 设置参数
smtpserver = ''     # smtp服务器
username = '' # 邮件账号
password = '' #登录密码
sender = '' #发件人
addressee = '' #收件人
exit_count = 5  #尝试联网次数
path = os.getcwd() #  获取图片路径

# 实现拍照
def getPicture():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cv2.imwrite(path+'/person.jpg', frame)
    # 关闭摄像头
    cap.release()

# 构建邮件内容
def setMsg():
    # 下面依次为邮件类型,主题,发件人和收件人
    msg = MIMEMultipart('mixed')
    msg['Subject'] = '电脑已经启动'
    msg['From'] = '发件人'
    msg['To'] = addressee

    # 下面为邮件的正文
    text = '主人，你的电脑已经开机！照片如下！'
    text_plain = MIMEText(text, 'plain', 'utf-8')
    msg.attach(text_plain)

    # 构造图片链接
    sendimagefile = open(path+'/person.jpg', 'rb').read()
    image = MIMEImage(sendimagefile)
    # 下面一句将收件人看到的附件照片名称改为people.png
    image['Content-Disposition'] = 'attachment; filename="perple.png"'
    msg.attach(image)
    return msg.as_string()

# 实现邮件发送
def sendEmail(msg):
    # 发送邮件
    smtp = smtplib.SMTP()
    smtp.connect('smtp.163.com')
    smtp.login(username, password)
    smtp.sendmail(sender, addressee, msg)
    smtp,quit()

# 判断网络联通状态

# 判断网络是否联通,成功返回0，不成功返回1
# linux中ping命令不会自动停止，需要加入参数 -c 4，表示在发送指定数目的包后停止。
def isLink():
    return os.system('ping -c 4 www.baidu.com')

# 主函数逻辑
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

'''# 实现开机启动
#切换到我们获取照片和发送邮件的工作目录
cd /home/projects/sendemail
#执行发送邮件的脚本
python2 sendEmile.py
然后 在/etc/rc.local最后添加一行
./home/projects/sendemail/autoStart.sh'''
