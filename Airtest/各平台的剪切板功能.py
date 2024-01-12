# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2024/1/12 17:29
# @Author : waxberry
# @File : 各平台的剪切板功能.py
# @Software : PyCharm

# 2. Android设备的剪切板功能
from airtest.core.api import *
auto_setup(__file__)
text_1 = 'test_clipboard'
set_clipboard(text_1)# 设置剪切板内容
get_text = get_clipboard()# 获得剪切板内容
print(get_text)# -> test_clipboard
# 剪切板粘贴接口
paste()  # => text(get_clipboard())



# 3. iOS设备的剪切板功能
# 但是 对于远程iOS设备，我们必须指定WDA的bundle ID：
# 远程iOS设备
text_1 = "test_clipboard"
bundle_id = "com.2303xxxxxxxxx.WebDriverAgentRunner.xctrunner"
set_clipboard(text_1,bundle_id) # 设置剪切板内容
get_text = get_clipboard(bundle_id) # 获得剪切板内容
print(get_text)  # -> test_clipboard
# 剪切板粘贴接口
paste(bundle_id)  # => text(get_clipboard())

# 1）小tips：关于如何获取WDA的bundle ID
# 我们可以使用Airtest1.3.0新增的iOS接口来查询：
from airtest.core.api import *
import airtest
auto_setup(__file__)
dev = device()
#列出并打印用户安装的APP
print("---------以下是用户安装的APP的信息-----------")
user_app = dev.list_app("user")
print(user_app)
# 此时，我们安装在手机上的WDA信息也会被打印出来，不过 该方式只能适用于本地的iOS设备 ！



# 4. Windows平台的剪切板功能
from airtest.core.api import *
auto_setup(__file__)
text("11111111")
# 模拟按键Ctrl+A，实现全选文本
keyevent("^a")
# 模拟按键Ctrl+C，实现复制文本
keyevent("^c")
# 回车换行
keyevent("{ENTER}")
# 模拟按键Ctrl+V，实现复制文本
keyevent("^v")