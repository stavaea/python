#递归调用：在调用一个函数的过程中，直接或者间接又调用该函数本身，称之为递归调用
#递归必备的两个阶段：1、递推  2、回溯

# import sys
# print(sys.getrecursionlimit())
# sys.setrecursionlimit(2000)
# print(sys.getrecursionlimit())

# def func(n):
#     print('---->',n)
#     func(n+1)
#
# func(0)


# def bar():
#     print('from bar')
#     func()
#
# def func():
#     print('from func')
#     bar()
#
# func()


# age(5) = age(4) + 2
# age(4) = age(3) + 2
# age(3) = age(2) + 2
# age(2) = age(1) + 2
#
# age(1) = 18

# age(n)=age(n-1)+2 # n > 1
# age(1) = 18 #n = 1


# def age(n):
#     if n == 1:
#         return 18
#     return age(n-1) + 2
#
# res=age(5)
# print(res)


# l=[1,[2,[3,[4,[5,[6,[7,]]]]]]]
#
#
# def func(l):
#     for item in l:
#         if type(item) is list:
#             func(item)
#         else:
#             print(item)



# def func():
#     print('===>')
#     func()
#
# func()


