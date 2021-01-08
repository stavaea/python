#coding:utf-8

import os,subprocess,time

class AppiumServer(object):
    '''启动，关闭appium server'''

    def __init__(self):
        global cmd_start_appium, base_url
        cmd_start_appium = IniHelper('cfginfo.ini').get_value('appium', 'start_appium')
        base_url = IniHelper('cfginfo.ini').get_value('appium', 'base_url')
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

    def start_server(self):
        '''启动appiumServer'''
        # TODO:目前只是单一手机测试，如果是多个手机，要增加端口
        # cmd = 'start /b appium -a 127.0.0.1 -p 4723'
        appium_log_path = log_dir + 'appium.log'
        subprocess.call(cmd_start_appium, shell=True, stdout=open(appium_log_path, 'w'), stderr=subprocess.STDOUT)
        time.sleep(4)
        if self.is_running():
            print ('启动appiumServer成功')
        else:
            print ('启动appiumServer失败')