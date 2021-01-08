from threading import Thread,Semaphore,current_thread
import time,random

sm=Semaphore(5)

def task():
    with sm:
        print('%s is laing' %current_thread().getName())
        time.sleep(random.randint(1,3))

if __name__ == '__main__':
    for i in range(20):
        t=Thread(target=task)
        t.start()

