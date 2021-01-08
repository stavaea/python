# import sys
# sys.argv
# sys.exit(0)
# sys.path

# print('[%-50s]' %('#'*1))
# print('[%-50s]' %('#'*2))
# print('[%-50s]' %('#'*3))
# print('[%-50s]' %('#'*4))
# print('[%-50s]' %('#'*5))

#([%-50s]) %('#'*10)
# print('[%%-%ds]' %50) #'[%-50s]'
#
# print(('[%%-%ds]' %50) %('#'*10)) #'[%-50s]' %('#'*10)
# print(('[%%-%ds]' %50) %('#'*10)) #'[%-50s]' %('#'*10)
# print(('[%%-%ds]' %50) %('#'*10)) #'[%-50s]' %('#'*10)
# print(('[%%-%ds]' %50) %('#'*10)) #'[%-50s]' %('#'*10)

# print('%d%%' %30)

import time

def progress(percent,width=50):
    if percent >= 1:
        percent=1
    show_str = ('[%%-%ds]' % width) % ('#' * int(width*percent))
    print('\r%s %d%%' %(show_str,int(100*percent)),end='')

recv_size=0
total_size=10241
while recv_size < total_size:
    time.sleep(0.1)
    recv_size+=1024
    progress(recv_size/total_size)