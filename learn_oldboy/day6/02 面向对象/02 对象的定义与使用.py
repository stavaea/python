'''
1、面向过程与面向对象
    面向过程：核心是过程二字，过程即解决问题的步骤，就是先干什么再干什么
    基于该思想写程序就好比在设计一条流水线，是一种机械式的思维方式
    优点：复杂的过程流程化，进而简单化
    缺点：扩展性差

    面向对象：核心是对象二字，对象是特征与技能的结合体
    基于该思想编写程序就好比在创造一个世界，世界是由一个个对象组成，是一种“上帝式”的思维方式
    优点：可扩展性强
    缺点：编程复杂高，容易出现过度设计

2、类
    对象是特征与技能的结合体，类就是一系列对象相似的特征与技能的结合体
    在现实世界中：一定是先有的一个个具体存在的对象，后总结出的类
    在程序中：一定保证先定义类，后产生对象

3、站在老男孩学校的角度
现实中的对象：
    对象1：
        特征
            学校=老男孩
            名字=李三炮
            性别=男
            年龄=18
        技能
            study
            选课

    对象2：
        特征
            学校=老男孩
            名字=张铁蛋
            性别=女
            年龄=38
        技能
            study
            选课

    对象3：
        特征
            学校=老男孩
            名字=武大郎
            性别=男
            年龄=28
        技能
            study
            选课

    对象4：
        特征
            学校=老男孩
            名字=egon
            性别=男
            年龄=18
        技能
            教学


现实中的老男孩学生类：
    老男孩学生类
        相似的特征
            学校=老男孩
        相似的技能
            study
            选课

'''
class Student:
    school='oldboy'

    #stu1,'李三炮','男',18
    def __init__(self,name,sex,age): #在调用类时会自动触发执行
        self.Name=name
        self.Sex=sex
        self.Age = age

        #stu1.Name='李三炮'
        #stu1.Sex='男'
        #stu1.Age=18

    def learn(self):
        print('is learning')

    def choose_course(self):
        print('choose course')

#调用类的过程又称之为实例化:stu1=Student('李三炮','男',18)
#1、得到一个返回值，即对象，该对象是一个空对象stu1
#2、Student.__init__(stu1,'李三炮','男',18)

stu1=Student('李三炮','男',18)
# print(stu1.__dict__)
# print(stu1.Name,stu1.Age,stu1.Sex)

stu2=Student('张铁蛋','女',38)
stu3=Student('武大郎','男',28)
# print(stu2.__dict__)
# print(stu3.__dict__)

# print(stu1,stu2,stu3)

# print(stu2.Name)