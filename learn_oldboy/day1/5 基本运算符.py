#算术
# print(10%3)
# print(2**3)
# print(10/3)
# print(10//3)


#比较
# print(10 > 3)
# print(10 < 3)
# print(10 == 3)
# print(10 != 3)

#赋值
# a=2
# b=a
#链式赋值
# a=b=c=2
# print(id(a),id(b),id(c))

#交叉赋值
# m=1
# n=2

# temp=m
# m=n
# n=temp
# print(m,n)
# m,n=n,m
# print(m,n)

#解压
l=[1,2,3,4]
# a,b,c,d=l
# print(a)
# print(b)
# print(c)
# print(d)


# a=l[0]
# _=l[1]
# _=l[2]
# d=l[3]
# a,_,_,d=l
# print(a,d)

# a,*_,d=l
# print(a)
# print(d)

#赋值运算符
# level=1
# level+=1 #level=level+1
# level-=1 #level=level-1
# print(level)







#逻辑and or not
# age=18
# is_pretty=True
# height=170
# weight=80

# print(age >= 18 and is_pretty == True and height > 160 and weight > 30 and weight < 90)

# print(1 > 2 or 1 > 3 or 3 > 1 or 4 < 3)


# print(not 4 > 2)



age=18
is_pretty=True
height=170
weight=80
print((height > 160 and weight > 60 and weight < 90) or is_pretty == True or age == 18
)


#身份
#is比较的是id
#而==比较的是值