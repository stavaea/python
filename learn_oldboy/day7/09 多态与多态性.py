# #1 多态：同一种事物的多种形态
# import abc
#
# class Animal(metaclass=abc.ABCMeta):
#     @abc.abstractmethod
#     def speak(self):
#         pass
#
# class Pig(Animal):
#     def speak(self):
#         print('哼哼')
#
# class Dog(Animal):
#     def speak(self):
#         print('汪汪')
#
# class People(Animal):
#     def speak(self):
#         print('say hello')
#
#
#
# people1=People()
# dog1=Dog()
# pig1=Pig()

#多态性：指的是在不考虑对象具体类型的情况下，直接使用对象（对象的方法）
# people1.speak()
# dog1.speak()
# pig1.speak()

# def talk(obj):
#     obj.speak()
#
# talk(people1) #people1.speak()
# talk(dog1)
# talk(pig1)


#list，str，tuple
# l=list([1,2,3])
# s=str('hello')
# t=tuple((1,'a',4,'b','c'))
#
# l.__len__()
# s.__len__()
# t.__len__()
#
# print(len(l))
# print(len(s))
# print(len(t))


#1 多态：同一种事物的多种形态
# import abc

# class Pig:
#     def speak(self):
#         print('哼哼')
#
# class Dog:
#     def speak(self):
#         print('汪汪')
#
# class People:
#     def speak(self):
#         print('say hello')
#
# class Radio:
#     def speak(self):
#         print('radio speak')
#
#
# people1=People()
# dog1=Dog()
# pig1=Pig()




import abc

class Disk:
    def read(self):
        print('disk read')

    def write(self):
        print('disk write')


class Process:
    def read(self):
        print('Process read')

    def write(self):
        print('Process write')