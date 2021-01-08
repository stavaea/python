#-*-coding:utf-8-*-
age = 15
if age <= 28 and age >= 14:
    print '团员'

age = 30
if age <= 28 and age >= 14:
    print '团员'
else:
    print '非团员'

score = -1
if score >= 0 and score < 60:
    print '成绩不及格'
elif  score >= 60 and score < 80:
    print '及格'
elif  score >= 80 and score < 90:
    print '良好'
elif  score >= 90 and score <= 100:
    print '优秀'
else:
    print '输入成绩不合法'

# if-else语句的嵌套
if score >= 0 and score <= 100:
    if score < 60:
        print '成绩不及格'
    elif score >= 60 and score < 80:
        print '及格'
    elif score >= 80 and score < 90:
        print '良好'
    elif score >= 90:
        print '优秀'
else:
    print '输入成绩不合法'


age = 20
if age >= 6:
    print '青少年'
elif age >= 18:
    print '成人'
elif age>=50:
    print '老年人'
else:
    print '儿童'