'''
整型：int
状态：等级，身份证号，年龄
'''
# level=10 #level=int(10)
# print(level,type(level),id(level))


'''
浮点型：float
状态：薪资，身高，体重
'''
# salary=3000.3 #salary=float(3000.3)
# print(salary,type(salary),id(salary))


'''
字符串：在引号（单引号，双引号，三引号）里定义的一堆字符
状态：描述性的内容，比如名字，性别，国籍
'''
# gender='male' #gender=str('male')
# print(type(gender))

# info="my name is egon i'm a teacher"
#
# msg='''
# xxxx
# yyy
# zzz
# '''
# print(msg)


# x=1
# y=2.3
# res=x+y
# print(res)

#字符只能跟字符串之间进行+或者*
# info1='hello'
# info2='world'
# res=info1+info2
# print(res)

# print('egon'*10)
# print(''*10)

# print('='*10)
# print('hello world')
# print('='*10)


'''
列表：在[]内，用逗号分隔开，存放多个任意类型的元素
状态：有序存放多个值
'''

# info='''
# name:xxx
# age:18
# sex:male
# '''
# print(info)

# info=['egon',18,'male',['欧德博爱','education',70]] #info=list([...])=
# print(info[0])
# print(info[3])
# print(info[3][0])


'''
字典类型：定义花括号内，用逗号分割key:value,value可以是任意类型，但是key必须不可变类型
状态：存放多个值
'''
    #  name  age  sex   company
# info=['egon',18,'male',['欧德博爱','education',70]]
# info[2]

    #  name  age  sex   company
info={
    'name':'egon',
    'age':18,
    'sex':'male',
    'company':['欧德博爱','education',70]
} #info=dict({....})
# print(info,type(info),id(info))

# print(info['sex'])
# print(info['company'][2])
#
#
#
# info={
#     'name':'egon',
#     'age':18,
#     'sex':'male',
#     'company':{'name':'欧德博爱','type':'education','emp_count':70}
# }
#
# print(info['company']['type'])



#
# dic={0:'egon',1:'xxx',2:'yyy'}
#
# print(dic[0])

# stduents=['egon','alex','wxx','yxx']


'''
布尔：True,False
状态：成立，不成立，用来做逻辑运算---》判断
'''

print(type(True))

age=38
print(age > 18)




