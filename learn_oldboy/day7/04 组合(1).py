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
#     def __init__(self,name,age,sex,course,stu_id,year,mon,day):
#         OldboyPeople.__init__(self,name,age,sex)
#         self.course=course
#         self.stu_id=stu_id
#
#         self.year=year
#         self.mon=mon
#         self.day=day
#
#     def learn(self):
#         print('%s is learning' %self.name)
#
#     def tell_info(self):
#         print('我是学生：',end='')
#         # self.tell_info() #stu1.tell_info()
#         OldboyPeople.tell_info(self)
#
#     def tell_birth(self):
#         print('出生日期是:<%s-%s-%s>' %(self.year,self.mon,self.day))
#
# class OldboyTeacher(OldboyPeople):
#     def __init__(self, name, age, sex, level,salary,year,mon,day):
#         OldboyPeople.__init__(self, name, age, sex)
#         self.level=level
#         self.salary=salary
#
#         self.year=year
#         self.mon=mon
#         self.day=day
#
#     def tell_birth(self):
#         print('出生日期是:<%s-%s-%s>' %(self.year,self.mon,self.day))
#
#     def teach(self):
#         print('%s is teaching' % self.name)
#
#     def tell_info(self):
#         print('我是老师：', end='')
#         OldboyPeople.tell_info(self)
#
#
# stu1=OldboyStudent('牛榴弹',18,'male','Python',1,1983,3,11)
# teacher1=OldboyTeacher('啊狗',18,'female',10,4000,1990,2,17)
#
#
# stu1.tell_birth()
# teacher1.tell_birth()
#
#
#






# class OldboyPeople:
#     school = 'Oldboy'
#
#     def __init__(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#
#     def tell_info(self):
#         print('<名字:%s 年龄:%s 性别:%s>' % (self.name, self.age, self.sex))
#
#
# class OldboyStudent(OldboyPeople):
#     def __init__(self, name, age, sex, course, stu_id,):
#         OldboyPeople.__init__(self, name, age, sex)
#         self.course = course
#         self.stu_id = stu_id
#
#
#
#     def learn(self):
#         print('%s is learning' % self.name)
#
#     def tell_info(self):
#         print('我是学生：', end='')
#         # self.tell_info() #stu1.tell_info()
#         OldboyPeople.tell_info(self)
#
# class OldboyTeacher(OldboyPeople):
#     def __init__(self, name, age, sex, level, salary):
#         OldboyPeople.__init__(self, name, age, sex)
#         self.level = level
#         self.salary = salary
#
#     def teach(self):
#         print('%s is teaching' % self.name)
#
#     def tell_info(self):
#         print('我是老师：', end='')
#         OldboyPeople.tell_info(self)
#
# class Date:
#     def __init__(self,year,mon,day):
#         self.year = year
#         self.mon = mon
#         self.day = day
#
#     def tell_birth(self):
#         print('出生日期是:<%s-%s-%s>' % (self.year, self.mon, self.day))
#
# stu1 = OldboyStudent('牛榴弹', 18, 'male', 'Python', 1,)
# date_obj1=Date(1983, 3, 11)
# stu1.birth=date_obj1
#
#
# teacher1 = OldboyTeacher('啊狗', 18, 'female', 10, 4000)
# date_obj2=Date( 1990, 2, 17)
# teacher1.birth=date_obj2
#
#
# # print(stu1.birth)
# # print(teacher1.birth)
#
# stu1.birth.tell_birth() #date_obj1.tell_birth()
# teacher1.birth.tell_birth()




