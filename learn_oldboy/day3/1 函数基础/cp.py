#!/usr/bin/env python

#1、源大小的问题：
#2、文件打开模式的问题:b

# import sys
# _,src_file,dst_file=sys.argv
#
# with open(src_file,'rb') as read_f,\
#         open(dst_file,'wb') as write_f:
#     # data=read_f.read()
#     # write_f.write(data)
#
#     for line in read_f:
#         write_f.write(line)
        # write_f.flush()

with open('access.log','a',encoding='utf-8') as f:
    f.write('aaaaa\n')
    f.flush()









