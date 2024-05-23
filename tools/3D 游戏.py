#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2024/5/23 17:39
@Author  : waxberry
@File    : 3D 游戏.py
@Software: PyCharm
"""



# 1、加载人物、对象、背景

avatar = viz.addAvatar('xxx.cfg', pos=(0,0,0), euler=(0,0,0))
viz.add('xxx.osgb',pos=(0,0,0), euler=(0,0,0))
viz.addChild('xxx.obj',pos=(-4,0,7.5))


# 2、鸽子随机漫步
''''①利用𝑣𝑖𝑧𝑎𝑐𝑡. 𝑟𝑎𝑛𝑑𝑓𝑙𝑜𝑎𝑡()生成随机位置，调用𝑣𝑖𝑧𝑎𝑐𝑡. 𝑤𝑎𝑙𝑘𝑇𝑜()实现鸽子漫步
②利用𝑣𝑖𝑧𝑎𝑐𝑡. 𝑐ℎ𝑜𝑖𝑐𝑒()生成随机选择，随机更新鸽子的𝑠𝑡𝑎𝑡𝑒状态
③调用𝑣𝑖𝑧𝑎𝑐𝑡. 𝑤𝑎𝑖𝑡𝑡𝑖𝑚𝑒()实现随机时间的等待
④利用𝑣𝑖𝑧𝑎𝑐𝑡. 𝑠𝑒𝑞𝑢𝑒𝑛𝑐𝑒()实现上述动作序列'''

pigeon = viz.addAvatar('pigeon.cfg',pos=(2,0,5))
random_walk = vizact.walkTo(pos=[vizact.randfloat(1.5,2.5),0,vizact.randfloat(4.5,5.5)])
random_animation = vizact.method.state(vizact.choice([1,3],vizact.RANDOM))
random_wait = vizact.waittime(vizact.randfloat(2.0,8.0))
pigeon_idle = vizact.sequence( random_walk, random_animation, random_wait, viz.FOREVER)
pigeon.runAction(pigeon_idle)


# 3、人物谈话动作

def PersonTalk():
  female = viz.addAvatar('vcc_female.cfg', pos=(1,0,8), euler=(-90,0,0))
  male = viz.addAvatar('vcc_male2.cfg', pos=(0,0,8), euler=(90,0,0))
  female.state(14)
  male.state(4)


# 4、角色移动
'''
①通过𝑣𝑖𝑧.𝑔𝑒𝑡𝐹𝑟𝑎𝑚𝑒𝐸𝑙𝑎𝑝𝑠𝑒𝑑() ∗ 𝑠𝑝𝑒𝑒𝑑计算移动速度
②初始化欧拉矩阵𝑚1 = 𝑣𝑖𝑧.𝑀𝑎𝑡𝑟𝑖𝑥.𝑒𝑢𝑙𝑒𝑟(0, 0, 0)
③通过𝑣𝑖𝑧.𝑘𝑒𝑦.𝑖𝑠𝐷𝑜𝑤𝑛()分析对应鼠标事件，根据人物朝向𝑎𝑣𝑎𝑡𝑎𝑟.𝑔𝑒𝑡𝐸𝑢𝑙𝑒𝑟()更新𝑚1平移变换矩阵
④通过𝑎𝑣𝑎𝑡𝑎𝑟.𝑠𝑒𝑡𝑃𝑜𝑠𝑖𝑡𝑖𝑜𝑛(𝑚1.𝑔𝑒𝑡𝑃𝑜𝑠𝑖𝑡𝑖𝑜𝑛())更新人物位置
⑤通过𝑣𝑖𝑧.𝑘𝑒𝑦.𝑖𝑠𝐷𝑜𝑤𝑛()分析对应鼠标事件，设置对应人物动画：
前进、后退动画：𝑎𝑣𝑎𝑡𝑎𝑟.𝑠𝑡𝑎𝑡𝑒(2)
左跨步动画：𝑎𝑣𝑎𝑡𝑎𝑟.𝑠𝑡𝑎𝑡𝑒(12)
右跨步动画：𝑎𝑣𝑎𝑡𝑎𝑟.𝑠𝑡𝑎𝑡𝑒(13)
人物静止动画：𝑎𝑣𝑎𝑡𝑎𝑟.𝑠𝑡𝑎𝑡𝑒(1)
'''

def roleMove():
    m1 = viz.Matrix.euler(0, 0, 0)
    dm = viz.getFrameElapsed() * speed
    temp = avatar.getEuler()[0] * math.pi / 180
    if viz.key.isDown('w'):
        m1.preTrans([dm * math.sin(temp), 0, dm * math.cos(temp)])
        avatar.state(2)
    elif viz.key.isDown('s'):
        m1.preTrans([-dm * math.sin(temp), 0, -dm * math.cos(temp)])
        avatar.state(2)
    elif viz.key.isDown('a'):
        m1.preTrans([-dm * 0.3 * math.cos(temp), 0, dm * 0.3 * math.sin(temp)])
        avatar.state(12)
    elif viz.key.isDown('d'):
        m1.preTrans([dm * 0.3 * math.cos(temp), 0, -dm * 0.3 * math.sin(temp)])
        avatar.state(13)
    else:
        avatar.state(1)

    avatar.setPosition(m1.getPosition(), viz.REL_PARENT)


# 5、获取鼠标位移
# 通过回调函数callback获取

def onMouseMove(e):
    global mp_x,mp_y
    mp_x=e.dx
    mp_y=e.dy
viz.callback(viz.MOUSE_MOVE_EVENT,onMouseMove)