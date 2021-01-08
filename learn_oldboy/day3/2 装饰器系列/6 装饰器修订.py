#装饰器语法：在被装饰对象正上方单独一行写上，@装饰器名

# #改进一：
# import time
# def timmer(func):
#     def inner():
#         start=time.time()
#         res=func()
#         stop=time.time()
#         print('run time is %s' %(stop-start))
#         return res
#     return inner
#
# @timmer #index=timmer(index)
# def index():
#     time.sleep(1)
#     print('welecome to index')
#     return 1111
#
# res=index() #res=inner()
# print(res)


#改进二：
import time
def timmer(func):
    def inner(*args,**kwargs):
        start=time.time()
        res=func(*args,**kwargs)
        stop=time.time()
        print('run time is %s' %(stop-start))
        return res
    return inner

# @timmer #index=timmer(index)
# def index(name):
#     time.sleep(1)
#     print('welecome %s to index' %name)
#     return 1111
# res=index('egon') #res=inner('egon')
# print(res)

@timmer #home=timmer(home)
def home(name):
    print('welcome %s to home page' %name)

home('egon') #inner('egon')