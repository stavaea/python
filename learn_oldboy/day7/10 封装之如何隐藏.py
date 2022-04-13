# coding=utf-8
#封装：
#1、__开头的属性只是一种语法意义上的变形，并不会真的限制外部的访问
#2、这种变形只在类定义阶段发送一次，类定义之后再新增的__开头的属性不会变形
#3、这种隐藏只对外不对内，因为类内部定义的属性在类定义阶段统一发生变形
# class Foo:
#     __N=1 #_Foo__N=1
#     def __init__(self,x,y):
#         self.x=x
#         self.__y=y #self._Foo__y=y
#
#     def __f1(self): #_Foo__f1
#         print('f1')
#
#     def f2(self):
#         print(self.__N,self.__y) #print(self._Foo__N,self._Foo__y)

# print(Foo.__N)
# print(Foo.__f1)
# print(Foo.__dict__)
# print(Foo._Foo__N)
# print(Foo._Foo__f1)

# obj=Foo(1,2)
# print(obj.__dict__)
# print(obj._Foo__y)

# Foo.__M=2
# print(Foo.__dict__)
# print(Foo.__M)

# obj=Foo(1,2)
# print(obj.__dict__)
# obj.__z=3
# print(obj.__dict__)
# print(obj.__z)

# obj=Foo(1,2)
# obj.f2()
# print(obj.__N)


class Foo:
    def __f1(self): #_Foo__f1
        print('Foo.f1')

    def f2(self):
        print('Foo.f2')
        self.__f1() #b._Foo__f1()

class Bar(Foo):
    def __f1(self): #_Bar__f1
        print('Bar.f1')


b=Bar()
b.f2()
