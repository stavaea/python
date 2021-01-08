from threading import Timer


def hello(name):
    print("hello, world %s " %name)


t = Timer(3, hello,args=('egon',))
t.start()  # after 1 seconds, "hello, world" will be printed