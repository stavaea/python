# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2023/12/6 14:38
# @Author : waxberry
# @File : 防止截图.py
# @Software : PyCharm




# Pillow、ImageGrab
from PIL import ImageGrab

def test_screenshot():
    im = ImageGrab.grab()
    im.show()

# 使用截图防护
def test_screenshot_protection():
    import win32clipboard
    try:
        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.CloseClipboard()
        print("Clipboard cleared")
    except Exception as e:
        print(e)

    im = ImageGrab.grabclipboard()
    if im:
        im.show()




# pyautogui、screenshot
import pyautogui

def test_screenshot():
    pyautogui.screenshot("screenshot.png")

# 使用截图防护
def test_screenshot_protection():
    import win32clipboard
    try:
        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.CloseClipboard()
        print("Clipboard cleared")
    except Exception as e:
        print(e)

    pyautogui.FAILSAFE = False
    pyautogui.PAUSE = 0
    image = pyautogui.screenshot()
    if image:
        image.show()




# win32gui API截屏
import win32gui
import win32ui
import win32con
import win32api

def capture_window(window_name):
    hwnd = win32gui.FindWindow(None, window_name)
    if hwnd != 0:
        l,t,r,b = win32gui.GetClientRect(hwnd)
        h = b - t + 1
        w = r - l + 1

        hDC = win32gui.GetWindowDC(hwnd)
        myDC = win32ui.CreateDCFromHandle(hDC)
        newDC = myDC.CreateCompatibleDC()

        myBitMap = win32ui.CreateBitmap()
        myBitMap.CreateCompatibleBitmap(myDC, w, h)

        newDC.SelectObject(myBitMap)

        win32gui.SetForegroundWindow(hwnd)
        newDC.BitBlt((0,0),(w, h) , myDC, (0, 0), win32con.SRCCOPY)
        myBitMap.SaveBitmapFile(newDC, bmp_file)

        win32gui.DeleteObject(myBitMap.GetHandle())
        newDC.DeleteDC()
        myDC.DeleteDC()
        win32gui.ReleaseDC(hwnd, hDC)





# pyhook监视屏幕
import threading
import pyHook
import pythoncom

def on_mouse_event(event):
    if event.MessageName == 'mouse left down':
        print("Mouse click detected.")
        return False
    return True

def install_hook():
    hm = pyHook.HookManager()
    hm.MouseAllButtonsDown = on_mouse_event
    hm.HookMouse()

    pythoncom.PumpMessages()

# 启动线程监测屏幕活动
def start_scanning():
    t = threading.Thread(target=install_hook)
    t.start()
    print("Hook installed")

# 停止屏幕扫描
def stop_scanning():
    pythoncom.PostQuitMessage(0)
    print("Hook removed")




# OpenGL渲染截屏
from OpenGL.GL import *
from OpenGL.GLU import *
import pygame
from pygame.locals import *

def render():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    gluPerspective(45, (640/480), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5.0)
    glColor3f(1.0, 1.0, 1.0)
    glBegin(GL_QUADS)
    glVertex3f(-1.0, 1.0, 0.0)
    glVertex3f(1.0, 1.0, 0.0)
    glVertex3f(1.0, -1.0, 0.0)
    glVertex3f(-1.0, -1.0, 0.0)
    glEnd()

def run():
    pygame.init()
    pygame.display.set_mode((640, 480), DOUBLEBUF|OPENGL)
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()

        render()
        pygame.display.flip()
        clock.tick(60)

run()






# 黑暗模式或水印
from PIL import Image, ImageDraw, ImageFont

# 黑暗模式
def dark_mode():
    image = Image.new('RGB', (500,500), color=(0,0,0))
    image.show()

# 水印
def add_watermark():
    image = Image.open("image.png")

    draw = ImageDraw.Draw(image)
    text = "Confidential"
    font = ImageFont.truetype("arial.ttf", 30)
    textwidth, textheight = draw.textsize(text, font)

    # 放置水印
    x, y = image.size
    draw.text((x - textwidth - 10, y - textheight - 10), text, font=font)
    image.show()