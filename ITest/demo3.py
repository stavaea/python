#coding:utf-8
import unittest
# from cases import eventdetail01, eventdetail02, login01, login02
#
# suite = unittest.TestSuite
# suite.addTest(eventdetail01.Test('test_eventdetail01'))
# suite.addTest(eventdetail02.Test('test_eventdetail02'))
# suite.addTest(login01.Test('test_login01'))
# suite.addTest(login02.Test('test_login02'))
# unittest.TextTestRunner().run(suite)

suite = unittest.defaultTestLoader.discover(start_dir='./cases/', pattern='*.py')
unittest.TextTestRunner.run(suite)