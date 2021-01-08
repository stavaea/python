#!/usr/bin/env python
#-*- coding:utf-8 -*-
# url拼接
def get(domin, url = None, data = None):
    result = 'http://'+domin
    if url:
        result + '/' + url
    if data:
        l = []
        for k, v in data.items():
            l.append(k + '=' + v)
            result = result + '?' + '&'.join(l)
    return result
print(get('www.baidu.com', 'huice/api', {'1': '1', '2': '2'}))

#函数封装
def num():
    list = []
    while True:
        a = input('请输入一个数字，输入负数停止')
        if a >= 0:
            list.append(a)
        else:
            break
    new = []
    for i in list:
        if str(i) not in new:
            new.append(str(i))
    print '您输入的数字组合是：%s' % '&'.join(new)
    return


#类和对象



'''设计一个汽车类Auto（显示给出一个没有参数的构造函数），
有速度属性speed，启动start、加速speedup(1次速度+10)和停止stop(1次速度-30)方法'''

class Auto:
    def __init__(self, name):
        self.name = name
        self.speed = 0
    def start(self):
        print('%s车开始运行' % self.name)
    def speedup(self):
        self.speed += 10
        return self.speed
    def stop(self):
        if self.speed >= 30:
            self.speed -=30
            return self.speed
        else:
            return 0
if __name__ == '__main__':
    auto1 = Auto('BMW')
    auto1.start()
    auto1.speed()
    auto1.stop()

'''利用列表实现数据结构--栈
理解setter和getter的作用
    0.不能直接访问栈
    1.初始化函数，传入栈的极限大小
    2.提供一个弾栈和一个压栈的方法
    3.提供一个获取栈极限大小的方法
    4.其他方法私有--判断栈是否到达极限，栈是否为空'''

class Stack:
    def __init__(self, size):
        self.__size = size
        self.__data = []

    def get_size(self):
        return self.__size

    def push(self, a):
        if len(self.__data) < self.__size:
            self.__data.append(a)
    def pop(self):
        if self.__data > 0:
            return self.__data.pop()

    def __str__(self):
        return ' '.join(self.__data)

if __name__ == '__main__':
    demo1 = Stack(5)
    demo1.push('a')
    demo1.push('b')
    demo1.push('c')

    print(demo1.pop())
    print(demo1)


#异常捕获

'''1.从开发的代码库中得到一组数据，表示每个文件的代码变更情况
  {'login.py': 'a 8 d 2 u 3 ', 'order.py': 'a 15 d 0 u 34', 'info.py': 'a 1 d 20 u 5 '}
  其中 a表示新增行数，d表示删除行数，u表示修改行数。login.py的变更行数为13
  要求：统计出每个文件的变更行数'''

data = {'login.py': 'a 8 d 2 u 3 ', 'order.py': 'a 15 d 0 u 34', 'info.py': 'a 1 d 20 u 5 '}
for k, v in data.items():
    s = v.split(' ')
    sum = 0
    for i in s:
        if i.isdigit():
            i = int(i)
            sum += i
    print(k, sum)

data = {'login.py': 'a 8 d 2 u 3 ', 'order.py': 'a 15 d 0 u 34', 'info.py': 'a 1 d 20 u 5 '}
for k, v in data.items():
    s = v.split(' ')
    l = []
    for i in s:
        try:
            l.append(int(i))
        except:
            pass
    print(k, sum(l))

'''2.优化练习
接受用户输入的一个字符串，如果是正整数就判断是否能同时被3和7整除'''


#异常抛出

'''1.编写一个计算减法的方法，当第一个数小于第二个数时，抛出“被减数不能小于减数"的异常
2.编写一个计算加法的方法，接收键盘输入的两个数字，进行加法运算，当输入的有非数字时，
通过异常处理机制使程序正常运行(返回0)
3.创建一个用户注册服务，其中有一个register方法。当用户名小于6位时，抛出自定义异常
系统异常NameError的子类异常UserNameError'''

#1
def sub(a, b):
    try:
        if a < b:
            raise IndentationError('被减数不能小于减数')
        else:
            return a - b
    except:
        pass
print(sub(1, 2))

#2
def sum(i):
    i = raw_input()
    j = raw_input()
    result = 0
    try:
       result = int(i) + int(j)
    except:
        pass
    return result

#3



#模块导入
'''新创建一个子包 sub
sub中有一个模块：util.py 其中有一个工具类：Util，有一个静态方法求两数之和；一个类方法求两数之积	
如果单独运行该文件，显示说明文字
在当前demo.py文件尝试调用该方法	'''


from sub.util import Util
print Util.sum(1, 2)
print(Util().chengji(2, 3))


#文件复制
import shutil
shutil.copy('G:\\data.csv', 'D:\\')
