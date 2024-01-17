# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2024/1/12 18:06
# @Author : waxberry
# @File : 18条超好用的Python小技巧.py
# @Software : PyCharm


# 处理用户的多个输入
# 有时我们需要从用户那里获得多个输入，以便使用循环或任何迭代，一般的写法如下:
# bad practice码
n1 = input("enter a number : ")
n2 = input("enter a number : ")
n2 = input("enter a number : ")
print(n1, n2, n3)
# 但是更好的处理方法如下:
# good practice
n1, n2, n3 = input("enter a number : ").split()
print(n1, n2, n3)

# 处理多个条件语句
# 如果我们在代码中需要检查多个条件语句，此时我们可以使用
all()
# 或any()
# 函数来实现我们的目标。一般来说, 当我们有多个 and 条件时使用all()，当我们有多个 or 条件时使用any()。
# 这种用法将使我们的代码更加清晰易读，可以方便我们在调试时不会遇到麻烦。
# 对于all()的一般例子如下:
size = "lg"
color = "blue"
price = 50
# bad practice
if size == "lg" and color == "blue" and price < 100:
    print("Yes, I want to but the product.")
# 更好的处理方法如下:
# good practice
conditions = [
    size == "lg",
    color == "blue",
    price < 100,
]
if all(conditions):
    print("Yes, I want to but the product.")
# 对于any()的一般例子如下:
# bad practice
size = "lg"
color = "blue"
price = 50
if size == "lg" or color == "blue" or price < 100:
    print("Yes, I want to but the product.")
# 更好的处理方法如下:
# good practice
conditions = [
    size == "lg",
    color == "blue",
    price < 100,
]
if any(conditions):
    print("Yes, I want to but the product.")

# 判断数字奇偶性
# 这很容易实现，我们从用户那里得到输入，将其转换为整数，检查
# 对数字2的求余操作，如果余数为零，则它是偶数。
print('odd' if int(input('Enter a number: ')) % 2 else 'even')

# 交换变量
# 在Python中如果需要交换变量的值，我们无需定义临时变量来操作。我们一般使用如下代码来实现变量交换:
v1 = 100
v2 = 200  # bad practicetemp = v1v1 = v2v2 = temp
# 但是更好的处理方法如下:
v1 = 100
v2 = 200
# good practice
v1, v2 = v2, v1

# 判断字符串是否为回文串
# 将字符串进行反转最简单的实现方式为[::-1], 代码如下:
print("John Deo"[::-1])

# 反转字符串
# 在Python中判断一个字符串是否为回文串, 只需要使用语句
# string.find(string[::-1]) == 0, 示例代码如下:
v1 = "madam"  # is a palindrome string
v2 = "master"  # is not a palindrome string
print(v1.find(v1[::-1]) == 0)  # True
print(v1.find(v2[::-1]) == 0)  # False

# 尽量使用Inline if statement
# 大多数情况下，我们在条件之后只有一个语句，因此使用Inline if statement
# 可以帮助我们编写更简洁的代码。举例如下, 一般的写法为:
name = "ali"
age = 22  # bad practicesif name:print(name)if name and age > 18:print("user is verified")
# 但是更好的处理方法如下:
# a better approach
print(name if name else "")
""" here you have to define the else condition too"""
# good practice
name and print(name)
age > 18 and name and print("user is verified")

# 删除list中的重复元素
# 我们不需要遍历整个list列表来检查重复元素，我们可以简单地使用
set()
# 来删除重复元素, 代码如下:
lst = [1, 2, 3, 4, 3, 4, 4, 5, 6, 3, 1, 6, 7, 9, 4, 0]
print(lst)
unique_lst = list(set(lst))
print(unique_lst)

# 找到list中重复最多的元素
# 在Python中可以使用max()函数并传递list.count作为key，即可找出列表list中重复次数最多的元素, 代码如下:
lst = [1, 2, 3, 4, 3, 4, 4, 5, 6, 3, 1, 6, 7, 9, 4, 0]
most_repeated_item = max(lst, key=lst.count)
print(most_repeated_item)

# list生成式
# Python中我最喜欢的功能就是list comprehensions, 这个特性可以使我们编写非常简洁功能强大的代码，而且这些代码读起来几乎像自然语言一样通俗易懂。
# 举例如下:
numbers = [1, 2, 3, 4, 5, 6, 7]
evens = [x for x in numbers if x % 2 is 0]
odds = [y for y in numbers if y not in evens]
cities = ['London', 'Dublin', 'Oslo']


