#-*-coding:utf-8-*-
month = input("请输入月份:")
days = 0

if month in [1, 3, 5, 7, 8, 10, 12]:
    print '%d 月有 31天' % (month)
elif month in [4, 6, 9, 11]:
    print '%d 月有 30天' % (month)
elif month == 2:
    print '%d 月有 28天' % (month)
else:
    print '输入不合法'
