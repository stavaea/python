# -*- coding: UTF-8 -*-
#了解的知识点
l=[1, 2, 10, 30, 33, 99, 101, 200, 301, 402] #从小到大排列的数字列表

def binary_search(l,num):
    print(l)
    if len(l) == 0:
        print('not exists')
        return
    mid_index=len(l) // 2
    if num > l[mid_index]:
        #往右找
        binary_search(l[mid_index+1:],num)

    elif num < l[mid_index]:
        #往左找
        binary_search(l[0:mid_index],num)
    else:
        print('find it')

# binary_search(l,301)
binary_search(l, 302)
