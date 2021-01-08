from multiprocessing import Process
import time

n=100

def task():
    global n
    time.sleep(5)
    n=0

if __name__ == '__main__':
    p=Process(target=task)
    p.start()
    # time.sleep(5)
    print(p.is_alive())
    p.join()
    print(p.is_alive())
    print('主',n)
