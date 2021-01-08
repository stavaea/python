#coding:utf-8
'''1.某市的出租车计费标准为：3公里以内10元，3公里以后每0.5公里加收1元；每等待2.
5分钟加收1元；超过15公里的加收原价的50%为空驶费。
要求编写程序，对于任意给定的里程数（单位：公里）和等待时间（单位：秒）计算出应付车费'''
price = 0.0
km = input('请输入公里数：')
wt = input('请输入等待秒数：')
if km <= 3.0:
    price = 10.0
elif km >3.0 and km <= 15.0:
    price = 10.0 + int((km - 3.0)/0.5)
elif km > 15.0:
    price = (10.0 + int((km - 3.0)/0.5))*1.5
if wt > 150:
    price += wt/150
print "应付金额:%.2f" % price


'''2.一个数如果恰好等于它的因子之和，这个数就称为“完数”。例如6=1＋2＋3.编程找出1000以内的所有完数'''
# 假完数
for n in range(2, 1000):
    k = []
    sum = 0
    for j in range(1, n):
        k.append(j)
    for j in k:
        sum += j
        if sum == n:
            print n

# 真完数
for i in range(1, 1000):
    s = 0
    for j in range(1, i):
        if i % j == 0:
            s += j
    if s == i:
        print i


'''3.用python实现选择排序
算法如下：[49, 38, 27, 45, 13]
第一趟[13, 38, 27, 45, 49]
第二趟[13, 27, 45, 38, 49]
第三趟[13, 27, 38, 45, 49]
'''

lists = [49, 38, 27, 45, 13]
#1
for i in range(0, len(lists)):
    for j in range(i, len(lists)):
        if lists[i] > lists[j]:
            lists[i], lists[j] = lists[j], lists[i]
print lists
#
#2
for i in range(0, len(lists)):
    min = i
    for j in range(i+1, len(lists)):
        if lists[min] > lists[j]:
            min = j
    lists[min], lists[i] = lists[i], lists[min]
print lists


'''4.
员工工资表，查询结果集如下：((1, 'zhangsan', 3000), (2, 'lisi', 2500), (3, 'tiantian', 20000))
*输出工资最高的员工姓名'''

data = ((1, 'zhangsan', 3000), (2, 'lisi', 2500), (3, 'tiantian', 20000))

#1
for i in range(len(data)):
    temp = 0
    j = 0
    if data[i][-1] > temp:
        temp = data[i][-1]
        j = i
print "工资最高的人是：%s" % data[j][1]

#2
salary = []
for i in range(0, len(data)):
    salary.append(data[i][-1])
topsalary = max(salary)
print data[salary.index(topsalary)][1]

#3
def my_sort(d):
    return d[-1]
print sorted(data, key=my_sort, reverse=True)[0][1]

#4
print sorted(data, key=lambda x: x[-1], reverse=True)[0][1]

'''5.接收用户输入的数字，输入负数时结束输入。存入一个列表，去掉重复数字，以字符串形式输出：2&5&3&4
提示：全部数字存入一个列表，利用课上说的新列表实现去重，再拼接成字符串输出'''
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
