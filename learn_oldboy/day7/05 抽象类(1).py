# import abc
#
# class Animal(metaclass=abc.ABCMeta):
#     @abc.abstractmethod
#     def eat(self):
#         pass
#
#     @abc.abstractmethod
#     def run(self):
#         pass
#
#
# class People(Animal):
#     def eat(self):
#         pass
#     def run(self):
#         pass
#
# class Pig(Animal):
#     def eat(self):
#         pass
#     def run(self):
#         pass
#
# peo1=People()
# pig1=Pig()

import abc

class File(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def read(self):
        pass

    @abc.abstractmethod
    def write(self):
        pass

class Disk(File):
    def read(self):
        print('disk read')

    def write(self):
        print('disk write')


class Process(File):
    def read(self):
        print('Process read')

    def write(self):
        print('Process write')

d=Disk()
p=Process()

d.read()
d.write()

p.read()
p.write()



