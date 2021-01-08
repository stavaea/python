# import os
# with open('info.txt','r',encoding='utf-8') as read_f,open('.info.txt.swap','w',encoding='utf-8') as write_f:
#     data=read_f.read()
#     write_f.write(data.replace('alex','SB'))
#
# os.remove('info.txt')
# os.rename('.info.txt.swap','info.txt')



import os

with open('info.txt', 'r', encoding='utf-8') as read_f, open('.info.txt.swap', 'w', encoding='utf-8') as write_f:
    for line in read_f:
        if 'SB' in line:
            line=line.replace('SB','alex')
        write_f.write(line)

os.remove('info.txt')
os.rename('.info.txt.swap', 'info.txt')