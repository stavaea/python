from threading import Thread,Event,current_thread
import time

event=Event()

def check():
    print('checking MySQL...')
    time.sleep(5)
    event.set()

def conn():
    count=1
    while not event.is_set():
        if count > 3:
            raise TimeoutError('超时')
        print('%s try to connect MySQL time %s' %(current_thread().getName(),count))
        event.wait(1)
        count+=1

    print('%s connected MySQL' %current_thread().getName())

if __name__ == '__main__':
    t1=Thread(target=check)
    t2=Thread(target=conn)
    t3=Thread(target=conn)
    t4=Thread(target=conn)


    t1.start()
    t2.start()
    t3.start()
    t4.start()





