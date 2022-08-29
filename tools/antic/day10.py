# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2022/8/29 10:17
# @Author : waxberry
# @File : day10.py
# @Software : PyCharm

from moviepy.editor import AudioFileClip

my_audio_clip = AudioFileClip('视频路径')
my_audio_clip.write_audiofile('写入音频')
