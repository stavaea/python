# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2024/1/17 14:38
# @Author : waxberry
# @File : MoviePy.py
# @Software : PyCharm




# duration属性保存剪辑的时长，如果为None，表示剪辑无限长。可以调用set_duration改变剪辑的时长。
# set_duration调用语法：set_duration(self, t, change_end=True)

if change_end:
 self.end = None if (t is None) else (self.start + t)
else:
 if self.duration is None:
  raise Exception("Cannot change clip start when new"
      "duration is None")
 self.start = self.end - t



 # 让视频向上滚动（在整个时间时长内滚动三次）
 from moviepy.editor import VideoFileClip
 src = VideoFileClip("t.mp4")
 w, h = src.size
 duration = src.duration

 def fl(gf, t):
     frame = gf(t)
     dh = int(h * t * 3 / duration) % h
     return np.vstack((frame[dh:], frame[:dh]))

 newclip = src.fl(fl, apply_to='mask')
 newclip.write_videofile("r.mp4")



 # 视频在前一半时间内从底部恢复到顶部的效果(素材被设置为2秒的时长）：
 from moviepy.editor import VideoFileClip
 src = VideoFileClip("t.mp4")
 w, h = src.size
 duration = 2
 src = src.set_duration(duration)

 def fl(gf, t):
     frame = gf(t).copy()
     frame[:max(0, h - round(h * t * 2 / duration))] = (0, 0, 0)
     return frame

 newclip = src.fl(fl, apply_to='mask')
 newclip.write_videofile("r.mp4")



 # 视频从左下角到右上角滚动的效果。
 def fl(gf, t):
     frame = gf(t).copy()
     frame[:max(0, h - round(h * t * 2 / duration))] = (0, 0, 0)
     frame[:, round(w * t * 2 / duration):w] = (0, 0, 0)
     return frame



 # 右侧蒙版不必重复修改右上角的黑色蒙版区域，那需要限制高度范围，高度变化为起始点h->h, 结束点0->h：
 def fl(gf, t):
     frame = gf(t).copy()
     x = round(w * t * 2 / duration)
     y = round(h * t * 2 / duration)
     frame[:max(0, h - y)] = (0, 0, 0)
     frame[max(0, h - y):h, x:w] = (0, 0, 0)
     return frame


 # fl_time本质是本质是对fl的封装，相对fl的区别在于传入的t_func参数只需要关注时间t。
 # 示例：
 modifiedClip1 = my_clip.fl_time(lambda t: 3 * t)
 modifiedClip2 = my_clip.fl_time(lambda t: 1 + sin(t))



 # spect_ratio属性表示剪辑的宽高比，可以自己通过w / h来计算。
 # 官网自定义make_frame示例：
 import gizeh
 import moviepy.editor as mpy
 def make_frame(t):
     surface = gizeh.Surface(128, 128)  # width, height
     radius = W * (1 + (t * (2 - t)) ** 2) / 6  # the radius varies over time
     circle = gizeh.circle(radius, xy=(64, 64), fill=(1, 0, 0))
     circle.draw(surface)
     return surface.get_npimage()  # returns a 8-bit RGB array

 clip = mpy.VideoClip(make_frame, duration=2)  # 2 seconds
 clip.write_gif("circle.gif", fps=15)


 # write_videofile方法
 # write_videofile方法用于将视频剪辑输出到文件，调用语法如下：
 write_videofile(self, filename, fps=None, codec=None,
                 bitrate=None, audio=True, audio_fps=44100,
                 preset="medium",
                 audio_nbytes=4, audio_codec=None,
                 audio_bitrate=None, audio_bufsize=2000,
                 temp_audiofile=None,
                 rewrite_audio=True, remove_temp=True,
                 write_logfile=False, verbose=True,
                 threads=None, ffmpeg_params=None,
                 logger='bar')



 # write_images_sequence方法
 # write_images_sequence方法用于将剪辑输出到一系列文件中，调用语法如下：
 write_images_sequence(self, nameformat, fps=None, verbose=True, withmask=True, logger='bar')



 # write_gif方法
 # write_gif将剪辑转换成gif动画输出到文件中，调用语法：
 def write_gif(self, filename, fps=None, program='imageio',
               opt='nq', fuzz=1, verbose=True,
               loop=0, dispose=False, colors=None, tempfiles=False,
               logger='bar'):



