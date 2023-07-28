# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2023/7/26 11:13
# @Author : waxberry
# @File : handle_sendEmail.py
# @Software : PyCharm


import smtplib
from utils.handle_logger import logger
from email.mime.text import MIMEText # 专门发送正文邮件
from email.mime.multipart import MIMEMultipart  # 发送正文、附件等
from email.mime.application import MIMEApplication # 发送附件

class HandleSendEmail:
    def __init__(self, part_text, attachment_list, password, user_list, subject='interface_autoTestReport',
                 smtp_server='smtp.163.com', from_user='hu_chunpu@163.com', filename='unit_test_report.html'):
        '''
        :param part_text: 正文
        :param attachment_list: 附件列表
        :param password: 邮箱服务器第三方密码
        :param user_list: 收件人列表
        :param subject: 主题
        :param smtp_server: 邮箱服务器
        :param from_user: 发件人
        :param filename: 附件名称
        '''
        self.subject = subject
        self.attachment_list = attachment_list
        self.password = password
        self.user_list = ','.join(user_list) # 多个收件人
        self.part_text = part_text
        self.smtp_server = smtp_server
        self.from_user = from_user
        self.filename = filename

    def _part(self):
        '''构建邮件内容'''
        # 1) 构造邮件集合体：
        msg = MIMEMultipart()
        msg['Subject'] = self.subject
        msg['From'] = self.from_user
        msg['To'] = self.user_list

        # 2) 构造邮件正文：
        text = MIMEText(self.part_text)
        msg.attach(text) # 把正文加到邮件体里面

        # 3) 构造邮件附件：
        for item in self.attachment_list:
            with open(item, 'rb+') as file:
                attachment =MIMEApplication(file.read())
            # 给附件命名
            attachment.add_header('Content-Disposition', 'attachment', filename=item)
            msg.attach(attachment)

        # 4) 得到完整的邮件内容：
        full_text = msg.as_string()
        return full_text

    def send_email(self):
        '''发送邮件'''
        # qq邮箱必须加上SSL
        if self.smtp_server == 'smtp.qq.com':
            smtp = smtplib.SMTP_SSL(self.smtp_server)
        else:
            smtp = smtplib.SMTP(self.smtp_server)
        # 登录服务器：.login(user=email_address,password=第三方授权码)
        smtp.login(self.from_user, self.password)
        logger.info('------邮件发送中------')
        try:
            logger.info('------邮件发送成功------')
            smtp.sendmail(self.from_user, self.user_list, self._part())
        except Exception as e:
            logger.error('发送邮件出错，错误信息为：{0}'.format(e))
        else:
            smtp.close()#关闭连接

if __name__ == '__main__':
    from base.base_path import *
    part_text = '附件为自动化测试报告,框架使用了pytest+allure'
    attachment_list = [report_path]
    password = ''
    user_list = ['']
    HandleSendEmail(part_text, attachment_list, password, user_list).send_email()