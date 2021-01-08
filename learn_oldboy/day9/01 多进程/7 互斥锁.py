from multiprocessing import Process,Lock
import json
import time
import random
import os

def search():
    time.sleep(random.randint(1,3))
    dic=json.load(open('db.txt','r',encoding='utf-8'))
    print('%s 查看到剩余票数%s' %(os.getpid(),dic['count']))

def get():
    dic=json.load(open('db.txt','r',encoding='utf-8'))
    if dic['count'] > 0:
        dic['count']-=1
        time.sleep(random.randint(1,3))
        json.dump(dic,open('db.txt','w',encoding='utf-8'))
        print('%s 购票成功' %os.getpid())

def task(mutex):
    search()
    mutex.acquire()
    get()
    mutex.release()

if __name__ == '__main__':
    mutex=Lock()
    for i in range(10):
        p=Process(target=task,args=(mutex,))
        p.start()
        # p.join()








