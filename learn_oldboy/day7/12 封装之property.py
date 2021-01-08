# class People:
#     def __init__(self,name,age,height,weight):
#         self.name=name
#         self.age=age
#         self.height=height
#         self.weight=weight
#
#     @property
#     def bmi(self):
#         return self.weight / (self.height ** 2)
#
# egon=People('egon',18,1.80,75)
# egon.height=1.82
# # print(egon.bmi())
#
# print(egon.bmi)





class People:
    def __init__(self,name,):
        self.__name=name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,obj):
        if type(obj) is not str:
            raise TypeError('name must be str')
        self.__name=obj

    @name.deleter
    def name(self):
        # del self.__name
        raise PermissionError('不让删')

egon=People('egon')

# print(egon.name)

# egon.name='EGON'
# egon.name=35357
# print(egon.name)

del egon.name

# print(egon.name)