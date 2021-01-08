#条件循环
'''
while 条件:
    代码1
    代码2
    代码3
'''

# age_of_oldboy=54
#
# guess=input('>>: ')
# guess=int(guess)
#
# if guess > age_of_oldboy:
#     print('too big')
# elif guess < age_of_oldboy:
#     print('too small')
# else:
#     print('you got it')
#
# guess=input('>>: ')
# guess=int(guess)
#
# if guess > age_of_oldboy:
#     print('too big')
# elif guess < age_of_oldboy:
#     print('too small')
# else:
#     print('you got it')
#
# guess=input('>>: ')
# guess=int(guess)
#
# if guess > age_of_oldboy:
#     print('too big')
# elif guess < age_of_oldboy:
#     print('too small')
# else:
#     print('you got it')




# count=0
# while count <= 10:
#     print(count)
#     count+=1


#while+break
# count=0
# while True:
#     if count == 5:
#         break #跳出本层
#     print(count)
#     count+=1

#while+continue
#1,2,3,4,5,7

# count=1
# while count <= 7:
#     if count == 6:
#         count += 1
#         continue #跳出本次循环
#     print(count)
#     count+=1


#嵌套循环
# count=1
# while True:
#     if count > 3:
#         print('too many tries')
#         break
#
#     name=input('name>>: ')
#     password=input('password>>: ')
#     if name == 'egon' and password == '123':
#         print('login successfull')
#         break
#     else:
#         print('user or password err')
#         count+=1







# count = 1
# while True:
#     if count > 3:
#         print('too many tries')
#         break
#
#     name = input('name>>: ')
#     password = input('password>>: ')
#     if name == 'egon' and password == '123':
#         print('login successfull')
#         while True:
#             cmd=input('cmd>>: ') #q
#             if cmd == 'q':
#                 break
#             print('run %s' %cmd)
#         break
#     else:
#         print('user or password err')
#         count += 1




# count = 1
# tag=True
# while tag:
#     if count > 3:
#         print('too many tries')
#         break
#
#     name = input('name>>: ')
#     password = input('password>>: ')
#     if name == 'egon' and password == '123':
#         print('login successfull')
#         while tag:
#             cmd=input('cmd>>: ') #q
#             if cmd == 'q':
#                 tag=False
#                 continue
#             print('run %s' %cmd)
#
#     else:
#         print('user or password err')
#         count += 1




#while+else
count=0
while count <= 5:
    if count == 3:
        break
    print(count)
    count+=1
else:
    print('当while循环在运行过程中没有被break打断，则执行我')



