# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2023/12/13 11:36
# @Author : waxberry
# @File : 在图片范围内随机点击.py
# @Software : PyCharm


from airtest.core.api import *
from airtest.cli.parser import cli_setup
from airtest.core.error import *
from airtest.core.settings import Settings as ST
import random

"""
获取模板匹配的目标区域的矩形 这一部分实现参考 cv.py 中 loop_find 部分
: param : tpl 模板
: param : intervalfunc 没有合适匹配时的回调函数
: return 最佳匹配的矩形区域(x1,y1,x2,y2)
"""

def rectangle(tpl, intervalfunc=None):
    G.LOGGING.info("Try finding:%s", tpl)
    start_time = time.time()
    while True:
        screen = G.DEVICE.snapshot(filename=None, quality=ST.SNAPSHOT_QUALITY)
        if screen is None:
            # 如果截图为空，则可能是屏幕锁定了
            G.LOGGING.warning("Screen is None, may be locked")
        else:
            match_result = tpl._cv_match(screen)
            if match_result:
                try_log_screen(screen)
                # 这里 rect 得到的是 4个坐标点 取出左上右下角 得到(x1,y1,x2,y2) 元组
                rect = match_result.get("rectangle")
                if rect is not None:
                    return (round(rect[0][0]), round(rect[0][1]), round(rect[2][0], round(rect[2][1]))

        if intervalfunc is not None:
            intervalfunc()

        # 超时则raise，未超时则进行下次循环:
        if (time.time() - start_time) > ST.FIND_TIMEOUT:
            try_log_screen(screen)
            # 如果超时，则抛出异常
            raise TargetNotFoundError('Picture %s not found in screen' % tpl)
        else:
            time.sleep(0.5)


"""
param : rect : 矩形区域 或模板
return : 区域内的随机坐标 
"""

# 获取矩形区域内的随机坐标
def random_point(rect):
    # 如果传入的是图片，则获取图片匹配的矩形区域
    if isinstance(rect, Template):
        x1, y1, x2, y2 = rectangle(rect)
    else:
        x1, y1, x2, y2 = rect
    # 在矩形区域内随机生成一个坐标点
    x = random.randint(x1, y1)
    y = random.randint(x2, y2)
    return x, y


"""
在 矩形范围内 随机点击 
param : v : 目标区域 or 模板 or 坐标点（兼容touch）
param : times : 点击次数
return ：最终点击的点的坐标
"""
@logwrap
def random_touch_in_area(v, times=1, **kwargs):
    if isinstance(v, Template) or (isinstance(v, tuple) and len(v) == 4):
        pos = random_point(v)
    else:
        try_log_screen()
        pos = v
    # 在目标区域内随机点击
    for _ in range(times):
        G.DEVICE.touch(pos, **kwargs)
        time.sleep(0.05)
    delay_after_operation()
    return pos


if __name__ == '__main__':
    # 如果没有通过命令行连接设备，则使用该连接命令，若使用IDE运行则可忽略这段代码，不用写上
    if not cli_setup():
        auto_setup(__file__, logdir=None, devices=['android:///',])
    # 录制图片
    tpl = Template(r'tpl1697636105500.png', record_pos=(0.243, -0.165), resolution=(1080, 2280))

    # 获取模板匹配的目标区域的矩形
    result = rectangle(tpl)
    print(f'图片所在矩形区域{result}')

    # 在目标区域内随机点击
    for i in range(10):
        p = random_touch_in_area(tpl)
        print(f'第{i+1:02d}次点击坐标{p}')
        sleep(1)