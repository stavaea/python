class Animal(object):
    def run(self):
        print 'Animal is running...'

    def eat(self):
        print 'Animal is eating...'

class Dog(Animal):
    def run(self):
        print 'Dog is running...'

    def eat(self):
        print 'Dog is eating...'

class Bird(Animal):
    def eat(self):
        print 'Bird is eating...'

class Cat(Animal):
    def run(self):
        print 'Cat is running...'

    def eat(self):
        print 'Cat is eating...'


class Person():
    def __init__(self, name):
        self.name = name



huahua = Cat()
huahua.run()

Person('tianlaoshi').feed(huahua)

xiaotiantian = Dog()
xiaoweiwei = Bird()
xiaofengfeng = Cat()
print type(xiaotiantian)
print type(xiaoweiwei)
print isinstance(xiaotiantian, Dog)
print isinstance(xiaotiantian, Bird)
print isinstance(xiaotiantian, Animal)