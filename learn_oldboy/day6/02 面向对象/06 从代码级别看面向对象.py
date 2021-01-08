'''
#1、在没有学习类这个概念时，数据与功能是分离的
def exc1(host,port,db,charset,sql):
    conn=connect(host,port,db,charset)
    res=conn.execute(sql)
    return res

def exc2(host,port,db,charset,proc_name)
    conn=connect(host,port,db,charset)
    res=conn.call_proc(prco_name)
    return res

#每次调用都需要重复传入一堆参数
exc1('127.0.0.1',3306,'db1','utf8','select * from tb1;')
exc2('127.0.0.1',3306,'db1','utf8','存储过程的名字')

exc1('127.0.0.1',3306,'db1','utf8','select * from tb2;')

#2、在没有学习类这个概念时，数据与功能是分离的
host='127.0.0.1'
port=3306
db='db1'
charset='utf-8'

x=1
y=2

def exc1(sql):
    conn=connect(host,port,db,charset)
    res=conn.execute(sql)
    return res

def exc2(proc_name)
    conn=connect(host,port,db,charset)
    res=conn.call_proc(prco_name)
    return res

def func1():
    print(x)
    print(y)

def func2():
    print(x)
    print(y)

#每次调用都需要重复传入一堆参数
exc1('select * from tb1;')
exc2('utf8','存储过程的名字')

exc1('select * from tb2;')

func()
'''

# class Mysqlhandle:
#     def __init__(self,host,port,db,charset='utf-8'):
#         self.host=host
#         self.port=port
#         self.db=db
#         self.charset=charset
#         self.conn=connect(host,port,db,charset)
#
#     def exc1(self,sql):
#         return self.conn.execute(sql)
#
#     def exc2(self,proc_name)
#         return self.conn.call_proc(prco_name)
#
# obj1=Mysqlhandle('127.0.0.1',3306,'db1')
#
# obj1.exc1('select * from t1')
# obj1.exc1('select * from t2')
# obj1.exc1('select * from t3')

# obj2=Mysqlhandle('10.10.10.9',3306,'db2')
# obj2.exc1('select * from t1 where id > 3')






