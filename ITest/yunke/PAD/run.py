#coding:utf-8

import unittest
import HTMLTestRunnerCN
import shutil
import time


if __name__ == '__main__':

    suite = unittest.defaultTestLoader.discover(start_dir='G:\python\ITest\yunke\PAD\cases', pattern='padApi.py')
    path = './report/' + time.strftime('%Y-%m-%d_%H_%M_%S', time.localtime(time.time())) + '.html'
    fm = open(path, 'wb')
    HTMLTestRunnerCN.HTMLTestRunner(stream=fm, tester='wxy', title='PAD接口', verbosity='2').run(suite)
    shutil.copyfile(path, './report.html')