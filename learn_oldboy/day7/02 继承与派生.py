# coding=utf-8
'''
1 什么是继承
    是一种新建类的方式，新建的类称为子类，子类会遗传父类的属性，可以减少代码冗余
    在python中，子类（派生类）可以继承一个或者多个父类（基类，超类）

'''
# class Parent1:
#     pass
#
# class Parent2(object):
#     pass
#
# class Sub1(Parent1):
#     pass
#
# class Sub2(Parent1,Parent2):
#     pass
#
#
# # print(Sub1.__bases__)
# # print(Sub2.__bases__)
#
# print(Parent1.__bases__)
# print(Parent2.__bases__)


#在Python2中类分为两种：
#1、经典类：指的就是没有继承object类的类，以及该类的子类
#2、新式类：指的就是继承object类的类，以及该类的子类

#在Python3中统一都为新式类
class OldboyPeople:
    school = 'Oldboy'

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def tell_info(self):
        print('<名字:%s 年龄:%s 性别:%s>' %(self.name,self.age,self.sex))

class OldboyStudent(OldboyPeople):
    def learn(self):
        print('%s is learning' %self.name)

    def tell_info(self, ):
        print('我是学生：', end='')
        print('<名字:%s 年龄:%s 性别:%s>' % (self.name, self.age, self.sex))

class OldboyTeacher(OldboyPeople):
    def teach(self):
        print('%s is teaching' %self.name)

    def tell_info(self, ):
        print('我是老师：', end='')
        print('<名字:%s 年龄:%s 性别:%s>' % (self.name, self.age, self.sex))

# stu1=OldboyStudent('牛榴弹',18,'male')
# teacher1=OldboyTeacher('egon',18,'male')

# print(stu1.__dict__)
# print(stu1.school)
# print(stu1.x)

# stu1.tell_info()
# teacher1.tell_info()



#属性查找
class Foo:
    def f1(self):
        print('Foo.f1')

    def f2(self): #self=obj
        print('Foo.f2')
        self.f1() #obj.f1()

class Bar(Foo):
    def f1(self):
        print('Bar.f1')

obj=Bar()
print(obj.__dict__)
obj.f2()




