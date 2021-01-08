from time import time

# str1 = 'Hello'
# str2 = 'World'
# newstr = str1 + str2
# print newstr
#
# # error
# # print newstr + 1
#
#
# listStr = ['www', 'huicewang', 'com']
# website = '.'.join(listStr)
# print website
#
# listStr = ('www', 'huicewang', 'com')
# website = '.'.join(listStr)
# print website
#
# listStr = {'type':'www', 'host':'huicewang', 'org':'com'}
# website = '.'.join(listStr)
# print website

# def method1():
#     t = time()
#     for i in xrange(100000):
#         s = 'pythontab'+'pythontab'+'pythontab'+'pythontab'+'pythontab'+'pythontab'+'pythontab'+'pythontab'+'pythontab'+'pythontab'+'pythontab'+'pythontab'+'pythontab'+'pythontab'+'pythontab'+'pythontab'+'pythontab'+'pythontab'+'pythontab'+'pythontab'+'pythontab'+'pythontab'+'pythontab'+'pythontab'+'pythontab'+'pythontab'+'pythontab'+'pythontab'+'pythontab'+'pythontab'+'pythontab'+'pythontab'+'pythontab'+'pythontab'+'pythontab'+'pythontab'+'pythontab'+'pythontab'+'pythontab'+'pythontab'+'pythontab'+'pythontab'+'pythontab'+'pythontab'+'pythontab'+'pythontab'
#     print time() - t
#
# def method2():
#     t = time()
#     for i in xrange(100000):
#         s = ''.join(['pythontab','pythontab','pythontab','pythontab','pythontab','pythontab','pythontab','pythontab','pythontab','pythontab','pythontab','pythontab','pythontab','pythontab','pythontab','pythontab','pythontab','pythontab','pythontab','pythontab','pythontab','pythontab','pythontab','pythontab','pythontab','pythontab','pythontab','pythontab','pythontab','pythontab','pythontab','pythontab','pythontab','pythontab','pythontab','pythontab','pythontab','pythontab','pythontab','pythontab','pythontab','pythontab','pythontab','pythontab','pythontab','pythontab'])
#     print time() -t
#
# method1()
# method2()

# def method3():
#     t = time()
#     for i in xrange(100000):
#         s = 'pythontab'+'pythontab'+'pythontab'+'pythontab'
#     print time() - t
#
# def method4():
#     t = time()
#     for i in xrange(100000):
#         s = ''.join(['pythontab','pythontab','pythontab','pythontab'])
#     print time() -t
#
# method3()
# method4()
#
text = 'I\'m {},{}'
print text.format('Zach', 'Welcome to my space!')

text = '{0},I\'m {1},my E-mail is {2}'
print text.format('Hello', 'Zach', 'zachlau@gmail.com')

text = '{1},I\'m {0},my E-mail is {2}'
print text.format('Zach', 'Hello', 'zachlau@gmail.com')

text = '{start},I\'m {name},my E-mail is {email}'
print text.format(start='Hello', name='Zach', email='zachlau@gmail.com')

text = '{start},my name is {name},i\'m {age} years old. i likes {fruit}'
print text.format(start='Hello', name='Zach', age=18, fruit=['apple', 'orange'])