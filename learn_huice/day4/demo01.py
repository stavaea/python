#coding:utf-8
import sys
import traceback
# ImportError:导入模块错误
# import A

# IndexError:索引超出范围
# list1 = [1,2,3]
# print list1[3]

# KeyError:字典中不存在的键
# dict1 = {'name':'ivy','age':20,'gender':'female'}
# print dict1['height']

# NameError：访问没有定义的变量
# print a

# IndentationError:缩进错误
# if 1==1:
# print 'aaa'

# SyntaxError:语法错误
# list2 = [1,2,3,4

# TypeError:不同类型间的无效操作
# print 1+'1'

# ZeroDivisionError:除数为0
# print 5/0

    # 无法预知的调用错误
# def sum(a, b):
#     print a+b
#
# print sum(0, 1)+2

def sum():
    try:
        print 5/0
        print 1
    except (TypeError, ZeroDivisionError) as e:
        print 'error'
        return 0
    finally:
        print '0000'

try:
    print 'try...'
    r = 10 / 0
    print 'result:', r
except ZeroDivisionError, e:
    print 'except:', e
finally:
    print 'finally...'
print 'END'
#
try:
    print 'try...'
    r = 10 / int('a')
    print 'result:', r
except ValueError, e:
    print 'ValueError:', e
except ZeroDivisionError, e:
    print 'ZeroDivisionError:', e
finally:
    print 'finally...'
print 'END'

"""1.从开发的代码库中得到一组数据，表示每个文件的代码变更情况
{'login.py': 'a 8 d 2 u 3 ', 'order.py': 'a 15 d 0 u 34', 'info.py': 'a 1 d 20 u 5 '}
其中 a表示新增行数，d表示删除行数，u表示修改行数。login.py的变更行数为13
要求：统计出每个文件的变更行数"""

data = {'login.py': 'a 8 d 2 u 3 ', 'order.py': 'a 15 d 0 u 34', 'info.py': 'a 1 d 20 u 5 '}
for k, v in data.items():
    line = []
    list = v.split(' ')
    for l in list:
        try:
            line.append(int(l))
        except:
            pass
    print "文件 %s 变更 %d 行" % (k, sum(line))

"""优化练习
    接受用户输入的一个字符串，如果是正整数就判断是否能同时被3和7整除"""
# 原始代码
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

# 优化代码
number = raw_input('请输入一个数字：')
try:
    number = long(number)
    if number > 0:
        if number % 3 == 0 and number % 7 == 0:
            print number, '能够被3和7同时整除'
        else:
            print number, '不能够被3和7同时整除'
    else:
        print number, '不是正整数'
except:
    print '输入的包含非数字'









# 编写一个计算减法的方法，当第一个数小于第二个数时，抛出“被减数不能小于减数"的异常
def sub(a, b):
    if a < b:
        raise ArithmeticError('被减数不能小于减数')
    return a-b

print sub(0, 2)

# 2
def sum(a, b):
    try:
        a, b = int(a), int(b)
    except ValueError:
        a = b = 0
    return a+b
a = raw_input('请输入第一个数字')
b = raw_input('请输入第二个数字')
print sum(a, b)

# 3
class UserNameError(NameError):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return str('用户名[%s]长度少于6位' % self.value)

class UserService(object):

    def register(self, name):
        if len(name) < 6:
            raise UserNameError(name)
        print "注册成功，欢迎[%s]" % name

try:
    name = raw_input('请输入用户名:')
    UserService().register(name)
except UserNameError, e:
    print e
