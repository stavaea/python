# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2022/9/13 10:55
# @Author : waxberry
# @File : Animation_image_converter.py
# @Software : PyCharm
import cv2
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import os
import logger
import sys

class CartoonUI(QWidget):
    def __init__(self):
        '''初始化ui界面应用'''
        super(CartoonUI, self).__init__()
        self.init_ui()

    def init_ui(self):
        '''自定义实现的ui应用函数
        :return :
        '''
        self.setWindowTitle('动漫图片转换器  公众号：xx')
        self.setWindowIcon(QIcon('ico.png'))
        self.setFixedWidth(500)

        hbox = QHBoxLayout()
        self.input_image_path = QLineEdit()
        self.input_image_path.setPlaceholderText('源图片路径')
        self.input_image_path.setReadOnly(True)

        self.input_image_btn = QPushButton('')
        self.input_image_btn.setText('导入源图片')
        self.input_image_btn.clicked.connect(self.input_image_btn_click)

        self.generate_btn = QPushButton()
        self.generate_btn.setText('一键生成动漫图片')
        self.generate_btn.clicked.connect(self.generate_btn_click)

        hbox.addWidget(self.input_image_path)
        hbox.addWidget(self.input_image_btn)
        hbox.addWidget(self.generate_btn)

        self.thread_ = WorkThread(self)
        self.thread_.finished.connect(self.finished)

        self.setLayout(hbox)

    def input_image_btn_click(self):
        '''
        input_image_btn按钮绑定的槽函数，用于实现打开文件浏览项
        :return:
        '''
        im_path = QFileDialog.getOpenFileName(self, os.getcwd(), '打开图片',
                                              'Image File(*.jpg);;Image File(*.png);;Image File(*.jpeg)')
        self.input_image_path.setText(im_path[0])

    def generate_btn_click(self):
        '''
        generate_btn按钮绑定的槽函数，用于启动业务子线程
        :return:
        '''
        self.thread_.start()
        self.generate_btn.serEnabled(False)

    def finished(self, finished):
        '''
        接收子线程中finished变量，判断子线程业务是否执行完成，若执行完成则将按钮状态改变为可点击状态
        :param finished:
        :return:
        '''
        if finished is True:
            self.generate_btn.serEnabled(True)


class WorkThread(QThread):
    finished = pyqtSignal(bool)

    def __init__(self, parent=None):
        '''
        子线程初始化函数
        :param parent:
        '''
        super(WorkThread, self).__init__(parent)
        self.parent = parent
        self.working = True

    def __del__(self):
        '''
        子线程停止函数
        :return:
        '''
        self.working = False
        self.wait()

    def run(self):
        '''
        子线程执行函数
        :return:
        '''
        try:
            input_picture_name = os.path.basename(self.parent.input_image_path.text().strip())
            logger.info(input_picture_name)
            output_picture_name = 'cartoon_' + self.input_picture_name
            num_down = 2# 缩减像素采样的数目
            num_bilateral = 7# 定义双边滤波的数目
            img_rgb = cv2.imread(input_picture_name)# 读取图片
            # 用高斯金字塔降低取样
            img_color = img_rgb

            for _ in range(num_down):
                img_color = cv2.pyrDown(img_color)

            # 重复使用小的双边滤波代替一个大的滤波
            for _ in range(num_bilateral):
                img_color = cv2.bilateralFilter(img_color, d=9, sigmaColor=9, sigmaSpace=7)

            # 升采样图片到原始大小
            for _ in range(num_down):
                img_color = cv2.pyrUp(img_color)

            # 转换为灰度并且使其产生中等的模糊
            img_gray = cv2.cvtColor(img_color, cv2.COLOR_RGB2GRAY)
            img_blur = cv2.medianBlur(img_gray, 7)
            # 检测到边缘并且增强其效果
            img_edge = cv2.adaptiveThreshold(img_blur, 255,
                                             cv2.ADAPTIVE_THRESH_MEAN_C,
                                             cv2.THRESH_BINARY,
                                             blockSize=9,
                                             C=2)
            # 转换回彩色图像
            img_edge = cv2.cvtColor(img_edge, cv2.COLOR_GRAY2RGB)
            img_cartoon = cv2.bitwise_and(img_color, img_edge)
            # 保存转换后的图片
            cv2.imwrite(output_picture_name, img_cartoon)

            logger.info("动漫图片转换完成")
            self.finished.emit(True)
        except Exception as e:
            logger.error(e)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = CartoonUI()
    main.show()
    sys.exit(app.exec_())