#return的特点：
#1、 函数内可以有多个return，但是只能执行一次return
#2、 执行return函数就立刻结束，并且return的后值当做本次调用的结果返回
# def foo(x,y):
#     return x+y
#
# res=foo(1,2)
#
# def my_max(x,y):
#     if x >= y:
#         return x
#     else:
#         return y
#
# res=my_max(1,2)
# print(res)

# def foo():
#     print('first')
#     return 1
#     print('second')
#     return 2
#     print('third')
#     return 3
#
# res=foo()
# print(res)




#1、返回的值没有类型限制
# def bar():
#     print('from bar')
#
# def foo():
#     return bar
# print(foo() is bar)

#2:return返回值的个数
#2.1: 没有return:默认返回None
#2.2：return 值：值本身
#3.3： return 多个值:返回一个元组

# def foo():
#     pass
#     return 1,'a',[1,2]
# print(foo())


#函数调用的三种形式
def my_max(x,y):
    if x >= y:
        return x
    else:
        return y

# res1=my_max(1,2)

# res2=my_max(1,2)*10

# res3=my_max(my_max(1,2),3)
# print(res3)

range(len([1,2,3]))