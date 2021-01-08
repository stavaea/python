class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say(self):
        print("旺旺~")
        return self

    def run(self):
        print("哒哒~")

p = Person("Alex", 9000)
p.say().run()
# p.run()
