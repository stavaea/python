# with open('a.txt','r',encoding='utf-8') as f:
#     data1=f.read()
#     print('==1==>',data1)
#     print(f.tell())
#
#     data2=f.read()
#     print('==2==>',data2)


#只有一种情况光标以字符为单位：文件以rt方式打开，read（3）
# with open('c.txt','rt',encoding='utf-8') as f:
#     # print(f.read(6))
#     # print(f.tell())
#     # f.seek(0,0)
#     # print(f.read(6))
#
#     # f.seek(6,0)
#     f.seek(8,0)
#     print(f.read())


# with open('c.txt','rb',) as f:
#     f.seek(6,0)
#     # f.seek(8,0)
#     print(f.read())

# with open('c.txt','rb') as f:
#     print(f.read(6))
#     f.seek(2,1)
#     print(f.tell())
#     print(f.read().decode('utf-8'))


# with open('c.txt','rb') as f:
#     # f.seek(-3,2)
#     # print(f.tell())
#     f.seek(0,2)

#tail -f access.log
# import time
# with open(r'C:\Users\Administrator\PycharmProjects\python20期\day3\access.log','rb') as f:
#     f.seek(0,2)
#     while True:
#         line=f.readline()
#         # print('===>',line)
#         if line:
#             print(line.decode(),end='')
#         else:
#             time.sleep(0.05)


#
# with open('access.log','a',encoding='utf-8') as f:
#     f.truncate(3)
