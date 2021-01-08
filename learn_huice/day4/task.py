#!/usr/bin/env python
#-*- coding:utf-8 -*-

'''1.
设计一个部门类Department，属性为部门名称（name）
需求：
	1.直接通过Department调用get_all方法，返回公司员工总数
	2.通过部门实例，调用方法get_count方法，返回部门员工数
	3.通过部门实例，调用方法get_employees()，显示该部门所有员工信息
	  格式为： 工号-xxx ，姓名-xxx ，手机号-xxx，工资-xxx
	提示：有人入职，员工数就要增加，部门存入员工对象

设计一个员工类Employee，员工属性有姓名（name）、手机号(phone)、工资(salary)、所属部门。
需求：
1.新员工入职时，分配一个不重复的工号。从1开始排列，已离职员工工号作废。
2.员工本人可以调用get_salary方法查询自己的工资
3.员工本人可以调用get_info方法查询自己的全部信息--字典形式

测试：人力资源部（小红）、技术部（田老师、刘老师）
	输出 每个部门的人员和公司总人数，输出两个部门的人员信息
'''

class Employee:
    id = 0

    def __init__(self, name, phone, salary, department):
        Employee.id = Employee.id + 1
        Department.All += 1
        self.id = Employee.id
        self.name = name
        self.phone = phone
        self.__salary = salary
        self.department = department
        department.eps.append(self)

    def get_salary(self):
        return self.__salary

    def get_info(self):
        dic = {}
        dic['name'] = self.name
        dic['phone'] = self.phone
        dic['salary'] = self.__salary
        dic['department'] = self.department.get_name()
        return dic

class Department:
    All = 0

    def __init__(self, name):
        self.eps = []
        self.__name = name

    def get_name(self):
        return self.__name

    def get_count(self):
        return len(self.eps)

    def get_employees(self):
        for e in self.eps:
            info = '工号-{id} ，姓名-{name} ，手机号-{phone}，工资-{salary}'.format(id=e.id,
                                         name=e.name, phone=e.phone, salary=e.get_salary())
            print(info)
    # def get_all():
    #     return Department.All

    @classmethod
    def get_all(cls):
        return cls.All


if __name__ == '__main__':
    hr = Department('hr')
    jishu = Department('jishu')
    zhangsan = Employee('zhangsan', '13000000000', 3000, hr)
    lisi = Employee('lisi', '13000000001', 3000, hr)
    tian = Employee('tian', '13000000000', 30000, jishu)
    print(zhangsan.get_salary())
    print(zhangsan.get_info())
    print(hr.get_count)
    hr.get_employees()
    print(jishu.get_all())

'''2.创建一个用户注册服务（server），其中有一个register方法。当用户名小于6位时，
抛出自定义异常--系统异常NameError的子类UserNameError，显示错误信息：用户名不能小于6位
'''
class UserNameError(NameError):
    pass

class Server:
    def register(self, user_name):
        if len(user_name) < 6:
            raise UserNameError('用户名不能小于6位')
        else:
            print ('注册成功')

try:
    Server().register('zzz')
except UserNameError, e:
    print(e)
