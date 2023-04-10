# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2023/4/10 10:39
# @Author : waxberry
# @File : 随机点名.py
# @Software : PyCharm

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from qdarkstyle import load_stylesheet_pyqt5

import os
import sys
import time
import random


def pyqtSingal(str):
    pass


class WorkThread(QThread):
    trigger = pyqtSingal(str)
    finished = pyqtSignal(bool)

    def __init__(self, parent=None):
        super(WorkThread, self).__init__(parent)
        self.parent = parent
        self.working = True

    def __del__(self):
        self.working = False
        self.wait()

    def run(self):
        data_list = self.parent.data_list
        if len(data_list) >= 1:
            ran = random.randint(6, 10)
            print ('遍历次数：', ran)
            for a in range(ran):
                name = random.choice(data_list)
                self.trigger.emit(name)
                print (name)
                time.sleep(0.6)
            self.finished.emit(True)
        else:
            self.trigger.emit('无数据')


class Qlabel:
    pass


class ClassCollSystem(QWidget):
    def __init__(self):
        super(ClassCollSystem, self).__init__()
        self.data_list = []
        self.init_ui()
    # 子线程调用
    def init_ui(self):
        self.thread_ = WorkThread(self)
        self.thread_.trigger.connect(self.set_name)
        self.thread_.finished.connect(self.finished)
        # 应用初始化信息
        self.setWindowTitle('课堂点名系统')
        self.setWindowIcon(QIcon('课堂点名.ico'))
        self.setFixedSize(500, 350)
        # 姓名信息布局
        vbox_name = QVBoxLayout()
        self.current_name = Qlabel()
        self.current_name.setText('随机点名啦')
        self.current_name.setStyleSheet('font-size:50px;text-align:center;font-weight:bold;font-family:"Microsoft JhengHei";')
        vbox_name.addWidget(self.current_name)
        vbox_name.setAlignment(Qt.AlignCenter)
        # 开始信息布局
        vbox_start = QVBoxLayout()
        self.start_btn = QPushButton('')
        self.start_btn.setText('开始点名')
        self.start_btn.setFixedSize(160, 50)
        self.start_btn.setStyleSheet('font-size:30px;font-weight:bold;text-align:center;font-family:"Microsoft JhengHei";')
        self.start_btn.clicked.connect(self.start_btn_click)

        vbox_start.addWidget(self.start_btn)
        vbox_start.setAlignment(Qt.AlignCenter)
        vbox_start.addSpacing(80)

        # 数据信息布局
        vbox_data = QHBoxLayout()
        self.message = QLabel('')
        self.message.setText('信息提示')
        self.message.setStyleSheet('font-size:12px;')
        self.import_btn = QPushButton()
        self.import_btn.setText('导入数据')
        self.import_btn.setFixedSize(90, 25)
        self.import_btn.clicked.connect(self.import_btn_click)

        vbox_data.addWidget(self.message)
        vbox_data.addStretch(1)
        vbox_data.addWidget(self.import_btn)

        # 整体布局
        vbox = QVBoxLayout()
        vbox.addLayout(vbox_name)
        vbox.addLayout(vbox_start)
        vbox.addLayout(vbox_data)

        self.setLayout(vbox)

    def start_btn_click(self):
        if self.start_btn.text().strip() == '开始点名':
            self.thread_.start()
        else:
            self.start_btn.setText('开始点名')

    def set_name(self, name):
        self.current_name.setText(name)

    def finished(self, finished):
        if finished is True:
            self.start_btn.setText('就是你了')

    def import_btn_click(self):
        file = QFileDialog.getSaveFileName(self, '选择文件', os.getcwd(), 'Text Files(*.txt)')
        file_path = file[0]
        print (file_path)
        f1 = open(str(file_path), 'r', encoding='utf-8')
        self.data_list = f1.read().strip().split('\n')
        print (self.data_list)
        self.message.setText('信息提示|成功导入[' + str(len(self.data_list)) + ']条人员信息')

# 运行
if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(load_stylesheet_pyqt5())
    main = ClassCollSystem()
    main.show()
    sys.exit(app.exec_())