# age=28

# if age > 18:
#     print('表白')

# age=28
# if age > 18 and age < 22:
#     print('表白')
# else:
#     print('阿姨好')


# age=19
# is_pretty=True
# success=True
# if age > 18 and age < 22 and is_pretty:
#     if success:
#         print('表白成功，在一起')
#     else:
#         print('去他妈的爱情')
# else:
#     print('阿姨好')



score=input('>>: ')
#>=90:优秀
#>=80 <90 :良好
#>=60 <80 :合格
#<60:滚犊子
score=int(score)

if score >= 90:
    print('优秀')
elif score >= 80:
    print('良好')
elif score >= 60:
    print('合格')
else:
    print('滚犊子')





