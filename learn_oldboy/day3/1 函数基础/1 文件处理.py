# f=open(r'a.txt','w',encoding='utf-8')
# # print(f.writable())
# f.write('1111\n')
# f.write('2222\n')
# f.writelines(['3333\n','444\n'])
# f.close()


#a：文件不存在则创建，文件存在那么在打开文件后立刻将光标移动到文件末尾，进行追加写
# f=open(r'b.txt','a',encoding='utf-8')
# # print(f.writable())
# f.write('4444\n')
# f.write('5555\n')
# f.writelines(['66666\n','7777\n'])
# f.close()


#r：
# f=open(r'b.txt','r',encoding='utf-8')
# # print(f.writable())
# # print(f.read())
# # print(f.readlines())
# print(f.readline(),end='')
# print(f.readline(),end='')
# f.close()


# with open('b.txt','r',encoding='utf-8') as f:
#     # while True:
#     #     line=f.readline()
#     #     if len(line) == 0:break
#     #     print(line)
#
#     # print(f.readline())
#     # print(f.readline())
#     # print(f.readline())
#     # print(f.readline())
#     # print(f.readline())
#     # print(f.readline())
#     # print(f.readline())
#     # print('第八次',f.readline())
#
#     for line in f:
#         print(line)


#b:bytes
# with open('111.png','rb') as f:
#     print(f.read())

# with open('b.txt','rb',) as f:
#     print(f.read().decode('utf-8'))

# with open('b.txt','rt',encoding='utf-8') as f:
#     print(f.read())


# with open('b.txt','wb') as f:
#     res='中问'.encode('utf-8')
#     print(res,type(res))
#     f.write(res)


# with open('b.txt','ab') as f:
#     res='哈哈哈'.encode('utf-8')
#     print(res,type(res))
#     f.write(res)






