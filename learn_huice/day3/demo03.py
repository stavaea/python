#coding:utf-8
class Student:
    school = 'huice'
    __expenses = '8800'

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.score = 0
        self.i = 0

    def set_score(self, score):
        self.score = score

    def get_score(self):
        return self.score

    def __len__(self):
        return len(self.name)

    # def __iter__(self):
    #     return self
    # #
    # def next(self):
    #     a = (self.name, self.age, self.score, self.school, self.__expenses)
    #     if self.i < len(a):
    #         b = a[self.i]
    #         self.i += 1
    #         return b
    #
    # def __getitem__(self, n):
    #     a = (self.name, self.age, self.score, self.school, self.__expenses)
    #     if n < len(a):
    #         return a[n]
    #     else:
    #         raise IndexError('index out of range')
    #
    # def __getattr__(self, item):
    #     return 'unknown'

std1 = Student('李四', 18)
# std1.set_score(85)
# print std1



for a in std1:
    if a == None:
        break
    else:
        print a

print std1[2]
#
#
# def set_age(self, age):
#     self.age = age
#
#
# from types import MethodType
#
# std1.set_age = MethodType(set_age, std1, Student)
# # Student.set_age = MethodType(set_age, None, Student)
# std1.set_age(25)
# print std1.age
#
# std2 = Student('lisi', 18)
# std2.set_age(40)
# print std2.age
