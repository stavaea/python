# coding:utf-8

# 参数
#1 不指定参数名
def my_function(a, b):
    print a+b

my_function(1, 2)

#2 指定参数名
def my_function1(name, age):
    print '姓名：%s, 年龄：%s' %(name, age)

my_function1('zhangsan', 10)
my_function1(10, 'zhangsan')
my_function1(age=10, name='zhangsan')

#3 使用默认值
def my_function2(name, age=18):
    print '姓名：%s, 年龄：%s' % (name, age)
#
my_function2('wanglaoshi')
my_function2('liulaoshi', 17)
my_function2('tianlaoshi', 46)

# def enroll(gender, age=6, city='Beijing', name):
#     print 'name:', name
#     print 'gender:', gender
#     print 'age:', age
#     print 'city:', city
#     print'-------------'
#
#
# enroll('tianweifeng', 0)
# enroll('liuze', 0, 7, 'Shanghai')
# enroll(gender=1, age=5, name='zhangsan')

def my_function3(name, age=18, sorces=[0, 0, 0]):
    print '姓名：%s, 年龄：%s, 成绩：%s' % (name, age, sorces)

my_function3('zhangsan', 20, [100, 98, 97])
my_function3('lisi', 19)

# 默认值顺序
# def my_function4(sorces=0, age):
# def my_function4(age, sorces=0, city='北京'):

# 默认值初始化逻辑
def d(c, p=[1, 2, 3]):
    p.append(c)
    return p
print d(5)
print d(6)
'''新的默认列表仅仅只在函数被定义时创建一次。
随后当 函数d 没有被指定的列表参数调用的时候，其使用的是同一个列表'''




# 练习
def extendList(val, list=[]):
    list.append(val)
    return list

list1 = extendList(10)
list2 = extendList(123, [])
list3 = extendList('a')

print "list1 = %s" % list1
print "list2 = %s" % list2
print "list3 = %s" % list3

# 解决方案
def extendList(val, list=None):
    if list is None:
        list = []
    list.append(val)
    return list

list1 = extendList(10)
list2 = extendList(123, [])
list3 = extendList('a')

print "list1 = %s" % list1
print "list2 = %s" % list2
print "list3 = %s" % list3

# 可变参数

def checkin(name, id, *other):
    print '姓名：%s, 工号：%s, 其他信息：%s' % (name, id, other)
#
checkin('田老师', '1234', 13800000000, '慧测')

info = (15000000000, '汤立路220号')
checkin('刘老师', '3456', info)

def checkin2(name, id, **other):
    print '姓名：%s, 工号：%s, 其他信息：%s' % (name, id, other)
#
checkin2('田老师', '1234', phone = 13800000000, address = '慧测')
info = {"phone": 15000000000, "address": "汤立路220号"}
checkin2('刘老师', '3456', **info)


# 生成get请求地址的方法
def url_format(domain, url=None, data=None):
    result = 'http://'+domain
    if url:
        result = result + '/' + url
    if data:
        list = []
        for k, v in data.items():
            list.append(str(k)+'='+str(v))
        result = result + '?' + '&'.join(list)
    return result

print url_format('127.0.0.1', 'huice/api', {'name': 'tiantian', 'password': '123'})

# 递归实现阶乘
def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)

print fact(5)

# 递归实现回声
def fact_voice(context):
    if len(context) == 0:
        return 0
    print context,
    context = context[1:]
    return fact_voice(context)

fact_voice(u'我爱北京天安门')

# 高阶函数

def add(a, b, f):
    return f(a)+f(b)

def f(x):
    return x**2

print add(2, 3, f)
print add(2, 3, lambda x: x**2)

# map
a = [1, 2, 3, 4, 5]
# 1
list = []
for i in a:
    list.append(i**2)
print list

#
# 2
print [i**2 for i in a]

#3
print map(lambda x: x**2, a)

#
"""1.利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']"""
data = ['adam', 'LISA', 'barT']

print map(lambda x: x.capitalize(), data)

name = ['xiaoming', 'xiaohong', 'xiaofang', 'xiaogang']
age = [19, 20, 21]
city = ['Beijing', 'Shanghai', 'Shenzhen', 'Hangzhou']
print zip(name, age, city)
print map(None, name, age, city)

# reduce
a = [1, 2, 3, 4, 5]


print reduce(lambda x, y: x*y, a)

def prod(x):
    return reduce(lambda i, j: i*j, x)

print prod(a)

# filter
a = [1, 2, 4, 5, 6, 9, 10, 15]
print filter(lambda x: x % 2 == 0, a)

b = ['A', 'B ', None, 'C', '  ', False, []]
print filter(lambda x: x and x.strip(), b)

