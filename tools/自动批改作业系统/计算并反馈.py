#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2024/5/23 14:44
@Author  : waxberry
@File    : 计算并反馈.py
@Software: PyCharm
"""

# 计算数值并返回结果  参数chars：['8', '-', '6', '=']
def calculation(chars):
    cstr = ''.join(chars)
    result = ''
    if("=" in cstr): # 有等号
        str_arr = cstr.split('=')
        c_str = str_arr[0]
        r_str = str_arr[1]
        c_str = c_str.replace("×","*")
        c_str = c_str.replace("÷","/")
        try:
            c_r = int(eval(c_str))
        except Exception as e:
            print("Exception",e)

        if r_str == "":
            result = c_r
        else:
            if str(c_r) == str(r_str):
                result = "√"
            else:
                result = "×"

    return result



# 反馈
# 绘制文本
def cv2ImgAddText(img, text, left, top, textColor=(255, 0, 0), textSize=20):
    if (isinstance(img, np.ndarray)):  # 判断是否OpenCV图片类型
        img = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    # 创建一个可以在给定图像上绘图的对象
    draw = ImageDraw.Draw(img)
    # 字体的格式
    fontStyle = ImageFont.truetype("fonts/fangzheng_shusong.ttf", textSize, encoding="utf-8")
    # 绘制文本
    draw.text((left, top), text, textColor, font=fontStyle)
    # 转换回OpenCV格式
    return cv2.cvtColor(np.asarray(img), cv2.COLOR_RGB2BGR)


# 获取切图标注，切图图片，原图图图片
all_mark_boxs,all_char_imgs,img_o = divImg(path,save)
# 恢复模型，用于图片识别
model = cnn.create_model()
model.load_weights('checkpoint/char_checkpoint')
class_name = np.load('class_name.npy')

# 遍历行
for i in range(0,len(all_char_imgs)):
    row_imgs = all_char_imgs[i]
    # 遍历块
    for j in range(0,len(row_imgs)):
        block_imgs = row_imgs[j]
        block_imgs = np.array(block_imgs)
        # 图片识别
        results = cnn.predict(model, block_imgs, class_name)
        print('recognize result:',results)
        # 计算结果
        result = calculation(results)
        print('calculate result:',result)
        # 获取块的标注坐标
        block_mark = all_mark_boxs[i][j]
        # 获取结果的坐标，写在块的最后一个字
        answer_box = block_mark[-1]
        # 计算最后一个字的位置
        x = answer_box[2]
        y = answer_box[3]
        iw = answer_box[2] - answer_box[0]
        ih = answer_box[3] - answer_box[1]
        # 计算字体大小
        textSize =  max(iw,ih)
        # 根据结果设置字体颜色
        if str(result) == "√":
            color = (0, 255, 0)
        elif str(result) == "×":
            color = (255, 0, 0)
        else:
            color = (192, 192,192)
        # 将结果写到原图上
        img_o = cv2ImgAddText(img_o, str(result), answer_box[2],  answer_box[1],color, textSize)
# 将写满结果的原图保存
cv2.imwrite('result.jpg', img_o)