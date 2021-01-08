# coding:utf-8
#补充演示：

tup1 = tuple([1, 2, 3])
tup2 = tuple('abc')
print tup1, tup2

str_list = ['c', 'c#', 'java', 'python', 'ruby', 'javascript']
str_list.sort()
print str_list

str_list.sort(key=len, reverse=True)
print str_list


"""接收用户输入的数字，输入负数时结束输入。存入一个列表
然后找出用户所输入的所有数字中最大的数，最小的数，再将所有数字从小到大排序输出"""
# list = []
# while True:
#     a = input('请输入一个数字')
#     if a >= 0:
#         list.append(a)
#     else:
#         break
# print "您输出的最大值为：%d, 最小值为：%d, 从小到大排序：%s" % (
#     max(list), min(list), sorted(list)
# )

'''调用慧测会议管理接口，需要填写一个参数sign-数字签名
sign的算法如下：
用户输入的参数用，去除username参数，将其余的参数按参数名的ASCII码降序排列，
在得到的参数字符串之前拼接上user=username值
组合成一个新的字符串,加密后作为sign
要求：用户入参如下：
    address=beijing&limit=200&title=Huice_Test&time=2018-01-30&username=tianlaoshi
    结果:user=tianlaoshititle=Huice_Test&time=2018-01-30&limit=200&address=beijing
'''

data = 'address=beijing&limit=200&title=Huice_Test&time=2018-01-30&username=tianlaoshi'
paras = data.split('&')
user = ''
for i in paras:
    if i.startswith('username='):
        user = i.split('=')[1]
        paras.remove(i)
paras.sort(reverse=True)
result = "user=%s%s" % (user, '&'.join(paras))
print result


# for 循环延伸 [x for x in y]

x = [1, 2, 3, 6]
y = [5, 8, 7, 10]
print [a + b for a in x for b in y if a % 2 == 0 and b % 2 == 0]

a = [1, 2, 3, 4, 5, 6]
print [a[x]+3 for x in range(len(a)) if (x+1) % 2 == 0]

z = [[1, 2], [3, 4], [5, 6]]
print [j*2 for i in z for j in i]

# zip函数应用
id = [1, 2, 3]
name = ['zhangsan', 'lisi', 'tiantian']
salary = [3000, 4500, 20000]
print tuple(zip(id, name, salary))

# 列表去重
list_1 = [7, 2, 3, 1, 2, 4, 5, 7, 1, 7]
list_new = []
for i in list_1:
    if i not in list_new:
        list_new.append(i)
print list_new

# 2
print {}.fromkeys(list_1).keys()

# 3
print sorted(list(set(list_1)), key=list_1.index)

# 列表合并
a = [1, 2, 3, 5, 6]
b = [0, 2, 5, 7, 8]

# 1
for i in a:
    if i not in b:
        b.append(i)
print b

# 2
new = []
for i in a:
    if i not in new:
        new.append(i)
for j in b:
    if j not in new:
        new.append(j)
print new

#3
new = []
a.extend(b)
for i in a:
    if i not in new:
        new.append(i)
print new

# 3 bug版
new = []
for i in zip(a, b):
    for j in i:
        if j not in new:
            new.append(j)
print new

#4
print list(set(a+b))

# 把字符串”k1:1|k2:2|k3:3”处理成 python 字典的形式:{'k3': 3, 'k2': 2, 'k1': 1}
string = "k1:1|k2:2|k3:3"
d = {}
for kv in string.split("|"):
    k, v = kv.split(":")
    if v.isdigit():
        v = int(v)
    d[k] = v
print d

dict1 = {'zhangsan': '2341', 'lisi': '9102', 'tiantian': '3258'}
dict2 = {2341: 'zhangsan', 9102: 'lisi', 3258: 'tiantian'}
dict3 = dict(name='zhangsan', id='lisi')
print dict1
print dict2
print dict2.pop(2341)
print dict2
print dict2.items()

