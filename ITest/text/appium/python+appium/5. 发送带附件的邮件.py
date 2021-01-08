#coding:utf-8

import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import Encoders
import time

def sendMailForAttch(smtpServer, sender, password, receivers, filePath, subject):
    # 限制收件人必须为列表格式，支持多个收件人
    if isinstance(receivers, list):
        if len(receivers) == 1:
            mailTo = receivers[0]
        else:
            # 多个收件人可以用逗号或分号隔开
            mailTo = ','.join(receivers)
    else:
        print u'收件人格式错误，收件人输入列表错误，发送邮件失败'
        return -1


    # 读取html文件内容
    with open(filePath, 'rb') as fp:
        mail_body = fp.read

    # 发送html文件
    msg = MIMEText(mail_body, 'html', 'utf-8')
    msg = MIMEMultipart()

    # 添加邮件正文内容
    body = MIMEText(mail_body, _subtype='html', _charset='utf-8')#创建一个实例，这里设置为html格式邮件

    msg.attach(body)

    # 添加附件
    attach = MIMEText(open(filePath, 'rb').read(), 'base64', 'utf-8')
    attach['Content-Type'] = 'applicationoctet-stream'

    # 这里的filename可以任意写，写什么名字，邮件里就显示什么
    attach['Content-Disposition'] = 'attachment; filename=027755.html'
    msg.attach(attach)

    # 定义邮件主题
    msg['Subject'] = Header(subject, 'utf-8')
    msg['From'] = sender
    msg['To'] = mailTo

    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(smtpServer)
        smtpObj.login(sender, password)
        smtpObj.sendmail(sender, receivers, msg.as_string())
        smtpObj.quit()#断开smtp连接
        print u'邮件发送成功'
    except smtplib.SMTPException as e:
        print 'Error 无法发送邮件'
        print e

sendMailForAttch('smtp@163.com', '18201274484@163.com', '87549319',
                ['18201274484@163.com', 'cdong2020@163.com', '451009894@qq.com'],
                'd:\\002755.html', u'seleium_stmp例子')