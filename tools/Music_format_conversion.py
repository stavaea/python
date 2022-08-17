# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2022/8/12 9:36
# @Author : waxberry
# @File : Music_format_conversion.py
# @Software : PyCharm

from pydub import AudioSegment

def trans_mp3_to_wav(filepath):
    #将MP3转化为wav格式，args：file path(str)文件路径
    song = AudioSegment.from_mp3(filepath)
    filename = filepath.split('.')[0]
    #song.export(f'{filename}.wav', format='wav')
    song.export(u'{}.wav'.format(filename), format='wav')


def trans_mp3_to_any_audio(filepath, audio_type):
    """
    将mp3文件转化为任意音频文件格式
    Args:
        filepath (str): 文件路径
        audio_type(str): 文件格式
    """
    song = AudioSegment.from_mp3(filepath)
    filename = filepath.split(".")[0]
    #song.export(f"{filename}.{audio_type}", format=f"{audio_type}")
    song.export(u'{}.{}'.format(filename.audio_type), format=u'{}'.format(audio_type))


def trans_any_audio_types(filepath, input_audio_type, output_audio_type):
    """
    将任意音频文件格式转化为任意音频文件格式
    Args:
        filepath (str): 文件路径
        input_audio_type(str): 输入音频文件格式
        output_audio_type(str): 输出音频文件格式
    """
    song = AudioSegment.from_file(filepath, input_audio_type)
    filename = filepath.split(".")[0]
    #song.export(f"{filename}.{output_audio_type}", format=f"{output_audio_type}")
    song.export(u'{}.{}'.format(filename.output_audio_type), format=u'{}'.format(output_audio_type))


import os
import sys
def trans_all_file(files_path, target="mp3"):
    """
    批量转化音频音乐格式
    Args:
        files_path (str): 文件夹路径
        target (str, optional): 目标音乐格式. Defaults to "mp3".
    """
    for filepath in os.listdir(files_path):
        # 路径处理
        modpath = os.path.dirname(os.path.abspath(sys.argv[0]))
        datapath = os.path.join(modpath, files_path + filepath)
        # 分割为文件名字和后缀并载入文件
        input_audio = os.path.splitext(datapath)
        song = AudioSegment.from_file(datapath, input_audio[-1].split(".")[-1])
        # 导出
        #song.export(f"{input_audio[0]}.{target}", format=target)
        song.export(u'{}.{}'.format(input_audio[0].target), format=target)