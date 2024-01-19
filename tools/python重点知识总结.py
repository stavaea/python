# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2024/1/19 15:31
# @Author : waxberry
# @File : python重点知识总结.py
# @Software : PyCharm


# Py2 VS Py3
# Py2 和 Py3 的差别
# 枚举的注意事项
from enum import Enum

class COLOR(Enum):
    YELLOW=1
#YELLOW=2#会报错
    GREEN=1#不会报错,GREEN可以看作是YELLOW的别名
    BLACK=3
    RED=4
print(COLOR.GREEN)#COLOR.YELLOW,还是会打印出YELLOW
for i in COLOR:#遍历一下COLOR并不会有GREEN
    print(i)
#COLOR.YELLOW\nCOLOR.BLACK\nCOLOR.RED\n怎么把别名遍历出来
for i in COLOR.__members__.items():
    print(i)
# output:('YELLOW', <COLOR.YELLOW: 1>)\n('GREEN', <COLOR.YELLOW: 1>)\n('BLACK', <COLOR.BLACK: 3>)\n('RED', <COLOR.RED: 4>)
for i in COLOR.__members__:
    print(i)
# output:YELLOW\nGREEN\nBLACK\nRED

#枚举转换
#最好在数据库存取使用枚举的数值而不是使用标签名字字符串
#在代码里面使用枚举类
a=1
print(COLOR(a))# output:COLOR.YELLOW

# py2/3 转换工具
'''six 模块：兼容 pyton2 和 pyton3 的模块
2to3 工具：改变代码语法版本
__future__：使用下一版本的功能'''





# 类库相关
# 常用库
    '''必须知道的 collections https://segmentfault.com/a/1190000017385799
    python排 序操作及 heapq 模块 https://segmentfault.com/a/1190000017383322
    itertools 模块超实用方法 https://segmentfault.com/a/1190000017416590'''
# 不常用但很重要的库
    '''dis(代码字节码分析)
    inspect(生成器状态)
    cProfile(性能分析)
    bisect(维护有序列表)
    fnmatch
    fnmatch(string,"*.txt") # win下不区分大小写
    fnmatch 根据系统决定
    fnmatchcase 完全区分大小写
    timeit(代码执行时间)'''
def isLen(strString):
    #还是应该使用三元表达式，更快
    return True if len(strString)>6 else False

def isLen1(strString):
    #这里注意false和true的位置
    return [False,True][len(strString)>6]
import timeit
print(timeit.timeit('isLen1("5fsdfsdfsaf")',setup="from __main__ import isLen1"))

print(timeit.timeit('isLen("5fsdfsdfsaf")',setup="from __main__ import isLen"))

# ypes(包含了标准解释器定义的所有类型的类型对象,可以将生成器函数修饰为异步模式)
import types
types.coroutine #相当于实现了__await__
# html(实现对html的转义)
import html
html.escape("<h1>I'm Jim</h1>") # output:'&lt;h1&gt;I&#x27;m Jim&lt;/h1&gt;'
html.unescape('&lt;h1&gt;I&#x27;m Jim&lt;/h1&gt;') # <h1>I'm Jim</h1>

# mock(解决测试依赖)
# concurrent(创建进程池和线程池)
from concurrent.futures import ThreadPoolExecutor
pool = ThreadPoolExecutor()
task = pool.submit('函数名','（参数）') #此方法不会阻塞，会立即返回
task.done()#查看任务执行是否完成
task.result()#阻塞的方法，查看任务返回值
task.cancel()#取消未执行的任务，返回True或False,取消成功返回True
task.add_done_callback()#回调函数
task.running()#是否正在执行     task就是一个Future对象
for data in pool.map('函数','参数列表'):#返回已经完成的任务结果列表，根据参数顺序执行
    print('返回任务完成得执行结果data')
from concurrent.futures import as_completed
as_completed('任务列表')#返回已经完成的任务列表，完成一个执行一个
wait('任务列表',return_when='条件')#根据条件进行阻塞主线程，有四个条件

# selector(封装select,用户多路复用io编程)
# asyncio
future=asyncio.ensure_future('协程')  等于后面的方式  future=loop.create_task(协程)
future.add_done_callback()添加一个完成后的回调函数
loop.run_until_complete(future)
future.result()查看写成返回结果

