# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2023/6/8 17:39
# @Author : waxberry
# @File : 花式照片墙.py
# @Software : PyCharm

import binascii
import os
from PIL import Image
import random
import numpy as np

KEYS = [0x80, 0x40, 0x20, 0x10, 0x08, 0x04, 0x02, 0x01]

'''
获取多个汉字点阵字
'''

def get_multiple_word_img(textStr):
    # 初始化16*16的点阵位置，每个汉字需要16*16=256个点来表示，需要32个字节才能显示一个汉字
    # 之所以32字节：256个点每个点是0或1，那么总共就是2的256次方，一个字节是2的8次方
    rect_list = [] * 16
    for i in range(16):
        rect_list.append([] * 16)

    for text in textStr:
        # 获取中文的gb2312编码，一个汉字是由2个字节编码组成
        gb2312 = text.encode('gb2312')
        # 将二进制编码数据转化为十六进制数据
        hex_str = binascii.b2a_hex(gb2312)
        # 将数据按unicode转化为字符串
        result = str(hex_str, encoding='utf-8')

        # 前两位对应汉字的第一个字节：区码，每一区记录94个字符
        area = eval('0x' + result[:2]) - 0xA0
        # 后两位对应汉字的第二个字节：位码，是汉字在其区的位置
        index = eval('0x' + result[2:]) - 0xA0
        # 汉字在HZK16中的绝对偏移位置，最后乘32是因为字库中的每个汉字字模都需要32字节
        offset = (94 * (area - 1) + (index - 1)) * 32

        font_rect = None

        # 读取HZK16汉字库文件
        with open(r'D:\360极速浏览器下载\字库\16x16\hzk16H', 'rb') as f:
            # 找到目标汉字的偏移位置
            f.seek(offset)
            # 从该字模数据中读取32字节数据
            font_rect = f.read(32)

        # font_rect的长度是32，此处相当于for k in range(16)
        for k in range(len(font_rect) // 2):
            # 每行数据
            row_list = rect_list[k]
            for j in range(2):
                for i in range(8):
                    asc = font_rect[k * 2 + j]
                    # 此处&为Python中的按位与运算符
                    flag = asc & KEYS[i]
                    # 数据规则获取字模中数据添加到16行每行中16个位置处每个位置
                    row_list.append(flag)

    # 根据获取到的16*16点阵信息，打印到控制台
    for row in rect_list:
        for i in row:
            if i:
                print('o', end=' ')
            else:
                print('.', end=' ')
        print()
    print('{}'.format(rect_list))
    # 返回值为点阵二维列表
    return rect_list

get_multiple_word_img('爱')




from PIL import Image
import os

'''
根据指定的frame_name 获取photo_wall_FRAME
# 定义绘制图形的框架，1表示不填充，0表示用头像填充
'''
def get_photo_wall_FRAME(frame_name):
    FRAME_DIC = {}
    # Heart frame 21*17,Heart形状共128个0
    HEART_FRAME = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1]]
    FRAME_DIC["HEART_FRAME"] = HEART_FRAME

    # FRAME_DIC["LOVE_FRAME"]=LOVE_FRAME

    return FRAME_DIC[frame_name]


'''
生成照片墙
'''
def generate_photo_wall(FRAME, img_path, photo_folder_name):
    # 导入照片
    # 需要拼接的照片文件夹完整路径
    photo_folder = r'{}\{}'.format(img_path, photo_folder_name)
    # 将以.jpg的图片放置于新键的列表中，为后续生成照片墙使用，目的是过滤掉非图片格式的文件
    pic_list = [] #存放图片位置
    for i in os.listdir(photo_folder):
        print(i)
        if i.endswith('.jpg') or i.endswith('.png') or i.endswith('.webp'):
            pic_list.append(i)
    total_photo = len(pic_list)
    print('文件夹中共有{}张照片'.format(total_photo))
    print('正在创建照片墙')

    # 设置图片的尺寸,所有图片尺寸要保持统一
    img_h = img_w = 192
    # 计算行数,即子列表的个数
    rows = len(FRAME)
    # 计算列数,即子列表中元素的个数
    columns = len(FRAME[0])

    # 画图
    # 使用Image.new()方法创建一个画布，一个白色图片
    # 第一个参数RGB
    # 第二个参数需要传入一个元组，元组的第一个参数是画布的宽，第二个是高
    # 第三个参数传入的是画布的颜色
    figure = Image.new('RGB', (img_w*columns, img_h*rows), 'white')

    # 将图片放在画布对应的位置，即数组中元素为0的位置

    # 表示图片的下标
    count = 0
    # 遍历行
    for i in range(len(FRAME)):
        # 遍历每行中的所有元素
        for j in range(len(FRAME[i])):
            # 如果元素是1,就不管
            if FRAME[i][j] == 1:
                continue
            # 如果元素不是1,放图上去
            else:
                # 做个异常处理，防止有些图片打开失败，导致程序中断
                try:
                    # 当照片数量不够时，循环使用已用过的照片，added by yimi on 20220521
                    if count == total_photo:
                        count = 0
                    # 使用Image.open("图片路径")方法获取图片对象
                    image = Image.open(os.path.join(photo_folder, pic_list[count]))
                except:
                    continue
                # resize((新的宽，新的高))用来改变图片的尺寸,接收一个元组
                image = image.resize((img_w, img_h))
                # 将修改尺寸后的图片(image)粘贴(paste)到画布(figure)上
                # 第一个参数 是图片对象
                # 第二个参数是 图片在画布上的位置，相当于单元格的位置
                figure.paste(image, (img_w*j, img_h*i))
                # 使用完一张图片就要记录下来，并开始使用下一张图片
                count += 1
    # 当循环结束，即表示照片墙图片已经完成
    # 将画好的画布显示出来
    figure.show()
    # 需要告知程序图片保存的路径
    figure.save(r'{}\{}_photo_wall1.png'.format(img_path, photo_folder_name), format="png")

    print('照片墙创建成功！')

# 程序入口
if __name__ == '__main__':
    # 图片存放的路径(当前项目是所有图片统一放在了程序所在的文件夹路径下方了，运用代码时可以改成自己照片存放的路径即可。)
    img_path = r'Photo\img'

    # 存放很多张照片集合的文件夹名称，将路径和文件夹名称分开保存在变量中是为了后续生成照片墙照片要用文件夹的名称
    photo_folder_name = 'baby'

    # 照片墙框架类型:"LOVE_FRAME","HEART_FRAME"
    frame_name = "HEART_FRAME"

    # 获取指定的照片墙框架
    FRAME = get_photo_wall_FRAME(frame_name)

    # 生成照片墙
    generate_photo_wall(FRAME, 'C:/drf2/drf2/图片', photo_folder_name)