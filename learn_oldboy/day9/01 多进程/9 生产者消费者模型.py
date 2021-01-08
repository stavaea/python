# from multiprocessing import Process,Queue
# import time
# import random
#
# def producer(name,food,q):
#     for i in range(3):
#         res='%s%s' %(food,i)
#         time.sleep(random.randint(1,3))
#         q.put(res)
#         print('厨师[%s]生产了<%s>' %(name,res))
#
#
# def consumer(name,q):
#     while True:
#         res=q.get()
#         if res is None:break
#         time.sleep(random.randint(1,3))
#         print('吃货[%s]吃了<%s>' % (name, res))
#
# if __name__ == '__main__':
#     #队列
#     q=Queue()
#     #生产者们
#     p1=Process(target=producer,args=('egon1','泔水',q))
#     p2=Process(target=producer,args=('egon2','骨头',q))
#     #消费者们
#     c1=Process(target=consumer,args=('管廷威',q))
#     c2=Process(target=consumer,args=('oldboy',q))
#     c3=Process(target=consumer,args=('oldgirl',q))
#
#
#     p1.start()
#     p2.start()
#     c1.start()
#     c2.start()
#     c3.start()
#
#     p1.join()
#     p2.join()
#     q.put(None)
#     q.put(None)
#     q.put(None)
#     print('主')



from multiprocessing import Process,JoinableQueue
import time
import random

def producer(name,food,q):
    for i in range(3):
        res='%s%s' %(food,i)
        time.sleep(random.randint(1,3))
        q.put(res)
        print('厨师[%s]生产了<%s>' %(name,res))


def consumer(name,q):
    while True:
        res=q.get()
        if res is None:break
        time.sleep(random.randint(1,3))
        print('吃货[%s]吃了<%s>' % (name, res))
        q.task_done()

if __name__ == '__main__':
    #队列
    q=JoinableQueue()
    #生产者们
    p1=Process(target=producer,args=('egon1','泔水',q))
    p2=Process(target=producer,args=('egon2','骨头',q))
    #消费者们
    c1=Process(target=consumer,args=('管廷威',q))
    c2=Process(target=consumer,args=('oldboy',q))
    c3=Process(target=consumer,args=('oldgirl',q))
    c1.daemon=True
    c2.daemon=True
    c3.daemon=True

    p1.start()
    p2.start()
    c1.start()
    c2.start()
    c3.start()

    p1.join()
    p2.join()
    q.join()
    print('主')
