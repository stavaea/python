# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2022/7/25 9:38
# @Author : waxberry
# @File : alarm_clock.py
# @Software : PyCharm

import time
from datetime import datetime
from playsound import playsound
import pyttsx3
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

def alarm():
    pp = pyttsx3.init()
    alarm_time = input("输入要设置的闹钟时间:HH:MM:SS\n")
    alarm_period = input("请输入要设置的时期（AM或PM):\n")
    alarm_hour = alarm_time[0:2]#获取小时
    alarm_minute = alarm_time[3:5]#获取分钟
    alarm_seconds = alarm_time[6:8]#多少秒
    alarm_period = alarm_period.upper()

    print("设置成功正在运行，祝您休息愉快....zzZZ..")
    flag = True
    while flag:
        now = datetime.now()
        current_hour = now.strftime("%I")
        current_minute = now.strftime("%M")
        current_seconds = now.strftime("%S")
        current_period = now.strftime("%p")
        if(alarm_period == current_period):
            if(alarm_hour == current_hour):
                if(alarm_minute == current_minute):
                    if(alarm_seconds == current_seconds):
                        print("Wake Up！！！")
                        playsound('1.mp3') ## 铃声名字最好不要带中文，会节码失败
                        if(int(now.strftime("%M"))-int(alarm_minute) == 10):#延迟十分钟在叫一次
                            playsound('1.mp3')
                            time.sleep(60)
                            pp.say('还不醒？那你可别怪我了都是为你好呀。这就去帮你辞职！哈哈哈哈')
                            pp.runAndWait()
    return 1

def mail_qq():
    my_sender = 'xxxxx@qq.com'  # 发件人邮箱账号
    my_pass = '***'  # 授权码   以QQ邮箱为例，进入设置，找到POP3/IMAP/SMTP/Exchange/CardDAV/CalDAV服务，全部选择已开启后，点击生成授权码
    my_user = 'xxxxxxx@qq.com'  # 收件人邮箱账号，我这边发送给自己

    def mail():
        ret = True
        try:
            msg = MIMEText('想睡觉，不干了', 'plain', 'utf-8')  # 填写内容
            msg['From'] = formataddr(["我是xx,老子不干了", my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
            msg['To'] = formataddr(["xx", my_user])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
            msg['Subject'] = "辞职报告"  # 邮件的主题，也可以说是标题你也可以写成分手报告

            server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器
            server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
            server.sendmail(my_sender, [my_user, ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
            server.quit()  # 关闭连接
        except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
            ret = False
        return ret

    ret = mail()
    if ret:
        print("邮件发送成功")
    else:
        print("邮件发送失败")

if __name__ == '__main__':
    a = alarm()
    #if a==1:    #如果闹钟没关闭就发邮件