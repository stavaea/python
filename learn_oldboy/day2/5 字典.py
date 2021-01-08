#用途：存放多个值，key:value,存取速度快

#定义：key必须是不可变类型（int，float，str，tuple），value可以是任意类型
# info={'name':'egon','age':18,'sex':'male'} #info=dict({'name':'egon','age':18,'sex':'male'})

#了解
# info=dict(age=18,sex='male',name='egon')
# print(info)

# info=dict([('name','egon'),('age',18),('sex','male')])
# info=dict([['name','egon'],['age',18],['sex','male']])
# print(info)

# info={}.fromkeys(['name','age','sex'],None)
# info={}.fromkeys('hello',None)
# print(info)

#优先掌握的操作：
#1、按key存取值：可存可取
# d={'name':'egon'}
# print(d['name'])
#
# d['age']=18
# print(d)

#2、长度len
# info={'name':'egon','age':18,'sex':'male'}
# print(len(info))

#3、成员运算in和not in
# info={'name':'egon','age':18,'sex':'male'}
# print('name' in info)

#4、删除
info={'name':'egon','age':18,'sex':'male'}
# print(info.pop('name'))
# print(info)
# print(info.popitem()) #('sex', 'male')
# print(info)

#5、键keys()，值values()，键值对items() #了解
# print(info.keys())
# print(list(info.keys())[0])

# print(list(info.values()))
# print(list(info.items()))

#6、循环
# info={'name':'egon','age':18,'sex':'male'}
# for k in info:
#     print(k,info[k])


#其他需要掌握的方法
# info={'name':'egon','age':18,'sex':'male'}
# print(info['hobbies'])
# print(info.get('hobbies','没有'))
# print(info.pop('name1',None))

# d={'x':1,'y':2,'name':'EGON'}
# info.update(d)
# print(info)

# info={'name':'egon','sex':'male'}
# value=info.setdefault('age',18)
# print(value)

# info={'name':'egon','age':16,'sex':'male'}
# value=info.setdefault('age',18) #如果key存在，则不修改，返回已经有的key对应的value
# print(value)
# print(info)

info={'name':'egon',}
# info['hobbies']=[]
# info['hobbies'].append('music')
# info['hobbies'].append('read')
# print(info)

info={'name':'egon',}
# if 'hobbies' not in info:
#     info['hobbies']=[]
# else:
#     info['hobbies'].append('music')

# hobbies_list=info.setdefault('hobbies',[])
# print(hobbies_list)
# hobbies_list.append('play')
# hobbies_list.append('read')
#
# print(info)


#二：该类型总结
# 1 存一个值or存多个值
#     可以存多个值，值都可以是任意类型,key必须是不可变类型
#
# 2 无序

# 3 可变or不可变
#     ！！！可变：值变，id不变。可变==不可hash
