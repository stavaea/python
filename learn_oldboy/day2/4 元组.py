#作用：存多个值，对比列表来说，元组不可变（是可以当做字典的key的），主要是用来读

#定义：与列表类型比，只不过[]换成()
age=(11,22,33,44,55) #本质age=tuple((11,22,33,44,55))
# print(type(age))
# age[0]=12

# t=(1,2,['a','b'])
# print(id(t[2]))
# t[2][0]='A'
# print(id(t[2]))
# print(t)

#优先掌握的操作：
#1、按索引取值(正向取+反向取)：只能取
#2、切片(顾头不顾尾，步长)
# age=(11,22,33,44,55)
# print(age[0:3])
# print(age)
#3、长度
# age=(11,22,33,44,55)
# print(len(age))
#4、成员运算in和not in
# age=(11,22,33,44,55)
# print(11 in age)
#5、循环
# for item in age:
#     print(item)


#掌握
# age=(11,22,33,44,55)
# print(age.index(33))
# print(age.index(33333))

# print(age.count(33))



#二：该类型总结
# 1 存一个值or存多个值
#     可以存多个值，值都可以是任意类型

# 2 有序

# 3 可变or不可变
#     ！！！不可变：值变，id就变。不可变==可hash