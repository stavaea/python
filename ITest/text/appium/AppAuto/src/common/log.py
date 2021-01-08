#coding:utf-8

import os, logging, time

class WriteLog(object):
    '''记录日志工具类'''

    def __init__(self, logger_name=''):
        self.logger_name = logger_name
        self.runtime_path = ''.join([log_dir, 'Runtime.log'])
        self.error_path = ''.join([log_dir, 'Error.log'])
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

    def add_logger(self):
        '''创建一个logging'''
        logger = logging.getLogger(self.logger_name)
        logger.setLevel(logging.INFO)
        if not logger.handlers:
            # 创建一个hander，用于写入日志
            fh = logging.FileHandler(self.runtime_path)
            fh.setLevel(logging.INFO)
            fh1 = logging.FileHandler(self.error_path)
            fh1.setLevel(logging.INFO)
            # create formatter
            fmt = '%(asctime)s [%(name)s-%(levelname)s]: %(message)s'
            datefmt = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            formatter = logging.Formatter(fmt, datefmt)
            fh.setFormatter(formatter)
            fh1.setFormatter(formatter)
            # 给logger添加hander
            logger.addHandler(fh)
            logger.addHandler(fh1)
        return logger