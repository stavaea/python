#coding:utf-8
from Tools.Scripts.findnocoding import args
from lanucher import Custom_lanucher
from Method import Method
import unittest
from airtest.core.api import *
from airtest.cli.runner import AirtestCase, run_script
from airtest.cli.parser import runner_parser


def devives(args):
    pass


class TestCaseDemo(unittest.TestCase):
    def setUp(self):
        auto_setup(args.script, devives, args.log, project_root)

    def test_01_register(self):
        self.exec_other_script('test_01register.air')

    def test_02_name(self):
        self.exec_other_script('login.air')
        self.exec_other_script('test_02add.air')

    def tearDown(self):
        Method.tearDown(self)

if __name__ == '__main__':
    unittest.main