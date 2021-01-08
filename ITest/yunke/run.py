#coding:utf-8

import unittest
import HTMLTestReportCN
import shutil
import time


if __name__ == '__main__':

    # suite = unittest.TestSuite()
    # suite.addTest(text.TestApi('test_StudentCenter'))
    # suite.addTest(text.TestApi('test_MyCourseList'))
    # suite.addTest(text.TestApi('test_MyCourseTable'))
    # unittest.TextTestRunner().run(suite)

    suite = unittest.defaultTestLoader.discover(start_dir='./miniGroup/', pattern='minigroup.py')
    path = './report/' + time.strftime('%Y-%m-%d_%H_%M_%S', time.localtime(time.time())) + '.html'
    fm = open(path, 'wb')
    HTMLTestReportCN.HTMLTestRunner(stream=fm, tester='wxy', title='云课接口', verbosity='2').run(suite)
    shutil.copyfile(path, './report.html')