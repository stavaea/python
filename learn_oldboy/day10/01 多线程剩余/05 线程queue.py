import queue

# q=queue.Queue(3) #队列：先进先出
#
# q.put(1)
# q.put(2)
# q.put(3)
# # q.put(4)
# # q.put_nowait(4)
# # q.put(4,block=False)
# q.put(4,block=True,timeout=3)
#
#
# # print(q.get())
# # print(q.get())
# # print(q.get())

# q=queue.LifoQueue(3) #堆栈：后进先出
# q.put(1)
# q.put(2)
# q.put(3)
#
# print(q.get())
# print(q.get())
# print(q.get())

q=queue.PriorityQueue(3) #优先级队列
q.put((10,'a'))
q.put((-3,'b'))
q.put((100,'c'))

print(q.get())
print(q.get())
print(q.get())

