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
# 类体代码在类的定义阶段就会立刻执行，
class Student:
    school='oldboy'

    def learn(self):
        print('is learning')

    def choose_course(self):
        print('choose course')

    # print('====run')


# print(Student)
# print(Student.__dict__)

#查看
# print(Student.school) #数据属性
# print(Student.learn) #函数属性

#增加
# Student.country='China'
# print(Student.country)

#修改
# Student.school='Oldboy'
# print(Student.school)

#删除
# del Student.country
# print(Student.country)

# print(Student.learn)
# Student.learn('xxxxx')


