#__str__
# l=list([1,2,3,4])
# print(l)

# class People:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
#     def __str__(self):
#         return '<name:%s age:%s>' %(self.name,self.age)
#
# egon=People('egon',18)
# print(egon) #print(egon.__str__())
#


#__del__
# f=open('a.txt','w',encoding='utf-8')
# f.read()
# f.close()


# class Foo:
#     def __del__(self):
#         print('del---->')
#
# obj=Foo()
# del obj
# print('主')



class Mysql:
    def __init__(self,host,port):
        self.host=host
        self.port=port
        self.conn=Connect(host,port)

    def __del__(self):
        self.conn.close()

m=Mysql('1.1.1.1',3306)
m.conn.execute('select * from db.user;')


