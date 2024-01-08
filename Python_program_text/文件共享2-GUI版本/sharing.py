# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2024/1/8 17:00
# @Author : waxberry
# @File : sharing.py
# @Software : PyCharm



from xmlrpclib import ServerProxy, Fault
from cmd import Cmd
from random import choice
from string import lowercase
from python.Python_program_text.使用XML-RPC进行远程文件共享.Server import *
from python.Python_program_text.使用XML-RPC进行远程文件共享.client import *
from threading import Thread
from time import sleep
from os import listdir
import wx
import sys

HEAD_START = 0.1
SECRET_LENGTH = 100

class ListableNode(Node):
    def list(self):
        return listdir((self.dirname))

class Client(wx.app):
    def __init__(self, url, dirname, urlfile):
        self.secret = randomString(SECRET_LENGTH)
        n = ListableNode(url, dirname, self.secret)
        t = Thread(target=n._start)
        t.setDaemon(1)
        t.start()
        sleep(HEAD_START)
        self.server = ServerProxy(url)
        for line in open(urlfile):
            line = line.strip()
            self.server.hello(line)

        super(Client, self).__init__()
    def updateList(self):
        self.files.Set(self.server.list())
    def OnInit(self):
        win = wx.Frame(None, title="File Sharing client", size=(400, 399))
        bkg = wx.Panel(win)
        self.input = input = wx.TextCtrl(bkg)
        submit = wx.Button(bkg, labal='Fetch', size=(80, 25))
        submit.Bind(wx.EVT_BUTTON, self.fetchHandler)
        hbox = wx.BoxSizer()
        hbox.Add(input, proportio =1, flag=wx.ALL|wx.EXPAND, border=10)
        hbox.Add(submit, flag=wx.TOP | wx.BOTTOM | wx.RIGHT,border = 10)
        self.files = files = wx.ListBox(bkg)
        self.updatelist()
        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(hbox, proportton=0, fLag = wx.EXPAND)
        vbox.Add(files, proportion=1, fLag = wx.EXPAND | wx.LEFT | wx.RIGHT | wx.BOTTOM, border=10)
        bkg.Setsizer(vbox)
        win.show()
        return True
        def fetchHandler(self, event):
            query = self.input.GetValue()
            try:
                self.server.fetch(query, self.secret)
                self.updateList()
            except Fault, f:
                if f.faultCode != UNHANDLED:
                    raise
                    print("Counldn't find the file", query)


def main():
    urlfile, directory, url = sys.argv[1:]
    client = Client(url, directory, urlfile)
    client.MainLoop()

if __name__ == '__main__':
    main()