# def func(): #func=内存地址
#     print('from func')
#
# func()
# func()


# 内存地址
# def my_sum(x,y):
#     return x+y

# print(lambda x,y:x+y)
# print((lambda x,y:x+y)(1,2))

# func=lambda x,y:x+y
# # print(func)
# print(func(1,2))


#max，min，sorted,map,reduce,filter
# salaries={
#     'egon':3000,
#     'alex':100000000,
#     'wupeiqi':10000,
#     'yuanhao':2000
# }
# print(max(salaries))

# s='hello'
# l=[1,2,3]
# g=zip(s,l)
# # print(g)
# print(list(g))

# g=zip(salaries.values(),salaries.keys())
# # print(list(g))
# print(max(g))

# def func(k):
#     return salaries[k]

# print(max(salaries,key=func)) #key=func('egon')

# print(max(salaries,key=lambda k:salaries[k])) #key=func('egon')
# print(min(salaries,key=lambda k:salaries[k])) #key=func('egon')






#sorted
# salaries={
#     'egon':3000,
#     'alex':100000000,
#     'wupeiqi':10000,
#     'yuanhao':2000
# }
# print(sorted(salaries,key=lambda k:salaries[k]))
# print(sorted(salaries,key=lambda k:salaries[k],reverse=True))


#map,reduce,filter
# names=['alex','wupeiqi','yuanhao']
# l=[]
# for name in names:
#     res='%s_SB' %name
#     l.append(res)
#
# print(l)

# g=map(lambda name:'%s_SB' %name,names)
# # print(g)
# print(list(g))


# names=['alex_sb','wupeiqi_sb','yuanhao_sb','egon']
# g=filter(lambda x:x.endswith('sb'),names)
# print(g)
# print(list(g))



from functools import reduce
print(reduce(lambda x,y:x+y,range(1,101),100))