def visit(city):
    print("Welcome to " + city)


for city in cities:
    visit(city)

# 使用 * args传递多个参数
# 在Python中我们可以使用 * args来向函数传递多个参数, 举例如下:


def sum_of_squares(n1, n2):
    return n1 ** 2 + n2 ** 2


print(sum_of_squares(2, 3))
# output: 13
"""
what ever if you want to pass, multiple args to the function 
as n number of args. so let's make it dynamic.
"""


def sum_of_squares(*args):
    return sum([item ** 2 for item in args])


# now you can pass as many parameters as you want
print(sum_of_squares(2, 3, 4))
print(sum_of_squares(2, 3, 4, 5, 6))

# 在循环时处理下标
# 有时我们在工作中, 想要获得循环中元素的下标, 一般来说, 比较优雅的写法如下:
lst = ["blue", "lightblue", "pink", "orange", "red"]
for idx, item in enumerate(lst):
    print(idx, item)

# 拼接list中多个元素
# 在Python中一般使用Join()函数来将list中所有元素拼接到一起, 当然我们也可以在拼接的时候添加拼接符号, 样例如下:
names = ["john", "sara", "jim", "rock"]
print(", ".join(names))

# 将两个字典进行合并
# 在Python中我们可以使用{**dict_name, **dict_name2, …}将多个字典进行合并, 样例如下:
d1 = {"v1": 22, "v2": 33}
d2 = {"v2": 44, "v3": 55}
d3 = {**d1, **d2}
print(d3)
# 结果如下:
{'v1': 22, 'v2': 44, 'v3': 55}

# 使用两个list生成一个字典
# 在Python中, 如果我们需要将两个列表中对应的元素组成字典, 那么我们可以使用zip功能来方便地做到这一点。代码如下:
keys = ['a', 'b', 'c']
vals = [1, 2, 3]
zipped = dict(zip(keys, vals))

# 字典按照value进行排序
# 在Python中我们使用sorted()函数来按照字典的value来对其进行排序.代码如下:
d = {
    "v1": 80,
    "v2": 20,
    "v3": 40,
    "v4": 20,
    "v5": 10,
}
sorted_d = dict(sorted(d.items(), key=lambda item: item[1]))
print(sorted_d)
# 当然我们也可以使用itemgetter()来替代上述lambda函数, 代码如下:
from operator import itemgettersorted_d = dict(sorted(d.items(), key=itemgetter(1)))
# 更进一步, 我们也可以通过传递reverse = True对其进行降序排序:
sorted_d = dict(sorted(d.items(), key=itemgetter(1), reverse=True))

# Pretty print
# 在Python中使用Print()函数, 有时候的输出贼拉拉丑陋, 此时我们使用pprint可以使输出更加美观, 样例如下:
from pprint import pprintdata = {"name": "john deo", "age": "22",
                                 "address": {"contry": "canada", "state": "an state of canada :)",
                                             "address": "street st.34 north 12"},
                                 "attr": {"verified": True, "emialaddress": True}, }
print(data)
pprint(data)
# 输出如下:
{'name': 'john deo', 'age': '22',
 'address': {'contry': 'canada', 'state': 'an state of canada :)', 'address': 'street st.34 north 12'},
 'attr': {'verified': True, 'emialaddress': True}}
{'address': {'address': 'street st.34 north 12', 'contry': 'canada', 'state': 'an state of canada :)'}, 'age': '22',
 'attr': {'emialaddress': True, 'verified': True}, 'name': 'john deo'}
# 可见使用pprint函数可以让字典的输出更加容易阅读

# 反转列表
# Python中通常有两种反转列表的方法：切片或reverse()函数调用。
# 这两种方法都可以反转列表，但需要注意的是内置函数reverse()会更改原始列表，而切片方法会创建一个新列表。
# 但是他们的表现呢？哪种方式更有效？让我们看一下下面的例子：
# 使用切片
$ python - m timeit - n 1000000 - s'import numpy as np' 'mylist=list(np.arange(0, 200))' 'mylist[::-1]' 1000000 loops, best of 5: 15.6 usec per loop

# 使用reverse()
$ python - m timeit - n 1000000 - s 'import numpy as np' 'mylist=list(np.arange(0, 200))' 'mylist.reverse()' 1000000 loops, best of 5: 10.7 usec per loop
# 这两种方法都可以反转列表，但需要注意的是内置函数reverse()会更改原始列表，而切片方法会创建一个新列表。
# 显然，内置函数reverse()比列表切片方法更快！