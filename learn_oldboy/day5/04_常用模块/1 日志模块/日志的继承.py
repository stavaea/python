import logging
#1、Logger：产生日志
logger1=logging.getLogger('root')
logger2=logging.getLogger('root.child1')
logger3=logging.getLogger('root.child1.child2')

#2、Filter：几乎不用

#3、Handler：接收Logger传过来的日志，进行日志格式化，可以打印到终端，也可以打印到文件
sh=logging.StreamHandler() #打印到终端

#4、Formatter：日志格式
formatter1=logging.Formatter(
    fmt='%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S %p',
)

#5、为handler绑定日志格式
sh.setFormatter(formatter1)


#6、为logger绑定handler
logger1.addHandler(sh)
logger2.addHandler(sh)
logger3.addHandler(sh)


#7、设置日志级别:logger对象的日志级别应该＜＝handler的日志界别
# logger1.setLevel(50)
logger1.setLevel(10) #
logger2.setLevel(10) #
logger3.setLevel(10) #
sh.setLevel(10)


#8、测试
logger1.debug('爷爷')
logger2.debug('爸爸')
logger3.debug('孙子')