asyncio.wait()接受一个可迭代的协程对象
asynicio.gather(*可迭代对象,*可迭代对象）    两者结果相同，但gather可以批量取消，gather对象.cancel()

# 一个线程中只有一个loop

在loop.stop时一定要loop.run_forever()否则会报错
loop.run_forever()可以执行非协程
最后执行finally模块中 loop.close()

asyncio.Task.all_tasks()拿到所有任务 然后依次迭代并使用任务.cancel()取消

# 偏函数partial(函数，参数)把函数包装成另一个函数名  其参数必须放在定义函数的前面

loop.call_soon(函数,参数)
call_soon_threadsafe()线程安全
loop.call_later(时间,函数,参数)
# 在同一代码块中call_soon优先执行，然后多个later根据时间的升序进行执行

# 如果非要运行有阻塞的代码
使用loop.run_in_executor(executor,函数，参数)包装成一个多线程，然后放入到一个task列表中，通过wait(task列表)来运行

# 通过asyncio实现http
reader,writer=await asyncio.open_connection(host,port)
writer.writer()发送请求
async for data in reader:
    data=data.decode("utf-8")
    list.append(data)
# 然后list中存储的就是html

as_completed(tasks)完成一个返回一个,返回的是一个可迭代对象

# 协程锁
async with Lock():







# Python进阶
# 进程间通信：
# Manager(内置了好多数据结构，可以实现多进程间内存共享)
from multiprocessing import Manager, Process
def add_data(p_dict, key, value):
    p_dict[key] = value
if __name__ == "__main__":
    progress_dict = Manager().dict()
    from queue import PriorityQueue

    first_progress = Process(target=add_data, args=(progress_dict, "bobby1", 22))
    second_progress = Process(target=add_data, args=(progress_dict, "bobby2", 23))

    first_progress.start()
    second_progress.start()
    first_progress.join()
    second_progress.join()

    print(progress_dict)

# Pipe(适用于两个进程)
from multiprocessing import Pipe,Process
#pipe的性能高于queue
def producer(pipe):
    pipe.send("bobby")
def consumer(pipe):
    print(pipe.recv())
if __name__ == "__main__":
    recevie_pipe, send_pipe = Pipe()
    #pipe只能适用于两个进程
    my_producer= Process(target=producer, args=(send_pipe, ))
    my_consumer = Process(target=consumer, args=(recevie_pipe,))

    my_producer.start()
    my_consumer.start()
    my_producer.join()
    my_consumer.join()

# Queue(不能用于进程池,进程池间通信需要使用Manager().Queue())
from multiprocessing import Queue,Process
def producer(queue):
    queue.put("a")
    time.sleep(2)
def consumer(queue):
    time.sleep(2)
    data = queue.get()
    print(data)
if __name__ == "__main__":
    queue = Queue(10)
    my_producer = Process(target=producer, args=(queue,))
    my_consumer = Process(target=consumer, args=(queue,))
    my_producer.start()
    my_consumer.start()
    my_producer.join()
    my_consumer.join()

# 进程池
def producer(queue):
    queue.put("a")
    time.sleep(2)
def consumer(queue):
    time.sleep(2)
    data = queue.get()
    print(data)
if __name__ == "__main__":
    queue = Manager().Queue(10)
    pool = Pool(2)

    pool.apply_async(producer, args=(queue,))
    pool.apply_async(consumer, args=(queue,))

    pool.close()
    pool.join()

# 采用any方式：all() 对于任何可迭代对象为空都会返回 True
# 方法一
True in [i in s for i in [a,b,c]]
# 方法二
any(i in s for i in [a,b,c])
# 方法三
list(filter(lambda x:x in s,[a,b,c]))

# 查看系统默认编码格式
import sys
sys.getdefaultencoding()    # setdefaultencodeing()设置系统编码方式

# getattr VS getattribute
class A(dict):
    def __getattr__(self,value):#当访问属性不存在的时候返回
        return 2
    def __getattribute__(self,item):#屏蔽所有的元素访问
        return item

# 实现从1-100每三个为一组分组
print([[x for x in range(1,101)][i:i+3] for i in range(0,100,3)])

# 什么是元类？
# 即创建类的类，创建类的时候只需要将metaclass=元类，元类需要继承type而不是object,因为type就是元类
type.__bases__  #(<class 'object'>,)
object.__bases__    #()
type(object)    #<class 'type'>
class Yuan(type):
        def __new__(cls,name,base,attr,*args,**kwargs):
            return type(name,base,attr,*args,**kwargs)
    class MyClass(metaclass=Yuan):
        pass

# 单元测试
# 一般测试类继承模块unittest下的TestCase
# pytest模块快捷测试(方法以test_开头/测试文件以test_开头/测试类以Test开头，并且不能带有 init 方法)
# coverage统计测试覆盖率
class MyTest(unittest.TestCase):
    def tearDown(self):# 每个测试用例执行前执行
        print('本方法开始测试了')

    def setUp(self):# 每个测试用例执行之前做操作
        print('本方法测试结束')

    @classmethod
    def tearDownClass(self):# 必须使用 @ classmethod装饰器, 所有test运行完后运行一次
        print('开始测试')
    @classmethod
    def setUpClass(self):# 必须使用@classmethod 装饰器,所有test运行前运行一次
        print('结束测试')

    def test_a_run(self):
        self.assertEqual(1, 1)  # 测试用例

# Hash扩容和Hash冲突解决方案
# 循环复制到新空间实现扩容
# 冲突解决：
# 链接法
# 二次探查(开放寻址法)：python使用
for gevent import monkey
monkey.patch_all()  #将代码中所有的阻塞方法都进行修改，可以指定具体要修改的方法

# 判断是否为生成器或者协程
co_flags = func.__code__.co_flags
# 检查是否是协程
if co_flags & 0x180:
    return func
# 检查是否是生成器
if co_flags & 0x20:
    return func

# 斐波那契解决的问题及变形
#一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
#请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？
#方式一：
fib = lambda n: n if n <= 2 else fib(n - 1) + fib(n - 2)
#方式二：
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return b

#一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
fib = lambda n: n if n < 2 else 2 * fib(n - 1)

# 获取电脑设置的环境变量
import os
os.getenv(env_name,None)#获取环境变量如果不存在为None

# 垃圾回收机制
# 引用计数
# 标记清除
# 分代回收
#查看分代回收触发
import gc
gc.get_threshold()  #output:(700, 10, 10)

# 10进制转2进制
def conver_bin(num):
    if num == 0:
        return num
    re = []
    while num:
        num, rem = divmod(num,2)
        re.append(str(rem))
    return "".join(reversed(re))
  conver_bin(10)

# list1 = ['A', 'B', 'C', 'D'] 如何才能得到以list中元素命名的新列表 A=[],B=[],C=[],D=[]呢
list1 = ['A', 'B', 'C', 'D']
# 方法一
for i in list1:
    globals()[i] = []   # 可以用于实现python版反射

# 方法二
for i in list1:
    exec(f'{i} = []')   # exec执行字符串语句

# memoryview与bytearray不常用，只是看到了记载一下
# bytearray是可变的，bytes是不可变的,memoryview不会产生新切片和对象
a = 'aaaaaa'
ma = memoryview(a)
ma.readonly  # 只读的memoryview
mb = ma[:2]  # 不会产生新的字符串

a = bytearray('aaaaaa')
ma = memoryview(a)
ma.readonly  # 可写的memoryview
mb = ma[:2]      # 不会会产生新的bytearray
mb[:2] = 'bb'    # 对mb的改动就是对ma的改动

# Ellipsis类型
# 代码中出现...省略号的现象就是一个Ellipsis对象
L = [1,2,3]
L.append(L)
print(L)    # output:[1,2,3,[…]]

# lazy惰性计算
class lazy(object):
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, cls):
        val = self.func(instance)    #其相当于执行的area(c),c为下面的Circle对象
        setattr(instance, self.func.__name__, val)
        return val`

class Circle(object):
    def __init__(self, radius):
        self.radius = radius

    @lazy
    def area(self):
        print('evalute')
        return 3.14 * self.radius ** 2

# 遍历文件，传入一个文件夹，将里面所有文件的路径打印出来(递归)
all_files = []
def getAllFiles(directory_path):
    import os
    for sChild in os.listdir(directory_path):
        sChildPath = os.path.join(directory_path,sChild)
        if os.path.isdir(sChildPath):
            getAllFiles(sChildPath)
        else:
            all_files.append(sChildPath)
    return all_files

# 文件存储时，文件名的处理
#secure_filename将字符串转化为安全的文件名
from werkzeug import secure_filename
secure_filename("My cool movie.mov") # output:My_cool_movie.mov
secure_filename("../../../etc/passwd") # output:etc_passwd
secure_filename(u'i contain cool \xfcml\xe4uts.txt') # output:i_contain_cool_umlauts.txt

# 日期格式化
from datetime import datetime
datetime.now().strftime("%Y-%m-%d")
import time
#这里只有localtime可以被格式化，time是不能格式化的
time.strftime("%Y-%m-%d",time.localtime())

# tuple使用+=奇怪的问题
# 会报错，但是tuple的值会改变，因为t[1]id没有发生变化
t=(1,[2,3])
t[1]+=[4,5]
# t[1]使用append\extend方法并不会报错，并可以成功执行

# __missing__你应该知道
class Mydict(dict):
    def __missing__(self,key): # 当Mydict使用切片访问属性不存在的时候返回的值
        return key

# +与+=
# +不能用来连接列表和元祖，而+=可以（通过iadd实现，内部实现方式为extends(),所以可以增加元组），+会创建新对象
#不可变对象没有__iadd__方法，所以直接使用的是__add__方法，因此元祖可以使用+=进行元祖之间的相加

# 如何将一个可迭代对象的每个元素变成一个字典的所有键？
dict.fromkeys(['jim','han'],21) # output:{'jim': 21, 'han': 21}





# 网络知识
# 常见响应状态码
    '''204 No Content //请求成功处理，没有实体的主体返回，一般用来表示删除成功
    206 Partial Content //Get范围请求已成功处理
    303 See Other //临时重定向，期望使用get定向获取
    304 Not Modified //请求缓存资源
    307 Temporary Redirect //临时重定向，Post不会变成Get
    401 Unauthorized //认证失败
    403 Forbidden //资源请求被拒绝
    400 //请求参数错误
    201 //添加或更改成功
    503 //服务器维护或者超负载'''

# WSGI
# environ：一个包含所有HTTP请求信息的dict对象
# start_response：一个发送HTTP响应的函数
def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return '<h1>Hello, web!</h1>'





# Mysql
# 失效场景：
# 例如：
'''select id from t where substring(name,1,3) = 'abc' – name;
以abc开头的，应改成：
select id from t where name like 'abc%' 
例如：
select id from t where datediff(day, createdate, '2005-11-30') = 0 – '2005-11-30';
应改为:'''