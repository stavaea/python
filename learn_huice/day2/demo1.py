# coding:utf-8

a = raw_input('请输入')  #接收用户输入的一个字符串，判断是否为纯数字
print a.isdigit()


# if
# 接受用户输入的一个字符串，如果是正整数就判断是否能同时被3和7整除
num = raw_input('输入一个数字：')
if num.isdigit():
    num = long(num)
    if num > 0:
        if num % 3 == 0 and num % 7 == 0:
            print '是正整数'
        else:
            print '不是正整数'
    else:
        print '请输入正整数'
else:
    print '不是数字'

# 根据输入的月份来输出，这个月有几天(默认2月有28天，不考虑闰年)
mouth = input('输入一个月份：')
if mouth in (1, 3, 5, 7, 8, 10, 12):
    print '%d月有31天' % mouth
elif mouth in (4, 6, 9, 11):
    print '%d月有30天' % mouth
elif mouth == 2:
    print '2月有28天'
else:
    print '不在输入范围内'


# 接收用户输入一个年份，判断是否是闰年(判断闰年的方法是该年能被4整除并且不能被100整除，或者是可以被400整除)

year = raw_input('输入一个数字：')
if year.isdigit():
    year = long(year)
    if year > 0:
        if year % 400 == 0 :
            print '%d年是闰年'%year
        else:
            print '%d年不是闰年'%year
    else:
        print '请输入正整数'
else:
    print '不是数字'

# 某电信公司的市内通话费计算标准如下：三分钟内0.2元，三分钟后每增加一分钟增加0.1元，不足一分钟的按一分钟计算。要求编写程序，给定一个通话时间（单位：秒）计算出应收费金额。
time = input('请输入时间:')
money = 0.0
if time <= 180 and time > 0:
    print '话费是0.2元'
    if time > 180:
        if time % 60 == 0:
            money += (time % 60 - 3)*0.1+0.2
            print '话费是%2.f元' % money
        else:
            money += (time % 60 - 2)*0.1+0.2
            print '话费是%2.f元' % money

