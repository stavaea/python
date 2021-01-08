from multiprocessing import Process
import time
import os

def task(n):
    print('pid:%s ppid:%s' %(os.getpid(),os.getppid()))
    time.sleep(n)


if __name__ == '__main__':
    p=Process(target=task,args=(15,),name='进程1')
    p.start()
    p.terminate()
    # time.sleep(1)
    print(p.is_alive())
    print('主pid:%s ppid:%s' %(os.getpid(),os.getppid()))
    # print(p.pid)
    p.name='xxxx'
    print(p.name)
