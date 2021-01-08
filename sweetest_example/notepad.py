from sweetest import Autotest, reporter
import sys
import json

# 项目名称，和测试用例、页面元素表文件名称中的项目名称必须一致
project_name = 'Notepad'

# 单 sheet 页面模式
sheet_name = 'notepad'

# sheet 页面匹配模式，仅支持结尾带*
#sheet_name = 'TestCase*'

# #sheet 页面列表模式
#sheet_name = ['TestCase', 'test']

# 环境配置信息
# Notepad
desired_caps = {'platformName': 'Windows', 'cmd_line': r'notepad.exe', 'timeout': 5, 'backend': 'win32', '#path': r'notepad.exe', '#backend': 'uia'}


# 执行
sweet = Autotest(project_name, sheet_name, desired_caps)

sweet.plan()
 
