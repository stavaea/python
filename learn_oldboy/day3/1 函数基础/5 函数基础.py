'''
1 为什么要有函数？没有函数带来的困扰？
    组织结构不清晰，可读性差
    代码冗余
    可扩展性差

2 什么是函数
    具备某一个功能的工具---》函数

    事先准备工具-》函数的定义
    拿来就用、重复使用-》函数的调用
    ps：先定义后调用

3 函数的分类：
    内置函数：len，max(10,11)，help(函数名)
    自定义函数：def
        语法：
            def 函数名(参数1，参数2，...):
                """注释"""
                函数体
                return 返回值
'''

#'函数即是变量'
# def print_tag():
#     print('*'*20)
#
# def print_msg(): #print_msg=<function print_msg at 0x00000000027EA8C8>
#     print('hello world')
#
#
# # print(print_msg)
# # print(print_tag)
#
# print_tag()
# print_msg()
# print_tag()



#2、定义函数阶段都发生了什么事：只检测语法，不执行代码
#定义阶段
# sex='male'
# def auth():
#     sex
#
#     name=input('name>>: ').strip()
#     password=input('password>>: ').strip()
#     if name =='egon' and password == '123':
#         print('login successfull')
#     else:
#         print('user or password err')
#
# #调用阶段
# auth()


#3、函数的使用：先定义后调用

# def bar():
#     print('from bar')
#
# def foo():
#     print('from foo')
#     bar()
#
# foo()

# #定义阶段
# def foo():
#     print('from foo')
#     bar()
#
# def bar():
#     print('from bar')
#
# #调用
# foo()


# # 定义阶段
# def foo():
#     print('from foo')
#     bar()
#
# # 调用
# foo()
#
# def bar():
#     print('from bar')
#






#4 定义函数的三种形式
#第一种：无参函数
#第二种：有参函数
#第三种：空函数

# def auth():
#     name=input('name>>: ').strip()
#     password=input('password>>: ').strip()
#     if name =='egon' and password == '123':
#         print('login successfull')
#     else:
#         print('user or password err')
#

# def my_max(x,y):
#     if x >= y:
#         print(x)
#     else:
#         print(y)
#
# my_max(1,2)



# def auth(name,password):
#     if name =='egon' and password == '123':
#         print('login successfull')
#     else:
#         print('user or password err')
#
# def interactive():
#     name=input('name>>: ').strip()
#     password=input('password>>: ').strip()
#     auth(name,password)
#
# interactive()



def auth():
    pass

def put():
    pass

def get():
    pass

def ls():
    pass









