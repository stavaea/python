#计算密集型:开多进程
# from multiprocessing import Process
# from threading import Thread
# import os,time
# def work():
#     res=0
#     for i in range(100000000):
#         res*=i
#
#
# if __name__ == '__main__':
#     l=[]
#     start=time.time()
#     for i in range(4):
#         # p=Process(target=work) #5.826333284378052
#         p=Thread(target=work) #run time is 19.91913938522339
#         l.append(p)
#         p.start()
#     for p in l:
#         p.join()
#     stop=time.time()
#     print('run time is %s' %(stop-start))


#I/O密集型：多线程效率高
# from multiprocessing import Process
# from threading import Thread
# import threading
# import os,time
# def work():
#     time.sleep(2)
#
# if __name__ == '__main__':
#     l=[]
#     start=time.time()
#     for i in range(400):
#         # p=Process(target=work) # 12.465712785720825
#         p=Thread(target=work) #2.037116765975952
#         l.append(p)
#         p.start()
#     for p in l:
#         p.join()
#     stop=time.time()
#     print('run time is %s' %(stop-start))
#



from threading import Thread,Lock
import time

n=100

def task():
    global n
    mutex.acquire()
    temp=n
    time.sleep(0.1)
    n=temp-1
    mutex.release()

if __name__ == '__main__':
    mutex=Lock()
    for i in range(3):
        t=Thread(target=task)
        t.start()
