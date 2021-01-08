#介绍
# import logging
# logging.basicConfig(
#     # filename='access.log',
#     format='%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s',
#     datefmt='%Y-%m-%d %H:%M:%S %p',
#     level=10
# )
#
# logging.debug('debug') # 10
# logging.info('info') # 20
# logging.warning('warn') #30
# logging.error('error') #40
# logging.critical('critial') #50


#日志模块的详细用法：
import logging
#1、Logger：产生日志
logger1=logging.getLogger('访问日志')
# logger2=logging.getLogger('错吴日志')


#2、Filter：几乎不用

#3、Handler：接收Logger传过来的日志，进行日志格式化，可以打印到终端，也可以打印到文件
sh=logging.StreamHandler() #打印到终端
fh1=logging.FileHandler('s1.log',encoding='utf-8')
fh2=logging.FileHandler('s2.log',encoding='utf-8')

#4、Formatter：日志格式
formatter1=logging.Formatter(
    fmt='%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S %p',
)
formatter2=logging.Formatter(
    fmt='%(asctime)s : %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S %p',
)
formatter3=logging.Formatter(
    fmt='%(asctime)s : %(module)s : %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S %p',
)

#5、为handler绑定日志格式
sh.setFormatter(formatter1)
fh1.setFormatter(formatter2)
fh2.setFormatter(formatter3)

#6、为logger绑定handler
logger1.addHandler(sh)
logger1.addHandler(fh1)
logger1.addHandler(fh2)

#7、设置日志级别:logger对象的日志级别应该＜＝handler的日志界别
# logger1.setLevel(50)
logger1.setLevel(10) #
sh.setLevel(10)
fh1.setLevel(10)
fh2.setLevel(10)

#8、测试
logger1.debug('测试着玩')
logger1.info('运行还算正常')
logger1.warning('可能要有bug了')
logger1.error('不好了，真tm出bug了')
logger1.critical('完犊子，推倒重写')