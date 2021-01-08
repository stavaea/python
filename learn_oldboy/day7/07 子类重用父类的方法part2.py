class OldboyPeople:
    school = 'Oldboy'

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def tell_info(self):
        print('<名字:%s 年龄:%s 性别:%s>' %(self.name,self.age,self.sex))

class OldboyStudent(OldboyPeople):
    def __init__(self,name,age,sex,course):
        # OldboyPeople.__init__(self,name,age,sex)
        super(OldboyStudent,self).__init__(name,age,sex)
        self.course=course

    def tell_info(self):
        print('我是学生: ',end='')
        # OldboyPeople.tell_info(self)
        super(OldboyStudent,self).tell_info()


stu1=OldboyStudent('egon',18,'male','python')

# print(stu1.name,stu1.age,stu1.sex,stu1.course)
stu1.tell_info()

