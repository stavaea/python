# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2023/5/26 10:24
# @Author : waxberry
# @File : dubbo_api.py
# @Software : PyCharm

import json
import telnetlib

from PyQt5.QtCore.QUrl import port


class Dubbo(telnetlib.Telnet):
    prompt = 'dubbo>'

    def __init__(self, host=None, port=0):
        super().__init__(host, port)
        self.write(b'\n')

    def command(self, flag, str_=''):
        data = self.read_until(flag.encode())
        self.write(str_.encode() + b'\n')
        return data

    def invoke(self, service_name, method_name):
        command_str = 'invoke {0}.{1}()'.format(service_name, method_name)
        self.command(Dubbo.prompt, command_str)
        data = self.command(Dubbo.prompt, '')
        data = json.loads(data.decode(Dubbo.coding, errors='ignore').split('\n')[0].strip())

if __name__ == '__main__':
    conn = Dubbo('serviceIp', port)
    result = conn.invoke(
        'serviceName',
        'serviceName.method'
    )
    print(result)