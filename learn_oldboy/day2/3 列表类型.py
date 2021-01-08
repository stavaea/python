#作用：多个装备，多个爱好，多门课程，多个女朋友等

#定义：[]内可以有多个任意类型的值，逗号分隔
# my_girl_friends=['alex','wupeiqi','yuanhao',4,5] #本质my_girl_friends=list([...])
# print(list('hello'))
# print(int('123'))
# print(str(123))

#优先掌握的操作：
#1、按索引存取值(正向存取+反向存取)：即可存也可以取
# my_girl_friends=['alex','wupeiqi','yuanhao',4,5]

#2、切片(顾头不顾尾，步长)

#3、长度
# print(my_girl_friends.__len__())
# print(len(my_girl_friends))
#4、成员运算in和not in
# print('wupeiqi' in my_girl_friends)

#5、追加
# my_girl_friends[5]=3 #IndexError: list assignment index out of range
# my_girl_friends.append(6)
# print(my_girl_friends)

#6、删除
my_girl_friends=['alex','wupeiqi','yuanhao',4,5]
#单纯的删除
# del my_girl_friends[0]
# print(my_girl_friends)

# res=my_girl_friends.remove('yuanhao')
# print(my_girl_friends)
# print(res)
# print(my_girl_friends)

#删除并拿到结果:取走一个值
# res=my_girl_friends.pop(2)
# res=my_girl_friends.pop()
# print(res)

# my_girl_friends=['alex','wupeiqi','yuanhao',4,5]
# print(my_girl_friends.pop(0)) #'alex'
# print(my_girl_friends.pop(0)) #'wupeqi'
# print(my_girl_friends.pop(0)) #'yuanhao'
#7、循环
# my_girl_friends=['alex','wupeiqi','yuanhao',4,5]

# i=0
# while i < len(my_girl_friends):
#     print(my_girl_friends[i])
#     i+=1

# for item in my_girl_friends:
#     print(item)

# for i in range(10):
#     if i== 3:
#         break
#         # continue
#     print(i)
# else:
#     print('===>')







#掌握的方法
my_girl_friends=['alex','wupeiqi','yuanhao','yuanhao',4,5]
# my_girl_friends.insert(1,'egon')
# print(my_girl_friends)

# my_girl_friends.clear()
# print(my_girl_friends)

# l=my_girl_friends.copy()
# print(l)

# print(my_girl_friends.count('yuanhao'))

# l=['egon1','egon2']
# my_girl_friends.extend(l)
# my_girl_friends.extend('hello')
# print(my_girl_friends)

# my_girl_friends=['alex','wupeiqi','yuanhao','yuanhao',4,5]
# print(my_girl_friends.index('wupeiqi'))
# print(my_girl_friends.index('wupeiqissssss'))

# my_girl_friends.reverse()
# my_girl_friends=['alex','wupeiqi','yuanhao','yuanhao',4,5]
# my_girl_friends.reverse()
# print(my_girl_friends)


# l=[1,10,4,11,2,]
# l.sort(reverse=True)
# print(l)

# x='healloworld'
# y='he2'

# print(x > y)

# l=['egon','alex','wupei']
# l.sort()
# print(l)



#二：该类型总结
# 1 存一个值or存多个值
#     可以存多个值，值都可以是任意类型

# 2 有序

# 3 可变or不可变
#     ！！！可变：值变，id不变。可变==不可hash


#练习
# 1. 有列表data=['alex',49,[1900,3,18]]，分别取出列表中的名字，年龄，出生的年，月，日赋值给不同的变量

# 2. 用列表模拟队列（先进先出）
l=[]
# l.append('alex')
# l.append('wupeiqi')
# l.append('yuanhao')
# l.append('huowentian')
# print(l)

# print(l.pop(0))
# print(l.pop(0))
# print(l.pop(0))
# print(l.pop(0))



# l=[]
# l.insert(0,'alex')
# l.insert(0,'wupeqiqi')
# l.insert(0,'yuanhao')
# l.insert(0,'huowentian')
# print(l)
#
# print(l.pop())
# print(l.pop())
# print(l.pop())
# print(l.pop())

# 3. 用列表模拟堆栈(先进后出，后进先出)

# 4. 有如下列表，请按照年龄排序（涉及到匿名函数）