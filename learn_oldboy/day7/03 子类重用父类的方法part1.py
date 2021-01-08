# class OldboyPeople:
#     school = 'Oldboy'
#
#     def __init__(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#
#     def tell_info(self):
#         print('<名字:%s 年龄:%s 性别:%s>' %(self.name,self.age,self.sex))
#
# class OldboyStudent(OldboyPeople):
#     def learn(self):
#         print('%s is learning' %self.name)
#
#     def tell_info(self):
#         print('我是学生：',end='')
#         # self.tell_info() #stu1.tell_info()
#         OldboyPeople.tell_info(self)
#
# stu1=OldboyStudent('牛榴弹',18,'male')
# stu1.tell_info()




class OldboyPeople:
    school = 'Oldboy'

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def tell_info(self):
        print('<名字:%s 年龄:%s 性别:%s>' %(self.name,self.age,self.sex))

class OldboyStudent(OldboyPeople):
    def __init__(self,name,age,sex,course,stu_id):
        # self.name=name
        # self.age=age
        # self.sex=sex
        OldboyPeople.__init__(self,name,age,sex)
        self.course=course
        self.stu_id=stu_id

    def learn(self):
        print('%s is learning' %self.name)

    def tell_info(self):
        print('我是学生：',end='')
        # self.tell_info() #stu1.tell_info()
        OldboyPeople.tell_info(self)

stu1=OldboyStudent('牛榴弹',18,'male','Python',1)
stu1.tell_info()