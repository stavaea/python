#coding:utf-8
import unittest
import HTMLTestRunnerCN
import shutil
import time


# from cases import eventdetail01, eventdetail02, login01, login02
#
# suite = unittest.TestSuite
# suite.addTest(eventdetail01.Test('test_eventdetail01'))
# suite.addTest(eventdetail02.Test('test_eventdetail02'))
# suite.addTest(login01.Test('test_login01'))
# suite.addTest(login02.Test('test_login02'))
# unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    suite = unittest.defaultTestLoader.discover(start_dir='./cases/', pattern='*.py')
    # unittest.TextTestRunner().run(suite)
    path = './report/' + time.strftime('%Y-%m-%d_%H_%M_%S', time.localtime(time.time())) + '.html'
    fm = open(path, 'wb')
    HTMLTestRunnerCN.HTMLTestRunner(stream=fm, tester='wxy', title=u'慧测接口项目测试', verbosity=2).run(suite)
    shutil.copyfile(path, './report.html')
    # shutil.copyfile(path, './report/report.html')
