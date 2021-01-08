from functools import wraps
import time
def timmer(func):
    @wraps(func)
    def inner(*args,**kwargs):
        start=time.time()
        res=func(*args,**kwargs)
        stop=time.time()
        print('run time is %s' %(stop-start))
        return res
    # inner.__doc__=func.__doc__
    # inner.__name__=func.__name__
    return inner

@timmer
def index(name): #index=inner
    '''index 函数。。。。。'''
    time.sleep(1)
    print('welecome %s to index' %name)
    return 1111

# res=index('egon')
# print(res)

print(help(index))