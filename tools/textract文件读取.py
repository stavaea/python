# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2024/2/6 17:10
# @Author : waxberry
# @File : textract文件读取.py
# @Software : PyCharm



# 使用textract从一个Word文档中提取文本信息：
import textract

# 提取文本
text = textract.process('document.docx')
# 打印文本
print(text.decode('utf-8'))




# 使用textract从一个PDF文件中提取图片：
import textract

# 提取图片
images = textract.process('document.pdf', method='tesseract', encoding='utf-8', pages='1-3')
# 保存图片
for i, image in enumerate(images):
    with open(f'image_{i}.png', 'wb') as f:
        f.write(image)




# 使用textract从一个PDF文件中提取特定区域的文本：
import textract

# 提取特定区域的文本
text = textract.process('document.pdf', method='pdfminer', encoding='utf-8', pages='1', area=(100, 100, 200, 200))
# 打印文本
print(text.decode('utf-8'))