# subfx实际上是调用基类Clip的fx方法来实现的。例如：
newclip = clip.subfx(vfx.speedx, 3, 6, factor=0.5)#将视频剪辑的3-6秒的位置的剪辑播放速度变成原速度的一半，返回的newclip 总时长比clip 的时长多了3秒



# speedx本身是moviepy.video.fx.speedx下的一个函数，在moviepy.editor中被动态赋予了VideoClip类作为实例方法：
for method in [
          "afx.audio_fadein",
          "afx.audio_fadeout",
          "afx.audio_normalize",
          "afx.volumex",
          "transfx.crossfadein",
          "transfx.crossfadeout",
          "vfx.crop",
          "vfx.fadein",
          "vfx.fadeout",
          "vfx.invert_colors",
          "vfx.loop",
          "vfx.margin",
          "vfx.mask_and",
          "vfx.mask_or",
          "vfx.resize",
          "vfx.rotate",
          "vfx.speedx"
          ]:

    exec("VideoClip.%s = %s" % (method.split('.')[1], method))



# fl_image只变换图像，因此image_func不带时间参数。
# 示例：
def invert_green_blue(image):
    return image[:,:,[0,2,1]]
modifiedClip = my_clip.fl_image( invert_green_blue )




# on_color方法
# 调用语法如下：
on_color(self, size=None, color=(0, 0, 0), pos=None, col_opacity=None)

# 给视频添加一个20px的蓝色透明边框：
clipVideo = VideoFileClip("t.mp4")
h,w = clipVideo.size
newclip = clipVideo.on_color(size=(h+20,w+20),color=(0,0,255),col_opacity=0.6)


# 将一个视频扩展到三倍宽度后分别放置：
threads = 4
clipVideo = VideoFileClip("t.mp4")
w, h = clipVideo.size
bgclip = clipVideo.on_color(
    size=(w*3+40, h+30), color=(0, 0, 255), col_opacity=0.6)
newclip = CompositeVideoClip([bgclip, clipVideo.set_position(('left', 'top')), clipVideo.set_position(
    (w+20, 'center')), clipVideo.set_position((w*2+40, 'bottom'))], bg_color=(255, 0, 0), use_bgclip=True)
newclip.write_videofile("r.mp4", threads=threads)
newclip.close()



# to_ImageClip方法
# to_ImageClip方法将剪辑对应时刻t的帧转换成ImageClip图像剪辑，图像剪辑是所有帧都是固定图像数据的剪辑，所有帧都对应为图像数据。
# 调用语法：to_ImageClip(self, t=0, with_mask=True, duration=None)
# 说明：输出文件时要指定codec类型，否则可能播放失败。
newclip = clipVideo.to_ImageClip(duration=1).set_fps(8)
newclip.write_videofile("img.mp4",threads=threads)




# 如果图片不带alpha层，transparent和fromalpha会被忽略。
# fromalpha、ismask和transparent参数互斥，优先使用fromalpha=True的设置，其次使用ismask=True的设置，最后应用transparent=True的设置。
# 具体实现为：
if img.shape[2] == 4:
    if fromalpha:
        img = 1.0 * img[:, :, 3] / 255
    elif ismask:
        img = 1.0 * img[:, :, 0] / 255
    elif transparent:
        self.mask = ImageClip(
        1.0 * img[:, :, 3] / 255, ismask=True)
    img = img[:, :, :3]
elif ismask:
    img = 1.0 * img[:, :, 0] / 255

