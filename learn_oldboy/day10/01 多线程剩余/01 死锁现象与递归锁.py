from threading import Thread,Lock,RLock
import time

# mutexA=Lock()
# mutexB=Lock()

mutexA=mutexB=RLock()

class MyThread(Thread):
    def run(self):
        self.f1()
        self.f2()

    def f1(self):
        mutexA.acquire()
        print('%s 拿到了A锁' %self.name)

        mutexB.acquire()
        print('%s 拿到了B锁' % self.name)
        mutexB.release() #1

        mutexA.release() #0

    def f2(self):
        mutexB.acquire()
        print('%s 拿到了B锁' % self.name)
        time.sleep(0.1)

        mutexA.acquire()
        print('%s 拿到了A锁' % self.name)
        mutexA.release()

        mutexB.release()



if __name__ == '__main__':
    for i in range(10):
        t=MyThread()
        t.start()