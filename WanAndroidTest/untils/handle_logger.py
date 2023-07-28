# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2023/7/26 11:31
# @Author : waxberry
# @File : handle_logger.py
# @Software : PyCharm

import sys
import logging
from time import strftime
from base.base_path import *

class Logger:
    def __init__(self):
        # 日志格式
        custom_format = "%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s: %(message)s"
        # 日期格式
        date_format = "%a, %d %b %Y %H:%M:%S"

        self.logger = logging.getLogger() #实例化
        self.filename = '{0}-{1}.log'.format(log_path, strftime('%Y-%m-%d'))# 日志文件名
        self.formatter = logging.Formatter(fmt=custom_format, datefmt=date_format)
        self._logger.addHandler(self._get_file_handler(self.filename))
        self._logger.addHandler(self._get_console_handler())
        self._logger.setLevel(logging.INFO) #默认等级

    def _get_file_handler(self, filename):
        '''输出到日志文件'''
        filehandler = logging.FileHandler(filename, encoding='utf-8')
        filehandler.setFormatter(self.formatter)
        return filehandler

    def _get_console_handler(self):
        '''输出到控制台'''
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(self.formatter)
        return console_handler

    @property
    def logger(self):
        return self._logger

'''
日志级别：
critical    严重错误，会导致程序退出
error        可控范围内的错误
warning        警告信息
info        提示信息
debug        调试程序时详细输出的记录
'''
# 实例
logger = Logger().logger


if __name__ == '__main__':
    import datetime
    logger.info(u'{}:开始xxx操作'.format(datetime.datetime.now()))
