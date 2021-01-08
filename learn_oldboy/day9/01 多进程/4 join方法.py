# from multiprocessing import Process
# import time
# import os
#
# def task(n):
#     print('%s is runing' %os.getpid())
#     time.sleep(n)
#     print('%s is done' %os.getpid())
#
#
# if __name__ == '__main__':
#
#     start_time=time.time()
#     p1=Process(target=task,args=(1,))
#     p2=Process(target=task,args=(2,))
#     p3=Process(target=task,args=(3,))
#
#     p_l=[p1,p2,p3]
#     # p1.start()
#     # p2.start()
#     # p3.start()
#     for p in p_l:
#         p.start()
#
#     # p3.join()  #3
#     # p1.join() #
#     # p2.join() #
#     for p in p_l:
#         p.join()
#     stop_time=time.time()
#     print('主',(stop_time-start_time))




# from multiprocessing import Process
# import time
# import os
#
# def task(n):
#     print('%s is runing' %os.getpid())
#     time.sleep(n)
#     print('%s is done' %os.getpid())
#
#
# if __name__ == '__main__':
#
#     start_time=time.time()
#     p1=Process(target=task,args=(1,))
#     p2=Process(target=task,args=(2,))
#     p3=Process(target=task,args=(3,))
#
#     p_l=[p1,p2,p3]
#     # p1.start()
#     # p2.start()
#     # p3.start()
#     for p in p_l:
#         p.start()
#
#     # p3.join()  #3
#     # p1.join() #
#     # p2.join() #
#     for p in p_l:
#         p.join()
#     stop_time=time.time()
#     print('主',(stop_time-start_time))


from multiprocessing import Process
import time
import os

def task(n):
    print('%s is runing' %os.getpid())
    time.sleep(n)
    print('%s is done' %os.getpid())


if __name__ == '__main__':

    start_time=time.time()
    p1=Process(target=task,args=(1,))
    p2=Process(target=task,args=(2,))
    p3=Process(target=task,args=(3,))


    p1.start()
    p1.join()
    p2.start()
    p2.join()
    p3.start()
    p3.join()
    stop_time=time.time()
    print('主',(stop_time-start_time))





