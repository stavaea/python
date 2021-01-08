#1、开放封闭原则：对扩展开放，对修改是封闭

#2、装饰器：装饰它人的，器指的是任意可调用对象，现在的场景装饰器-》函数，被装饰的对象也是-》函数
#原则：1、不修改被装饰对象的源代码 2、不修改被装饰对象的调用方式
#装饰器的目的：在遵循1,2的前提下为被装饰对象添加上新功能

#错误的示范
# import time
#
# def index():
#     time.sleep(3)
#     print('welecome to index')
#
# def timmer(func):
#     start=time.time()
#     func()
#     stop=time.time()
#     print('run time is %s' %(stop-start))
#
# timmer(index)



import time
def index():
    time.sleep(3)
    print('welecome to index')

def timmer(func):
    # func=index #最原始的index
    def inner():
        start=time.time()
        func() #最原始的index
        stop=time.time()
        print('run time is %s' %(stop-start))
    return inner

index=timmer(index) #index=inner
# print(f)
index() #inner()