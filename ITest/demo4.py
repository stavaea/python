#coding:utf-8
import time

# print time.time()
# print time.localtime(1)
# print time.ctime(1)美式时间
print (time.strftime('%Y-%m-%d_%H:%M:%S', time.localtime(time.time())))