#迭代器：迭代的工具

#1 什么是迭代：指的是一个重复的过程，每一次重复称为一次迭代，并且每一次重复的结果是下一次重复的初始值
# while True:
#     print('=====>')

# l=['a','b','c']
# count=0
# while count < len(l):
#     print(l[count])
#     count+=1

#2 为什么要有迭代器？
#对于序列类型：str，list，tuple，可以依赖索引来迭代取值，
# 但是对于dict，set，文件,python必须为我们提供一种不依赖于索引的迭代取值的方式-》迭代器



#3 可迭代的对象(下列都是)：obj.__iter__
# name='egon'
# l=[1,2,3]
# t=(1,2,3)
# d={'name':'egon','age':18,'sex':'male'}
# s={'a','b','c'}
# f=open('a.txt','w',encoding='utf-8')
#
# name.__iter__
# l.__iter__
# t.__iter__
# d.__iter__
# s.__iter__
# f.__iter__

#4 迭代器对象（文件是）：obj.__iter__,obj.__next__
# f.__iter__
# f.__next__


#总结：
#1 可迭代对象不一定是迭代器对象
#2 迭代器对象一定是可迭代的对象
#3 调用obj.__iter__()方法,得到的是迭代器对象(对于迭代器对象，执行__iter__得到的仍然是它本身)


# d={'name':'egon','age':18,'sex':'male'}
# d_iter=d.__iter__()

# f=open('a.txt','w',encoding='utf-8')
# f_iter=f.__iter__().__iter__().__iter__().__iter__()
#
# print(f_iter is f)


# d={'name':'egon','age':18,'sex':'male'}
# d_iter=d.__iter__()
#
# print(d_iter.__next__())
# print(d_iter.__next__())
# print(d_iter.__next__())
# print(d_iter.__next__()) #迭代器d_iter没有值了，就会抛出异常StopIteration



# f=open('a.txt','r',encoding='utf-8')
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# f.close()


# l=['a','b','c']
# l_iter=l.__iter__()
#
# print(l_iter.__next__())
# print(l_iter.__next__())
# print(l_iter.__next__())
# print(l_iter.__next__())



# d={'name':'egon','age':18,'sex':'male'}
# d_iter=iter(d) #d_iter=d.__iter__()
#
# #len(obj) 等同于obj.__len__()
#
# while True:
#     try:
#         print(next(d_iter)) #print(d_iter.__next__())
#     except StopIteration:
#         break
#
# print('=>>>')
# print('=>>>')
# print('=>>>')
# print('=>>>')


#for循环详解:
#1、调用in后的obj_iter=obj.__iter__()
#2、k=obj_iter.__next__()
#3、捕捉StopIteration异常，结束迭代
# d={'name':'egon','age':18,'sex':'male'}
# for k in d:
#     print(k)


#总结迭代器的优缺点：
#优点:
#1、提供一种统一的、不依赖于索引的取值方式，为for循环的实现提供了依据
#2、迭代器同一时间在内存中只有一个值——》更节省内存，

#缺点：
#1、只能往后取，并且是一次性的
#2、不能统计值的个数，即长度

# l=[1,2,3,4,5,6]
# l[0]
# l[1]
# l[2]
# l[0]

# l_iter=l.__iter__()
# # print(l_iter)
# print(next(l_iter))
# print(next(l_iter))
# print(next(l_iter))
# print(next(l_iter))
# print(next(l_iter))
# print(next(l_iter))
# print(next(l_iter))
#
# l_iter=l.__iter__()
# print(next(l_iter))
# print(next(l_iter))
# print(next(l_iter))

# print(len(l_iter))





















