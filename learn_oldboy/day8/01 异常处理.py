#1 什么是异常？
# 异常是错误发生的信号，一旦程序出错，就会产生一个异常，应用程序未处理该异常，
# 异常便会抛出，程序随之终止

#2、常见异常类型
#I:语法错误应该在程序运行前修正
# if 1 >2
#     print('xxxxx')

#II:逻辑错误
# x

# l=[]
# l[10000] #IndexError

# class Foo:
#     pass
# Foo.x #AttributeError:

# k={'x':1}
# k['y'] #KeyError

# 1/0 #ZeroDivisionError

# for i in 3: #TypeError:
#     pass


# age=input('>>: ') #ValueError
# age=int(age)

#3、如何处理异常
# print('====>start<=====')
#
# try:
#     l=[]
#     print(l[1111])
#     print('====>1')
#     print('====>2')
#     print('====>3')
# except IndexError:
#     pass
#
# print('====>end<=======')



# print('====>start<=====')
# try:
#     l=[]
#     print(l[1111])
#     print('====>1')
#     print('====>2')
#     print('====>3')
# except IndexError as e:
#     print('===>',e)
#
# print('====>end<=======')




# print('====>start<=====')
# try:
#     l=[]
#     # print(l[1111])
#     print('====>1')
#     d={}
#     d['k']
#     print('====>2')
#     print('====>3')
# except IndexError as e:
#     print('===>',e)
# except KeyError as e:
#     print('----',e)
#
# print('====>end<=======')



# print('====>start<=====')
# try:
#     l=[]
#     # print(l[1111])
#     print('====>1')
#     d={}
#     d['k']
#     print('====>2')
#     print('====>3')
# except IndexError:
#     pass
# except KeyError:
#     pass
# except Exception as e:
#     print('万能异常--->',e)
#
# print('====>end<=======')



# print('====>start<=====')
# try:
#     l=[]
#     print(l[1111])
#     # print('====>1')
#     d={}
#     # d['k']
#     # print('====>2')
#     # print('====>3')
# except IndexError:
#     pass
# except KeyError:
#     pass
# except Exception as e:
#     print('万能异常--->',e)
# else:
#     print('没有异常发生的时候触发')
# finally:
#     print('有没有异常都触发')
#
#
# print('====>end<=======')



'''
try:
    conn=connect('1.1.1.1',3306)
    conn.execute('select * from db1.t1')
finally:
    conn.close()
'''

# stus=['egon','alex','wxxx']
ip_list=[
    # '1.1.1.1:8080',
    # '1.1.1.2:8081',
    # '1.1.1.3:8082',
]

# if len(ip_list) == 0:
#     raise TypeError
# assert len(ip_list) > 0

# print('从ip_list取出ip地址，验证可用性')



# class MyException(BaseException):
#     def __init__(self,msg):
#         super(MyException,self).__init__()
#         self.msg=msg
#
#     def __str__(self):
#         return '<%s>' %self.msg
#
# raise MyException('类型错误') #异常的值：print(obj)




age=input('>>: ')
if age.isdigit():
    age=int(age)

    if age > 50:
        print('====>too big')




