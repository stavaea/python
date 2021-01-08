#守护进程：当子进程执行的任务在父进程代码运行完毕后就没有存在的必要了，那
#该子进程就应该被设置为守护进程
# from multiprocessing import Process
# import time
#
# def task(name):
#     p=Process(target=time.sleep,args=(6,))
#     p.start()
#     print('%s is running' %name)
#     time.sleep(5)
#     print('%s is done' %name)
#
#
# if __name__ == '__main__':
#     p=Process(target=task,args=('alex',))
#     p.daemon=True
#     p.start()
#     time.sleep(1)
#     print('主')


#主进程代码运行完毕,守护进程就会结束
from multiprocessing import Process
from threading import Thread
import time
def foo():
    print(123)
    time.sleep(1)
    print("end123")

def bar():
    print(456)
    time.sleep(3)
    print("end456")

if __name__ == '__main__':

    p1=Process(target=foo)
    p2=Process(target=bar)

    p1.daemon=True
    p1.start()
    p2.start()
    print("main-------")
