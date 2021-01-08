#封装数据属性的目的：外部无法直接访问数据属性，类内部开放接口，然后可以在接口内严格控制对属性的增删改查操作
# class People:
#     def __init__(self,name,age):
#         # self.__name=name
#         # self.__age=age
#         self.set_info(name,age)
#
#     def tell_info(self):
#         print("姓名:<%s> 年龄:<%s>" %(self.__name,self.__age))
#
#     def set_info(self,name,age):
#         if type(name) is not str:
#             raise TypeError('name must be str')
#         if type(age) is not int:
#             raise TypeError('age must be int')
#
#         self.__name=name
#         self.__age=age
#
# p=People('egon',18)
#
# # print(p.__name,p.__age)
# # p.tell_info()
#
# # p.set_info('EGON',20)
# p.set_info(3537,20)
# p.tell_info()

#封装方法的目的是：隔离复杂度

class ATM:
    def __card(self):
        print('插卡')
    def __auth(self):
        print('用户认证')
    def __input(self):
        print('输入取款金额')
    def __print_bill(self):
        print('打印账单')
    def __take_money(self):
        print('取款')

    def withdraw(self):
        self.__card()
        self.__auth()
        self.__input()
        self.__print_bill()
        self.__take_money()
