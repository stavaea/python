from gevent import monkey;monkey.patch_all()
import gevent
import time

def eat(name):
    print('%s eat 1' %name)
    # gevent.sleep(3)
    time.sleep(3)
    print('%s eat 2' %name)


def play(name):
    print('%s play 1' % name)
    # gevent.sleep(2)
    time.sleep(3)
    print('%s play 2' % name)

g1=gevent.spawn(eat,'egon')
g2=gevent.spawn(play,'alex')
# gevent.sleep(1)

# g1.join()
# g2.join()
gevent.joinall([g1,g2])