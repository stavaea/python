#-*-coding:utf-8-*-
# 循环嵌套，Python 语言允许在一个循环体里面嵌入另一个循环体。


#举例：对列表[50,20,30,10]进行冒泡排序,按照升序排列
# 冒泡排序：从前往后将相邻的两个数进行比较，将较小的数放在前面，较大的数放在后面
# 第一轮
# 20 50 30 10
# 20 30 50 10
# 20 30 10 50
# 第二轮
# 20 30 10 50
# 20 10 30 50
# 第三轮
# 10 20 30 50
# 冒泡排序原理: 每一轮只能将一个数归位, 如果有n个数进行排序,只需将n-1个数归位,
# 也就是说要进行n-1轮操作(已经归位的数不用再比较)
aList = [20, 30, 10, 50]

for i in range(len(aList)-1): #比较几轮,第一轮：0，第二轮：1，第三轮：2
    for j in range(0, len(aList)-i-1): #定义比较的索引,第一轮，0-1,1-2,2-3，第二轮：0-1,1-2，第三轮：0-1
        if aList[j] > aList[j+1]:
            aList[j], aList[j + 1] = aList[j+1], aList[j]
print aList


for i in range(1, 101):
    if i % 2 == 0:
        print i

j = 1
while j < 101:
    if j % 2 == 0:
        print j
    j += 1

for i in range(2, 101, 2):
    print i

for i in range(1, 101, 2):
    print i