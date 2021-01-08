#coding:utf-8
import os

os.system('adb shell am start -W com.taobao.taobao/com.taobao.tao.homepage.MainActivity3')
print os.popen('adb shell am start -W com.taobao.taobao/com.taobao.tao.homepage.MainActivity3').readlines()

os.system(r'C:\"Program Files (x86)\Mozilla Firefox\firefox.exe"')
os.startfile(r'C:\Program Files (x86)\Mozilla Firefox\firefox.exe')

import subprocess
subprocess.Popen(r'C:\Program Files (x86)\Mozilla Firefox\firefox.exe')

print os.getcwd()
print os.listdir('.')

os.mkdir('D:\\test')
os.makedirs('D:\\test\class01\stu01')
os.rmdir('D:\\test')
os.removedirs('D:\\test\\1')

os.chdir('D:\\')
print os.listdir('.')
print os.path.abspath('.')

print os.path.isfile('D:\\test\\class01\\stu01')
print os.path.isdir('D:\\test\\class01\\stu01')
print os.path.exists('D:\\test\\class01\\stu01')
print os.path.exists('D:\\test\\class01\\stu01\\1.txt')
print os.path.split('D:\\test\\class01\\stu01\\1.txt')

file = r'D:\test\class01\stu01\1.txt'
print os.path.getctime(file)
print os.path.getmtime(file)
print os.path.getsize(file)


"""report文件夹中，是所有自动化测试报告的存放路径。取出本次生成的报告文件名"""

def new_report(report_path):
    lists = os.listdir(report_path)
    report_list = []
    for file in lists:
        file_path = os.path.join(report_path, file)
        if os.path.isfile(file_path):
            report_list.append(file)
    report_list.sort(reverse=True)
    return os.path.join(report_path, report_list[0])
#
def new_file(report_path):
    lists = os.listdir(report_path)
    report_list = []
    for file in lists:
        file_path = os.path.join(report_path, file)
        if os.path.isfile(file_path):
            report_list.append(file)
    report_list.sort(key=lambda fn: os.path.getmtime(report_path+'\\'+fn))
    return os.path.join(report_path, lists[-1])

import shutil
shutil.copyfile('D:\\report\\20171009235827.html', 'D:\\1.html')
shutil.copy('D:\\report\\20171009235827.html', 'D:\\1.html')

shutil.copytree('D:\\report', 'D:\\report_temp')
shutil.copytree('D:\\report', 'D:\\report_temp', ignore=shutil.ignore_patterns('*.html'))
shutil.rmtree('D:\\report_temp')


def my_range(start, stop, step=1):
    while start < stop:
        yield start
        start += step

#执行函数得到生成器，本质就是迭代器
obj=my_range(1, 7, 2) #1  3  5
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj)) #StopIteration

#应用于for循环
for i in my_range(1, 7, 2):
    print(i)
