# f=open(r'C:\Users\Administrator\PycharmProjects\python20期\day2\a.txt')

# f=open('a.txt','r',encoding='utf-8')
# data=f.read()
# print(data)
# print(f)
# f.close() #文件关闭，回收操作系统的资源
# print(f)
# f.read()

# with open('a.txt','r',encoding='utf-8') as f: #f=open('a.txt','r',encoding='utf-8')
#     pass


#读操作:r只读模式，默认是rt文本读
# f=open('a.txt','r',encoding='utf-8')
# # data1=f.read()
# # print('=1===>',data1)
# # data2=f.read()
# # print('=2===>',data2)
#
# # print(f.readlines())
#
# # print(f.readline(),end='')
# # print(f.readline(),end='')
# # print(f.readline(),end='')
#
#
# f.close()


#写操作:w只写模式，默认是wt文本写，如果文件不存在则创建，存在则清空+覆盖
f=open('a.txt','w',encoding='utf-8')
# f.write('11111\n')
# f.write('222222\n')
# f.write('1111\n2222\n3333\n')
# f.writelines(['哈哈哈哈\n','你好','alex'])
f.close()


