#了解
# print(abs(-1))

# print(all([1,'a','b',0]))
# print(all([]))

# print(any([None,False,0,1]))
# print(any([]))


# print(bin(11))
# print(hex(11))
# print(oct(11))

# print('xxx'.encode('utf-8'))
# print(bytes('xxx',encoding='utf-8'))

# print(callable(max))

# print(chr(65))
# # print(chr(90))
# # print(chr(39))
# print(ord('A'))
# print(ord('@'))


# import os
# print(dir(os))


# s=set({1,2,3})
# s.add(4)
# print(s)

# s=frozenset({1,2,3}) #不可变集合

# print(hash('xxx'))

# l=[1,2,'a',4]
# print(list(reversed(l)))


# s=slice(1,5,2)
# l=['a','b','c','d','e']
#
# # print(l[1:5:2])
# # print(l[1:5:2])
#
# print(l[s])


# print(vars() is locals())


#面向对象
classmethod
staticmethod
property


hasattr
getattr
setattr
delattr

isinstance
issubclass

object

super

# obj.__dict__() #vars(obj)

#__import__
# choice=input('>>: ')
# print(choice,type(choice))
#
# # import 'time'
# m=__import__(choice)
# m.sleep(10)



#掌握：
#divmod
# print(divmod(10011,25))


#enumerate
# l=['a','b','c']

# for i in l:
#     print(l.index(i),i,)

# for i,v in enumerate(l):
#     print(i,v)

#eval:
# res=eval('[1,2,3]')
# print(res,type(res))

# res=exec('[1,2,3]')
# print(res)

#pow
# res=pow(2,3,3) # (2 ** 3 )%3
# print(res)

#round
# print(round(3.5))


