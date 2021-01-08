import time
def timmer(func):
    def inner(*args,**kwargs):
        start=time.time()
        res=func(*args,**kwargs)
        stop=time.time()
        print('run time is %s' %(stop-start))
        return res
    return inner

def auth2(engine='file'):
    def auth(func): # func=index
        def inner(*args,**kwargs):
            if engine == 'file':
                name=input('name>>: ').strip()
                password=input('password>>: ').strip()
                if name == 'egon' and password == '123':
                    print('login successful')
                    return func(*args,**kwargs)
                else:
                    print('login err')
            elif engine == 'mysql':
                print('mysql auth')
            elif engine == 'ldap':
                print('ldap auth')
            else:
                print('engin not exists')
        return inner
    return auth


@auth2(engine='file')
@timmer
def index(name):
    time.sleep(1)
    print('welecome %s to index' %name)
    return 1111

res=index('egon')
print(res)