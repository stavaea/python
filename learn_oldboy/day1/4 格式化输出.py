# name=input('name>>: ')
# age=input('age>>: ')
#
# print('my name is [%s] my age is <%s>' %(name,age))

# print('my name is %s' %'egon')
# print('my name is %s' %11111111111111)

# print('my age is %d' %10)
# print('my age is %d' %'xxxx') #%d只能接收数字，而%s既可以接收数字又可以接收字符串


name=input('name>>: ')
age=input('age>>: ')
sex=input('sex>>: ')
job=input('job>>: ')

msg='''
------------ info of %s -----------
Name  : %s
Age   : %s
Sex   : %s
Job   : %s
------------- end -----------------
''' %(name,name,age,sex,job)

print(msg)