#!/usr/bin/python2
#_*_coding:utf-8_*_
'''1.某市的出租车计费标准为：3公里以内10元，3公里以后每0.5公里加收1元；每等待2.5分钟加收1元；超过15公里的加收原价的50%为空驶费。
要求编写程序，对于任意给定的里程数（单位：公里）和等待时间（单位：秒）计算出应付车费
'''

km = input('输入里程数：\n')
wt = input('输入等待时间：\n')
money = 0

if km <= 3:
    print('车费是10元')
elif km > 3 and km <= 15:
    money = (10 + (km - 3) / 0.5 * 1) + time / 150
    print('车费是%2.f元'%money)
elif km > 15:
    money = ((10 + (km - 3) / 0.5 * 1) * 1.5) + time / 150
    print('车费是%2.f元'%money)

if km <= 3:
    money = 10
elif km > 3 and km <= 15:
    money = 10 + (km - 3) / 0.5 * 1
elif km > 15:
    money = (10 + (km - 3) / 0.5 * 1) * 1.5
if wt > 150:
    money += wt/150
print('车费是%2.f元'%money)

'''2.一个数如果恰好等于它的因子之和，这个数就称为“完数”。例如6=1＋2＋3.编程找出1000以内的所有完数
'''
list = []
for i in range(0,1000):
    sum = 0
    for j in range(1,i):
        if i % j == 0:
            sum += j
            list.append(j)
    if i == sum:
        print(i)
        print(list)
    list = []

'''*3.用python实现选择排序
算法如下：[49, 38, 27, 45, 13]
第一趟[13, 49, 38, 27, 45]
第二趟[13, 27, 49, 38, 45]
第三趟[13, 27, 38, 49, 45]
第四趟[13, 27, 38, 45, 49]
'''
l = [49, 38, 27, 45, 13]
for i in range(0,len(l)):
    min = i
    for j in range(i+1,len(l)):
        if l[j] < l[min]:
            min = j
            l[i],l[min] = l[min],l[i]
#print(i,j)
print(l)

'''4.员工工资表，查询结果集如下：((1, 'zhangsan', 3000), (2, 'lisi', 4500), (3, 'tiantian', 20000))
  *输出工资最高的员工姓名
'''
t = ((1,'zhangsan',3000), (2,'lisi',4500), (3,'tiantian',20000))
l = list(t)
for i in range(len(l)-1):
    for j in range(0,len(l)-i-1):
        if l[j][2] > l[j+1][2]:
            l[j],l[j+1] = l[j+1],l[j]
print(l)
print(l[-1][1])

t = ((1,'zhangsan',3000), (3,'tiantian',20000),(2,'lisi',4500))
l = list(t)
for i in range(len(l)-1):
    for j in range(0,len(l)-i-1):
        if l[j][2] < l[j+1][2]:
            l[j],l[j+1] = l[j+1],l[j]
print(l)
print(l[0][1])

'''5.接收用户输入的数字，输入负数时结束输入。存入一个列表，去掉重复数字，以字符串形式输出：2&5&3&4
提示：全部数字存入一个列表，利用课上说的新列表实现去重，再拼接成字符串输出
'''
list = []
while True:
    num = raw_input('输入一个数字：\n')
    intnum = int(num)
    if intnum < 0:
        break
    else:
        if num not in list:
            list.append(num)
print ('&'.join(list))
