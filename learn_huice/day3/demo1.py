#!/usr/bin/env python
# -*- coding:utf-8 -*-

#lambda
#一行代码输出[[1, 'zhangsan', 3000], [2, 'lisi', 2500], [3, 'tiantian', 20000]] 工资最高人的姓名
l = [[1, 'zhangsan', 3000], [2, 'lisi', 2500], [3, 'tiantian', 20000]]
print(sorted(l, key=lambda value: value[-1]))

#sorted()
#key指定一个接收一个参数的函数，这个函数用于从每个元素中提取一个用于比较的关键字。默认为Nonereverse是一个布尔值。如果设置为True，列表元素将被倒序排列
tag = True
while tag:
    num = input('输入一个数字')
    intnum = int(num)
    l = []
    if num < 0:
        break
    else:
        l.append(num)
print(max(l))
print(min(l))
# print(l.sort(l))
'''调用慧测会议管理接口，需要填写一个参数sign-数字签名
  sign的算法如下：
    用户输入的参数用，去除username参数，将其余的参数按参数名的ASCII码降序排列，
    在得到的参数字符串之前拼接上user=username值
    组合成一个新的字符串,加密后作为sign
  要求：用户入参如下：
        address=beijing&limit=200&title=Huice_Test&time=2018-01-30&username=tianlaoshi
        结果:user=tianlaoshititle=Huice_Test&time=2018-01-30&limit=200&address=beijing
'''
data = 'address=beijing&limit=200&title=Huice_Test&time=2018-01-30&username=tianlaoshii'
l = data.split('&')
user = ''
for i in l:
    if data.startswith('username='):
        l.pop(i)
        l[i] == 'tianlaoshi'
l.sort(reverse=True)
print(l)

#set
data = [1, 2, 3, 5, 3, 1, 2, 0, 2]
new_data = set(data)
print(new_data)
result = list(new_data)
result.sort(key= data.index)
print(result)

#dict
dic = {'id': '1', 'name': 'zhangsan', 'salary': '2000'}
print(dic)

#把字符串”k1:1|k2:2|k3:3”处理成 python 字典的形式:{'k3': 3, 'k2': 2, 'k1': 1}
s = 'k1:1|k2:2|k3:3'
dic = {}
new_s = s.split('|')
for i in new_s:
    key = (i.split(':'))[0]
    value = (i.split(':'))[1]
    dic[key] = value
print(dic)

dic = {'id': '1', 'name': 'zhangsan', 'salary': '2000'}
for k, v in dic.items():
    print (k, v)


#去除字典中value重复的项{'zhangsan':100, 'lisi':65, 'tianlaoshi':65, 'liulaoshi':99}
dic = {'zhangsan': 100, 'lisi': 65, 'tianlaoshi': 65, 'liulaoshi': 99}
for k, v in dic.items():
    if dic.values().count(v) > 1:
        del dic[k]
print(dic)

print(sorted(dic.items(), key=lambda x: x[-1]))

'''编写一组数据，记录组内每个人的语文成绩
    data = {
         'JiaNaiLiang': 60,
         'LiXiaoLu': 75,
         'TianLaoShi': 99,
         'MaSu': 88,
         'KongLingHui': 35,
         'LiuLaoShi': 100
    }
    a.算出平均分
    b.再找出学霸
'''
data = {
         'JiaNaiLiang': 60,
         'LiXiaoLu': 75,
         'TianLaoShi': 99,
         'MaSu': 88,
         'KongLingHui': 35,
         'LiuLaoShi': 100
    }
score = sum(data.values())/len(data)
print(score)

#max(data.values())

print(sorted(data.items(), key=lambda x: x[-1], reverse=True))[0][0]

good = (sorted(data.items(), key=lambda x: x[-1], reverse=True))
print(good[0][0])


'''编写一组数据，记录组内每个人的语文成绩、数学成绩、英语成绩
    data = {
         'JiaNaiLiang': [60, 68, 45], 
         'LiXiaoLu': [10, 28, 5],
         'TianLaoShi': [44, 86, 73],
         'MaSu': [99, 95, 95],
         'KongLingHui': [98, 65, 100],
         'LiuLaoShi': [77, 97, 65]
    }
    a.找到平均分不足60分的人
    b.找出各科的最高分
    c.算出各科的平均分，再找出各科的学霸
'''
data = {
         'JiaNaiLiang': [60, 68, 45],
         'LiXiaoLu': [10, 28, 5],
         'TianLaoShi': [44, 86, 73],
         'MaSu': [99, 95, 95],
         'KongLingHui': [98, 65, 100],
         'LiuLaoShi': [77, 97, 65]
    }

#a
for k, v in data.items():
    if sum(v) / len(v) < 60:
        print(k)

#b
cn = []
math = []
en = []
for k, v in data.items():
    cn.append(v[0])
    math.append(v[1])
    en.append(v[2])
print(max(cn))
print(max(math))
print(max(en))
#
#c
print(sum(cn) / len(cn))
print(sum(math) / len(math))
print(sum(en) / len(en))

print(sorted(data.items(), key=lambda x: x[-1][0], reverse=True)[0][0])
print(sorted(data.items(), key=lambda x: x[-1][1], reverse=True)[0][0])
print(sorted(data.items(), key=lambda x: x[-1][-1], reverse=True)[0][0])




