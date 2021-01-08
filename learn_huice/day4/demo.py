#coding:utf-8
class HuiCeStudent:

    __xuefei__ = 8800

    def __init__(self, name):
        self.name = name

    def __print_name(self):
        '''qqqqqq'''
        print self.name

    @classmethod
    def print_xuefei(cls):
        print cls.__xuefei


class Auto:
    def __init__(self, name):
        self.name = name
        self.speed = 0
    def start(self):
        print '%s车开始运行' % self.name

    def speed(self):
        self.speed += 10
        return self.speed
    def stop(self):
        if self.speed >= 30:
            self.speed -= 30
            return self.speed
        else:
            return 0

class Stack(Auto):

    def __init__(self, size):
        self.__size = size
        self.__data = []

    def get_size(self):
        return self.__size

    def __isfull(self):
        if len(self.__data)<self.__size:
            return False
        else:
            return True

    def push(self, a):
        if self.__isfull():
            self.__data.append(a)

    def pop(self):
        if len(self.__data) > 0:
            return self.__data.pop()

    def __str__(self):
        return ' '.join(self.__data)

if __name__ == '__main__':
    demo1 = Stack(5)
    demo1.push('a')
    demo1.push('b')
    demo1.push('c')
    print demo1.pop()
    print demo1

data = {'login.py': 'a 8 d 2 u 3', 'order.py': 'a 15 d 0 u 34', 'info.py': 'a 1 d 20 u 5'}

for k, v in data.items():
    list = v.split(' ')
    sum = 0
    for l in list:
        if l.isdigit():
            sum += int(l)
    print k, '文件，变更：',sum


# 接受用户输入的一个字符串，如果是正整数就判断是否能同时被3和7整除
number = raw_input('请输入一个数字：')
if number.isdigit() or (number.startswith('-') and number[1:].isdigit()):
    number = long(number)
    if number > 0:
        if number % 3 == 0 and number % 7 == 0:
            print number, '能够被3和7同时整除'
        else:
            print number, '不能够被3和7同时整除'
    else:
        print number, '不是正整数'
else:
    print '输入的包含非数字'


