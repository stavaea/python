#1 列表推导式
# l=[]
# for i in range(1,11):
#     res='egg'+str(i)
#     l.append(res)
#
# print(l)

# l=['egg'+str(i) for i in range(1,11)]
# print(l)

# l1=['egg'+str(i) for i in range(1,11) if i >= 6]
# print(l1)

# l1=[]
# for i in range(1,11):
#     if i >= 6:
#         l1.append('egg'+str(i))
#

#2 生成器表达式

# g=('egg'+str(i) for i in range(0,1000000000000000000000000000000000))
# print(g)
# print(next(g))
# print(next(g))
# print(next(g))


#练习
names=['egon','alex_sb','wupeiqi','yuanhao']

# names=[name.upper() for name in names]
# print(names)

# sbs=[name for name in names if name.endswith('sb')]
# print(sbs)


# obj=list('abcdef')
# print(obj)

# print(max([1,2,3,4,5]))

# g=(i for i in range(10))
# print(max(g))
#
# print(max(g))

with open('a.txt','r',encoding='utf-8') as f:
    # l=[]
    # for line in f:
    #     # print(len(line))
    #     l.append(len(line))

    # g=(len(line) for line in f)
    # res=max(g)
    # print(res)

    # print(max(len(line) for line in f))

    print(sum(len(line) for line in f))