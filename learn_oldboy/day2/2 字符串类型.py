#用途：姓名，性别，住址等描述性的数据
#定义方式：‘’ ，“”，''' '''内定义的一串字符
msg='hello world'

#优先掌握的操作：
#1、按索引取值(正向取+反向取) ：只能取
# print(msg[0],type(msg[0]))
# print(msg[-1])

#2、切片(顾头不顾尾，步长)
# print(msg[0:3]) #>=0 <3
# print(msg[0:7]) #>=0 <7
# print(msg[0:7:1]) #>=0 <7
# print(msg[0:7:2]) #hello w   #hlow
# print(msg[:])
# print(msg[5:1:-1])
# print(msg[-1::-1])

#3、长度len
# print(msg.__len__())
# print(len(msg)) #msg.__len__()

#4、成员运算in和not in
# msg='hello world'
# print('llo' in msg)
# print('llo' not in msg)

#5、移除空白strip
# password='    alex3714     '
# print(password.strip())

# password=input('>>: ').strip()

# password='alex 3714     '
# print(password.strip())

#6、切分split
# user_info='root:x:0:0::/root:/bin/bash'
# res=user_info.split(':')
# print(res[0])

# cmd='get /root/a/b/c/d.txt'
# print(cmd.split())

# file_path='C:\\a\\d.txt'
# print(file_path.split('\\',1))

# file_path='C:\\a\\d.txt'
# print(file_path.rsplit('\\',1))

#7、循环
msg='hel'

# n=0
# size=len(msg)
# while n < size:
#     print(msg[n])
#     n+=1

# for i in msg: #i=l
#     print(i)

# for i in range(0,5,2): #0 2 4
#     print(i)

# msg='hel'
# for i in range(len(msg)): #0 1 2
#     print(msg[i])

# for i in range(3):
#     print(i)



# x='aaa'
# print(id(x))
# x='bbb'
# print(id(x))



#二：该类型总结
# 1 存一个值or存多个值
#     只能存一个值

# 2 有序

# 3 可变or不可变
#     ！！！不可变：值变，id就变。不可变==可hash













#需要掌握的
#1、strip,lstrip,rstrip
# print("**alex****".strip('*'))
# print("**alex****".lstrip('*'))
# print("**alex****".rstrip('*'))

#2、lower,upper
# print('ALeX'.lower())
# print('aaa'.upper())

#3、startswith,endswith
# msg='alex is SB'
# print(msg.startswith('alex'))
# print(msg.startswith('a'))
# print(msg.endswith('SB'))

#4、format的三种玩法
# print('my name is %s my age is %s' %('alex',18))

# print('my name is {} my age is {}'.format('alex',18))
# print('my name is {} my age is {}'.format(18,'alex'))

# print('{0} {1} {0}'.format('alex',18))

# print('my name is {name} my age is {age}'.format(age=18,name='male'))


#5、split,rsplit
# info='root:x:0:0'
# l=info.split(':')
# print(l)
#6、join
# print(':'.join(l))

# l=[1,2,3]
# ' '.join(l) #报错：只有在列表内的元素全是字符串类型，才能用join拼接


#7、replace
# msg='alex say my name is alex ,alex have on tesla'
# msg=msg.replace('alex','SB',1)
# print(msg)


#8、isdigit
# age=input('>>: ').strip()
# # print(age.isdigit()) #age='123'
# if age.isdigit():
#     age=int(age)
# else:
#     print('必须输入数字')




#了解
#1、find,rfind,index,rindex,count
msg='hello world'
# print(msg.find('wo'))
# print(msg.find('SB'))

# print(msg.index('wo'))
# print(msg.index('SB')) #ValueError: substring not found

# print(msg.count('l'))
# print(msg.count('SB'))


#2、center,ljust,rjust,zfill
# print('egon'.center(30,'*'))
# print('egon'.ljust(30,'*'))
# print('egon'.rjust(30,'*'))
# print('egon'.zfill(30))


#3、expandtabs
# print('hello\tworld'.expandtabs(10))

#4、captalize,swapcase,title
# print('i am egon'.capitalize())
# print('i am egon'.title())
# print('AbC'.swapcase())

#5、is数字系列
# num1=b'4' #bytes
# num2=u'4' #unicode,python3中无需加u就是unicode
# num3='壹' #中文数字
# num4='Ⅳ' #罗马数字

#bytes,unicode
# print(num1.isdigit())
# print(num2.isdigit())
# print(num3.isdigit())
# print(num4.isdigit())

#unicode
# print(num2.isdecimal())
# print(num3.isdecimal())
# print(num4.isdecimal())

#unicode，中文，罗马
# print(num2.isnumeric())
# print(num3.isnumeric())
# print(num4.isnumeric())

#6、is其他
# name='egon123'
# print(name.isalnum()) #字符串由字母或数字组成
# print(name.isalpha()) #字符串只由字母组成

# print('print1111'.isidentifier())
# print('abcA'.islower())
# print(name.isupper())
# print(' '.isspace())
# print('Am Ia'.istitle())




