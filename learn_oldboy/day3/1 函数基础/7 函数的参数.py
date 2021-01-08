#函数的参数分类两种：
#形参：在定义阶段括号内指定的参数，相当于变量名
#实参：在调用阶段括号内传入的值称之为实参，相当于值
#在调用阶段，实参的值会绑定给形参，在调用结束后解除绑定
# def foo(x,y): #x=1,y=2
#     print(x,y)
#
# foo(1,2)

#在python中参数的分类：
#1、位置参数：按照从左到右的顺序依次定义的参数
#位置形参：必须被传值，多一个少一个都不行
#位置实参：与形参一一对应传值
# def foo(x,y):
#     print(x,y)
#
# foo(2,1)

#2、关键字参数：在函数调用时，按照key=value的形式定义的实参
#特点：指名道姓地给形参传值，不再依赖与位置
def foo(name,age,sex):
    print(name,age,sex)

# foo('egon',18,'male')
# foo(sex='male',age=18,name='egon',)
#注意：
#1、 关键字实参必须在位置实参的后面
#2、 不能为同一个参数赋值多次

# foo('egon',sex='male',age=18,name='egon')


#3、默认参数：在函数定义阶段，就已经为形参赋值了
#特点：定义阶段已经有值意味着调用阶段可以不用传值
#位置参数通常用于经常变化的参数，而默认参数指的是大多数情况下都一样的
# def foo(x,y=1):
#     print(x,y)

# foo(1,2)
# foo(y=3,x=1)
# foo(111)
# foo(x=1111)


# def register(name,age,sex='male'):
#     print(name,age,sex)
#
# register('egon1',18)
# register('egon2',18)
# register('egon3',18)
# register('alex',38,'female')

#注意：
#1、默认参数必须放到位置形参的后面
# def register(name,sex='male',age,):
#     print(name,age,sex)
#2、默认参数的值只在定义时被赋值一次
#3、默认的参数的值通常应该是不可变类型
# res=1
# def foo(x,y=res):
#     print(x,y)
#
# res=10
# foo('aaaaaaaa')


#4 可变长参数：在调用函数时，实参值的个数不固定
#实参的形式有：位置实参和关键字实参，
#形参的解决方案：*，**

#*args的用法
# def foo(x,y,*args): #z=(3,4,5,6)
#     print(x,y)
#     print(args)
#
# # foo(1,2,3,4,5,6)
#
# foo(1,2,*[3,4,5,6]) #foo(1,2,3,4,5,6)
# foo(*[1,2,3,4,5,6]) #foo(1,2,3,4,5,6)

# def foo(x,y):
#     print(x,y)
#
# foo(*(1,2)) #foo(1,2)

#**kwargs
# def foo(x,y,**kwargs): #kwargs={'c':5,'a':3,'b':4}
#     print(x,y)
#     print(kwargs)
#
# # foo(y=2,x=1,a=3,b=4,c=5)
#
# foo(y=2,**{'c':5,'x':1,'b':4,'a':3}) #foo(y=2,a=3,c=5,b=4)


# def foo(name,age):
#     print(name,age)

# foo(**{'name':'egon','age':18})
# foo({'name':'egon','age':18})



# def bar(x,y,z):
#     print(x,y,z)
#
# def wrapper(*args,**kwargs): #args=(1,),kwargs={'z':2,'y':3}
#     # print(args,kwargs)
#     bar(*args,**kwargs) #bar(*(1,),**{'z':2,'y':3}) #bar(1,z=2,y=3,)
#
# wrapper(1,z=2,y=3)



#命名关键字参数：指的是定义在*后的参数，该参数必须被传值（除非有它有默认值），而且必须按照key=value的形式传值
# def foo(x,y,*args,m=100000,n):
#     print(x,y)
#     print(args)
#     print(m,n)
#
# foo(1,2,3,n=4,)
# 
