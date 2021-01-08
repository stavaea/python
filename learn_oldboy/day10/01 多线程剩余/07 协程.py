# 单纯地切换反而会降低运行效率
#串行执行
# import time
# def consumer(res):
#     '''任务1:接收数据,处理数据'''
#     pass
#
# def producer():
#     '''任务2:生产数据'''
#     res=[]
#     for i in range(10000000):
#         res.append(i)
#     return res
#
# start=time.time()
# #串行执行
# res=producer()
# consumer(res)
# stop=time.time()
# print(stop-start)



#基于yield并发执行
import time
def consumer():
    '''任务1:接收数据,处理数据'''
    while True:
        print('consumer')
        x=yield
        time.sleep(100)

def producer():
    '''任务2:生产数据'''
    g=consumer()
    next(g)
    for i in range(10000000):
        print('producer')
        g.send(i)

start=time.time()
#基于yield保存状态,实现两个任务直接来回切换,即并发的效果
#PS:如果每个任务中都加上打印,那么明显地看到两个任务的打印是你一次我一次,即并发执行的.
producer()

stop=time.time()
print(stop-start) #

