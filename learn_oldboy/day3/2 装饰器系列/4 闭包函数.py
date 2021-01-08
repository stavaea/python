#闭包函数：
#1 定义在函数内部的函数
#2 该函数的函数体代码包含对外部作用域（而不是全局作用域）名字的引用
#3 通常将闭包函数用return返回，然后可以在任意使用
# z=1
# def outer():
#     x=1
#     y=2
#     def inner():
#         print(x,y)
#         # print(z)
#     return inner
#
# f=outer()
# print(f.__closure__[0].cell_contents)
# print(f.__closure__[1].cell_contents)
# print(f.__closure__)


# def bar():
#     x=111121
#     y=2222
#     f()
#
# bar()




# def foo(x,y):
#     print(x+y)
#
# foo(1,2)

# def outter():
#     x=1
#     y=2
#     def foo():
#         print(x+y)
#     return foo
#
#
# f=outter()
#
# f()



#爬页面:闭包函数为我们提供了一种新的为函数传参的方式
import requests #pip3 install requests

# def get(url):
#     response=requests.get(url)
#     if response.status_code == 200:
#         print(len(response.text))
#
# get('https://www.baidu.com')
# get('https://www.baidu.com')
# get('https://www.baidu.com')

def outter(url):
    # url = 'https://www.baidu.com'
    def get():
        response=requests.get(url)
        if response.status_code == 200:
            print(len(response.text))
    return get

baidu=outter('https://www.baidu.com')
python=outter('https://www.python.org')
# baidu()
# baidu()
# baidu()



