#1 什么是生成器：只要在函数体内出现yield关键字，那么再执行函数就不会执行函数代码，会得到一个结果，该结果就是生成器
def func():
    print('=====>1')
    yield 1
    print('=====>2')
    yield 2
    print('=====>3')
    yield 3

#生成器就是迭代器
# g=func()
#
# res1=next(g)
# print(res1)
#
#
# res2=next(g)
# print(res2)
#
#
# res3=next(g)
# print(res3)


#yield的功能：
#1、yield为我们提供了一种自定义迭代器对象的方法
#2、yield与return的区别1：yield可以返回多次值 #2：函数暂停与再继续的状态是由yield帮我们保存的

# obj=range(1,1000000000000000000000000000000000000000000000000000000000000000,2)
# obj_iter=obj.__iter__()
# print(next(obj_iter))
# print(next(obj_iter))
# print(next(obj_iter))
# print(next(obj_iter))
# print(next(obj_iter))


# def my_range(start,stop,step=1):
#     while start < stop:
#         yield start #start=1
#         start+=step #start=3
#
#
# g=my_range(1,5,2)
# print(g)

# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# for i in my_range(1,5,2):
#     print(i)


#小练习：:tail -f access.log | grep '404'
# import time
# def tail(filepath):
#     with open(filepath,'rb') as f:
#         f.seek(0,2)
#         while True:
#             line=f.readline()
#             if line:
#                 yield line
#             else:
#                 time.sleep(0.05)
#
# def grep(lines,pattern):
#     for line in lines:
#         line=line.decode('utf-8')
#         if pattern in line:
#             yield line
#
#
# lines=grep(tail('access.log'),'404')
#
# for line in lines:
#     print(line)




#了解知识点：yield表达式形式的用法
def eater(name):
    print('%s ready to eat' %name)
    food_list=[]
    while True:
        food=yield food_list#food=yield='一盆骨头'
        food_list.append(food)
        print('%s start to eat %s' %(name,food))


e=eater('alex')

#首先初始化：
print(e.send(None)) # next(e)
#然后e.send:1 从暂停的位置将值传给yield  2、与next一样
print(e.send('一桶泔水'))
print(e.send('一盆骨头'))


























