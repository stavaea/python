# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2023/8/24 10:55
# @Author : waxberry
# @File : 10行代码.py
# @Software : PyCharm

# 百度飞桨

# 批量抠图
import os
import paddlehub as hub
# 加载模型
humanseg = hub.Module(name='deeplabv3p_xception65_humanseg')
path = './heben'# 文件目录
# 获取文件列表
files = [path + i for i in os.listdir(path)]
# 抠图
results = humanseg.segmentation(data={'image': files})
for result in results:
    print(result)


# 自然语言处理
senta = hub.Module(name='senta_lstm')# 加载模型
sentence = [
    # 准备要识别的语句
    '你好漂亮', '你真难看呀', '他好难过', '我不开心', '这是一款什么游戏，真垃圾', '这个游戏太好玩了',
]
results = senta.sentiment_classify(data={'text': sentence}) # 情绪识别
# 输出识别结果
for result in results:
    print(result)


# 人脸识别
module = hub.Module(name='pyramidbox_lite_mobile_mask')# 加载模型
image_list = ['face2.jpg']#图片列表
input_dict = {'image':image_list}# 获取图片字典
module.face_detection(data=input_dict)# 检测是否带了口罩


# 人脸关键点检测
face_landmark = hub.Module(name='face_landmark_localization')
image = 'face.jpg'
result = face_landmark.keypoint_detection(images=[cv2.imread(image)], visualization=True)
print(result)





# OpenCV

import cv2
# 猫脸识别
'''到安装目录下提取锚链识别 XML 分类器，具体目录如下C:\Python3\Lib\site-packages\cv2\data,复制 haarcascade_frontalcatface.xml 到自己的项目下即可'''
# 待检测的图片路径
ImagePath = './cat/cat.jpg'

# 读取图片
image = cv2.imread(ImagePath)
# 把图片转换为灰度模式
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 探测图片中的猫脸
# 获取训练好的猫脸的参数数据,进行猫脸检测
face_cascade = cv2.CascadeClassifier(r'./haarcascade_frontalcatface.xml')
faces = face_cascade.detectMultiScale(gray,scaleFactor=1.15,minNeighbors=5,minSize=(3, 3))

search_info = "Find %d face."%len(faces) if len(faces) <= 1 else "Find %d faces."%len(faces)

# 绘制猫脸的矩形区域(红色边框)
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x,y), (x+w,y+h), (0,0,255), 2)

# 显示图片
# cv2.imshow('Find faces!', image)
# cv2.waitKey(0)
cv2.imwrite("./cat/cat2.jpg", image)


# 获取摄像头人脸
detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detector.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    cv2.imshow('frame', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()




# 快速生成动图
import imageio
image_list = ['image/1.jpg','image/2.jpg', 'image/3.jpg', 'image/4.jpg']
gif_name = "dongtu.gif"
duration = 1
frames = []
for image_name in image_list:
    frames.append(imageio.imread(image_name))
imageio.mimsave(gif_name, frames, 'GIF', duration=duration)




# ftp 服务器
'''代码非常简单，直接运行 Python 自带的 http 服务器即可
python -m http.server 8090'''




# 字符画
import PIL.Image
IMG = "3.jpg"
WIDTH = 80
HEIGHT = 40
OUTPUT = "./ascii/ascii.txt"
ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
# 将256灰度映射到70个字符上
def get_char(r, g, b, alpha = 256):
    if alpha == 0:
        return ' '
    length = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.7122 * b)
    unit = (256.0 + 1)/length
    return ascii_char[int(gray/unit)]
im = Image.open(IMG)
im = im.resize((WIDTH, HEIGHT), Image.NEAREST)
txt = ''
for i in range(HEIGHT):
    for j in range(WIDTH):
        txt += get_char(*im.getpixel((i, j)))
    txt += '\n'
print(txt)
#字符画输出到文件
with open(OUTPUT, 'w') as f:
    f.write(txt)