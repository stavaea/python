# pythons=['egon','axx','ysb','wxx']
# linuxs=['egon','oldboy','oldgirl','smallboy','smallgirl']
#
# python_linux=[]
#
# for student in pythons:
#     if student in linuxs:
#         python_linux.append(student)
#
# print(python_linux)

#作用：关系运算，去重
#定义集合：{}内用逗号分割每个元素都必须是不可变类型,元素不能重复,无序
# s={1,'a',[1,2]} #TypeError: unhashable type: 'list'
# s={1,2,3,1} #s=set({1,2,3,1})
# print(s,type(s))


#优先掌握的操作：
#1、长度len
# s={1,2,3,1} #s=set({1,2,3,1})
# print(len(s))

#2、成员运算in和not in
# names={'egon','alex'}
# print('egon' in names)

#3、|合集
pythons={'egon','axx','ysb','wxx'}
linuxs={'egon','oldboy','oldgirl','smallboy','smallgirl'}

#4、&交集:同时报名两门课程的学生
# print(pythons & linuxs)
# print(pythons.intersection(linuxs))

#5、|合集:老男孩所有的学生
# print(pythons | linuxs)
# print(pythons.union(linuxs))

#6、^对称差集:没有同时报名两门课程
# print(pythons ^ linuxs)
# print(pythons.symmetric_difference(linuxs))

#7.1  -差集：只报名python课程的学生
# print(pythons - linuxs)
# print(pythons.difference(linuxs))

#7.2  -差集：只报名linux课程的学生
# print(linuxs-pythons)

#8 父集:>,>=,子集：<，<=
# s1={1,2,3}
# s2={1,2,}
# print(s1 >= s2)
# print(s1.issuperset(s2))
# print(s2.issubset(s1))

# linuxs={'egon','oldboy','oldgirl','smallboy','smallgirl'}
# for student in linuxs:
#     print(student)



#了解的知识点
# s1={1,2,3}
# s2={1,2,}
# print(s1-s2)
# print(s1.difference(s2))
# s1.difference_update(s2) #s1=s1.difference(s2)
# print(s1)

# s2={1,2,3,4,5,'a'}
# print(s2.pop())

# s2.add('b')
# print(s2)

# s2.discard('b')
# s2.remove('b') #删除的元素不存在则报错
# print(s2)


# s1={1,2,3,4,5,'a'}
# s2={'b','c',}
# print(s1.isdisjoint(s2)) #两个集合没有共同部分时，返回值为True


# s2={1,2,3,4,5,'a'}
# s2.update({6,7,8})
# print(s2)


# l=['a','b',1,'a','a']
# print(list(set(l)))

# print(set('hello'))
# print(set({'a':1,'b':2,'c':3}))



name='egon'