# 示例：
from moviepy.editor import ImageClip, vfx, VideoFileClip, CompositeVideoClip
src = VideoFileClip("t.mp4")
w, h = src.size
clip = ImageClip("mask.png", duration=src.duration)
clip = clip.fx(vfx.resize, (w-40, h//3))
r = CompositeVideoClip([src, clip])
r.write_videofile("r.mp4", fps=8)



# ColorClip
# ColorClip是仅显示同一种颜色的剪辑。
# 示例：
colClip = ColorClip((360,360),color = (255,0,0),ismask=False,duration=5).set_fps(1)
colClip.write_videofile("red.mp4", codec='mpeg4')




# TextClip
# TextClip需要先调用ImageMagick将文本转换成一个png图片，使用前需要先安装ImageMagick，然后最好设置一下IMAGEMAGICK_BINARY环境变量为ImageMagick安装后的运行目录。
# moviepy通过命令行方式调用ImageMagick，该应用对应官方下载地址：http://www.imagemagick.org/script/download.php
# TextClip构造方法语法如下：
__init__(self, txt=None, filename=None, size=None, color='black',
                 bg_color='transparent', fontsize=None, font='Courier',
                 stroke_color=None, stroke_width=1, method='label',
                 kerning=None, align='center', interline=None,
                 tempfilename=None, temptxt=None,
                 transparent=True, remove_temp=True,
                 print_cmd=False)


# list方法：用于返回TextClip构造方法中font和color参数在执行机器上可以使用的相关取值列表。
# 调用语法为：list(arg)其中参数arg只有两个取值’font’和’color’
# 该方法是一个静态方法，直接带类名就可以调用。如：
TextClip.list('font')
TextClip.list('color')
# 以上代码执行时可能会因为编码原因报错，需要针对性修改源码。
# **search(string, arg)方法：**就是对list方法的结果进行过滤，也是一个静态方法。例如：
>>> TextClip.search(b'red','color')
[b'DarkRed', b'IndianRed', b'IndianRed1', b'IndianRed2', b'IndianRed3', b'IndianRed4', b'MediumVioletRed', b'OrangeRed', b'OrangeRed1', b'OrangeRed2', b'OrangeRed3', b'OrangeRed4', b'PaleVioletRed', b'PaleVioletRed1', b'PaleVioletRed2', b'PaleVioletRed3', b'PaleVioletRed4', b'red', b'red1', b'red2', b'red3', b'red4', b'VioletRed', b'VioletRed1', b'VioletRed2', b'VioletRed3', b'VioletRed4']
>>> TextClip.search('GB','font')
['仿宋_GB2312']




# filename属性用于存储读取视频文件的文件名，该文件名与读取视频文件给的名字完全一致，无需进行本地化路径转换。
# 构造方法：
__init__(self, filename, has_mask=False,
                 audio=True, audio_buffersize=200000,
                 target_resolution=None, resize_algorithm='bicubic',
                 audio_fps=44100, audio_nbytes=2, verbose=False,
                 fps_source='tbr')




# ImageSequenceClip
# write_images_sequence方法用于将剪辑输出到一系列图像文件中，而ImageSequenceClip则基本上与write_images_sequence过程可逆，用于将一系列图像生成剪辑。
# ImageSequenceClip是VideoClip的直接子类，该类自身只有构造方法，其他方法和属性都是继承自父类。
# 构造方法：
__init__(self, sequence, fps=None, durations=None, with_mask=True,
                 ismask=False, load_images=False)



# oncatenate_videoclips合成同屏播放的视频
# 语法：
concatenate_videoclips(clips, method="chain", transition=None, bg_color=None, ismask=False, padding = 0)



# clips_array视频的堆叠（同屏显示）
# 调用语法：
clips_array(array, rows_widths=None, cols_widths=None, bg_color = None)
# 官网示例：
from moviepy.editor import VideoFileClip, clips_array, vfx
clip1 = VideoFileClip("myvideo.mp4").margin(10) # add 10px contour
clip2 = clip1.fx( vfx.mirror_x)
clip3 = clip1.fx( vfx.mirror_y)
clip4 = clip1.resize(0.60) # downsize 60%
final_clip = clips_array([[clip1, clip2],
                          [clip3, clip4]])
final_clip.resize(width=480).write_videofile("my_stack.mp4")




# fadein、fadeout函数
# fadein使剪辑开始播放时在指定时间内从某种颜色中逐渐显示出来。
# fadeout使剪辑快结束前在指定时间内逐渐淡隐于某种颜色。
# 调用语法：
# fadein(clip, duration, initial_color=None)
# fadeout(clip, duration, final_color=None)
# duration为淡入淡出的时长，单位为秒。
# 两个函数内部的fl核心实现为：
# 作用于开始阶段
fading = (1.0*t/duration)
return fading*gf(t) + (1-fading)*initial_color
# 作用于结束阶段
fading = 1.0 * (clip.duration - t) / duration
return fading*gf(t) + (1-fading)*final_color


# invert_colors函数
# invert_colors将像素对应颜色进行反转，核心实现：
maxi = (1.0 if clip.ismask else 255)
return clip.fl_image(lambda f : maxi - f)


# freeze_region函数
# 设置region，矩形区域内的内容固定不变：
#构建矩形区域固定显示为剪辑第5秒的内容
clipVideo1 = clipVideo.fx(vfx.freeze_region ,t=5,region=(200,300,500,700))
# 设置outside_region，矩形区域外的内容固定不变：
# 构建矩形区域外固定显示为剪辑第10秒的内容
clipVideo2 = clipVideo.fx(vfx.freeze_region, t=10, outside_region=(200,300,500,700))
# 设置一个透明度0.5的mask，此时15秒时刻的指定大小的画面融合到整个时间的所有帧（时间时长低于30秒）：
# 取剪辑15秒时刻的屏幕作为一个新剪辑，新剪辑的遮罩设置为半透明
c2 = ColorClip((360, 400), ismask=True, color=0.5, duration=30)
clipVideo3 = clipVideo.fx(vfx.freeze_region, t=15, mask=c2)




# speedx函数
# speedx函数用于将视频倍速播放，factor会播放的速度。
# 调用语法：speedx(clip, factor=None, final_duration=None)
# final_duration为新剪辑的最终播放时长，设置final_duration时，会根据final_duration的值计算出factor，原有的factor即使设置也会被忽略。
# 函数的核心实现为：
newclip = clip.fl_time(lambda t: factor * t, apply_to=['mask', 'audio'])
newclip = newclip.set_duration(clip.duration / factor)



# time_mirror函数
# time_mirror函数用于实现倒放效果，实现为：
self.fl_time(lambda t: self.duration - t, keep_duration=True)


# crop函数
# 源码核心计算逻辑：
if width and x1 is not None:
    x2 = x1 + width
elif width and x2 is not None:
    x1 = x2 - width
if height and y1 is not None:
    y2 = y1 + height
elif height and y2 is not None:
    y1 = y2 - height
if x_center:
    x1, x2 = x_center - width / 2, x_center + width / 2
if y_center:
    y1, y2 = y_center - height / 2, y_center + height / 2



# resize函数
# resize函数用于调整剪辑的大小，包括缩小或放大。
# 调用语法：resize(clip, newsize=None, height=None, width=None, apply_to_mask=True)
# resize会依次尝试使用OpenCV、PIL或Scipy进行缩放，都没有安装则无法使用。
# newsize可以指定新剪辑的大小，未指定newsize时 width、height可以二选一指定一个，会等比例缩放自动计算另一个的值。
# newsize还可以指定一个函数，例如：
def getsize(t):
    if t<2:return (600,800)
    else:return (0.8-1/t)



# headblur函数
# 该函数依赖OpenCV，要求必须安装OpenCV后才能使用。安装命令：
#
# pip install opencv-python
# 该函数的源码存在bug，完全可以自行实现。
# 修改点在于：
if r_blur is None: r_blur = 2*r_zone//3
# 和
im = gf(t).copy()



# 音量调整函数
# volumex(clip, factor)可以分别调整多个声道的音量，例如将右声道静音，左声道音量调整为原来的一半：
audio.volumex([0.5,0])