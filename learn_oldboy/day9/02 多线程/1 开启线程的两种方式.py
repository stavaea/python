# from threading import Thread
# import time
# import random
#
# def piao(name):
#     print('%s is piaoing' %name)
#     time.sleep(random.randint(1,3))
#     print('%s is piao end' %name)
#
#
# if __name__ == '__main__':
#     t1=Thread(target=piao,args=('alex',))
#     t1.start()
#     print('主')


from threading import Thread
import time
import random

class MyThread(Thread):
    def __init__(self,name):
        super().__init__()
        self.name=name

    def run(self):
        print('%s is piaoing' %self.name)
        time.sleep(random.randint(1,3))
        print('%s is piao end' %self.name)


if __name__ == '__main__':
    t1=MyThread('alex')
    t1.start()
    print('主')