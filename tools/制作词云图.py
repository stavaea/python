# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2024/1/17 14:53
# @Author : waxberry
# @File : 制作词云图.py
# @Software : PyCharm



# 导入模块
from wordcloud import WordCloud
# 准备文本数据，是一个字符串，单词之间用空格分隔
sentence = "hello satori hello mashiro hello satori"
# 创建词云对象
wc = WordCloud()
# 根据文本生成词云
wc.generate(sentence)
# 保存为图片
wc.to_file("word.png")




from wordcloud import WordCloud
sentence = "i do not need sex, because life fucks me every every single day"
wc = WordCloud(
    width=500,  # 设置宽度为500px
    height=300,  # 设置高度为300px
    background_color='pink',  # 设置背景为粉色
    stopwords={"sex", "fucks"},  # 设置禁用词
    max_font_size=100,  # 设置最大的字体大小，所有词都不会超过 100px
    min_font_size=10,  # 设置最小的字体大小，所有词都会超过 10px
    max_words=10  # 最多生成 10 个词，当然这里单词比较少，看不出来什么
)

wc.generate(sentence)
wc.to_file("word.png")




from wordcloud import WordCloud
from PIL import Image
import numpy as np

# 一篇英文文章
with open("article.txt") as f:
    sentence = f.read()
# 加载一张图片，转化成numpy中的数组
mask = np.array(Image.open("哆啦A梦.png"))
# 传入mask
wc = WordCloud(mask=mask)
wc.generate(sentence)
wc.to_file("word.png")



# 中文
from wordcloud import WordCloud
wc = WordCloud()
wc.generate("古明地觉的编程教室")
wc.to_file("word.png")

from wordcloud import WordCloud
# 传入本机支持中文的字体名称
wc = WordCloud(font_path="Arial Unicode.ttf")
wc.generate("古明地觉的编程教室")
wc.to_file("word.png")


# 使用 jieba 分词，将单词进行分隔。
from wordcloud import WordCloud
import jieba
with open("出师表.txt") as f:
    sentence = f.read()
# 分词得到列表，手动使用空格拼接
sentence = " ".join(jieba.cut(sentence))
wc = WordCloud(font_path="Arial Unicode.ttf")
wc.generate(sentence)
wc.to_file("word.png")



# 将词云保存成除图片其它格式。
from io import BytesIO
from wordcloud import WordCloud
import jieba

with open("出师表.txt") as f:
    sentence = f.read()

sentence = " ".join(jieba.cut(sentence))
wc = WordCloud(font_path="Arial Unicode.ttf")
wc.generate(sentence)

# 将词云保存为 PIL 的 Image 对象
im = wc.to_image()
buf = BytesIO()
# 将词云的字节流保存在 buf 中，这样可以直接交给客户端进行渲染
im.save(buf, "png")
print(buf.getvalue())

# 当然也可以保存为文件，im.save(filename)
# wc.to_file() 底层也是先转成 Image 对象、然后调用 im.save() 实现的

# 或者还可以保存为 SVG 格式
svg = wc.to_svg()
# 将 svg 的内容保存成文件，就得到 SVG 图片了
print(svg)