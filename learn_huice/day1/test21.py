# -*-coding:utf-8-*-

#  打印1到100的数（while循环）
x = 1
while x <= 100:
    print x
    x += 1

name = ''
while not name:
    name = raw_input('please enter your name:')
print 'hello.%s!' %name



names = ['马超', '马云', '马化腾']
# for name in ['马超', '马云', '马化腾']:
for name in names:
    print name

sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + x
print sum


# range()
#从0到10(不包含10)
print range(10)
#从1到10(不包含10)
print range(1, 10)
#从1到10，间隔2(不包含10)
print range(1, 10, 2)

sum = 0
for x in range(101):
    sum = sum + x
print sum

studentList = ['小明', '小红', '田威峰', '刘则']
for index in range(len(studentList)):
    print '学号：%d 姓名:%s' %(index, studentList[index])


enumerate(studentList)
for id, name in enumerate(studentList):
    print '学号：%d 姓名:%s' % (id, name)

# 强制结束循环，遇到break结束循环的情况时，不执行else
sum = 0
for num in range(1, 11):
    sum = sum + num
    # if sum > 40:
    #     break
else:
    print 'sum is %d' % (sum)

# import time
# for num in range(30):
#     print num
#     time.sleep(1)
# else:
#     print 'bye'

# 找100以内最大平方数，那么程序可以从100往下迭代到0，步长为-1
from math import sqrt
for n in range(99, 0, -1):
    root = sqrt(n)
    if root == int(root):
        print n
        break

from math import sqrt
for n in range(99, 0, -1):
    root = sqrt(n)
    if root == int(root):
        print n
        continue