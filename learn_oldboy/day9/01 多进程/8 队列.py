from multiprocessing import Queue

q=Queue(3)

q.put('first')
q.put(2)
q.put({'count':3})
# q.put('fourth',block=False) #q.put_nowait('fourth')
# q.put('fourth',block=True,timeout=3)

print(q.get())
print(q.get())
print(q.get())
# print(q.get(block=False)) #q.get_nowait()
print(q.get(block=True,timeout=3))
