#coding:utf-8

# # 用python输出一个简单的旋转风车，模拟等待图标
while True:
    for i in ['/', '|', '\\', "-"]:
        print '%s\r' % i,
#
# # 接收用户输入的一个字符串，判断是否为纯数字
str = raw_input('请输入一个字符串')
print str.isdigit()

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

# 根据输入的月份来输出，这个月有几天(默认2月有28天，不考虑闰年)
month = input("请输入月份:")
if month in [1, 3, 5, 7, 8, 10, 12]:
    print '%d 月有 31天' % (month)
elif month in [4, 6, 9, 11]:
    print '%d 月有 30天' % (month)
elif month == 2:
    print '%d 月有 28天' % (month)
else:
    print '输入不合法'

# 接收用户输入一个年份，判断是否是闰年(判断闰年的方法是该年能被4整除并且不能被100整除，或者是可以被400整除)
year = input('请输入一个年份')
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400:
            print '%d，是闰年' % year
        else:
            print '%d，不是闰年' % year
    else:
        print '%d，是闰年' % year
else:
    print '%d，不是闰年' % year

"""某电信公司的市内通话费计算标准如下：三分钟内0.2元，
三分钟后每增加一分钟增加0.1元，不足一分钟的按一分
钟计算。要求编写程序，给定一个通话时间（单位：秒）
计算出应收费金额。
"""
seconds = input('请输入通话时间：(s)')
seconds = int(seconds)
total = 0.0
if seconds in range(1, 181):
    total = 0.2
elif seconds > 180:
    if seconds % 60 == 0:
        total = 0.2 + ((seconds-180) / 60)*0.1
    else:
        total = 0.2 + ((seconds-180) / 60 + 1)*0.1
print '应收话费：%.2f' % total

# 给定一个字符串 target = 'hello huice'，从中找出第一个不重复的字符,输出它是第几位
target = 'hello huice'
for s in target:
    if target.count(s) == 1:
        print '第一个不重复的字符是：%s, 它是第%d位' %(s, target.index(s))
        break

# 去除上一题中的重复字符，得到一个新的字符串
target = 'hello huice'
# #1
new = []
for s in target:
    if s not in new:
        new.append(s)
print ''.join(new)
#
# #2
print ''.join(sorted(set(target), key=target.index))

# 输入n, 计算1-n的阶乘
n = input('请输入N')
sum = 1
if n > 0:
    for i in range(1, n+1):
        print i
        sum *= i
print sum

# 分别使用while与for循环输出1-100之间的所有偶数
j = 1
while j < 101:
    if j % 2 == 0:
        print j
    j += 1

for i in range(1, 101):
    if i % 2 == 0:
        print i

for i in range(2, 101, 2):
    print i


# 找100以内最大平方数，那么程序可以从100往下迭代到0，步长为-1
from math import sqrt
for n in range(99, 0, -1):
    root = sqrt(n)
    if root == int(root):
        print n
        break

for n in range(99, 0, -1):
    root = sqrt(n)
    if root == int(root):
        print n
        continue

# 输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数
str = raw_input('请输入一组字符')
pha = 0
num = 0
space = 0
other = 0
for s in str:
    if s.isalpha():
        pha += 1
    elif s.isspace():
        space += 1
    elif s.isdigit():
        num += 1
    else:
        other += 1
print '您输入的共有，英文字母%d个，空格%d个，数字%d个，其他字符%d个' % (pha, space, num, other)

# 输出9*9口诀
for i in range(1, 10):
    for j in range(1, i+1):
        print '%d*%d=%d\t' % (i, j, i*j),
    print '\r'

# 回文数
x = int(raw_input("input a number:\n"))
x = str(x)
for i in range(len(x)/2):
    if x[i] != x[-i - 1]:
        print 'this number is not a huiwen'
        break
print 'this number is a huiwen'

"""打印出100-999中所有的"水仙花数"，所谓"水仙花数"是指一
个三位数，其各位数字立方和等于该数本身。例如：
153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方"""

# 百位 /100  十位 %10  个位876/10-80
for i in range(100, 1000):
    b = i / 100
    s = i % 10
    g = i / 10 - b * 10
    if b**3 + s**3 + g**3 == i:
        print i

"""输出100之内的素数总个数，
所谓"素数"是指除了1和它本身以外，不能被任何整数整除的数，例如17"""
total = 0
for i in range(2, 101):
    flag = 0
    for j in range(2, i):
        if i % j == 0:
            flag = 1
            break
    if flag == 0:
        total += 1
print total

# 举例：对列表[50,20,30,10]进行冒泡排序,按照升序排列
# 冒泡排序：从前往后将相邻的两个数进行比较，将较小的数放在前面，较大的数放在后面
# 第一轮
# 20 50 30 10
# 20 30 50 10
# 20 30 10 50
# 第二轮
# 20 30 10 50
# 20 10 30 50
# 第三轮
# 10 20 30 50
# 冒泡排序原理: 每一轮只能将一个数归位, 如果有n个数进行排序,只需将n-1个数归位,
# 也就是说要进行n-1轮操作(已经归位的数不用再比较)
aList = [20, 30, 10, 50]
for i in range(0, len(aList)-1): #比较几轮,第一轮：0，第二轮：1，第三轮：2
    for j in range(0, len(aList)-i-1): #定义比较的索引,第一轮，0-1,1-2,2-3，第二轮：0-1,1-2，第三轮：0-1
        if aList[j] > aList[j+1]:
            aList[j], aList[j + 1] = aList[j+1], aList[j]
print aList



# 接收用户输入一组整数，输入负数时结束输入，输出这组数字的和：格式--您输入的数字之和是：10
total = 0
while True:
    number = input('请输入一个数字')
    if number < 0:
        break
    else:
        total += number
print '您输入的数字之和是：', int(total)

# 接收用户输入的一个字符串：l,w 代表矩形的长和宽，打印一个空心的矩形
str = raw_input('请输入参数表达式：')
h = int(str.split(',')[0])
w = int(str.split(',')[1])

for i in range(0, h+1):
    for j in range(0, w):
        if i == 0 or i == h or j == 0 or j == w-1:
            print '*',
        else:
            print ' ',
    print '\r'

# 选择排序
def select_sort(lists):
    count = len(lists)
    for i in range(0, count):
        min = i
        for j in range(i + 1, count):
            if lists[min] > lists[j]:
                min = j
        lists[min], lists[i] = lists[i], lists[min]
    return lists

# 快速排序
def quick_sort(lists, left, right):
    if left >= right:
        return lists
    key = lists[left]
    low = left
    high = right
    while left < right:
        while left < right and lists[right] >= key:
            right -= 1
        lists[left] = lists[right]
        while left < right and lists[left] <= key:
            left += 1
        lists[right] = lists[left]
    lists[right] = key
    quick_sort(lists, low, left - 1)
    quick_sort(lists, left + 1, high)
    return lists

# Stack
stack = []
size = 5
x = 100
# push
if len(stack) < 5:
    stack.append(x)
# pop
if len(stack) > 0:
    stack.pop()

"""接收用户输入的数字，输入负数时结束输入。存入一个列表
然后找出用户所输入的所有数字中最大的数，最小的数，再将所有数字从小到大排序输出"""
list = []
while True:
    number = input('请输入一个数字：')
    if number > 0:
        list.append(number)
    else:
        break
list.sort()
print '您输入的列表，最大值：%d， 最小值：%d，列表从小到大排序为：%s' % (max(list), min(list), list)


