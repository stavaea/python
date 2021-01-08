# from threading import Thread
# import time
# import random
# import os
#
# def piao():
#     print('%s is piaoing' %os.getpid())
#     time.sleep(random.randint(1,3))
#
#
# if __name__ == '__main__':
#     t1=Thread(target=piao,)
#     t2=Thread(target=piao,)
#     t3=Thread(target=piao,)
#     t1.start()a
#     t2.start()
#     t3.start()
#     print('主',os.getpid())
#


from threading import Thread
import time
import random
import os

n=100
def piao():
    global n
    n=0

if __name__ == '__main__':
    t1=Thread(target=piao,)
    t1.start()
    t1.join()
    print('主',n)


