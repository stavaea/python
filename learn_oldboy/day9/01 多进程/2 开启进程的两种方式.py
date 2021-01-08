#方式一：
from multiprocessing import Process
import time

def task(name):
    print('%s is running' %name)
    time.sleep(5)
    print('%s is done' %name)


if __name__ == '__main__':
    p=Process(target=task,args=('alex',))
    p.start()
    print('主')


#方式二：
# from multiprocessing import Process
# import time
#
# class MyProcess(Process):
#     def __init__(self,name):
#         super(MyProcess,self).__init__()
#         self.name=name
#
#     def run(self):
#         print('%s is running' %self.name)
#         time.sleep(3)
#         print('%s is done' %self.name)
#
# if __name__ == '__main__':
#     p=MyProcess('进程1')
#     p.start() #p.run()
#     print('主')