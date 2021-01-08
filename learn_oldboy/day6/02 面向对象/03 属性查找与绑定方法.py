x=1
class Student:
    school='oldboy'
    # Name='xxx'

    def __init__(self,name,sex,age): #在调用类时会自动触发执行
        self.Name = name
        self.Sex = sex
        self.Age = age


        #stu1.Name='李三炮'
        #stu1.Sex='男'
        #stu1.Age=18

    def learn(self,x,y):
        print('%s is learning' %self.Name)
        print(x,y)

    def choose_course(self):
        print('choose course')

    def commit_hw():
        print('commit homework')

#1、查找一个对象的属性顺序是：先找对象自己的__dict__,再找类的__dict__
# stu1=Student('李三炮','男',18)
# # print(stu1.__dict__)
#
# # print(stu1.Name)
# # print(stu1.school)
# # print(stu1.x)

stu1=Student('李三炮','男',18)
stu2=Student('张铁蛋','女',38)
stu3=Student('武大郎','男',28)


# 2、类的数据属性是所有对象共享，所有对象都指向同一个内存地址
# stu1.school='xxx'
# Student.school='Oldgirl'
# print(Student.school,id(Student.school))
# print(stu1.school,id(stu1.school))
# print(stu2.school,id(stu2.school))
# print(stu3.school,id(stu3.school))

# 3、类中定义的函数是绑定给对象使用：
# 3.1：不同对象就是不同绑定方法
# 3.2：绑定给谁，就应该由谁来调用,谁来调用就会把谁当做第一个参数传给对应的函数
# print(Student.learn)
# print(stu1.learn)
# print(stu2.learn)
# print(stu3.learn)

# stu1.learn(1,2) #Student.learn(stu1,1,2)
# stu2.learn(1,3)
# stu3.learn(1,4)
# print(Student.learn)

# stu1.commit_hw()