#
# class OldboyPeople:
#     school = 'Oldboy'
#
#     def __init__(self, name, age, sex,date_obj):
#         self.name = name
#         self.age = age
#         self.sex = sex
#         self.birth = date_obj
#
#     def tell_info(self):
#         print('<名字:%s 年龄:%s 性别:%s>' % (self.name, self.age, self.sex))
#
# class OldboyStudent(OldboyPeople):
#     def __init__(self, name, age, sex, course, stu_id,date_obj):
#         OldboyPeople.__init__(self, name, age, sex,date_obj)
#         self.course = course
#         self.stu_id = stu_id
#
#
#     def learn(self):
#         print('%s is learning' % self.name)
#
#     def tell_info(self):
#         print('我是学生：', end='')
#         # self.tell_info() #stu1.tell_info()
#         OldboyPeople.tell_info(self)
#
# class OldboyTeacher(OldboyPeople):
#     def __init__(self, name, age, sex, level, salary,date_obj):
#         OldboyPeople.__init__(self, name, age, sex,date_obj)
#         self.level = level
#         self.salary = salary
#
#     def teach(self):
#         print('%s is teaching' % self.name)
#
#     def tell_info(self):
#         print('我是老师：', end='')
#         OldboyPeople.tell_info(self)
#
# class OldboySale(OldboyPeople):
#     def __init__(self,name,age,sex,kpi,date_obj):
#         OldboyPeople.__init__(self,name,age,sex,date_obj)
#         self.kpi=kpi
#
#     def tell_info(self):
#         print('我是销售: ',end='')
#         OldboyPeople.tell_info(self)
#
# class Date:
#     def __init__(self,year,mon,day):
#         self.year = year
#         self.mon = mon
#         self.day = day
#
#     def tell_birth(self):
#         print('出生日期是:<%s-%s-%s>' % (self.year, self.mon, self.day))
#
# date_obj1=Date(1983, 3, 11)
# sale1=OldboySale('歪歪',38,'male',7.3,date_obj1)
# # sale1.birth=date_obj1
# # sale1.tell_info()
#
# sale1.birth.tell_birth()









class OldboyPeople:
    school = 'Oldboy'

    def __init__(self, name, age, sex,date_obj):
        self.name = name
        self.age = age
        self.sex = sex
        self.birth = date_obj

    def tell_info(self):
        print('<名字:%s 年龄:%s 性别:%s>' % (self.name, self.age, self.sex))

class OldboyStudent(OldboyPeople):
    def __init__(self, name, age, sex, stu_id,date_obj):
        OldboyPeople.__init__(self, name, age, sex,date_obj)
        self.courses=[]
        self.stu_id = stu_id


    def learn(self):
        print('%s is learning' % self.name)

    def tell_info(self):
        print('我是学生：', end='')
        # self.tell_info() #stu1.tell_info()
        OldboyPeople.tell_info(self)

class OldboyTeacher(OldboyPeople):
    def __init__(self, name, age, sex, level, salary,date_obj):
        OldboyPeople.__init__(self, name, age, sex,date_obj)
        self.level = level
        self.salary = salary
        self.courses=[]

    def teach(self):
        print('%s is teaching' % self.name)

    def tell_info(self):
        print('我是老师：', end='')
        OldboyPeople.tell_info(self)

class OldboySale(OldboyPeople):
    def __init__(self,name,age,sex,kpi,date_obj):
        OldboyPeople.__init__(self,name,age,sex,date_obj)
        self.kpi=kpi

    def tell_info(self):
        print('我是销售: ',end='')
        OldboyPeople.tell_info(self)

class Date:
    def __init__(self,year,mon,day):
        self.year = year
        self.mon = mon
        self.day = day

    def tell_birth(self):
        print('出生日期是:<%s-%s-%s>' % (self.year, self.mon, self.day))

class Course:
    def __init__(self,name,price,period):
        self.name=name
        self.price=price
        self.period=period

    def tell_info(self):
        print('课程详细信息:<%s,%s,%s>' %(self.name,self.price,self.period))

Python=Course('python自动化养猪',3000,'3mon')
Linux=Course('大数据分析-linux',3000,'3mon')
date_obj=Date(1993,3,13)

# teacher1=OldboyTeacher('egon',18,'male',100,3000,date_obj)
# teacher1.courses.append(Python)
# teacher1.courses.append(Linux)
#
# # print(teacher1.courses)
# for course in teacher1.courses:
#     course.tell_info()


stu1=OldboyStudent('xxxx',28,'female',1,date_obj)
# print(stu1.courses)

stu1.courses.append(Python)
stu1.courses.append(Linux)

print(stu1.courses)
