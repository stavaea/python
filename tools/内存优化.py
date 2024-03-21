# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2024/3/12 14:55
# @Author : waxberry
# @File : 内存优化.py
# @Software : PyCharm


# 1. 在类定义中使用__slots__

class Author:
    def __init__(self, name, age):
        self.name = name
        self.age = age

me = Author('Yang Zhou', 30)
me.job = 'Software Engineer'
print(me.job)

class Author:
    __slots__ = ('name', 'age')
    def __init__(self, name, age):
        self.name = name
        self.age = age
me = Author('Yang Zhou', 30)
me.job = 'Software Engineer'
print(me.job)

# 一个简单的比较程序
import sys
class Author:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class AuthorWithSlots:
    __slots__ = ['name', 'age']

    def __init__(self, name, age):
        self.name = name
        self.age = age


# Creating instances
me = Author('Yang', 30)
me_with_slots = AuthorWithSlots('Yang', 30)

# Comparing memory usage
memory_without_slots = sys.getsizeof(me) + sys.getsizeof(me.__dict__)
memory_with_slots = sys.getsizeof(me_with_slots)  # __slots__ classes don't have __dict__

print(memory_without_slots, memory_with_slots)
# 152 48
print(me.__dict__)
# {'name': 'Yang', 'age': 30}
print(me_with_slots.__dict__)


# 2. 使用生成器
def number_generator():
    for i in range(100):
        yield i

numbers = number_generator()
print(numbers)

print(next(numbers))
#0
print(next(numbers))
#1

# 比较一下生成器和列表
import sys
numbers = []
for i in range(100):
    numbers.append(i)

def number_generator():
    for i in range(100):
        yield i

numbers_generator = number_generator()
print(sys.getsizeof(numbers_generator))
#112
print(sys.getsizeof(numbers))
#920

# 定义生成器的更简便的方法：
import sys
numbers = [i for i in range(100)]
numbers_generator = (i for i in range(100))
print(sys.getsizeof(numbers_generator))
#112
print(sys.getsizeof(numbers))
#920



# 3. 利用内存映射文件支持大文件处理
# 使用mmap进行文件处理的方法：
import mmap
with open('test.txt', "r+b") as f:
    # memory-map the file, size 0 means whole file
    with mmap.mmap(f.fileno(), 0) as mm:
        # read content via standard file methods
        print(mm.read())
        # read content via slice notation
        snippet = mm[0:10]
        print(snippet.decode('utf-8'))


# 4. 减少全局变量的使用



# 5. 利用逻辑运算符的短路求值
result_a = expensive_function_a()
result_b = expensive_function_b()
result = result_a if result_a else result_b
# 上面的代码能够工作，但实际上执行了两个内存效率低下的函数。获取相同结果的更聪明的方法如下：
result = expensive_function1() or expensive_function2()



# 6. 谨慎选择数据类型
import sys
my_tuple = (1, 2, 3, 4, 5)
my_list = [1, 2, 3, 4, 5]
print(sys.getsizeof(my_tuple))
#80
print(sys.getsizeof(my_list))
#120

# 如果列表的元素都是相同类型，使用数组会更节省内存：
import sys
import array
my_list = [i for i in range(1000)]
my_array = array.array('i', [i for i in range(1000)])
print(sys.getsizeof(my_list))
#8856
print(sys.getsizeof(my_array))
#4064