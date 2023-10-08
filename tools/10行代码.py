# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2023/8/24 10:55
# @Author : waxberry
# @File : 10行代码.py
# @Software : PyCharm

# 百度飞桨


# 一、生成二维码
# pip install qrcode
import qrcode

text = input('输入文字或URL：')
# 设置URL必须添加http://
img =qrcode.make(text)
img.save()
#保存图片至本地目录，可以设定路径
img.show()
import myqr
# pip install  myqr
def gakki_code():
    version, level, qr_name = myqr.run(
        words='https://520mg.com/it/#/main/2',
        # 可以是字符串，也可以是网址(前面要加http(s)://)
        version=1,  # 设置容错率为最高
        level='H',
        # 控制纠错水平，范围是L、M、Q、H，从左到右依次升高
        picture='gakki.gif',
        # 将二维码和图片合成
        colorized=True,  # 彩色二维码
        contrast=1.0,
        # 用以调节图片的对比度，1.0 表示原始图片，更小的值表示更低对比度，更大反之。默认为1.0
        brightness=1.0,
        # 用来调节图片的亮度，其余用法和取值同上
        save_name=gakki_code.gif,
        # 保存文件的名字，格式可以是jpg,png,bmp,gif
        save_dir=os.getcwd()  # 控制位置

    )
gakki_code()

# 二、生成词云
# pip install wordcloud
# pip install jieba
# pip install matplotlib
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import jieba

text_from_file_with_apath = open('/Users/hecom/23tips.txt').read()

wordlist_after_jieba = jieba.cut(text_from_file_with_apath, cut_all = True)
wl_space_split =  .join(wordlist_after_jieba)

my_wordcloud = WordCloud().generate(wl_space_split)

plt.imshow(my_wordcloud)
plt.axis(off)
plt.show()

# 三、批量抠图
'''我们需要安装两个模块就可以很快的实现批量抠图了，第一个是PaddlePaddle：
python -m pip install paddlepaddle -i https://mirror.baidu.com/pypi/simple
还有一个是paddlehub模型库：
pip install -i https://mirror.baidu.com/pypi/simple paddlehub'''
# 接下来我们只需要5行代码就能实现批量抠图：
import os, paddlehub as hub
humanseg = hub.Module(name='deeplabv3p_xception65_humanseg')        # 加载模型
path = 'D:/CodeField/Workplace/PythonWorkplace/GrapImage/'    # 文件目录
files = [path + i for i in os.listdir(path)]    # 获取文件列表
results = humanseg.segmentation(data={'image':files})    # 抠图

# 四、文字情绪识别
import paddlehub as hub
senta = hub.Module(name='senta_lstm')        # 加载模型
sentence = [    # 准备要识别的语句
    '你真美', '你真丑', '我好难过', '我不开心', '这个游戏好好玩', '什么垃圾游戏',
]
results = senta.sentiment_classify(data={text:sentence})    # 情绪识别
# 输出识别结果
for result in results:
    print(result)

# 五、识别是否带了口罩
import paddlehub as hub
# 加载模型
module = hub.Module(name='pyramidbox_lite_mobile_mask')
# 图片列表
image_list = ['face.jpg']
# 获取图片字典
input_dict = {'image':image_list}
# 检测是否带了口罩
module.face_detection(data=input_dict)

# 六、简易信息轰炸
# pip install -i https://pypi.tuna.tsinghua.edu.cn/simple/ pynput
# 在写代码之前我们需要手动获取输入框的坐标：
from pynput import mouse
# 创建一个鼠标
m_mouse = mouse.Controller()
# 输出鼠标位置
print(m_mouse.position)
# 获取后我们就可以记录这个坐标，消息窗口不要移动。然后我们执行下列代码并将窗口切换至消息页面：
import time
from pynput import mouse, keyboard
time.sleep(5)
m_mouse = mouse.Controller()    # 创建一个鼠标
m_keyboard = keyboard.Controller()  # 创建一个键盘
m_mouse.position = (850, 670)       # 将鼠标移动到指定位置
m_mouse.click(mouse.Button.left) # 点击鼠标左键
while(True):
    m_keyboard.type('你好')        # 打字
    m_keyboard.press(keyboard.Key.enter)    # 按下enter
    m_keyboard.release(keyboard.Key.enter)    # 松开enter
    time.sleep(0.5)    # 等待 0.5秒

# 七、识别图片中的文字
import pytesseract
from PIL import Image
img = Image.open('text.jpg')
text = pytesseract.image_to_string(img)
print(text)

# 八、简单的小游戏
import random
print('1-100数字猜谜游戏！')
num = random.randint(1,100)
guess =guess

i = 0
while guess != num:
    i += 1
    guess = int(input('请输入你猜的数字：'))

    if guess == num:
        print('恭喜，你猜对了！')
    elif guess < num:
        print('你猜的数小了...')
    else:
        print('你猜的数大了...')

print('你总共猜了%d %i + 次')





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