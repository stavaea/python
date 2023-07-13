# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2023/7/6 11:32
# @Author : waxberry
# @File : main.py
# @Software : PyCharm
import os

from PySide2.QtCore import QStringListModel
from png import Image

from gif import Ui_Form
'''
带有文字“选择图片”和“生成gif”的组件是两个 QPushButton
“选择图片”按钮下方的是一个 QListVIew 组件
再往下的三段文字是 QLabel 组件，后面分别对应的 QLineEdit 组件
“生成gif”按钮下方的也是两个 QLabel 组件，分别用来预览图片和作者声明
完成布局之后，保存当前配置，例如保存为“gif.ui”
pip install PySide2
安装完成之后，直接在 cmd 命令行输入pyside2-uic -o gif.py gif.ui，就可以把刚刚生成的 ui 文件转化为 py 代码
'''
from PySide2.QtWidgets import QMainWindow, QApplication, QFileDialog


class QMoive:
    pass


class CreateGif(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setup()
        self.show()

    # 设置setup函数，给对应的组件设置初始值
    def setup(self):
        self.imgs = None
        self.gifImgName = None
        self.lineEdit.setText('0')
        self.lineEdit_2.setText('0')
        self.lineEdit_3.setText('500')
    # 编写选择图片的函数
    def choose_img(self):
        self.imgs = QFileDialog.getOpenFileNames(
            caption='选择图片', filter=''
        )[0]
        if self.imgs:
            imgwidth, imgheight = Image.open(self.imgs[0]).size
            self.lineEdit.setText(str(imgwidth))
            self.lineEdit_2.setText(str(imgheight))
            new_imgs = []
            for img in self.imgs:
                img_name = os.path.basename(img)
                new_imgs.append(img_name)
            strings = QStringListModel(new_imgs)
            self.listView.setModel(strings)


    # 生成gif的函数
    def gen_gif(self):
        frames = []
        imgwidth = int(self.lineEdit.text())
        imgherght = int(self.lineEdit_2.text())
        imgspeed = int(self.lineEdit_3.text())
        for img in self.imgs:
            img = Image.open(img).resize((imgwidth, imgherght)).convert('RGBA')
            frames.append(img)
        self.gifImgName = os.path.splitext(os.path.basename(self.imgs[0]))[0]
        frames[0].save(f'{self.gifImgName}.gif', append_images=frames[1:], loop=0, save_all=True, duration=imgspeed)
        self.displayGif()

    # 展示生成gif
    def displayGif(self):
        self.movie = QMoive()
        self.movie.setFileName(f'{self.gifImgName}.gif')
        self.label.setMovie(self.movie)
        self.movie.start()
