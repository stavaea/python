#提交任务的两种方式：
#同步调用：提交完任务后，就在原地等待，等待任务执行完毕，拿到任务的返回值，才能继续下一行代码，导致程序串行执行
#异步调用+回调机制：提交完任务后，不在原地等待，任务一旦执行完毕就会触发回调函数的执行， 程序是并发执行

#进程的执行状态：
#阻塞
#非阻塞


# #同步调用示例：
# # from multiprocessing import Pool
# from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor
# import time,random,os
#
# def task(n):
#     print('%s is ruuning' %os.getpid())
#     time.sleep(random.randint(1,3))
#     return n**2
#
# def handle(res):
#     print('handle res %s' %res)
#
# if __name__ == '__main__':
#     #同步调用
#     pool=ProcessPoolExecutor(2)
#
#     for i in range(5):
#         res=pool.submit(task,i).result()
#         # print(res)
#         handle(res)
#
#     pool.shutdown(wait=True)
#     # pool.submit(task,33333)
#     print('主')


#异步调用示例：
# from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor
# import time,random,os
#
# def task(n):
#     print('%s is ruuning' %os.getpid())
#     time.sleep(random.randint(1,3))
#     # res=n**2
#     # handle(res)
#     return n**2
#
# def handle(res):
#     res=res.result()
#     print('handle res %s' %res)
#
# if __name__ == '__main__':
#     #异步调用
#     pool=ProcessPoolExecutor(2)
#
#     for i in range(5):
#         obj=pool.submit(task,i)
#         obj.add_done_callback(handle) #handle(obj)
#
#     pool.shutdown(wait=True)
#     print('主')


#线程池
from concurrent.futures import ThreadPoolExecutor
from threading import current_thread
import requests
import time

def get(url):
    print('%s GET %s' %(current_thread().getName(),url))
    response=requests.get(url)
    time.sleep(2)
    if response.status_code == 200:
        return {'url':url,'content':response.text}

def parse(res):
    res=res.result()
    print('parse:[%s] res:[%s]' %(res['url'],len(res['content'])))


if __name__ == '__main__':
    pool=ThreadPoolExecutor(2)

    urls=[
        'https://www.baidu.com',
        'https://www.python.org',
        'https://www.openstack.org',
        'https://www.openstack.org',
        'https://www.openstack.org',
        'https://www.openstack.org',
        'https://www.openstack.org',
        'https://www.openstack.org',
        'https://www.openstack.org',
        'https://www.openstack.org',
        'https://www.openstack.org',
        'https://www.openstack.org',
    ]
    for url in urls:
        pool.submit(get,url).add_done_callback(parse)

    pool.shutdown(wait=True)