# 字典合并
dict1 = {'zhangsan': '2341', 'lisi': '9102', 'tiantian': '3258'}
dict2 = {'wangyi': '2341', 'zhangsan': '9889', 'lisi': '7540'}
dict1.update(dict2)
print dict1

# 字符串格式化的一个延伸用法
template = '''
    <html>
        <head>
            <title>%(title)s</title>
        </head>
            <body>
                <h1>%(h1)s</h1>
                <p>%(text)s</p>
            </body>
    </html>
'''
data = {'h1': '我的主页', 'title': '笨方法学Python', 'text': '欢迎来到Python学习小站'}
print template % data

# 去除字典中value重复的项
dic = {'zhangsan':100, 'lisi':65, 'tianlaoshi':65, 'liulaoshi':99.9}
for k, v in dic.items():
    if dic.values().count(v) > 1:
        del dic[k]
print dic

# switch
list_id = [2341, 3102, 3258, 7540, 7541]
list_name = ['zhangsan', 'lisi', 'tiantian', 'liuze', 'mayun']
dic_new = dict(zip(list_id, list_name))
print dic_new
print dict([[2341,'zhangsan'],[3102,'lisi'],[3258,'tiantian'],[7540,'liuze'],[7541,'mayun']])

# 排序
data = {
    'JiaNaiLiang': 60,
    'LiXiaoLu': 75,
    'TiaoLaoShi': 99,
    'MaSu': 88,
    'KongLingHui': 35,
    'LiuLaoShi': 100
}
print sorted(data.values())
print sorted(data.keys())
print sorted(data.items())

def my_sort(d):
    return d[1]
print sorted(data.items(), key=my_sort)

print sorted(data.items(), key=lambda x: x[1])
print sorted(data.items(), key=lambda x: x[0])

# 习题：成绩计算

# 1
data = {
     'JiaNaiLiang': 60,
     'LiXiaoLu': 75,
     'TianLaoShi': 99,
     'MaSu': 88,
     'KongLingHui': 35,
     'LiuLaoShi': 100
}
total = 0.0
for s in data.values():
    total += s
avg = total/len(data.values())
print "学生的语文平均分为：%.2f" % avg

result = sorted(data.items(), key=lambda x:x[1], reverse=True)
print "学霸是：%s" % result[0][0]
print "学渣是：%s" % result[-1][0]

import collections
d1 = collections.OrderedDict()
for i in result:
    d1[i[0]] = i[1]
print d1

# 2
data = {
    'JiaNaiLiang': [60, 68, 45],
    'LiXiaoLu': [10, 28, 5],
    'TianLaoShi': [44, 86, 73],
    'MaSu': [99, 95, 95],
    'KongLingHui': [98, 65, 100],
    'LiuLaoShi': [77, 97, 65]
}

for k, v in data.items():
    total = 0
    for s in v:
        total += s
    if total/len(v) < 60:
        print k

yuwen = []
shuxue = []
yingyu = []
for v in data.values():
    yuwen.append(v[0])
    shuxue.append(v[1])
    yingyu.append(v[2])
print '语文最高分：%d, 数学最高分：%d, 英语最高分：%d' % (max(yuwen), max(shuxue), max(yingyu))
print '语文最高分：%.2f, 数学最高分：%.2f, 英语最高分：%.2f' % (sum(yuwen)/float(len(yuwen)),
                                                          sum(shuxue)/float(len(shuxue)),
                                                          sum(yingyu)/float(len(yingyu))
                                                          )
yuwen = {}
shuxue = {}
yingyu = {}
for k, v in data.items():
    yuwen[k] = v[0]
    shuxue[k] = v[1]
    yingyu[k] = v[2]

print '语文学霸：%s, 数学学霸：%s, 英语学霸：%s' % (
        sorted(yuwen.items(), key=lambda x: x[1], reverse=True)[0][0],
        sorted(shuxue.items(), key=lambda x: x[1], reverse=True)[0][0],
        sorted(yingyu.items(), key=lambda x: x[1], reverse=True)[0][0]
    )



