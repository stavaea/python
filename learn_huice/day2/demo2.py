# coding:utf-8

# while
while True:
    num = input('输入一个数字:')
    if num > 0:
        print num
    else:
        break

# for
# 给定一个字符串 target = 'hello huice'，从中找出第一个不重复的字符,输出它是第几位
target = 'hello huice'
for i in target:
    if target.count(i) == 1:
        print i,
        print target.index(i)
        break


while True:
    for i in ['|', '-', '\\', '/']:
        print '%s\r' % i,

# 输入n, 计算1到n的阶乘
x = [1, 2, 3]
num = input('输入一个数字')
sum = 1
for i in range(1, num+1):
    sum *= i
    print sum

# 分别使用while与for循环输出1-100之间的所有偶数
for i in range(1, 101):
    if i % 2 == 0:
        print i,

i = 1
while i <= 100:
    if i % 2 == 0:
        print i
for i in range(2, 101, 2):   #步长
    print i

# 找100以内最大平方数
from math import sqrt
for i in range(99, 0, -1):
    n = sqrt(i)
    if n == int(n):
        print n
        break

# 输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数
str = raw_input('输入一串字符：')
num = 0
word = 0
space = 0
other = 0
for i in str:
    if str.isalpha():
        num += 1
    elif str.isspace():
        word += 1
    elif str.isdigit():
        space += 1
    else:
        other += 1
print str.count()

# 一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同
num = raw_input('输入一串数字')
for i in range(len(num)/2):
    if num[i] != num[-i-1]:
        print '%s不是回文数' % num
        break
else:
    print '%s是回文数' % num

# 打印出100-999中所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方

for i in range(100, 1000):
    b = int(i / 100)
    s = int(i % 100 / 10)
    g = int(i % 10)
    if b**3 + s**3 + g**3 == b*100 + s*10 +g*1:
        print '%d是水仙花数' % i

for i in range(999, 101, -1):
    b = int(i / 100)
    s = int(i % 100 / 10)
    g = int(i % 10)
    if b**3 + s**3 + g**3 == b*100 + s*10 +g*1:
        print '%d是水仙花数' % i
        break

# 输出9*9口诀
for i in range(1, 10):
    for j in range(1, i+1):
        sum = i * j
        print '%d * %d = %d\t' % (i, j, sum),
    print '\r'

# 输出100之内的素数总个数，所谓"素数"是指除了1和它本身以外，不能被任何整数整除的数，例如17
for i in range(1, 101):
    for j in range(2, i-1):
        if i % j == 0:
           # print '%d不是素数'%j
            break
    else:
        print '%d是素数' % i
sum = []
for i in range(1, 101):
    for j in range(2, i):
        if i % j == 0:
           # print '%d不是素数'%j
            break
    else:
        sum.append(i)
print sum
print len(sum)

# 接收用户输入一组整数，输入负数时结束输入，输出这组数字的和：格式--您输入的数字之和是：10
sum = 0
while True:
    num = input('输入一个数字')
    if num > 0:
        sum += num
    else:
        break
print sum

# 接收用户输入的一个字符串：h,w 代表矩形的长和宽，打印一个空心的矩形
s = raw_input('输入一组数字')
#a = s.split(',')
h = int(s.split(',')[0])
w = int(s.split(',')[1])
for i in range(0, h):
    for j in range(0, w):
        if i == 0 or i == h-1 or j == 0  or j == w-1:
            print '*',
        else:
             print ' ',
    print '\r'

# 冒泡排序
list = [20, 10, 40, 30, 60, 50]
for i in range(len(list)-1):
    for j in range(0, len(list)-i-1):
        if list[j] > list[j+1]:
            list[j], list[j + 1] = list[j + 1], list[j]
print list