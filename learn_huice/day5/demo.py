#coding:utf-8

class Employee:
    id = 0

    def __init__(self, name, phone, salary, department):
        Employee.id = Employee.id + 1
        Department.ALL+=1
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
    ALL = 0
    def __init__(self, name):
        self.eps = []
        self.__name = name

    def get_name(self):
        return self.__name

    def get_count(self):
        return len(self.eps)

    def get_employees(self):
        for e in self.eps:
            info = '工号-{id} ，姓名-{name} ，手机号-{phone}，工资-{salary}'.format(
                id=e.id, name=e.name, phone=e.phone, salary=e.get_salary()
            )
            print info

    @staticmethod
    def get_all():
        return Department.ALL

    # @classmethod
    # def get_all(cls):
    #     return cls.ALL

if __name__ == '__main__':
        hr = Department('hr')
        jishu = Department('jishu')
        zhangsan = Employee('zhangsan', '13800000000', 3000, hr)
        lisi = Employee('lisi', '15000000000', 5000, hr)
        tianlaoshi = Employee('tianlaoshi', 18000000000, 10000, jishu)
        print zhangsan.get_salary()
        print zhangsan.get_info()
        print hr.get_count()
        hr.get_employees()
        print Department.get_all()