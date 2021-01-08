#!/usr/bin/env python
#-*- coding:utf-8 -*-

#元组
#员工工资表，查询结果集如下：((1, 'zhangsan', 3000), (2, 'lisi', 4500), (3, 'tiantian', 20000))计算员工的平均工资

#rerult = select id, name, salary from salary
tuple = ((1, 'zhangsan', 3000), (2, 'lisi', 4500), (3, 'tiantian', 20000))
salary = 0
for i in tuple:
    salary += i[-1]
pj = salary/len(tuple)
print pj

str = 'title=华为春季新品发布会&sign=0&limit=100&status=0&address=国家会议中心&time=2018-03-28'
list = []
for i in str.split('&'):
    if i.startswith('sign='):
        list.append('sign= ')
    else:
        list.append(i)
print '&'.join(list)

#去除'hello huice'中的重复字符，得到一个新的字符串
target = 'hello huice'
list = ['h', 'e', 'l', 'o', 'u', 'i', 'c']
for i in target:
    if i not in list:
        list.append(i)
print ''.join(list)

'sign = '
