from django.test import TestCase

# Create your tests here.


# x=1
# d={}
# d[x]=12
# print(d)


#
# class Animal():
#    x=12
#
#    def running(self):
#        print(self.x)
#
#
# class Dog(Animal):
#
#     def __init__(self, name):
#         self.name = name
#
# alex=Dog("alex")
#
# alex.running()


temp=[]
l=[1,2,3]
temp.append(123)

temp.extend(l)

print(temp)