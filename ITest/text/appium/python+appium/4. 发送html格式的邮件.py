#coding:utf-8
import smtplib
from email.mime.text import MIMEText
from email.header import Header

import time

def sendMailForText(smtServer, sender, password, receivers, filePath, subject):
    # 限制收件人必须为列表格式，支持多个收件人
    if isinstance(receivers, list):
        if len(receivers) == 1:
            mailTo = receivers[0]
        else:
            # 多个收件人可以用逗号或分号隔开
            mailTo = ",".join(receivers)
    else:
        print u'收件人格式错误，收件人输入列表，发送邮件失败'
        return -1

    # 定义发送的文本内容
    mail_body = u'''
    各位好：
    “xx V1.2”版本第一轮测试已完成，请注意查收邮件。
    请及时修复bug，准备第二轮测试。
    
    主要问题：导入商户流程不通，请尽快修复。
    '''

    # 发送文本文件
    message = MIMEText(mail_body, _subtype='html', _charset='utf-8')
    subject = subject

    # 定义邮件的主题
    message['Subject'] = Header(subject, 'utf-8')
    message['From'] = sender
    message['To'] = mailTo

    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(smtServer)
        smtpObj.login(sender, password)
        smtpObj.sendmail(sender, receivers, message.as_string())
        print u'邮件发送成功'
    except smtplib.SMTPException as e:
        print 'Error:无法发送邮件'
        print e

sendMailForText('smtp.163.com', '18201274484@163.com', '87549319',
                ['18201274484@163.com', 'cdong2020@163.com', '451009894@qq.com'],
                'd:\\002755.html', u'seleium_stmp例子')