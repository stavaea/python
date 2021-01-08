#名称空间指的是：存放名字与值绑定关系的地方，

#内置名称空间（python解释器启动就有）：python解释器内置的名字，max，len，print
#全局名称空间（执行python文件时生效）：文件级别定义的名字
# x=1
# def func():pass
# import time
# if x == 1:
#     y=2

#局部名称空间（函数调用时生效，调用结束失效）:函数内部定义的名字
# func()

#加载顺序：内置---》全局----》局部名称空间
#访问名字的顺序：局部名称空间===》全局----》内置
# x=1
# print(x)

# print(max)

# max=2
# def func():
#     # max=1
#     print(max)
#
# func()


# x='gobal'
# def f1():
#     # x=1
#     def f2():
#        # x=2
#        def f3():
#            # x=3
#            print(x)
#        f3()
#     f2()
#
# f1()



#全局作用域（全局范围）：内置名称空间与全局名称空间的名字，全局存活，全局有效，globals()
#局部作用域（局部范围）：局部名称空间的名字,临时存活，局部有效,locals()
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx=111111111111111111111
# print(globals())
# print(dir(globals()['__builtins__']))

# print(locals() is globals())

# def func():
#     yyyyyyyyyyyyyyyyyyyyyyyy=22222222
#     print(globals())
#     print(locals())
#
# func()


# x=100
# def func():
#     global x
#     x=1
#
# func()
# print(x)



# x='global'
# def f1():
#     # x=1
#     def f2():
#         nonlocal x
#         x=0
#     f2()
#     print('===f1 innter--->',x)
#
# f1()
# print(x)





#强调两点：
#1、打破函数层级限制来调用函数
# def outter():
#     def inner():
#         print('inner')
#     return inner
#
# f=outter()
# # print(f)
#
# def bar():
#     f()
# bar()


#2、函数的作用域关系是在函数定义阶段就已经固定了，与调用位置无关
x=1
def outter():
    # x=2
    def inner():
        print('inner',x)
    return inner

f=outter()
# print(f)
# x=1111111111111111111111111111111111111111111111111111111111111111111111111111111111
def bar():
    x=3
    f()
# x=1111111111111111111111111111111111111111111111111111111111111111111111111111111111
bar()
x=1111111111111111111111111111111111111111111111111111111111111111111111111111111111







