# school='xxxxx'
class Student:
    school='Oldboy'

    def __init__(self,name,age,sex):
        if type(name) is not str:
            raise TypeError('名字必须是str')
        self.name=name
        self.age=age
        self.sex=sex
        # return None #不允许
        #stu1.name='egon'
        #stu1.age=18
        #stu1.sex='sex'

    def learn(self):
        print('%s is learning' %self.name)

# print(Student.__dict__)
# print(Student.school)
# print(Student.learn)
# Student.learn()
# Student.x=1

# stu1=Student(35357,18,'sex') #Student.__init__(stu1,'egon',18,'sex')
stu1=Student('egon1',18,'sex') #Student.__init__(stu1,'egon',18,'sex')
stu2=Student('egon2',18,'sex') #Student.__init__(stu1,'egon',18,'sex')
# stu2=Student()
# stu3=Student()

# print(stu1.__dict__)

# print(stu1.name)
# stu1.school='xxxx'
# print(stu1.school)

print(Student.learn)
print(stu1.learn)
print(stu2.learn)
# stu1.learn()

# stu1.learn() #learn(stu1)
# stu2.learn() #learn(stu1)

stu1.learn() #Student.learn(stu1)






